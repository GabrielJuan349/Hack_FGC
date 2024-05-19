import os
# from tts.transform_Text_Speech import text_to_speech
from .tts.transform_Text_Speech import text_to_speech
from .tools.get_tickets import get_fgc_lines, get_fgc_tickets
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
                "description": "The ticket to confirm",
            },
            "amount": {
                "type": "number",
                "description": "The quantity of tickets to confirm",
            },
            "price": {
                "type": "number",
                "description": "The price of the ticket",
            },
            "zones": {
                "type": "string",
                "description": "The zones covered by the ticket",
            },
        },
        "required": [
            "ticket",
            "quantity",
        ],
    },
)

cancel_order = FunctionDeclaration(
    name="cancel_order",
    description="Cancel the order",
    parameters={
        "type": "object",
        "properties": {
            "ticket": {
                "type": "string",
                "description": "The ticket to cancel",
            },
            "amount": {
                "type": "number",
                "description": "The quantity of tickets to cancel",
            },
            "price": {
                "type": "number",
                "description": "The price of the ticket",
            },
            "zones": {
                "type": "string",
                "description": "The zones covered by the ticket",
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
            "ticket": {
                "type": "string",
                "description": "The ticket that will be put on the card",
            },
            "amount": {
                "type": "number",
                "description": "The quantity of tickets to confirm",
            },
            "price": {
                "type": "number",
                "description": "The price of the ticket",
            },
            "zones": {
                "type": "string",
                "description": "The zones covered by the ticket",
            },
        },
        "required": [
            "card",
            "amount",
        ],
    },
)

# confirm_purchase = FunctionDeclaration(
#     name="confirm_purchase",
#     description="Confirm the purchase",
#     parameters={
#         "type": "object",
#         "properties": {
#             "ticket": {
#                 "type": "string",
#                 "description": "The ticket to confirm",
#             },
#             "amount": {
#                 "type": "number",
#                 "description": "The quantity of tickets to confirm",
#             },
#             "price": {
#                 "type": "number",
#                 "description": "The price of the ticket",
#             },
#             "zones": {
#                 "type": "string",
#                 "description": "The zones covered by the ticket",
#             },
#         },
#     },
# )

fgc_tool = Tool(
    function_declarations=[
        get_available_tickets,
        get_available_lines,
        order_ticket,
        recharge_card,
        cancel_order,
        # confirm_purchase,
    ],
)


class GeminiService:
    def __init__(self, location= "Lleida", max_quantity=5):
        self.location = location
        self.max_quantity = max_quantity

        self.options = {}

        # system_instruction = f"""
        # You are building a chatbot that helps users use the FGC (Ferrocarrils de la Generalitat de Catalunya) in Barcelona.
        # The chatbot should be able to help users buy a ticket (Transport card) or recharge an existing transport card.
        # The chatbot should be able to provide information about the different types of tickets available, their prices, and the zones they cover.
        # Do not ask the user where they are, as you know that the ticket machine is in {self.location}, so the user is in {self.location}. Do not ask the user their destination; ask them how many zones they want to travel through.
        # Always use tools to get the information about the tickets and lines; do not assume the information.
        # Always show the prices of the tickets, and if the user asks for the price of a ticket, show the price of the ticket they asked for.
        # Always show the zones of the tickets, and if the user asks for the zones of a ticket, show the zones of the ticket they asked for.
        # Always ask for zones; do not assume the user wants to travel to a specific zone.
        # The chatbot should be able to provide information about available tickets and lines if the user asks for it.
        # Some tickets are for FM (Families Monoparentals) and FN (Families Nombroses). If the user asks for a ticket of this type, ask them if they are a FM or FN.
        # Do not allow the user to buy a ticket with a discount if they are not a FM or FN. They also need to provide their Familia Monoparental or Familia Numerosa card number to get these tickets.
        # Allow only buying a maximum of {self.max_quantity} tickets at a time.
        # Always ask the user if they want to buy a ticket or recharge an existing transport card.
        # Always get their Familia Monoparental or Familia Numerosa status before showing the tickets.

        # In case of recharge, the user should have scanned the card before asking for the recharge. Do not allow the user to recharge a card if they have not scanned it. Do not ask the user for the card number, as you know the card number from the scan.

        # You will get {options} as a JSON with info from the machine, like the card number, the ticket number, if the user has a Familia Monoparental or Familia Numerosa card, if the user has scanned the card, etc. Use this information to provide the user with the information they need.

        # If the user confirms the purchase, send the order to the machine. If the user confirms the recharge, send the recharge to the machine.
        # """

        system_instruction = f"""
        Eres un chatbot que ayuda a los usuarios a utilizar los FGC (Ferrocarrils de la Generalitat de Catalunya) en Barcelona.
        El chatbot debe ser capaz de ayudar a los usuarios a comprar un billete (tarjeta de transporte) o recargar una tarjeta de transporte existente.
        El chatbot debe ser capaz de proporcionar información sobre los diferentes tipos de billetes disponibles, sus precios y las zonas que cubren.
        No preguntes al usuario dónde está, ya que sabes que la máquina de billetes está en {self.location}, por lo que el usuario está en {self.location}. No preguntes al usuario su destino; pregúntale cuántas zonas quiere viajar.
        Siempre utiliza herramientas para obtener la información sobre los billetes y líneas; no asumas la información.
        Siempre muestra los precios de los billetes, y si el usuario pregunta por el precio de un billete, muestra el precio del billete que ha preguntado.
        Siempre muestra las zonas de los billetes, y si el usuario pregunta por las zonas de un billete, muestra las zonas del billete que ha preguntado.
        Siempre pregunta por las zonas; no asumas que el usuario quiere viajar a una zona específica.
        El chatbot debe ser capaz de proporcionar información sobre los billetes y líneas disponibles si el usuario lo solicita.
        Algunos billetes son para FM (Familias Monoparentales) y FN (Familias Numerosas). Si el usuario pide un billete de este tipo, pregúntale si es FM o FN.
        No permitas que el usuario compre un billete con descuento si no es FM o FN. También debe proporcionar su número de tarjeta de Familia Monoparental o Familia Numerosa para obtener estos billetes.
        Permite la compra de un máximo de {self.max_quantity} billetes a la vez.
        Siempre pregunta al usuario si quiere comprar un billete o recargar una tarjeta de transporte existente.
        Siempre obtén su estado de Familia Monoparental o Familia Numerosa antes de mostrar los billetes.

        En caso de recarga, el usuario debe haber escaneado la tarjeta antes de pedir la recarga. No permitas que el usuario recargue una tarjeta si no la ha escaneado. No preguntes al usuario por el número de la tarjeta, ya que conoces el número de la tarjeta por el escaneo.
        Si la tarjeta es blanca, el usuario asociado a ella es anonimo. Por tanto, no se le puede aplicar el descuento de familia monoparental o numerosa. Avise al usuario de que no se le aplicará el descuento.
        Pide al usuario que tipo de billete quiere comprar para recargar su tarjeta, y cuántos billetes quiere comprar. No permitas que el usuario compre más de {self.max_quantity} billetes a la vez para recargar su tarjeta.

        Recibirás a cada conversación un JSON  {self.options} con información que te da la máquina, como por ejemplo el identificador de tarjeta si el usuario quiere recargar, el número de billete, si el usuario tiene una tarjeta de Familia Monoparental o Familia Numerosa, si el usuario ha escaneado la tarjeta, etc. Usa esta información para proporcionar al usuario la información que necesita.
        
        Si el usuario confirma la compra, envía el pedido a la máquina. Si el usuario confirma la recarga, envía la recarga a la máquina.
       
        """


        
        self.model = GenerativeModel(
            "gemini-1.5-pro-preview-0514",
            generation_config=GenerationConfig(temperature=0),
            tools=[fgc_tool],
            system_instruction=system_instruction,
        )

        self.chat = self.model.start_chat(response_validation=False)
    
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

            op = input("Enter your options: ")

            if op:
                self.options = {
                    "options": op
                }

            try:
                joined_options = " ".join([f"{key}: {value}" for key, value in self.options.items()])

                print(f"Options: {joined_options}")

                joined_message = f"{q} {joined_options}"

                response = self.chat.send_message(joined_message) # Send the user's question to Gemini

                function_calls = self.extract_function_calls(response)

                print(function_calls)

                if function_calls:
                    print(self.call_functions(function_calls))
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
    
    def return_response_json(self, response: str, action: str, options: Dict):
        base64_audio = text_to_speech(response)

        return  {
            "audio": base64_audio,
            "plain_text": response,
            "action": action,
            "options": options
        }
                 

    def call_functions(self, function_calls: List[Dict]):
        print("Function calls extracted from response:")
        print(function_calls)
        api_response = {}

        result = None

        action = None
        options = None

        # Loop over multiple function calls
        for function_call in function_calls:
            # Extract the function name
            print(function_call)
            for key in function_call:
                function_name = key

            # Determine which external API call to make
            if function_name == "get_available_tickets":
                result = get_fgc_tickets(function_call["get_available_tickets"]["origin"], function_call["get_available_tickets"]["zone"], function_call["get_available_tickets"]["familia_numerosa_o_monoparental"])
                action = "show_tickets"
            elif function_name == "get_available_lines":
                result = get_fgc_lines()
                action = "show_lines"
            elif function_name == "order_ticket":
                # We return go_to_payment as the action to be taken by the machine
                options = {
                    "ticket": function_call["order_ticket"]["ticket"],
                    "amount": function_call["order_ticket"]["amount"],
                    "price": function_call["order_ticket"]["price"],
                    "zones": function_call["order_ticket"]["zones"],
                }
                action = "go_to_payment"
            elif function_name == "recharge_card":
                # We return go_to_payment as the action to be taken by the machine
                options = {
                    "card": function_call["recharge_card"]["card"],
                    "ticket": function_call["recharge_card"]["ticket"],
                    "amount": function_call["recharge_card"]["amount"],
                    "price": function_call["recharge_card"]["price"],
                    "zones": function_call["recharge_card"]["zones"],
                }
                action = "go_to_payment"
            elif function_name == "cancel_order":
                # We return cancel_order as the action to be taken by the machine
                options = {
                    "ticket": function_call["cancel_order"]["ticket"],
                    "amount": function_call["cancel_order"]["amount"],
                    "price": function_call["cancel_order"]["price"],
                    "zones": function_call["cancel_order"]["zones"],
                }
                action = "cancel_order"

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

            self.return_response_json(response.text, action, options)
                   
        
        except Exception as e:
            print(str(e))
            self.return_response_json("Error processing the request", "", {})

    

    def text_to_sql(self, text: str, options: Dict):
        try:
            if options:
                self.options = options
            
            joined_options = " ".join([f"{key}: {value}" for key, value in self.options.items()])

            print(f"Options: {joined_options}")

            joined_message = f"{text} {joined_options}"

            response = self.chat.send_message(joined_message) # Send the user's question to Gemini

            function_calls = self.extract_function_calls(response)

            if function_calls:
                return self.call_functions(function_calls)
            elif response.text:
                return self.return_response_json(response.text, "just_talk", {})
        except Exception as e:
            print(str(e))
            self.return_response_json("Error processing the request", "", {})
        
    def initial_poke(self, options: Dict):
        try:
            if options:
                self.options = options
                
            joined_options = " ".join([f"{key}: {value}" for key, value in self.options.items()])

            print(f"Options: {joined_options}")

            joined_message = f"{"Hola"} {joined_options}"
            
            response = self.chat.send_message(joined_message)

            function_calls = self.extract_function_calls(response)

            if function_calls:
                return self.call_functions(function_calls)
            elif response.text:
                return self.return_response_json(response.text, "just_talk", {})
        except Exception as e:
            print(str(e))
            self.return_response_json("Error processing the request", "", {})

if __name__ == "__main__":
    gemini_service = GeminiService()
    gemini_service.run_cli()
