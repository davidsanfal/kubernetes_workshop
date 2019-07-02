from flask import Flask, jsonify
import requests
import os
app = Flask(__name__)

cpu_request = '{}/api/v1/query?query=container_cpu_user_seconds_total\{pod_name="{}",container_name="{}"\}'


@app.route("/")
def version():
    url = os.getenv("PROMETHEUS_API_URL") + '/api/v1/query?query=container_cpu_user_seconds_total{pod_name="' + os.getenv("POD_NAME") + '",container_name="' + os.getenv("CONTAINER_NAME")+'"}'
    r = requests.get(url)
    # return jsonify({'url': url, 'response': r.text})
    return jsonify(r.json().get('data', {}).get('result', [{}])[0])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
