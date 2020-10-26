import requests
from urllib import parse
import json
import sys
from typing import Tuple
from config import config_json_str


def get_tianqi_city_weather(city_name: str) -> Tuple[dict, str]:
    """
    Get city weather and aqi stats from Tianqi API
    :param city_name: string, city name to query.
    :return: result in dict and json string format
    """
    config_dict = json.loads(config_json_str)
    tianqi_api_appid = config_dict["api_keys"]["tianqi_api"]["appid"]
    tianqi_api_appsecret = config_dict["api_keys"]["tianqi_api"]["appsecret"]
    tianqi_api_endpoint = "https://www.tianqiapi.com/api/?appid=" + tianqi_api_appid + \
        "&appsecret=" + tianqi_api_appsecret + "&version=v9&cityid=0&city="
    r = requests.get(tianqi_api_endpoint + parse.quote(city_name.strip()))
    temp_dict = json.loads(r.text)
    return temp_dict, r.text


def main(argv):
    _, tianqi_city_weather_json_str = get_tianqi_city_weather(argv[0])
    print(tianqi_city_weather_json_str)


if __name__ == '__main__':
    main(sys.argv[1:])
