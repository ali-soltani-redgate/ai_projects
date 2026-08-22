
# We are using few-shot prompting to test the model's ability to learn from examples. We will provide a few examples of input-output pairs and then ask the model to generate an output for a new input.
# I am going to create custom datasets needed for Redgate Test Data Mangarer.
# Link: https://documentation.red-gate.com/testdatamanager/command-line-interface-cli/anonymization/masking/using-different-or-custom-datasets
# We will cover the two types of datasets:
# 1. value lists
# 2. pattern-based datasets

# Steps:
# 1. Get samples by dataset type
# 2. Create system prompt for each dataset type with instructions on how to use the examples
# 3. Create user prompt with the new input for which we want to generate an output
# 4. Call the LLM with the system prompt, user prompt, and examples. Use a simple Ollma model, tinyllama, for this.
# 5. Print the answer


from enum import Enum

from dotenv import load_dotenv
from langfuse import get_client, observe
import argparse
from ollama import chat

load_dotenv()

def main():
    system_prompt_value_list = """You are a helpful assistant that generates datasets based on examples.
   You will be given a few examples of input-output pairs, and you will return a dataset output for a new input based on the patterns in the examples. 
   The output should be a JSON array of string values in the same format as the examples."""

    system_prompt_pattern = """You are a helpful assistant that generates format pattern templates.
   IMPORTANT: You NEVER generate real data. You ONLY output abstract format patterns using these placeholders:
   - '#' represents a single digit (0-9)
   - '?' represents a single letter (a-z or A-Z)
   - All other characters (spaces, dashes, parentheses, dots) are literal.
   
   Examples of CORRECT output: ["###-###-####", "(###) ###-####", "?. ?."]
   Examples of WRONG output: ["123-456-7890", "John", "A. B."]
   
   Return ONLY a JSON array of pattern strings. No explanations."""


    parser = argparse.ArgumentParser(description="Few-shot prompting example")
    parser.add_argument("--dataset_type", type=str, choices=[DatasetType.VALUE_LIST.value,
                        DatasetType.PATTERN.value], required=True, help="The type of dataset to use for few-shot prompting.")
    parser.add_argument("--user_prompt", type=str, required=True, help="The user prompt for which we want to generate an output.")
    args = parser.parse_args()
    
    user_prompt = args.user_prompt
    dataset_type = DatasetType(args.dataset_type)
    examples = get_samples_by_dataset_type(dataset_type)
    system_prompt = system_prompt_pattern if dataset_type == DatasetType.PATTERN else system_prompt_value_list
    messages = build_prompt_template(system_prompt, user_prompt, examples)

    print("Generating output...")
    response = call_ollama_model(messages) 
    print("Output:", response)
    

@observe(as_type="generation")
def call_ollama_model(messages: list) -> str:
    """
    This function simulates calling an Ollama model with a list of messages for few-shot prompting
    and streams the generated summary in real-time.
    Args:
        messages (list): A list of messages including the system prompt, user prompt, and examples.
    Returns:
        str: The generated output based on the examples and prompts.
    """
    llm_model = "tinyllama"  # Replace with the actual model name you want to uses
    get_client().update_current_generation(model=llm_model)

    stream = chat(
        model=llm_model,
        messages=messages,
        stream=True,
        options={"temperature": 0},)

    parts = []
    for event in stream:
        if event.message and event.message.content:
            print(event.message.content, end="", flush=True)
            parts.append(event.message.content)
    print()  # for newline after streaming is done
    summary = "".join(parts).strip()

    return summary

def build_prompt_template(system_prompt, user_prompt, examples):
    messages = [{"role": "system", "content": system_prompt}]
    for example in examples:
        messages.append({"role": "user", "content": example["input"]})
        messages.append({"role": "assistant", "content": example["output"]})
    messages.append({"role": "user", "content": user_prompt})
    return messages

class DatasetType(Enum):
    VALUE_LIST = "value_list"
    PATTERN = "pattern"


def get_samples_by_dataset_type(dataset_type: DatasetType):
    """
    This function retrieves samples based on the specified dataset type. 
    It can be extended to fetch samples from a database, file, or any other source. The samples should be relevant to the dataset type and can be used for few-shot prompting.

    Args:
        dataset_type (DatasetType): The type of dataset to get samples for.
    Returns: 
        A list of samples for the given dataset type.        
    """

    if dataset_type == DatasetType.VALUE_LIST:
        return [
            {"input": "Persian names", "output": '["Ali", "Fatemeh", "Reza"]'},
            {"input": "Spanish names", "output": '["Juan", "Maria", "Alba"]'},
            {"input": "ShortFirstNames",
                "output": '["Ann", "Bob", "Carl", "Dave"]'}
        ]
    elif dataset_type == DatasetType.PATTERN:
        return [
            {"input": "PhoneNumbers", "output":
                r'["(###) ###-####", "(###) ###-#### x####","1-###-###-####", "###-###-####", "[23456789]## ###-####"]'},
            {"input": "MiddleInitials", "output": '["?.", "?. ?."]'}
        ]


if __name__ == "__main__":
    main()
