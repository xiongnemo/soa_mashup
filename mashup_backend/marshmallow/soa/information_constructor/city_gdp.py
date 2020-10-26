from marshmallow.soa.information_fetcher.baidu_city_gdp import baidu_gdp_with_city_name

def get_city_gdp(city_name: str) -> dict:
    temp_dict, _ = baidu_gdp_with_city_name(city_name)
    return_dict = dict()
    return_dict["city_name"] = city_name
    return_dict["gdp"] = temp_dict["gdp"].lstrip("(").rstrip(")")
    return_dict["gdp_time"] = temp_dict["gdp_time"]
    return return_dict