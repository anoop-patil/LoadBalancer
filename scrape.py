# import threading
# from bs4 import BeautifulSoup
# import requests
# import time
#
# def scrape_website(url):
#     print(f"Scraping {url}")
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     title = soup.find('title').text
#     print(f"Title of the {url} is {title}")
#
#
# urls = [
#     'https://www.python.org',
#     'https://www.github.com',
#     'https://www.stackoverflow.com',
#     'https://www.reddit.com'
# ]
#
# start_time = time.time()
# threads = []
#
# for url in urls:
#     thread = threading.Thread(target=scrape_website, args=(url,))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# #Synchronously scraping the URLs - takes an inordinate
# # amount of time compared to the threading based approach.
# # for url in urls:
# #     scrape_website(url)
#
# print(f"Scraped {len(urls)}
# websites in{time.time() - start_time} seconds...")
#
#
#
#
# import threading
#
# class SafeCounter:
#     def __init__(self):
#         self.counter = 0
#         self.lock = threading.Lock()
#
#     def increment(self):
#         with self.lock:
#             self.counter += 1
#             print(f"Counter is now at {self.counter}")
#
#
#
# def increment_counter(safe_counter):
#     for _ in range(1000):
#         safe_counter.increment()
#
#
# counter = SafeCounter()
#
# threads = []
#
# for _ in range(10):
#     thread = threading.Thread(target=increment_counter, args=(counter, ))
#     threads.append(thread)
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
#
# print(f"Final Counter value is {counter.counter}")
#
#
#
#
#
# from concurrent.futures import ThreadPoolExecutor
# import concurrent.futures
#
# import urllib.request
#
#
# URLS = [
#     'http://www.foxnews.com/',
#     'http://www.cnn.com/',
#     'http://europe.wsj.com/',
#     'http://www.bbc.co.uk/',
# ]
#
#
# def load_url(url, timeout):
#     with urllib.request.urlopen(url, timeout=timeout) as conn:
#         return conn.read()
#
#
# with ThreadPoolExecutor(max_workers=4) as executor:
#     future_to_url = {executor.submit(load_url, url, 10): url for url in URLS}
#     for future in concurrent.futures.as_completed(future_to_url):
#         url = future_to_url[future]
#         try:
#             data = future.result()
#             print(f"{url} is {len(data)} bytes")
#         except Exception as exc:
#             print(f"{url} generated an exception: {exc}")
#
# from multiprocessing import Pool
# import time
#
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def calculate_primes(n):
#     return [x for x in range(n) if is_prime(x)]
#
# start = time.time()
# numbers = [1000000, 2000000, 3000000, 4000000,
# 5000000, 6000000, 7000000, 8000000]
# with Pool(processes=8) as pool:
#     results = pool.map(calculate_primes, numbers)
#     for result in results:
#         print(f"Found {len(result)} primes...")
#
#
# #
# # for n in numbers:
# #     primes = calculate_primes(n)
# #     print(f"Found {len(primes)} primes...")
#
# stop = time.time()
# print(f"Time taken to complete: {stop - start} seconds")
