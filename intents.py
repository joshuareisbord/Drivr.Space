from get_response import get_entities, get_intents

"""
These are the functions called based on intents retutned in the JSON from Wit.ai
"""

def intent_buy_vehicle(json):

    # Try to see if there was the type of vehicle, else prompt asking for it.
    try:
        typeOfVehicle = json["type_of_vehicle:type_of_vehicle"][0][body]

        # Provide some options here, like asking questions to narrow down the search.

    except:
        errorMSG = ""
        return errorMSG



def intent_research_vehicle(json):
    #Something

def intent_sell_vehicle(json):
    #Something
