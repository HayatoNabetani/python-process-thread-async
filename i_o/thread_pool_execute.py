import requests
from concurrent.futures import ThreadPoolExecutor
import time

URLS = [
    f"https://pokeapi.co/api/v2/pokemon/{i}"
    for i in range(1, 11)
]


def fetch_url(url):
    response = requests.get(url)
    return response.status_code


def run_threadpool_executor():
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch_url, URLS))

    return results


start_time = time.time()
results = run_threadpool_executor()
end_time = time.time()

print("Results:", results)
print("Time taken:", end_time - start_time)
