from .salesforce import handle_salesforce
from .ups import handle_ups

PROVIDERS = {
    "salesforce": handle_salesforce,
    "ups": handle_ups,
}

def get_handler(name):
    return PROVIDERS.get(name)