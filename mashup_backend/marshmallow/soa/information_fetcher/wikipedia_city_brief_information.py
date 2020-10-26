import requests
from urllib import parse
import json
import sys
from typing import Tuple
from config import config_json_str
from marshmallow.common.utils.strings import get_proxy_address_from_protocol_and_address_and_port


def get_wikipedia_city_brief_information(city_name: str) -> Tuple[dict, str]:
    """
    Get wikipedia brief information(as shown in popups)
    :param city_name: string, city name to query.
    :return: result in dict and json string format
    """
    config_dict = json.loads(config_json_str)
    proxy_protocol = config_dict["proxy_options"]["proxy_protocol"]
    proxy_address = config_dict["proxy_options"]["proxy_address"]
    proxy_port = config_dict["proxy_options"]["proxy_port"]
    proxy_address = get_proxy_address_from_protocol_and_address_and_port(
        proxy_protocol, proxy_address, proxy_port)
    wikipedia_summary_api_endpoint = "https://zh.wikipedia.org/api/rest_v1/page/summary/"
    r = requests.get(wikipedia_summary_api_endpoint + parse.quote(city_name.strip()),
                     proxies=dict(http=proxy_address, https=proxy_address))
    temp_dict = json.loads(r.text)
    return temp_dict, r.text


def main(argv):
    _, wikipedia_city_brief_information_json_str = get_wikipedia_city_brief_information(
        argv[0])
    print(wikipedia_city_brief_information_json_str)


if __name__ == '__main__':
    main(sys.argv[1:])
