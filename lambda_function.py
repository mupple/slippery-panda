import os
import json
from datetime import date


TODAY = date.today()


def string_to_date(date_string):
    [year, month, date] = [int(s) for s in date_string.split("-")]
    return date(year, month, day)
    
    
def is_in_the_past(date_string):
    return string_to_date(date_string) < TODAY



def get_intent_name(event):
    return event['sessionState']['intent']['name']
    
    
def get_invocation_source(event):
    return event['invocationSource']





def delegate(event):
    return {
        "sessionState": {
            "dialogAction": {
                "type": "Delegate"
            }
        }
    }


handlers = {
    "BookCar": {
        "DialogCodeHook": delegate,
        "FulfillmentCodeHook": delegate,
    },
    "BookHotel": {
        "DialogCodeHook": delegate,
        "FulfillmentCodeHook": delegate,
    },
    "BookFlight": {
        "DialogCodeHook": delegate,
        "FulfillmentCodeHook": delegate,
    },
}



def router(event):
    intent_name = get_intent_name(event)
    invocation_source = get_invocation_source(event)
    
    
    # By default, allow the chatbot to proceed with its proposed action
    handler = delegate
    
    # Now see if there any handlers for this intent_name
    if intent_name in handlers and handlers[intent_name] is not None:
        intent_handlers = handlers[intent_name]
        
        # If so, is there a handler for this particular invocation_source (i.e. DialogCodeHook or FulfillmentCodeHook)?
        if invocation_source in intent_handlers and intent_handlers[invocation_source] is not None:
            # If so, use it instead of the default
            handler = intent_handlers[invocation_source]
            
    return handler


def lambda_handler(event, context):
    # Log the incoming event for dev purposes
    print(event)
    
    # Find the appropriate handler
    handler = router(event)
    
    # Create the response
    response = handler(event)
    
    # Log the response for dev purposes
    print(response)
    
    # and send it on its way
    return response
  
