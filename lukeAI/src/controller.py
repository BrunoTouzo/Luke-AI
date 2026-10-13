# imports
from langchain_ollama import OllamaLLM as ol
from langchain_core.prompts import ChatPromptTemplate
import model as m

class Chatbot():

    def __init__(self):
        pass
        # attributes
        self.info:dict = {}
        self.info_path:str = "lukeAI\\env\\info.json"
        self.context_path = "lukeAI\\env\\context_history.json"
        self.context:dict = {}
        self.turn_counter:int = 0

        # Getting models info from env
        self.info = m.load_json(self.info_path)


    def handle_context_history(self,message:str) -> None:
        self.context[f'turn {self.turn_counter}'] = message
        self.turn_counter+=1


    def save_context_history(self) -> str:
        response = m.save_json(self.context_path,self.context)
        if response == -1:
            print('\n**An error ocurred while trying to save the context history,'+
                ' please check the information and try again later**\n')


    def chatting(self,user_prompt:str) -> str:

        #str treatment before creating full response
        if user_prompt is None or user_prompt.strip() == '':
            return 'empty / invalid prompt'

        # Creating response
        user_prompt = user_prompt.lower().strip()
        chain_template = """
            Answer the user question below.

            Here is the conversation history for knowledge: {context}

            question:{question}
        """

        # setting ai model and prompt template
        model = ol(model=self.info["AI_MODEL"])
        prompt = ChatPromptTemplate.from_template(chain_template)
        chain = prompt | model

        # fetching result
        result:str = chain.invoke({"context":self.context,"question":user_prompt}).strip()

        # storing the conversation history
        self.handle_context_history(f'User: {user_prompt}')
        self.handle_context_history(f'Chat: {result}')

        # returning result
        return result