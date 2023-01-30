import utils
from flask import Flask


app = Flask(__name__)

@app.route("/", methods=["GET"])
def convert():
    try:
        from_curr, to_curr, amount = utils.get_params()
        result = utils.make_api_call(from_curr, to_curr, amount)
        output = {
            "msg": result[0],
            "result": result[1]
        }
    except Exception as e:
        output = {
            "msg": e,
            "result": 0.0
        }
    return output