import subprocess
import threading
import requests
import platform
import time


minikube = {
    'Linux': 'minikube',
    'Darwin': 'minikube',
    'Windows': 'minikube.exe',
}.get(platform.system(), None)
if minikube:
    count = 0
    while(count < 9):
        count += 1
        result = subprocess.run([minikube, 'ip'], stdout=subprocess.PIPE)
        minikube_ip = result.stdout.decode('utf-8').rstrip()

        def req():
            response = requests.get("http://{}:30010/service?cost=40".format(minikube_ip))
            if not response.status_code == 200:
                print(response.text)

        threads = []

        for a in range(600):
            thread = threading.Thread(target=req)
            threads.append(thread)

        print("[{}]: Starting all Threads".format(count))

        # Start them all
        for thread in threads:
            thread.start()

        # Wait for all to complete
        for thread in threads:
            thread.join()
        time.sleep(20)
