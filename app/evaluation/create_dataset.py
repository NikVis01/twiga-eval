"""
Script to create a dataset for evaluating the Twiga chatbot 
TODO: 
- Add more examples to the dataset
"""
from langsmith import Client
from dotenv import load_dotenv
import os


DATASET_NAME="Twiga Eval Dataset Test"


# Load environment variables
load_dotenv()
client = Client()

# Try to create the dataset, or load it if it already exists
try:
    dataset = client.create_dataset(
        dataset_name=DATASET_NAME,
        description="Dataset for Twiga chatbot response evaluation"
    )
    print(f"Dataset created: {dataset.name}")
except Exception as e:
    print(f"Dataset creation failed: {e}")
    dataset = client.read_dataset(dataset_name=DATASET_NAME)
    print("Loaded existing dataset.")



examples = [
    #NOTE: This is just a test example to check if the dataset is working, the real examples should have the same structure
    {
        "inputs": {"question": "make me a lesson plan for chapter2", 
                   "context": "Chapter 2 covers agriculture including types, effects of population growth, small- and large-scale farming..."
                   }, 
        "outputs": {"answer": "*Chapter 2: Agriculture* ## Lesson Plan ### Introduction (10 minutes) - Introduce the topic of Agriculture - Explain the meaning and types of agriculture ### Direct Instruction (20 minutes) 1. Discuss the effects of rapid population growth on small-scale agriculture 2. Explain the characteristics of small-scale agriculture 3. Highlight the advantages and disadvantages of small-scale agriculture 4. Provide ways of improving small-scale agriculture ### Guided Practice (15 minutes) - Discuss types of large-scale agriculture in the world - Identify major crops grown in each type of large-scale agriculture ### Independent Practice (15 minutes) - Examine the characteristics of large-scale agriculture and problems facing large-scale agriculture in Tanzania and the USA ### Conclusion (10 minutes) - Summarize key points - Ask students to reflect on what they learned *Note: This is a general lesson plan and may need to be adjusted based on specific classroom needs and time constraints.*"}
    }, 
    {
        "inputs": {"question": "give me a summary of chapter 2", 
                   "context": "Chapter 2 covers agriculture including types, effects of population growth, small- and large-scale farming..."
                   }, 
        "outputs": {"answer": "## Chapter 2: Agriculture ### Introduction Agriculture is the cultivation of crops and rearing of livestock for food, fiber, and other products. It is a vital sector in many countries, including Tanzania. ### Types of Agriculture There are two main types of agriculture: small-scale and large-scale. #### Small-Scale Agriculture - Characterized by small land area, simple tools, and low capital investment. - Effects of rapid population growth on small-scale agriculture: - Increased pressure on land - Decreased farm size - Reduced crop yields - Characteristics: - Use of traditional farming methods - Limited use of technology - Low productivity - Advantages: - Provides employment opportunities - Contributes to food security - Encourages sustainable farming practices - Disadvantages: - Low income for farmers - Limited access to markets - Vulnerability to climate change - Ways of improving small-scale agriculture: - Use of modern farming techniques - Access to credit facilities - Market access and infrastructure development #### Large-Scale Agriculture - Characterized by large land area, advanced technology, and high capital investment. - Types of large-scale agriculture: - Plantations (e.g., tea, coffee, rubber) - Ranching (e.g., cattle, sheep) - Intensive farming (e.g., wheat, maize) - Characteristics: - Use of advanced technology and machinery - High productivity - Economies of scale - Problems facing large-scale agriculture in Tanzania and the USA: - Climate change and variability - Soil degradation - Limited access to markets and finance ### Conclusion Agriculture is a crucial sector in many countries, providing food, employment, and income. Understanding the types, characteristics, advantages, and disadvantages of small-scale and large-scale agriculture is essential for sustainable agricultural development."}
    },
   
    # add more examples here
]


# Get existing examples and prepare input signature set
existing_examples = client.list_examples(dataset_id=dataset.id)
existing_inputs = {tuple(sorted(example.inputs.items())) for example in existing_examples}

# Filter out duplicates
new_examples = [
    ex for ex in examples
    if tuple(sorted(ex["inputs"].items())) not in existing_inputs
]

# Upload only new examples
if new_examples:
    client.create_examples(dataset_id=dataset.id, examples=new_examples)
    print(f"Uploaded {len(new_examples)} new examples to dataset '{dataset.name}'.")
else:
    print("No new examples to upload — all inputs already exist.")

