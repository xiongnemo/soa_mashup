from flask import Flask, request, Response
import random
from gevent.pywsgi import WSGIServer
import json
from marshmallow.common.variables.idiot_status_code import idiot_status_code
from marshmallow.common.utils.files import is_file
from marshmallow.common.utils.xml import json_to_xml
from marshmallow.soa.information_constructor.city_gdp import get_city_gdp
from marshmallow.soa.information_constructor.city_news import get_city_news
from marshmallow.soa.information_constructor.city_brief_information import get_city_brief_information
from marshmallow.soa.information_constructor.city_position import get_city_position
from marshmallow.soa.information_constructor.city_weather import get_city_weather
from marshmallow.soa.mashup import mashup
import random
from testcases.frontend_test_data import test_xml_list

app = Flask(__name__)
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.after_request(after_request)

@app.route('/', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH'])
def default():
    return Response("{'you': 'idiot'}", status=random.choice(idiot_status_code), mimetype='application/json')


@app.route('/xmltest', methods=['GET'])
def xmltest():
    xml_str = json_to_xml("""{"you": "idiot"}""")
    return Response(xml_str, mimetype='text/xml')


@app.route('/city_gdp', methods=['GET'])
def city_gdp():
    city_name = request.args.get('city_name')
    return get_city_gdp(city_name)


@app.route('/city_news', methods=['GET'])
def city_news():
    city_name = request.args.get('city_name')
    return get_city_news(city_name)


@app.route('/city_brief_information', methods=['GET'])
def city_brief_information():
    city_name = request.args.get('city_name')
    return get_city_brief_information(city_name)


@app.route('/city_weather', methods=['GET'])
def city_weather():
    city_name = request.args.get('city_name')
    return get_city_weather(city_name)


@app.route('/city_position', methods=['GET'])
def city_position():
    city_name = request.args.get('city_name')
    return get_city_position(city_name)


@app.route('/mashup', methods=['GET'])
def mashup_():
    city_name = request.args.get('city_name')
    xml_str = mashup(city_name)
    return Response(xml_str, mimetype='text/xml')

@app.route('/test', methods=['GET'])
def mashup_test():
    xml_str = random.choice(test_xml_list)
    return Response(xml_str, mimetype='text/xml')

def get_server(port_num: int, use_http: bool):
    print("Will listen on port " + str(port_num) + "...")
    if is_file("privkey.pem") and is_file("fullchain.pem") and (not use_http):
        https_server = WSGIServer(
            ('', port_num), app, keyfile='privkey.pem', certfile='fullchain.pem')
        print("Now serving on https...")
        return https_server
    else:
        http_server = WSGIServer(('', port_num), app)
        print("Now serving on http...")
        return http_server


def main():
    port_num = 5000
    use_http = True
    try:
        with open('config.py') as _:
            from config import config_json_str
            json_data = json.loads(config_json_str)
            port_num = json_data['listen_options']['port_num']
            use_http = json_data['listen_options']['use_http']
        print("Config file found.")
    except FileNotFoundError:
        print("Config file not found. Fallback to default.")
    main_server = get_server(port_num, use_http)
    main_server.serve_forever()


if __name__ == '__main__':
    main()
