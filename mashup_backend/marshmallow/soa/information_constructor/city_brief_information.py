from marshmallow.soa.information_fetcher.wikipedia_city_brief_information import get_wikipedia_city_brief_information

def get_city_brief_information(city_name: str) -> dict:
    temp_dict, _ = get_wikipedia_city_brief_information(city_name)
    return_dict = dict()
    return_dict["city_name"] = city_name
    return_dict["brief_intro"] = temp_dict["extract"]
    return_dict["brief_intro_html"] = temp_dict["extract_html"]
    return return_dict