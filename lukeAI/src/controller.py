# imports
from langchain_ollama import OllamaLLM as ol
import json

class Chatbot():

    def __init__(self):
        pass
        # attr
        self.info = {}

        # Getting models info from env
        with open("lukeAI\\env\\info.json", "r") as file:
            self.info = json.load(file)


    def chatting(self,prompt:str) -> str:

        #str treatment before creating full response
        if prompt is None or prompt.strip() == '':
            return 'empty / invalid prompt'

        # Creating response
        prompt = prompt.lower().strip()

        model = ol(model=self.info["AI_MODEL"])

        result:str = model.invoke(input=prompt)
        return result.strip()