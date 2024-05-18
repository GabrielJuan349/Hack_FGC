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

# Helper function to extract one or more function calls from a Gemini Function Call response
def extract_function_calls(response: GenerationResponse) -> List[Dict]:
    function_calls = []
    if response.candidates[0].function_calls:
        for function_call in response.candidates[0].function_calls:
            function_call_dict = {function_call.name: {}}
            for key, value in function_call.args.items():
                function_call_dict[function_call.name][key] = value
            function_calls.append(function_call_dict)
    return function_calls


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

# get_order_info_func = FunctionDeclaration(
#     name="get_order_status",
#     description="Get information about an order",
#     parameters={
#         "type": "object",
#         "properties": {
#             "orderid": {"type": "string", "description": "The order ID"},
#             "zipcode": {"type": "string", "description": "The zipcode where the order was shipped to"},
#         },
#             "required": [
#                     "orderid",
#                     "zipcode"
#                 ]
#     },
# )

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

location = "Lleida"

system_instruction = f"""
You are building a chatbot that helps users using the FGC (Ferrocarrils de la Generalitat de Catalunya) in Barcelona.
Also, the chatbot should be able to help users buy a ticket (Transport card) or recharge an existing transport card.
The chatbot should be able to provide information about the different types of tickets available, the prices, and the zones they cover.
You should not ask the user where he is, as you know that the ticket machine is in {location}, so the user is in {location}. Don't ask the user the destination, ask him how many zones he wants to travel.
Always use tools to get the information about the tickets and lines, don't assume the information.
Always show the prices of the tickets, and if the user asks for the price of a ticket, show the price of the ticket he asked for.
Always show the zones of the tickets, and if the user asks for the zones of a ticket, show the zones of the ticket he asked for.
Always ask for zones, don't assume the user wants to travel to a specific zone.
The chatbot should be able to provide information about available tickets and lines if the user asks for it.
Some tickets are for FM (Families Monoparentals) and FN (Families Nombroses). If the user asks for a ticket of this type, ask him if he is a FM or FN. 
Don't allow the user to buy a ticket with a discount if he is not a FM or FN.
Always get his Familia Monoparental or Familia Numerosa status before showing the tickets.
"""

model = GenerativeModel(
    "gemini-1.5-pro-preview-0514",
    generation_config=GenerationConfig(temperature=0),
    tools=[fgc_tool],
    system_instruction=system_instruction,
)
chat = model.start_chat()

prompt = "Me gustaría pedir un nuevo billete a FGC. ¿Pueden ayudarme?" # Soy Familia Monoparental y quiero viajar a 2 zonas."

response = chat.send_message(prompt)

if response.text:
    print(response.text)

function_calls = extract_function_calls(response)

print(function_calls)


while True:
    q = input("Enter your question: ")

    response = chat.send_message(q) # Send the user's question to Gemini

    function_calls = extract_function_calls(response)

    print(function_calls)

    if function_calls:
        print("Function calls extracted from response:")
        print(function_calls)
        api_response = {}

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


            # Return the API response to Gemini
            response = chat.send_message(
                Part.from_function_response(
                    name=function_name,
                    response={
                        "content": api_response,
                    },
                ),
            )


            print(response.text)

    elif response.text:
        print(response.text)

