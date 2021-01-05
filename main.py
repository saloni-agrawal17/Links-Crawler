import threading
from spider import Spider
from queue import Queue
from create import *
from domain import *
PROJECT_NAME = 'thesite'
HOMEPAGE = 'https://dazzling-kids-pre-school.business.site/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()

spider = Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)



def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links)>0:
        print(str(len(queued_links))+'Links in the queue')
        create_jobs()


def create_jobs():
    for links in file_to_set(QUEUE_FILE):
        queue.put(links)
        queue.join()
        crawl()


def create_workers():
    for thread in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while True:
        url = queue.get()
        print(url)
        spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


create_workers()
crawl()
