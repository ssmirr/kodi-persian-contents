#! /usr/bin/env python -u
# coding=utf-8
from multiprocessing import Process
from scrapy.cmdline import execute       
import os

def remove_file(name):
    if os.path.exists(name):
        os.remove(name)


def execute_spider(crawler_name, output_file_name):
    execute(argv=['scrapy', 'runspider', crawler_name, '-o', output_file_name, '-s', 'LOG_LEVEL=INFO'])
    

def run_crawlers():
    remove_file("TVs.json")
    remove_file("Movies.json")
    # execute_spider('TVSpider.py', 'TVs.json')
    execute_spider('movies/movies/spiders/movie_spider.py', 'Movies.json')
    # os.system('export.py')


if __name__ == "__main__":
    run_crawlers()
