import openai
import readline # optional, for command history and editing
import os

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Function to generate bot response
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Main loop for chatbot
while True:
    # Get user input
    try:
        user_input = input("You: ")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        break

    # Generate bot response
    prompt = f"You: {user_input}\nBot:"
    bot_response = generate_response(prompt)

    # Print bot response
    os.system('cls' if os.name == 'nt' else 'clear') # optional, clear the console before printing response
    print(f"Bot: {bot_response}")
