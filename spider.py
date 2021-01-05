from urllib.request import urlopen
from link_finder import LinkFinder
from create import *
from domain import *


class Spider:

    def __init__(self, project_name, base_url, domain_name):
        self.project_name = project_name
        self.base_url = base_url
        self.domain_name = domain_name
        self.queue_file = project_name + '/queue.txt'
        self.crawled_file = project_name + '/crawled.txt'
        self.queue = set()
        self.crawled = set()
        self.boot()
        self.crawl_page('First Spider', self.base_url)

    def boot(self):
        create_directory(self.project_name)
        create_data_files(self.project_name, self.base_url)
        self.queue = file_to_set(self.queue_file)
        self.crawled = file_to_set(self.crawled_file)

    def crawl_page(self, thread_name, page_url):
        if page_url not in self.crawled:
            print(thread_name + 'Now crawling ' + page_url)
            print('Queue' + str(len(self.queue)) + ' | Crawled' + str(len(self.crawled)))
            self.add_links_to_queue(self.gather_links(page_url))
            self.queue.remove(page_url)
            self.crawled.add(page_url)
            self.update_files()

    def gather_links(self, page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes = response.read()
                html_string = html_bytes.decode("utf-8")

            finder = LinkFinder(self.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()

    def add_links_to_queue(self, links):
        for url in links:
            if(url in self.queue) or (url in self.crawled):
                continue
            if self.domain_name != get_domain_name(url):
                continue
            self.queue.add(url)

    def update_files(self):
        set_to_file(self.queue, self.queue_file)
        set_to_file(self.crawled, self.crawled_file)
