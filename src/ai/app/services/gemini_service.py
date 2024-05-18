import os
from tools.get_tickets import get_fgc_lines, get_fgc_tickets
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")  # Get the value of PROJECT_ID from .env file
LOCATION = "us-central1"  # @param {type:"string"}

import vertexai
import wikipedia

vertexai.init(project=PROJECT_ID, location=LOCATION)


from typing import List, Dict
from vertexai.generative_models import (
    Content,
    GenerationConfig,
    GenerationResponse,
    GenerativeModel,
    HarmCategory,
    HarmBlockThreshold,
    Image,
    FunctionDeclaration,
    Part,
    Tool,
)
from vertexai.language_models import TextEmbeddingModel
from vertexai.vision_models import MultiModalEmbeddingModel



get_available_tickets = FunctionDeclaration(
    name="get_available_tickets",
    description="Gets list of available tickets you can get from FGC (Ferrocarrils de la Generalitat de Catalunya) in Barcelona. The user should provide the origin and the zone he wants to travel to.",
    parameters={
        "type": "object",
        "properties": {
            "origin": {
                "type": "string",
                "description": "Origin of the ticket",
            },
            "zone": {
                "type": "number",
                "description": "Zone of the ticket",
            },
            "familia_numerosa_o_monoparental": {
                "type": "boolean",
                "description": "Whether the user is a Familia Monoparental or Familia Numerosa",
            },
        },
        "required": [
            "origin",
            "zone",
            "familia_numerosa_o_monoparental",
        ],
    },
)     

get_available_lines = FunctionDeclaration(
    name="get_available_lines",
    description="Gets list of available lines you can get from FGC (Ferrocarrils de la Generalitat de Catalunya) in Barcelona.",
    parameters={
        "type": "object",
        "properties": {
        },
    }
)

order_ticket = FunctionDeclaration(
    name="order_ticket",
    description="Order a ticket",
    parameters={
        "type": "object",
        "properties": {
            "ticket": {
                "type": "string",
                "description": "The ticket to order",
            },
            "quantity": {
                "type": "number",
                "description": "The quantity of tickets to order",
            },
        },
        "required": [
            "ticket",
            "quantity",
        ],
    },
)

recharge_card = FunctionDeclaration(
    name="recharge_card",
    description="Recharge an existing transport card",
    parameters={
        "type": "object",
        "properties": {
            "card": {
                "type": "string",
                "description": "The card to recharge",
            },
            "amount": {
                "type": "number",
                "description": "The amount to recharge",
            },
        },
        "required": [
            "card",
            "amount",
        ],
    },
)

fgc_tool = Tool(
    function_declarations=[
        get_available_tickets,
        get_available_lines,
        order_ticket,
    ],
)


