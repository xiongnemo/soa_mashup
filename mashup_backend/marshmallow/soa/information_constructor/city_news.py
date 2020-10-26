from marshmallow.soa.information_fetcher.baidu_city_news import baidu_news_with_city_name

def get_city_news(city_name: str) -> dict:
    temp_list, _ = baidu_news_with_city_name(city_name)
    return_dict = dict()
    return_dict["city_name"] = city_name
    return_dict["news_count"] = len(temp_list)
    return_dict["news_list"] = temp_list
    return return_dict