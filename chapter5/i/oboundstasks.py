"""I/O Bound Tasks"""

import threading
import requests

def download_url(url):
    response = requests.get(url)
    print(f"Downloaded {len(response.content)} bytes from {url}")

urls = [
        "https://leetcode.com",
        "https://openai.com",
        "https://google.com",
        "https://github.com",
]

threads = []

for url in urls:
    t = threading.Thread(target=download_url, args=(url,))
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()

print("All downloads complete!!")



