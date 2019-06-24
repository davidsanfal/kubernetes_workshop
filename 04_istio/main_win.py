import subprocess
import requests
import json

result = subprocess.run(["minikube.exe", "ip"], stdout=subprocess.PIPE)
response = requests.get("http://{}".format(result.stdout.decode('utf-8').rstrip()))
print(json.dumps(dict(response.headers), indent=4, sort_keys=True))
print(json.dumps(response.json(), indent=4, sort_keys=True))
# print(response.headers)
# print(response.json())
