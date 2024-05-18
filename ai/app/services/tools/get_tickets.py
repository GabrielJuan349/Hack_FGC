from pathlib import Path
import pandas as pd

# function to get the tickets from the .csv file

def ingest_tickets():
    """
    Ingests ticket data from a CSV file and returns a list of ticket objects.

    Returns:
        list: A list of ticket objects, where each object contains the following attributes:
            - line (str): The line of the ticket.
            - type (str): The type of the ticket.
            - ticket (str): The name of the ticket.
            - zone (str): The zones covered by the ticket.
            - price (float): The price of the ticket.
    """
    # get path to "billetes2020.csv"
    p = Path(__file__).parent / "billetes2020.csv"
    # read the .csv file
    df = pd.read_csv(p, sep=";")

    tickets = []

    for index, row in df.iterrows():
        # line
        line = row["Linea"]

        fgc_integrado = row["Billete de FGC/Integrados/Combinados"]

        # get the ticket name
        type = row["Tipo de billete"]
        ticket = row["Billete"]

        zone = row["Zonas"]

        # get the ticket price
        price = row["Precio"]
 
        # add the ticket to the list of tickets
        obj = {
            "line": line,
            "type": type,
            "ticket": ticket,
            "zone": zone,
            "price": price
        }

        tickets.append(obj)

    return tickets

tickets = ingest_tickets()

def get_fgc_tickets(origin: str, zone: int, familia_numerosa_o_monoparental: bool) -> list[dict]:
    """
    Retrieves FGC tickets based on the specified origin, zone, and family status.

    Args:
        origin (str): The origin of the ticket.
        zone (int): The zone of the ticket.
        familia_numerosa_o_monoparental (bool): Indicates whether the ticket is for a family with a large family or single parent.

    Returns:
        list[dict]: A list of filtered FGC tickets.
    """
    zone = int(zone)
    tickets_filtered = []

    i = 0 

    if familia_numerosa_o_monoparental:
        # filter tickets for Familia Numerosa or Monoparental
        for ticket in tickets:
            if "FM/FN general" in ticket["ticket"]: # and ticket["zone"] == zone:
                print(ticket)
                ticket['index'] = i
                i += 1
                tickets_filtered.append(ticket)
    else:
        tickets_filtered = tickets

    print(len(tickets_filtered))

    tickets_filtered_filtered = []

    for ticket in tickets_filtered:
        if origin in ticket["line"] and ticket["zone"] == zone:
            ticket['index'] = i
            i += 1
            tickets_filtered_filtered.append(ticket) 
        
        if ticket["line"] == "Totes" and ticket["zone"] == zone:
            ticket['index'] = i
            i += 1
            tickets_filtered_filtered.append(ticket)
        
    return tickets_filtered

# function to get the lines from the .csv file

def ingest_lines():
    """
    Reads a CSV file containing ticket information and returns a list of lines and zones.

    Returns:
        list: A list of dictionaries, where each dictionary represents a line and its corresponding zone.
              Each dictionary has the following keys:
              - "line": The line number.
              - "zone": The zone associated with the line.
    """
    # get path to "billetes2020.csv"
    p = Path(__file__).parent / "billetes2020.csv"
    # read the .csv file
    df = pd.read_csv(p, sep=";")

    lines = []

    for index, row in df.iterrows():
        # line
        line = row["Linea"]
        zone = row["Zonas"]

        obj = {
            "line": line,
            "zone": zone
        }

        lines.append(obj)

    return lines

lines = ingest_lines()

def get_fgc_lines() -> list[str]:
    return lines