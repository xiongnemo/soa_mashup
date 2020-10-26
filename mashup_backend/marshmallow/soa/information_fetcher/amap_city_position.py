from config import config_json_str
import xmltodict
import requests
from urllib import parse
import json
import sys
from typing import Tuple


def get_amap_city_position(city_name: str) -> Tuple[dict, str]:
    """
    Get city position and corresponding stats from Amap
    :param city_name: string, city name to query.
    :return: result in dict and xml string format
    """
    config_dict = json.loads(config_json_str)
    amap_web_service_api_key = config_dict["api_keys"]["amap"]["web_service_api_key"]
    amap_api_endpoint = "https://restapi.amap.com/v3/config/district?&subdistrict=2&key=" + \
        amap_web_service_api_key + "&extensions=base&output=xml&keywords="
    r = requests.get(amap_api_endpoint + parse.quote(city_name.strip()))
    temp_dict = xmltodict.parse(r.text)
    return temp_dict, r.text


def main(argv):
    _, amap_city_position_json_str = get_amap_city_position(argv[0])
    print(amap_city_position_json_str)


if __name__ == '__main__':
    main(sys.argv[1:])
