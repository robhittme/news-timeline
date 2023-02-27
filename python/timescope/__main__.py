from termcolor import colored, cprint
from configparser import ConfigParser 
import requests
import json
from sys import argv
from timescope import cli, __app_name__

def main():
    cli.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()

#config = ConfigParser()
#config.read('config.ini')
#
#API_KEY = config['news']['NYTApiKey'] 
#
#url = ('https://api.nytimes.com/svc/search/v2/articlesearch.json')
#
#class Article(object):
#    date = ""
#    web_url = ""
#    headline = ""
#
#    def __init__(self, date, web_url, headline):
#        self.date = date
#        self.web_url = web_url
#        self.headline = headline
#    
#
##TODO: will get rate limited at 10. will want to filter more. thats a 100 stories. can filter?
#def get_articles_by_timeline_topic(topic, page = 0, counter = 0):
#    if counter == 10:
#        return
#    query_params = {
#            "q": topic,
#            "begin_date": "20230124",
#            "end_date": "20230224",
#            "fl": "pub_date,snippet,web_url,headline",
#            "fq": "source:(\"The New York Times\"),news_desk:(\"Foreign\")",
#            "sort": "newest",
#            "page": page,
#            "api-key": API_KEY
#    }
#    response = requests.get(url,params=query_params)
#    articles = response.json()
#    if len(articles) > 0:
#        for article in articles["response"]["docs"]:
#            date = article["pub_date"]
#            web_url =  article["web_url"]
#            headline = article["headline"]["main"]
#            a = Article(date, url, headline)
#            print(json_formatter(a))
#    if len(articles["response"]["docs"]) == 10:
#        get_articles_by_timeline_topic(topic, page+1, counter+1)
#
#def json_formatter(js):
#    return json.dumps(js.__dict__, indent=2)
#
#if __name__ == "__main__":
#    if argv[1]:
#        print(f"Getting news for {argv[1]}...\n")
#        get_articles_by_timeline_topic(argv[1])
#
