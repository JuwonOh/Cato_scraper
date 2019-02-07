import re
import time
from .parser import parse_page
from .utils import get_soup
from .utils import news_dateformat
from .utils import user_dateformat
from .utils import strf_to_datetime

patterns = [re.compile('https://www.cato.org/publications/[\w]+')]
url_base = 'https://www.cato.org/publications/archives/studies/all/all?page={}'

def is_matched(url):
    for pattern in patterns:
        if pattern.match(url):
            return True
    return False

def yield_latest_allnews(begin_date, max_num=10, sleep=1.0):
    """
    Artuments
    ---------
    begin_date : str
        eg. 2018-01-01
    max_num : int
        Maximum number of news to be scraped
    sleep : float
        Sleep time. Default 1.0 sec

    It yields
    ---------
    news : json object
    """

    # prepare parameters
    d_begin = strf_to_datetime(begin_date, user_dateformat)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all = []
        url = url_base.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('p', class_= 'text-large experts-more-h')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links

        links_all = ['https://www.cato.org' + i for i in links_all]
        urls = [url for url in links_all if is_matched(url)]

        # scrap
        for url in links_all:

            news_json = parse_page(url)

            # check date
            d_news = strf_to_datetime(news_json['date'], news_dateformat)
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

             # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)

def get_allnews_urls(begin_page=0, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_base.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('p', class_= 'text-large experts-more-h')
        links = [i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))

    links_all = ['https://www.cato.org' + i for i in links_all]
    return links_all

def get_last_page_num():
    """
    Returns
    -------
    page : int
        Last page number.
        eg: 503 in 'https://www.cato.org/publications/archives/studies/all/all?page=72'
    """
    last_page = []

    soup = get_soup('https://www.cato.org/publications/archives/studies/all/all')
    last_page_list = soup.find_all('li', class_ = 'pager-last btn-light last')
    last_page = [i.find('a')['href'] for i in last_page_list]
    last_page = ['https://www.cato.org' + i for i in last_page]
    return last_page
