
import asyncio
import aiohttp
import requests
from top_articles.models import Story
from django.core.exceptions import ObjectDoesNotExist

def check_db_story_ids(articlesID_list):
    new_articleID_list = []
    for id in articlesID_list:
        try:
            Story.objects.get(id=id)
        except ObjectDoesNotExist:
            new_articleID_list.append(id)
    return new_articleID_list


def get_article_urls(url):
    """
    Fetch all ids of top trending articles
    args: None
    return:None
    """
    articlesID_list = requests.get(
        url).json()
    url_list = []
    print("article length",len(articlesID_list))
    newarticlesID_list = check_db_story_ids(articlesID_list)
    for id in newarticlesID_list:
        url ="https://hacker-news.firebaseio.com/v0/item/%s.json?print=pretty" % id
        url_list.append(url)
    return url_list, articlesID_list, newarticlesID_list

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
    else:
        return None

def main(url):
    urls_list, articlesID_list, newarticlesID_list = get_article_urls(url)
    print(urls_list, articlesID_list, newarticlesID_list)
    result_dict = fetch_articles(urls_list)
    return result_dict, articlesID_list, newarticlesID_list
