from bs4 import BeautifulSoup
import requests
from urllib import parse
import sys
from typing import Tuple
from marshmallow.common.variables.http_headers_collection import baidu_headers


class CityGdp:
    def __init__(self, gdp_city_name, gdp, gdp_time):
        self.gdp_city_name = gdp_city_name
        self.gdp = gdp
        self.gdp_time = gdp_time


def deal_with_city_name(city_name: str) -> str:
    if city_name[-1] != "市":
        return (city_name + "市")
    return city_name


def parse_baidu_gdp_html(baidu_gdp_contents: str) -> dict:
    """
    Parse Baidu City GDP's html(百度)
    :param baidu_gdp_contents: string, baidu's gdp html contents
    :return: list of gdp selected, consult CityNews Class
    """
    soup = BeautifulSoup(baidu_gdp_contents, "html.parser")
    gdp_city_name_tags = soup.select("p.op_exactqa_s_prop")
    assert len(gdp_city_name_tags) == 1
    city_name = gdp_city_name_tags[0].text.strip().strip("GDP：")
    gdp_tags = soup.select("div.op_exactqa_s_answer")
    assert len(gdp_tags) == 1
    gdp_tag_text_splited = gdp_tags[0].text.strip().splitlines()
    gdp = gdp_tag_text_splited[0]
    gdp_time = gdp_tag_text_splited[1].strip()
    city_gdp_data = CityGdp(city_name, gdp, gdp_time)
    return city_gdp_data.__dict__


def baidu_gdp_with_city_name(city_name: str) -> Tuple[dict, str]:
    """
    Get City GDP in dict
    :param city_name: string, city name to query.
    :return: gdp list in dict and json string format
    """
    baidu_gdp_endpoint = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd="
    s = requests.session()
    s.get("https://www.baidu.com/", headers=baidu_headers)
    # print(deal_with_city_name(city_name.strip()))
    r = s.get(baidu_gdp_endpoint + parse.quote(deal_with_city_name(
        city_name.strip()) + " GDP"), headers=baidu_headers)
    city_gdp_dict = parse_baidu_gdp_html(r.text)
    # print(str(city_gdp_dict))
    city_gdp_dict_json_str = str(city_gdp_dict).replace("'", "\"")
    return city_gdp_dict, city_gdp_dict_json_str


def main(argv):
    _, baidu_gdp_json_str = baidu_gdp_with_city_name(argv[0])
    print(baidu_gdp_json_str)


if __name__ == '__main__':
    main(sys.argv[1:])
