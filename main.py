from newsapi import NewsApiClient
import json

newsapi = NewsApiClient(api_key='08ab850ca86b42c9beb9211b8e0ecf60')

all_articles = newsapi.get_everything(q='stock market',
                                      from_param='2018-06-30',
                                      to='2018-07-01',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)

top = newsapi.get_top_headlines(sources='the-wall-street-journal')




print(json.dumps(top, sort_keys=True, indent=4))