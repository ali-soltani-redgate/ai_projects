
# 1. Make the system prompt
# 2. Get the user prompt
# 3. Make the prompt template with zero shot prompting
# 4. Call the LLM with the prompt template. Use a simple Ollma model, tinyllama, for this. 
# 5. Print the answer

from ollama import ChatResponse, chat


def main():
    # 1. Make the system prompt for summariseing a text
    system_prompt = "You are a helpful assistant that summarises text. You will be given a piece of text, and you will return a concise summary of the main points in the text. The summary should be no more than 3 sentences long."

    # 2. Get the user prompt
    user_prompt = input("Please enter the text you want to summarise: ")

    # # 3. Make the prompt template with zero shot prompting
    # prompt_template = f"{system_prompt}\n\nText: {user_prompt}\nSummary:"

    # 3 and 4. Call the LLM with the user prompt and system prompt. Use a simple Ollma model, tinyllama, for this.
    print("Generating summary...")
    response = call_ollama_model(system_prompt, user_prompt)

    # 5. Print the answer
    summary = (response.message.content or "").strip()
    if summary:
        print(f"Summary: {summary}")
    else:
        print("Summary: [No text returned by model]")

def call_ollama_model(system_prompt: str, user_prompt: str) -> ChatResponse:

    llm_model = "tinyllama"
    response: ChatResponse = chat(
        model=llm_model, 
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ])

    return response


if __name__ == "__main__":
    main()