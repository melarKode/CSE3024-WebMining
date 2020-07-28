import time
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor, as_completed

URLs = ['https://medium.com/@apbetahouse45/asynchronous-web-scraping-in-python-using-concurrent-module-a5ca1b7f82e4',
'https://appliedmachinelearning.blog/2018/07/31/developing-a-fast-indexing-and-full-text-search-engine-with-whoosh-a-pure-python-library/',
'https://www.geeksforgeeks.org/python-positional-index/']

def parse(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    return soup.find_all('a')

with ProcessPoolExecutor(max_workers=4) as executor:
    start = time.time()
    futures = [executor.submit(parse, url) for url in URLs]
    results = []
    for result in as_completed(futures):
        results.append(result)
    end = time.time()
    print('Time taken : {:.6f}s'.format(end-start))