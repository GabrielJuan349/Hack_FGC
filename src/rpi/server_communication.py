import time
from typing import Any

import requests
import logging

from requests import RequestException


class Request:
    audio: str | None = None
    frame: str
    location: str
    options: object | None = None


class ServerCommunication:
    def __init__(self, config: dict):
        self.host = config['host']
        self.endpoint = config['endpoint']

    def call_server(self, frame: str, location: str, audio: str = None, options: object = None) -> dict | Any:
        """
        Call the server with the given action and parameters.
        :param action: Action to be performed on the server.
        :param params: Parameters required for the action.
        :return: Response from the server.
        """
        request = Request()
        request.frame = frame
        request.location = location
        request.audio = audio
        request.options = options

        logging.info(f"Calling server {self.host}/{self.endpoint} with {request.__dict__}...")
        for attempt in range(3):
            try:
                response = requests.get(f"{self.host}/{self.endpoint}",
                                        json=request.__dict__,
                                        headers={'Content-Type': 'application/json'})
            except RequestException:
                response = None
                logging.error("Failed to connect to the server. Please check the server configurations.")

            logging.info(f"Server response: {response}")
            if response.status_code == 200:
                return response.json()
            else:
                logging.error(f"Failed to call server. Status code: {response.status_code}. Reason: {response.reason}")
                logging.info(f"Retrying... ({attempt + 1}/{3})")
                time.sleep(1)

        return -1

# Example usage
# server_communication = ServerCommunication({'host': 'http://localhost:8000', 'endpoint': 'call_gemini'})
# response = server_communication.call_server(frame="frame", location="location",
#                                             audio="BASE64_ENCODED_AUDIO")
# print(response)
