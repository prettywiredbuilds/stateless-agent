import anthropic

client = anthropic.Anthropic()

while True:
    user_message = {
        "role": "user",
        "content": input("User: ")
    }

    if user_message["content"] == "quit":
        break

    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1000,
        messages=[user_message],
    ) 

    response = message.content[0].text
    print(response)
