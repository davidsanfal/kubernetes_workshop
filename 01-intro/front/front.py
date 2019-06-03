from flask import Flask
import requests
import os
app = Flask(__name__)


@app.route("/")
def version():
    r = requests.get(os.getenv("DOMAIN_API_URL")).json().get('version')
    return "Domain api version {}".format(r)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
