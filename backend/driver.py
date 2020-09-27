"""
This is the intents module
"""
from wit_message import witObjects
import json

def intent_driver(intents: witObjects) -> str:
    try:
        if intents.get_intents()["name"] == "buy_vehicle":
            # Do this
            return "buy"
        elif intents.get_intents()["name"] == "research_vehicle":
            # Do this
            return "research"
        elif intents.get_intents()["name"] == "sell_vehicle":
            # Do this
            return "sell"
        else:
            return "What went wrong here?"
    except:
        raise Exception("There was an error, message did not have an intent")

def send_research_reponse(intent: witObjects) -> json:
    # get vehicle type and model and send it through the wikipedia thing to try to correct the name
    # find the vehicle in the csv file and get information about the newest model year of said vehicle
    # create json reponse containing the summary of the vehicle from wikipedia, and the relevent information about
    # engine size, fuel economy, seats, etc...

    reponse = {
               "make": None,
               "model": None,
               "year": None,
               "vehicle_class": None,
               "rangeCity": None,
               "rangeHwy": None,
               "range": None,
               "mpg": None,
               "fuel_grade": None,
               "drive": None,
               "transmission": None,
               }

    try:
        make = witObjects.get_entities()["vehicle_make:vehicle_make"]

    except:
        make = None
        model = None



