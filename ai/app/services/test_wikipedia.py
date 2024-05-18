import os
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


search_wikipedia = FunctionDeclaration(
    name="search_wikipedia",
    description="Search for articles on Wikipedia",
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Query to search for on Wikipedia",
            },
        },
    },
)

suggest_wikipedia = FunctionDeclaration(
    name="suggest_wikipedia",
    description="Get suggested titles from Wikipedia for a given term",
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Query to search for suggested titles on Wikipedia",
            },
        },
    },
)

summarize_wikipedia = FunctionDeclaration(
    name="summarize_wikipedia",
    description="Get article summaries from Wikipedia",
    parameters={
        "type": "object",
        "properties": {
            "topic": {
                "type": "string",
                "description": "Query to search for article summaries on Wikipedia",
            },
        },
    },
)

wikipedia_tool = Tool(
    function_declarations=[
        search_wikipedia,
        suggest_wikipedia,
        summarize_wikipedia,
    ],
)

model = GenerativeModel(
    "gemini-1.5-pro-preview-0514",
    generation_config=GenerationConfig(temperature=0),
    tools=[wikipedia_tool],
)
chat = model.start_chat()

prompt = "Show the search results, variations, and article summaries about Wikipedia articles related to the solar system"

response = chat.send_message(prompt)

function_calls = extract_function_calls(response)


api_response = {}

# Loop over multiple function calls
for function_call in function_calls:
    # Extract the function name
    print(function_call)
    for key in function_call:
        function_name = key

    # Determine which external API call to make
    if function_name == "search_wikipedia":
        result = wikipedia.search(function_call["search_wikipedia"]["query"])
    if function_name == "suggest_wikipedia":
        result = wikipedia.suggest(function_call["suggest_wikipedia"]["query"])
    if function_name == "summarize_wikipedia":
        result = wikipedia.summary(
            function_call["summarize_wikipedia"]["topic"], auto_suggest=False
        )

    # Collect all API responses
    api_response[function_name] = result


# Return the API response to Gemini
response = chat.send_message(
    Part.from_function_response(
        name="search_wikipedia",
        response={
            "content": api_response,
        },
    ),
)


print(response.text)