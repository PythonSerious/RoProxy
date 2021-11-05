# PythonSerious - 2021
try:
    import os
    os.system('python3 -m pip install --upgrade pip')
except:
    pass


try:
    from flask import Flask, request, abort, jsonify

except:
    import os
    os.system('pip3 install flask')
    try:
        from flask import Flask, request, abort, jsonify
    except:
        os.system('pip install flask')
        try:
            from flask import Flask, request, abort, jsonify
        except:
            os.system('python3 -m pip install flask')
            from flask import Flask, request, abort, jsonify
import requests
import json
import os

print("booting...")

with open("config.json", "r") as f:
    config = json.load(f)

app = Flask(__name__)

webhookRoute = config["endpoint"]

@app.route(f"/{webhookRoute}", methods=["POST"])
def webhookpost():
    try:
        try:
            print(request.json)
            jsonfile = request.json
            payloadurl = str(jsonfile['payloadurl'])

        except:
            print(request.data)
            jsonfile = json.loads(request.data)
            payloadurl = str(jsonfile['payloadurl'])
        result = requests.post(payloadurl, json=jsonfile['payload'])
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:

            return json.dumps({'error': str(err)}), 400
        else:
            print("Payload delivered successfully, code {}.".format(result.status_code))
            return 'Payload delivered successfully.', 200
    except Exception as err:
        return json.dumps({"error": str(err)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(config["port"]))
