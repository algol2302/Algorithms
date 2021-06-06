"""A simple web-crawler app based on BFS"""

import re
import logging

import requests

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s  %(message)s")
logger = logging.getLogger(name=__name__)


class WebCrawler:

    def __init__(self):
        # we want to avoid revisiting the same website over and over
        # again
        self.discovered_websites = []

    def crawl(self, start_url):
        queue = [start_url]
        self.discovered_websites.append(start_url)

        # this is a standard breadth-first search
        while queue:
            actual_url = queue.pop(0)
            logging.info(actual_url)

            # this is the raw html representation of the given website
            # (URL)
            actual_url_html = self.read_raw_html(url=actual_url)

            for url in self.get_links_from_html(raw_html=actual_url_html):
                if url not in self.discovered_websites:
                    self.discovered_websites.append(url)
                    queue.append(url)

    @staticmethod
    def get_links_from_html(raw_html: str):
        return re.findall(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", raw_html)

    @staticmethod
    def read_raw_html(url: str):

        raw_html = ''

        try:
            raw_html = requests.get(url).text
        except Exception as exc:
            logger.error(exc)

        return raw_html


def main():
    crawler = WebCrawler()
    crawler.crawl('https://www.cnn.com')


if __name__ == '__main__':
    main()
