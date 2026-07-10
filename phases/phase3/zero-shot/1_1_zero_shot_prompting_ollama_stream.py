
# 1. Make the system prompt
# 2. Get the user prompt
# 3. Make the prompt template with zero shot prompting
# 4. Call the LLM with the prompt template. Use a simple Ollma model, tinyllama, for this.
# 5. Print the answer

from ollama import ChatResponse, chat


def main():
    # 1. Make the system prompt for summariseing a text
    system_prompt = "You are a helpful assistant that summarises text. You will be given a piece of text, and you will return a concise summary of the main points in the text. The summary should be no more than 1 sentence long."

    # 2. Get the user prompt
    """
    Sample user prompt:
    Last Saturday, the city library organized a community reading event for children and parents. More than 150 people attended the event, which included storytelling sessions, book exchanges, and creative writing workshops. 
    Local authors spoke about the importance of reading habits and encouraged children to explore different genres. 
    Volunteers also collected donated books for schools in underserved neighborhoods. The event lasted four hours and received positive feedback from attendees, many of whom requested that similar programs be held more often throughout the year.
    
    Expected summary:
    A city library hosted a successful community reading event with storytelling, workshops, and book donations, attracting over 150 attendees and receiving positive feedback.
    """
    user_prompt = input("Please enter the text you want to summarise: ")

    # # 3. Make the prompt template with zero shot prompting
    # prompt_template = f"{system_prompt}\n\nText: {user_prompt}\nSummary:"

    # 3 and 4. Call the LLM with the user prompt and system prompt. Use a simple Ollma model, tinyllama, for this.
    # 5. Print the answer
    print("Generating summary...")
    summary = call_ollama_model(system_prompt, user_prompt)
    if not summary:
        print("Summary: [No text returned by model]")


def call_ollama_model(system_prompt: str, user_prompt: str) -> str:

    stream = chat(
        model="gemma3:4b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        stream=True,)

    # 5. Print the answer as it streams
    parts = []
    for event in stream:
        if event.message and event.message.content:
            print(event.message.content, end="", flush=True)
            parts.append(event.message.content)
    print()  # for newline after streaming is done
    summary = "".join(parts).strip()
    return summary


if __name__ == "__main__":
    main()
