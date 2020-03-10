import sys
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize
from newspaper import Article
from urllib import parse

print(f"{sys.argv[1]}에 대하여 검색합니다. 최근 뉴스 10 항목")
keyword_naver = parse.quote(sys.argv[1])
URL = f"https://search.naver.com/search.naver?where=news&query={keyword_naver}"

get_requests = requests.get(URL)
links = BeautifulSoup(get_requests.text, 'html.parser').select('ul.type01 dt a')

for link in links:
    try:
        s_link = str(link.get("href"))
        news = Article(s_link, language="ko")
        news.download()
        news.parse()
        print("\n\n\n\n","-"*70)
        print(f"{news.title} \n\n")
        print(f"{summarize(news.text, word_count=49)}")
    except:
        print("\n\n\n\n","-"*70)
        print("undefined")

