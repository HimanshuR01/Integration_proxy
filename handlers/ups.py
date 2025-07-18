import asyncio

async def handle_ups(action, parameters):
    # Simulate a UPS API call
    await asyncio.sleep(1)  # Simulating network delay
    xml_input = f"<soap><action>{action}</action><params>{parameters}</params></soap>"
    xml_output = f"<soap-response><status>Ok</status><detail>Action {action} completed</detail></soap-response>"
    return {"xml_input": xml_input, "xml_output": xml_output}