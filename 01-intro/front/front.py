from flask import Flask, jsonify
import requests
import os
app = Flask(__name__)


@app.route("/")
def version():
    r = requests.get(os.getenv("DOMAIN_API_URL"))
    return jsonify(
        {
            'version': "Domain api version {}".format(r.json().get('version')),
            'header': dict(r.headers)
        }
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
