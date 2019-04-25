from flask import Flask, jsonify
import os
app = Flask(__name__)


@app.route("/", methods=['GET'])
def version():
    return jsonify({'version': os.getenv("DOMAIN_API_VERSION")})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
