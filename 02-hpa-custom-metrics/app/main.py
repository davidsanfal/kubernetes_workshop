import threading
import requests


def req():
    response = requests.get("http://192.168.99.120:31699/service?cost=40")
    print(response.text)


threads = []


for a in range(600):
    thread = threading.Thread(target=req)
    threads.append(thread)

print("Starting all Threads")

# Start them all
for thread in threads:
    thread.start()

# Wait for all to complete
for thread in threads:
    thread.join()