class GeminiService:
    def __init__(self, location= "Lleida", max_quantity=5):
        self.location = location
        self.max_quantity = max_quantity

        options = {
        }

        system_instruction = f"""
        If user says "Hola", respond with "Hola", and ask him how you can help him. Always answer in Spanish or Catalan.
        You are building a chatbot that helps users using the FGC (Ferrocarrils de la Generalitat de Catalunya) in Barcelona.
        Also, the chatbot should be able to help users buy a ticket (Transport card) or recharge an existing transport card.
        The chatbot should be able to provide information about the different types of tickets available, the prices, and the zones they cover.
        You should not ask the user where he is, as you know that the ticket machine is in {self.location}, so the user is in {self.location}. Don't ask the user the destination, ask him how many zones he wants to travel.
        Always use tools to get the information about the tickets and lines, don't assume the information.
        Always show the prices of the tickets, and if the user asks for the price of a ticket, show the price of the ticket he asked for.
        Always show the zones of the tickets, and if the user asks for the zones of a ticket, show the zones of the ticket he asked for.
        Always ask for zones, don't assume the user wants to travel to a specific zone.
        The chatbot should be able to provide information about available tickets and lines if the user asks for it.
        Some tickets are for FM (Families Monoparentals) and FN (Families Nombroses). If the user asks for a ticket of this type, ask him if he is a FM or FN. 
        Don't allow the user to buy a ticket with a discount if he is not a FM or FN. He also needs to provide his Familia Monoparental or Familia Numerosa card number to get these tickets.
        Allow only buying a maximum of {self.max_quantity} tickets at a time.
        Always ask the user if he wants to buy a ticket or recharge an existing transport card.
        Always get his Familia Monoparental or Familia Numerosa status before showing the tickets. 

        In case of recharge, user should have scanned the card before asking for the recharge. Don't allow the user to recharge a card if he hasn't scanned it. Don't ask the user for the card number, as you know the card number from the scan.

        You will get {options} as a json with info from the machine, like the card number, the ticket number, if the user has a Familia Monoparental or Familia Numerosa card, 
        if the user has scanned the card, etc. Use this information to provide the user with the information he needs.

        """

        self.model = GenerativeModel(
            "gemini-1.5-pro-preview-0514",
            generation_config=GenerationConfig(temperature=0),
            tools=[fgc_tool],
            system_instruction=system_instruction,
        )

        self.chat = self.model.start_chat() 
    
    def run_cli(self):
        # prompt = "Me gustaría pedir un nuevo billete a FGC. ¿Pueden ayudarme? Soy Familia Monoparental y quiero viajar a 2 zonas."

        # response = self.chat.send_message(prompt)

        # try:
        #     if response.text:
        #         print(response.text)
        # except Exception as e:
        #     print(str(e))

        # function_calls = self.extract_function_calls(response)

        # print(function_calls)
                
        # if function_calls:
        #     self.call_functions(function_calls)
        Initial_poke = self.initial_poke()

        print(Initial_poke)


        while True:
            q = input("Enter your question: ")

            response = self.chat.send_message(q) # Send the user's question to Gemini

            function_calls = self.extract_function_calls(response)

            print(function_calls)

            try:
                if function_calls:
                    self.call_functions(function_calls)
                elif response.text:
                    print(response.text)
            except Exception as e:
                print(str(e))


    # Helper function to extract one or more function calls from a Gemini Function Call response
    def extract_function_calls(self, response: GenerationResponse) -> List[Dict]:
        function_calls = []
        if response.candidates[0].function_calls:
            for function_call in response.candidates[0].function_calls:
                function_call_dict = {function_call.name: {}}
                for key, value in function_call.args.items():
                    function_call_dict[function_call.name][key] = value
                function_calls.append(function_call_dict)
        return function_calls

    def call_functions(self, function_calls: List[Dict]):
        print("Function calls extracted from response:")
        print(function_calls)
        api_response = {}

        result = None

        # Loop over multiple function calls
        for function_call in function_calls:
            # Extract the function name
            print(function_call)
            for key in function_call:
                function_name = key

            # Determine which external API call to make
            if function_name == "get_available_tickets":
                result = get_fgc_tickets(function_call["get_available_tickets"]["origin"], function_call["get_available_tickets"]["zone"], function_call["get_available_tickets"]["familia_numerosa_o_monoparental"])
            elif function_name == "get_available_lines":
                result = get_fgc_lines()

            # Collect all API responses
            api_response[function_name] = result

        try:
            # Return the API response to Gemini
            response = self.chat.send_message(
                Part.from_function_response(
                    name=function_name,
                    response={
                        "content": api_response,
                    },
                ),
            )

            print(response.text)

            return response.text
        
        except Exception as e:
            print(str(e))
            return str(e)
    

    def text_to_sql(self, text: str) -> str:
        response = self.chat.send_message(text)

        function_calls = self.extract_function_calls(response)

        if function_calls:
            return self.call_functions(function_calls)
        elif response.text:
            return response.text
        
    def initial_poke(self):
        response = self.chat.send_message("Hola")

        function_calls = self.extract_function_calls(response)

        if function_calls:
            return self.call_functions(function_calls)
        elif response.text:
            return response.text

if __name__ == "__main__":
    gemini_service = GeminiService()
    gemini_service.run_cli()
