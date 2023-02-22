from bs4 import BeautifulSoup
import requests 

LINK = 'https://qotd.hideoushumpbackfreak.com/'

def get_qotd (link):
    req = requests.get(LINK)
    page_parse = BeautifulSoup(req.text, 'html.parser')
    quote_and_author = page_parse.find('div', {'class':'article__content'}).find_all('p')
    quote = quote_and_author[0].text
    author = quote_and_author[1].text
    return quote, author

if __name__ == "__main__":
    quote, author = get_qotd(LINK)
    print('\n')
    print(quote)
    print('\n')
    print(author)

