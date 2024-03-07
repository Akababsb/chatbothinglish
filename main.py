import discord
import openai
import os

# Discord bot token
TOKEN = os.getenv('DISCORD_TOKEN')

# OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize the Discord client
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)

# Set up OpenAI API
openai.api_key = OPENAI_API_KEY

# Function to generate response from OpenAI
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Event handler for when a message is received
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Generate response
    prompt = message.content
    response = generate_response(prompt)
    await message.channel.send(response)

# Run the bot
client.run(TOKEN)
