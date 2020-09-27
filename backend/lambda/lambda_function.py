import json
import boto3
from query_response import get_response_wit
from generate_response import generate_research_response_json
from wit_message import witObjects

def lambda_handler(event, context):
    # TODO implement
    print(event)
    event = json.loads(event)
    message = event["body"]
    print(message)
    out = {}
    try:
        """
        Passing a message will determine the intent, and respond with the vehicle information.
        :param message: json message passed from the website
        :return: json containing all the information for said vehicle.
        """
        response = witObjects(get_response_wit(message))
    
        intents = response.get_intents()
        print(intents)
        make = response.get_make_and_model()["make"][0]["body"]
        model = response.get_make_and_model()["model"][0]["body"]
    
        print(make)
        print(model)
        
        if response.get_intents()["name"] == "research_vehicle":
            # Collect information about the exact vehicle in the message.
            out = generate_research_response_json(make, model)

    except Exception as e:
        print(e)
        return {
            "headers": {
                "Access-Control-Allow-Origin" : "*", 
        		"Access-Control-Allow-Methods": "GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE, PATCH",
        		"Access-Control-Allow-Credentials" : "true",
        		"Access-Control-Allow-Headers": "status,date,content-type,content-length,x-amzn-requestid,x-amz-apigw-id,x-amzn-trace-id"
            },
            'statusCode': 500,
            'body': str(e)
            
        }
        
    return {
        "headers": {
            "Access-Control-Allow-Origin" : "*", 
    		"Access-Control-Allow-Methods": "GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE, PATCH",
    		"Access-Control-Allow-Credentials" : "true",
    		"Access-Control-Allow-Headers": "status,date,content-type,content-length,x-amzn-requestid,x-amz-apigw-id,x-amzn-trace-id"
        },
        'statusCode': 200,
        'body': out
    }

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


