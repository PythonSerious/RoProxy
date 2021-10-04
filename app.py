from flask import Flask, request, abort, jsonify
import requests
import json
import os

print("booting...")



app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhookpost():
    try:
        jsonfile = request.json
        payloadurl = str(jsonfile['payloadurl'])
        result = requests.post(payloadurl, json=jsonfile['payload'])
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:

            return json.dumps({'error': str(err)}), 400
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))
            return '', 200
    except Exception as err:
        raise err
        return json.dumps({"error": str(Exception)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

