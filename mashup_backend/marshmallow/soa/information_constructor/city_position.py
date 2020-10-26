from marshmallow.soa.information_fetcher.amap_city_position import get_amap_city_position


def get_city_position(city_name: str) -> dict:
    temp_dict, _ = get_amap_city_position(city_name)
    return_dict = dict()
    return_dict["city_name"] = city_name
    # this is an xmltodict issue.
    try:
        city_center = temp_dict["response"]["districts"]["district"][0]["center"]
    except KeyError: 
        city_center = temp_dict["response"]["districts"]["district"]["center"]
    city_center_list = city_center.split(',')
    city_center_longitude = float(city_center_list[0])
    city_center_latitude = float(city_center_list[1])
    return_dict["city_center"] = city_center
    return_dict["city_center_longitude"] = city_center_longitude
    return_dict["city_center_latitude"] = city_center_latitude
    return return_dict
