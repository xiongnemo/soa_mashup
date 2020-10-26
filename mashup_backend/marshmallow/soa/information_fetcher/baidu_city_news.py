from bs4 import BeautifulSoup
import requests
from urllib import parse
import json
import sys
from typing import Tuple
from marshmallow.common.variables.http_headers_collection import baidu_headers


class CityNews:
    def __init__(self, news_title, news_source, news_time, news_contents):
        self.news_title = news_title
        self.news_source = news_source
        self.news_time = news_time
        self.news_contents = news_contents


def parse_baidu_news_html(baidu_news_contents: str) -> list:
    """
    Parse Baidu News's html(百度资讯)
    :param baidu_news_contents: string, baidu's news html contents
    :return: list of news selected, consult CityNews Class for assistance
    """
    soup = BeautifulSoup(baidu_news_contents, "html.parser")
    news_tags = soup.select("div[data-cost]")
    assert len(news_tags) != 0
    city_news_list = []
    for temp_tag in news_tags:
        lines = temp_tag.text.splitlines()
        for i in lines:
            if i == "":
                lines.remove(i)
        temp_news = CityNews(lines[0], lines[-3], lines[-2], lines[-1].rstrip("百度快照"))
        city_news_list.append(temp_news.__dict__)
    return city_news_list


def baidu_news_with_city_name(city_name: str) -> Tuple[list, str]:
    """
    Get Baidu News in dict
    :param city_name: string, city name to query.
    :return: news list in dict and json string format
    """
    baidu_news_endpoint = "https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&rsv_dl=ns_pc&word="
    s = requests.session()
    s.get("https://www.baidu.com/", headers=baidu_headers)
    r = s.get(baidu_news_endpoint + parse.quote(city_name.strip()),
              headers=baidu_headers)
    city_news_list = parse_baidu_news_html(r.text)
    city_news_list_json_str = str(city_news_list).replace("'", "\"")
    city_news_list_json_loaded = json.loads(city_news_list_json_str)
    return city_news_list_json_loaded, city_news_list_json_str


def main(argv):
    _, baidu_news_json_str = baidu_news_with_city_name(argv[0])
    print(baidu_news_json_str)


if __name__ == '__main__':
    main(sys.argv[1:])
