from .utils import get_soup
from .utils import now
from dateutil.parser import parse

def parse_page(url):
    if '/public-opinion-brief/' in url:
        return parse_opinion(url)
    else:
        return parse_normal(url)
    return None


def parse_normal(url):
    def parse_author(soup):
        names = soup.find('div', id='pub-authors')
        if not names:
            return ''
        return names.text[2:-1]

    def parse_title(soup):
        title = soup.find('h1', class_= 'page-h1')
        if not title:
            return ''
        return title.text

    def parse_date(soup):
        date = soup.find('span', class_='date-display-single')
        if not date:
            return ''
        return parse(date.text)

    def parse_content(soup):
        content = soup.find('div', class_= 'field-body')
        if not content:
            return ''
        return content.text

    soup = get_soup(url)
    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'author': parse_author(soup),
        'content': parse_content(soup),
        'scraping_date': now()
    }

def parse_opinion(url):
    def parse_author(soup):
        names = soup.find('div', id='pub-authors')
        if not names:
            return ''
        return names.text[2:-1]

    def parse_title(soup):
        title = soup.find('h1', class_= 'page-h1')
        if not title:
            return ''
        return title.text

    def parse_date(soup):
        date = soup.find('div', class_='field-source-info')
        if not date:
            return ''
        return parse(date.text[5:-101])

    def parse_content(soup):
        temp_content = soup.find_all('p')
        content = '\n'.join([p.text.strip() for p in temp_content])
        if not content:
            return ''
        return content

    soup = get_soup(url)
    return {
        'url': url,
        'title': parse_title(soup),
        'date': parse_date(soup),
        'author': parse_author(soup),
        'content': parse_content(soup),
        'scraping_date': now()
    }
