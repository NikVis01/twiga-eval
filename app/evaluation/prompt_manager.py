import yaml
import os
from typing import Optional, Dict, List
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableConfig
from dotenv import load_dotenv
from typing import Dict, List

BASE_PATH = "app/evaluation/prompts"

categories = [
        name for name in os.listdir(BASE_PATH)
        if os.path.isdir(os.path.join(BASE_PATH, name))
    ]

print(f"Found categories: {categories}")

def load_and_print_all_prompts(filename: str = "v1.yaml") -> None:
    """Load all YAML files and print their prompt content"""
    base_path = "app/evaluation/prompts"
    
    file_path = os.path.join(base_path, filename)
    print(f"Filename: {filename}:")

    for category in categories:
        category_path = os.path.join(base_path, category)

        print(f"Category: {category}")
        
        for filename in os.listdir(category_path):
            if filename.endswith('.yaml'):
                file_path = os.path.join(category_path, filename)
                
                print(f"{filename}:")

                with open(file_path, 'r') as f:
                    data = yaml.safe_load(f)
                    prompt_content = data.get('prompt', 'No prompt found')
                    print(f"{prompt_content}")
                    print()

if __name__ == "__main__":
    load_and_print_all_prompts()
