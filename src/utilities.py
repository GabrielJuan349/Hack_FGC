from typing import Tuple
import pandas as pd
import numpy as np
import dotenv as env

env_var = env.dotenv_values(".env")

class Get_info:

    url = env_var.get("TICKET_LOCAL_URL")

    def __init__(self):
        self._fee_bd = pd.read_csv(self.url, delimiter=";", index_col=False, header=0)
    
    
    def get_unique_tickets(self, location: str) -> np.array:
        """
        Get unique tickets from the specified location.

        Args:
            location (str): The location (line) from which to retrieve tickets.

        Returns:
            np.array: A NumPy array containing the unique tickets from the given location.
        """
        # Filter tickets based on location
        tickets_filtered = self._fee_bd[self._fee_bd["Linea"] == location]

        # Get unique tickets from the "Billete" column
        unique_tickets = tickets_filtered["Billete"].unique()
        if not unique_tickets.any():
            return unique_tickets 
        else:
            return None

    def get_ticket(self, location:str, ticket:str, zona:int, num_bitllets: int )->Tuple[int, int]:
        """Get the ticket from the location of the file
        Args:
            location (str): Line where the station is located
            ticket (str): Ticket to be searched
            zona (int): Number of zones
        Returns:
            ticket (Tuple[int, int]): Tuple with the ticket information
        """
        ticket = self._fee_bd[(self._fee_bd["Linea"] == location) & (self._fee_bd["Billete"] == ticket) & (self._fee_bd["Zonas"]==zona)]
        if not ticket.empty:
            return (ticket["Precio"].values[0], ticket["Precio"].values[0]*num_bitllets)
        else:
            return None

## Prueba de rendimiento  
# gi = Get_info()
# # gi.get_tickets("Lleida - La Pobla de Segur")
# print(gi.get_unique_tickets("Lleida - La Pobla de Segur"))
# print(gi.get_ticket("Lleida - La Pobla de Segur", "T-10", 1, 10))