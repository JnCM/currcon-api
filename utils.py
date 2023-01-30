import constants
import requests
from flask import request


def get_params():
    from_curr = request.args.get('from', '')
    to_curr = request.args.get('to', '')
    amount = float(request.args.get('amount', 0.0))
    return from_curr, to_curr, amount

def make_api_call(from_curr, to_curr, amount):
    try:
        url = constants.BASE_URL + "convert"
        headers = {
            "apikey": constants.API_KEY
        }
        params = {
            "from": from_curr,
            "to": to_curr,
            "amount": amount
        }
        response = requests.get(url, params=params, headers=headers)
        response = response.json()
        if "result" in response:
            return "success", round(response["result"], 2)
        else:
            return "An unexpected error occurred!", 0.0
    except Exception as e:
        return e, 0.0
