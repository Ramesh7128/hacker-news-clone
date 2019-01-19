
import asyncio
import aiohttp
import requests
from top_articles.models import Story


def get_article_urls():
    """
    Fetch all ids of top trending articles
    args: None
    return:None
    """
    articlesID_list = requests.get(
        'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty').json()
    url_list = []
    print(len(articlesID_list))
    for id in articlesID_list[:100]:
        url ="https://hacker-news.firebaseio.com/v0/item/%s.json?print=pretty" % id
        url_list.append(url)
    return url_list

async def fetch_url(session, url):
    async with session.get(url, timeout=60 * 60) as response:
        return await response.json()

async def fetch_all_urls(session, urls, loop):
    results = await asyncio.gather(*[fetch_url(session, url) for url in urls],
    return_exceptions=True)
    return results

def fetch_articles(urls):
    if len(urls) > 1:
        loop = asyncio.get_event_loop()
        connector = aiohttp.TCPConnector(limit=100)
        with aiohttp.ClientSession(loop=loop, connector=connector) as session:
            articles = loop.run_until_complete(fetch_all_urls(session, urls, loop))
        raw_result = articles
    return raw_result

def main():
    result_dict = fetch_articles(get_article_urls())
    return result_dict
