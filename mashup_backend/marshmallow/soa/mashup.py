from marshmallow.soa.information_constructor.city_gdp import get_city_gdp
from marshmallow.soa.information_constructor.city_news import get_city_news
from marshmallow.soa.information_constructor.city_brief_information import get_city_brief_information
from marshmallow.soa.information_constructor.city_position import get_city_position
from marshmallow.soa.information_constructor.city_weather import get_city_weather
from marshmallow.common.utils.xml import json_to_xml, dict_to_xml
import json


def mashup(city_name: str) -> str:
    try:
        city_gdp_dict = get_city_gdp(city_name)
        city_news_dict = get_city_news(city_name)
        city_brief_information_dict = get_city_brief_information(city_name)
        city_position_dict = get_city_position(city_name)
        city_weather_dict = get_city_weather(city_name)
        return_dict = {
            "mashup": {
                "city_gdp": None,
                "city_news": None,
                "city_brief_information": None,
                "city_position": None,
                "city_weather": None
            }
        }
        return_dict["mashup"]["city_gdp"] = city_gdp_dict
        return_dict["mashup"]["city_news"] = city_news_dict
        return_dict["mashup"]["city_brief_information"] = city_brief_information_dict
        return_dict["mashup"]["city_position"] = city_position_dict
        return_dict["mashup"]["city_weather"] = city_weather_dict
        json_str = json.dumps(return_dict, indent=4)
        return json_to_xml(json_str)
    except:
        xml_str = json_to_xml("""{"you": "idiot"}""")
        return xml_str
