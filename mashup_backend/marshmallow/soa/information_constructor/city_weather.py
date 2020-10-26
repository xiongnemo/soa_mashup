from marshmallow.soa.information_fetcher.tianqi_api_city_weather import get_tianqi_city_weather

def get_city_weather(city_name: str) -> dict:
    temp_dict, _ = get_tianqi_city_weather(city_name)
    return_dict = dict()
    return_dict["city_name"] = city_name
    return_dict["current_weather"] = temp_dict["data"][0]["wea"]
    return_dict["current_temp"] = temp_dict["data"][0]["tem"]
    return_dict["today_temp_low"] = temp_dict["data"][0]["tem2"]
    return_dict["today_temp_high"] = temp_dict["data"][0]["tem1"]
    return_dict["current_aqi"] = temp_dict["aqi"]["air"]
    return_dict["current_aqi_str"] = temp_dict["aqi"]["air_level"]
    return return_dict