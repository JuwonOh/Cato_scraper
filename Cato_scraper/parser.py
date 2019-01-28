from .utils import get_soup
from .utils import now

def parse_page(url):
    """
    Argument
    --------
    url : str
        Web page url

    Returns
    -------
    json_object : dict
        JSON format web page contents
        It consists with
            title : article title
            time : article written time
            content : text with line separator \\n
            url : web page url
            scrap_time : scrapped time
    """

    try:
        soup = get_soup(url)
        title = soup.find('h1', class_= 'page-h1').text
        time = soup.find('div', class_= 'field-date').text[1:-1]
        content = soup.find('div', class_= 'field-body').text
        author = soup.find('div', id = 'pub-authors').text[6:]

        json_object = {
            'title' : title,
            'time' : time,
            'author' :author,
            'content' : content,
            'url' : url,
            'scrap_time' : now()
        }
        return json_object
    except Exception as e:
        print(e)
        print('Parsing error from {}'.format(url))
        return None
