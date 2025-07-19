
import google.generativeai as genai
import chainlit as cl
import random

genai.configure(api_key="AIzaSyB8cvXddzU0gNdfM0DWsV-bFc3BzVB0V_Y")

class OpenAIWrapper:
    @staticmethod
    def chat(model, prompt):
        response = genai.GenerativeModel(model).generate_content(prompt)
        return response.text

def roll_dice():
    return random.randint(1, 6)

@cl.on_message
async def main(message: cl.Message):

    story = OpenAIWrapper.chat("gemini-1.5-flash", "Start a fantasy adventure story.")
    monster = f"Monster attacks! Dice rolled: {roll_dice()}"
    reward = OpenAIWrapper.chat("gemini-1.5-flash", "Give a reward item after battle.")
    response = f"**Story:**\n{story}\n\n**Battle:**\n{monster}\n\n**Reward:**\n{reward}"
    await cl.Message(content=response).send()