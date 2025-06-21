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
    # {
    #     "inputs": {"question": "make me a lesson plan for chapter2", 
    #                "context": "Chapter 2 covers agriculture including types, effects of population growth, small- and large-scale farming..."
    #                }, 
    #     "outputs": {"answer": "*Chapter 2: Agriculture* ## Lesson Plan ### Introduction (10 minutes) - Introduce the topic of Agriculture - Explain the meaning and types of agriculture ### Direct Instruction (20 minutes) 1. Discuss the effects of rapid population growth on small-scale agriculture 2. Explain the characteristics of small-scale agriculture 3. Highlight the advantages and disadvantages of small-scale agriculture 4. Provide ways of improving small-scale agriculture ### Guided Practice (15 minutes) - Discuss types of large-scale agriculture in the world - Identify major crops grown in each type of large-scale agriculture ### Independent Practice (15 minutes) - Examine the characteristics of large-scale agriculture and problems facing large-scale agriculture in Tanzania and the USA ### Conclusion (10 minutes) - Summarize key points - Ask students to reflect on what they learned *Note: This is a general lesson plan and may need to be adjusted based on specific classroom needs and time constraints.*"}
    # }, 
    # {
    #     "inputs": {"question": "give me a summary of chapter 2", 
    #                "context": "Chapter 2 covers agriculture including types, effects of population growth, small- and large-scale farming..."
    #                }, 
    #     "outputs": {"answer": "## Chapter 2: Agriculture ### Introduction Agriculture is the cultivation of crops and rearing of livestock for food, fiber, and other products. It is a vital sector in many countries, including Tanzania. ### Types of Agriculture There are two main types of agriculture: small-scale and large-scale. #### Small-Scale Agriculture - Characterized by small land area, simple tools, and low capital investment. - Effects of rapid population growth on small-scale agriculture: - Increased pressure on land - Decreased farm size - Reduced crop yields - Characteristics: - Use of traditional farming methods - Limited use of technology - Low productivity - Advantages: - Provides employment opportunities - Contributes to food security - Encourages sustainable farming practices - Disadvantages: - Low income for farmers - Limited access to markets - Vulnerability to climate change - Ways of improving small-scale agriculture: - Use of modern farming techniques - Access to credit facilities - Market access and infrastructure development #### Large-Scale Agriculture - Characterized by large land area, advanced technology, and high capital investment. - Types of large-scale agriculture: - Plantations (e.g., tea, coffee, rubber) - Ranching (e.g., cattle, sheep) - Intensive farming (e.g., wheat, maize) - Characteristics: - Use of advanced technology and machinery - High productivity - Economies of scale - Problems facing large-scale agriculture in Tanzania and the USA: - Climate change and variability - Soil degradation - Limited access to markets and finance ### Conclusion Agriculture is a crucial sector in many countries, providing food, employment, and income. Understanding the types, characteristics, advantages, and disadvantages of small-scale and large-scale agriculture is essential for sustainable agricultural development."}
    # },
   # More examplesets based on chapter 2
    {
      "inputs": {
        "question": "Make a lesson plan for teaching small-scale crop cultivation.",
        "context": "Small-scale crop cultivation is the growing of crops on a small piece of land. It is also called subsistence farming. It aims to produce enough food for the wellbeing of families. In some instances, when the production is high, the surplus is sold. Individuals engaging in small-scale crop cultivation are known as peasants. They are also called subsistence farmers as they grow food crops to feed themselves and their families with little or no surplus for sale."
      },
      "outputs": {
        "answer": "*Lesson Plan: Small-scale Crop Cultivation*\n\n**Introduction (5 min):** Explain the meaning of small-scale farming and its goals.\n**Theory (10 min):** Discuss characteristics, tools, and crops involved. Highlight family labour and use of simple tools.\n**Activity (15 min):** Group students to list advantages/disadvantages and present findings.\n**Conclusion (5 min):** Recap main points and answer students' questions."
      }
    },
    {
      "inputs": {
        "question": "Create 3 exam questions on the effects of population growth on small-scale farming.",
        "context": "The rapid population growth puts more pressure on small-scale farmers. Yet,  subsistence farmers are not likely to raise their output to feed the growing numbers because of lack of capital. Subsequently, land becomes overpopulated and resources overused. Also high population growth is associated with smaller farms and lower farm wages."
      },
      "outputs": {
        "answer": "1. How does rapid population growth affect the size of small-scale farms?\n2. Explain why subsistence farmers may struggle to feed a growing population.\n3. What are two consequences of overpopulated farming areas?"
      }
    },
    {
      "inputs": {
        "question": "Give me key terms and definitions from Chapter 2 for use as lesson keywords.",
        "context": "Shifting cultivation: This is a traditional system of cultivation used in tropical rainforest and miombo wooded savanna. It operates where population is sparse. Crop rotation involves growing different crops on the same land at different times. Bush fallowing is similar to shifting cultivation but with permanent settlements."
      },
      "outputs": {
        "answer": "- Shifting cultivation: Farming method involving moving fields after yields decline.\n- Crop rotation: Growing different crops on the same land at different times.\n- Bush fallowing: Letting land rest and recover fertility after a period of use."
      }
    },
    {
      "inputs": {
        "question": "Summarize the main topics covered in Chapter 2: Agriculture.",
        "context": "In this chapter, you will learn about the meaning and types of agriculture, the effects of rapid population growth on small-scale agriculture, characteristics of small-scale agriculture, advantages and disadvantages of small-scale agriculture, and ways of improving small-scale agriculture. You will also learn about types of large-scale agriculture in the world, major crops grown in each type of large-scale agriculture, characteristics of large-scale agriculture and problems facing large-scale agriculture in Tanzania and the USA."
      },
      "outputs": {
        "answer": "Chapter 2 covers the types and meaning of agriculture, impacts of population growth on farming, features, pros and cons of small- and large-scale farming, major crops and regions, and how agriculture affects the economy."
      }
    },
    {
      "inputs": {
        "question": "Explain the difference between small-scale and large-scale crop cultivation.",
        "context": "Small-scale crop cultivation is the growing of crops on a small piece of land, mainly for family use. Large-scale crop cultivation covers a large area to produce one type of crop for commercial purposes. Large-scale farms use machines, require more capital, and often focus on monoculture."
      },
      "outputs": {
        "answer": "Small-scale cultivation is for family use on small land, with simple tools and many crops. Large-scale is commercial, uses machines, and focuses on single crops for sale."
      }
    },
    {
      "inputs": {
        "question": "List three advantages of small-scale crop cultivation.",
        "context": "Small-scale crop production is cheap to operate since it involves the use of simple farming tools such as hand hoes and machetes. It is also cheap because the sources of labour are family members and, hence, easy to manage. In addition, small-scale agriculture needs small capital since it operates on small pieces of land."
      },
      "outputs": {
        "answer": "1. Low operating costs with simple tools\n2. Family labour makes it easy to manage\n3. Needs little capital and provides fresh food"
      }
    },
    {
      "inputs": {
        "question": "What are ways to improve small-scale farming?",
        "context": "Small-scale farmers need training on the best cultivation practises such as the application of manure and proper use of chemical fertilisers. Farmers should also be educated on the use of hybrid seeds and irrigation schemes. Furthermore, the establishment of co-operative unions can help small-scale farmers to get soft loans, access markets, undergo training and benefit from extension services."
      },
      "outputs": {
        "answer": "Ways to improve: Training in farming methods, use of manure and fertilisers, hybrid seeds, irrigation, and forming co-ops for loans and market access."
      }
    },
    {
      "inputs": {
        "question": "Write a short class presentation on coffee cultivation in Tanzania.",
        "context": "Coffee is grown in Kagera, Kilimanjaro, Arusha, Mbeya, Katavi, Iringa, Mara, Njombe, Tanga, Morogoro, Kigoma and Ruvuma regions. Coffee requires heat, humidity and abundant rainfall. It is a major export crop."
      },
      "outputs": {
        "answer": "Coffee is a key export crop in Tanzania, grown in many regions. It needs heat, humidity, and much rainfall. Main areas are Kagera, Kilimanjaro, and Mbeya. Coffee contributes to the economy and is grown mainly for export."
      }
    },
    {
      "inputs": {
        "question": "What are the required conditions for growing rice?",
        "context": "Rice is a tropical crop which grows well where the average temperature during the growing season is between 20°C and 27°C. Paddy cultivation is done only in those areas where minimum rainfall is 1,150 mm. Paddy also needs flooded conditions."
      },
      "outputs": {
        "answer": "Rice needs temperatures between 20–27°C, high rainfall (over 1,150 mm), and flooded fields during growth."
      }
    },
    {
      "inputs": {
        "question": "List important cash crops in Tanzania and the regions where they are grown.",
        "context": "Table 2.1 Major cash crops grown in Tanzania: Coffee – Kagera, Kilimanjaro, Arusha, Mbeya, Ruvuma, Kigoma and Mara. Cotton – Mwanza, Tabora, Mara, Tanga, Shinyanga, Geita and Simiyu. Palm oil trees – Kigoma. Tea – Mbeya, Iringa, Njombe, Tanga, Kilimanjaro and Kagera. Sisal – Tanga, Kilimanjaro, Arusha, Morogoro, Lindi and Mtwara. Cloves – Unguja and Pemba."
      },
      "outputs": {
        "answer": "- Coffee: Kagera, Kilimanjaro, Arusha, Mbeya, Ruvuma, Kigoma, Mara\n- Cotton: Mwanza, Tabora, Mara, Tanga, Shinyanga, Geita, Simiyu\n- Palm oil: Kigoma\n- Tea: Mbeya, Iringa, Njombe, Tanga, Kilimanjaro, Kagera\n- Sisal: Tanga, Kilimanjaro, Arusha, Morogoro, Lindi, Mtwara\n- Cloves: Unguja, Pemba"
      }
    },
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

