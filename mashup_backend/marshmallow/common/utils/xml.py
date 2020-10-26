import xmltodict
import json
from xml.etree.ElementTree import Element, tostring

def json_to_xml(json_str: str) -> str:
    """
    This function uses "xmltodict" module.

    Input: a string in json's format.

    Output: a string in xml's format.

    """
    input_dict=json.loads(json_str)
    xml_str = xmltodict.unparse(input_dict)
    return xml_str


def xml_to_json(xml_str: str) -> str:
    """
    This function uses "xmltodict" module.

    Input: a string in xml's format.

    Output: a string in json's format.

    """
    parsed_dict = xmltodict.parse(xml_str)
    json_str = json.dumps(parsed_dict, indent=4)
    return json_str

def dict_to_xml(tag: str, d: dict):
    '''
    Turns a simple dict of key/value pairs into XML.
    Uses xml.etree.ElementTree.

    Input: 
        para_1: tag of the output xml
        para_2: input dict

    Output: a string in xml's format.

    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    xml_str_binary = tostring(elem)
    xml_str = xml_str_binary.decode('utf-8')
    return xml_str