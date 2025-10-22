# Make a basic chatbot
# Input: user question
# Output: response to user

# Ideally the LLM gives a responsible response
# Worry about hallucinations later (maybe...)

# Use OpenAI model
# source: https://platform.openai.com/docs/guides/evals?api-mode=responses
# for memory the source: https://platform.openai.com/docs/guides/conversation-state?api-mode=responses


# Basic format: Single question, single response
# Overall: infinite loop until user exits
# Advanced: implement memory

from openai import OpenAI
client = OpenAI()

# Have a memory of what has been said
history = []

# Infinite loop
while True:

    # User input
    request = input("Ask the chatbot a question: ")

    # Exit condition
    if request.lower() == "exit":
        break

    # Append to history 
    history += [{"role": "user", "content": request}]

    # API call
    response = client.responses.create(
        model="gpt-4.1",
        input=history
    )

    # Print response
    print(response.output_text)
