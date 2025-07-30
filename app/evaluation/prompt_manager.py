import yaml
import os
import re
from typing import Optional, Dict, List
from dotenv import load_dotenv

from langsmith import Client
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

BASE_PATH = "app/evaluation/prompts"

categories = [
        name for name in os.listdir(BASE_PATH)
        if os.path.isdir(os.path.join(BASE_PATH, name))
    ]

print(f"Found categories: {categories}")

def get_latest_version_file(category_path: str) -> Optional[str]:
    """Get the filename with the highest version number in a category"""
    version_files = []
    
    for filename in os.listdir(category_path):
        if filename.endswith('.yaml'):
            # Extract version number from filename (e.g. v1.yaml would be 1 and so on)
            match = re.match(r'v(\d+)\.yaml', filename)
            if match:
                version_num = int(match.group(1))
                version_files.append((version_num, filename))
    
    if version_files:
        version_files.sort(key=lambda x: x[0], reverse=True)
        return version_files[0][1]
    
    return None

def load_and_print_all_prompts() -> Dict[str, str]:
    """Load all YAML files and return prompts as dict with category as key"""
    base_path = "app/evaluation/prompts"
    prompts_dict = {}

    for category in categories:
        category_path = os.path.join(base_path, category)
        category_prompts = []
        
        # Get the latest version file for this category so we only load the most recent prompt. 
        # This assumes the files are named like "v1.yaml", "v2.yaml", etc.
        latest_file = get_latest_version_file(category_path)
        
        if latest_file:
            file_path = os.path.join(category_path, latest_file)
            
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
                prompt_content = data.get('prompt', 'No prompt found')
                category_prompts.append(prompt_content)
        
        if category_prompts:
            prompts_dict[category] = '\n\n'.join(category_prompts)
    
    return prompts_dict


class LangchainPromptManager:
    def __init__(self, base_path: str = BASE_PATH, category: str = "default"):
        self.base_path = base_path
        self.client = Client()
        self.category = category

    def batch_load_prompts(self, prompts_dict: Dict[str, str]) -> None:
        """Batch push prompts to LangSmith using category as key and name"""
        for category, prompt_content in prompts_dict.items():
            prompt = ChatPromptTemplate.from_template(prompt_content)
            url = self.client.push_prompt(category, object=prompt)
            print(f"Category: {category}")
            print(f"Prompt URL: {url}")
            print("-" * 30)


if __name__ == "__main__":
    # Load all prompts
    prompts = load_and_print_all_prompts()
    
    # Print loaded prompts
    for category, prompt in prompts.items():
        print(f"Category: {category}")
        print(f"Prompt: {prompt}")
        print("-" * 50)
    
    # Batch push to LangSmith
    print("\nPushing prompts to LangSmith...")
    prompt_manager = LangchainPromptManager()
    prompt_manager.batch_load_prompts(prompts)
