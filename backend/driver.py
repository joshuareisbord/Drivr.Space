"""
This is the intents module
"""
from backend.query_response import get_response_wit
from backend.generate_response import generate_research_response_json
from backend.wit_message import witObjects  # This might need to be changed when moving project to AWS
import json

def intent_driver(message: json) -> json:
    """
    Passing a message will determine the intent, and respond with the vehicle information.
    :param message: json message passed from the website
    :return: json containing all the information for said vehicle.
    """
    response = witObjects(get_response_wit(message))

    # intents = response.get_intents()

    make = response.get_make_and_model()["make"][0]["body"]
    model = response.get_make_and_model()["model"][0]["body"]

    print(make)
    print(model)

    try:
        if response.get_intents()["name"] == "buy_vehicle":
            # Do this
            return "buy"
        elif response.get_intents()["name"] == "research_vehicle":
            # Collect information about the exact vehicle in the message.
            return generate_research_response_json(make, model)
        elif response.get_intents()["name"] == "sell_vehicle":
            # Do this
            return "sell"
        else:
            return "What went wrong here?"
    except:
        raise Exception("There was an error, message did not have an intent")

if __name__ == '__main__':
    message = "i want to learn about the Porsche 911"
    print(intent_driver(message))
