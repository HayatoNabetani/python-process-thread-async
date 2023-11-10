import requests
import time

URLS = [
    f"https://pokeapi.co/api/v2/pokemon/{i}"
    for i in range(1, 11)
]


def fetch_url(url):
    response = requests.get(url)
    return response.status_code


start_time = time.time()
results = [
    fetch_url(url)
    for url in URLS
]
end_time = time.time()

print("Results:", results)
print("Time taken:", end_time - start_time)
