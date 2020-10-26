# SOA Project

Backend for SOA mashup project, Semester 1, Tongji SSE 2020

## Prerequisites

``` bash
pip3 install flask flask_cors gevent bs4
pip3 install -U requests[socks] # use bash here, don't use zsh
```

Place an SSL certificate if you want to use `https`.

## Config

`config.py` contains config for backend, in `JSON` str format for Python.

``` json
config_json_str = """
{
    "listen_options": {
        "port_num": ****, // port number to listen on. Value is an int.
        "use_http": **** // if we should use http even if SSL certificate is provided. Can be true / false.
    },
    "proxy_options": {  // !!! Be sure to enter right proxy here as it affects Wikipedia's API! Inproper config would let the API calling failed and thus cause the frontend to throw error.
        "proxy_protocol": "****",  // Controls proxy protocol. Popular options include "http" and "socks5".
        "proxy_address": "***", // Proxy address. Value is a vaild hostname or IP address.
        "proxy_port": "****" // Proxy port. Value is an int.
    },
    "api_keys": {
        "amap": {
            "web_service_api_key": "****************************" // Fill your Amap web service API key here.
        },
        "tianqi_api": {
            "appid": "*************", // Fill your Tianqi app id here.
            "appsecret": "********" // Fill your Tianqi app secret here.
        }
    }
}
"""
```

## Debug Run

``` bash
FLASK_APP=marshmallow_soa_webapi_main.py FLASK_ENV=development python -m flask run
```

* by default, it listens on port 5000 on any interface.

## Run

``` bash
python3 ./marshmallow_soa_webapi_main.py
```

* by default, it listens on port 5000 on any interface.

## Data Source and Service Providers

### Map

Amap ([link](https://lbs.amap.com/api/javascript-api/guide/abc/quickstart))

### City Position

Amap ([link](https://lbs.amap.com/api/webservice/guide/api/district))

### City Weather

TianqiAPI ([link](http://doc.tianqiapi.com/603579))

### City News

Baidu Search (unstable)

### City GDP

Baidu Search (unstable)

### City Brief Information

Wikipedia

## API Endpoints

Query: `city_name`.

See `Mashup Response` for detailed information on what exactly each API endpoint returns.

### City GDP Endpoint

`/city_gdp`

returns an `JSON`.

### City Position Endpoint

`/city_position`

returns an `JSON`.

### City Weather Endpoint

`/city_weather`

returns an `JSON`.

### City Brief Information Endpoint

`/city_brief_information`

returns an `JSON`.

### Mashup Endpoint

`/city_gdp`

returns a `XML`.

## Mashup Response

``` xml
<?xml version="1.0" encoding="utf-8"?>
<mashup>
    <city_gdp>
        <city_name>天津</city_name>
        <gdp>14104.28亿元</gdp>
        <gdp_time>(2019年)</gdp_time>
    </city_gdp>
    <city_news>
        <city_name>天津</city_name>
        <news_count>10</news_count>
        <news_list>
            <news_title>落户天津,你还在犹豫和观望</news_title>
            <news_source>腾讯网</news_source>
            <news_time>8小时前</news_time>
            <news_contents>2018年5月16日,天津发布了新的人才引进政策,加入“抢人大战”,在津工作且符合相关条件的本科、大专、中专毕业生可以直接落户。随后就引爆了全国,无数仁人志士纷纷...</news_contents>
        </news_list>
        <news_list>
            <news_title>告别“老破小”!天津住建委发布《天津市城镇老旧小区更新改造工作...</news_title>
            <news_source>腾讯网</news_source>
            <news_time>13分钟前</news_time>
            <news_contents>近日,天津市住房城乡建设委发布关于向社会公开征求《天津市城镇老旧小区更新改造工作方案(征求意见稿)》意见的公告。 公告指出,城镇老旧小区更新改造包括城镇老旧小区...</news_contents>
        </news_list>
        <news_list>
            <news_title>过往频繁跳槽、业绩平淡,新行长会给天津银行带来什么?</news_title>
            <news_source>证券市场红周刊</news_source>
            <news_time>42分钟前</news_time>
            <news_contents>刚刚迎来70后新行长的天津银行遭遇投资者用脚投票,本周二股价一度创下历史新低,仅为2.70港元。就上市商业银行的市场表现来说,天津银行是2016年以来表现最差的商业...</news_contents>
        </news_list>
        <news_list>
            <news_title>天津考古勘探发现古代墓葬近900处 为运河文化提供实证</news_title>
            <news_source>央视新闻</news_source>
            <news_time>6小时前</news_time>
            <news_contents>天津市文化遗产保护中心日前组织完成了对西青区大运河国家文化公园、文化小镇建设区域的考古勘探,发现区域内古代墓葬近900处,据墓葬形制、埋深、包含物信息等推测,其...</news_contents>
        </news_list>
        <news_list>
            <news_title>支援前线的“天津故事”</news_title>
            <news_source>北方网</news_source>
            <news_time>8小时前</news_time>
            <news_contents>《天津日报》刊载的《津四万余青年集会 黄敬同志作时事报告》的消息。 工商业大游行队伍行至和平区中心花园路。 电车公司职工加紧赶制机车,支援抗美援朝。 1951年4...</news_contents>
        </news_list>
        <news_list>
            <news_title>总书记重要讲话在天津引发强烈反响:沿着英雄足迹不断砥砺奋进</news_title>
            <news_source>北方网</news_source>
            <news_time>7小时前</news_time>
            <news_contents>天津北方网讯:连日来,习近平总书记在纪念中国人民志愿军抗美援朝出国作战70周年大会上的重要讲话,在本市干部群众中引起强烈反响。大家纷纷表示,要把伟大抗美援朝精神...</news_contents>
        </news_list>
        <news_list>
            <news_title>曝光| 天津10个地方被举报!情况通报来了!</news_title>
            <news_source>澎湃新闻</news_source>
            <news_time>5小时前</news_time>
            <news_contents>调查核实情况:经查,万科金域华府小区西侧墙外“喀斯特木业”原租赁“丽明纺织公司”厂房,“卡斯特木业”已于2019年10月停业注销;现厂房租赁给“天津味美特餐饮服务有...</news_contents>
        </news_list>
        <news_list>
            <news_title>咱天津的“粉丝”越来越多了</news_title>
            <news_source>新华网天津站</news_source>
            <news_time>7小时前</news_time>
            <news_contents>日前,由国家文旅部、天津市政府共同主办的2020中国旅游产业博览会圆满收官,期间线上总浏览量达116.3万人次,依托旅博会官网展示交易平台的交易额达4260万元,依托...</news_contents>
        </news_list>
        <news_list>
            <news_title>天津发现古代墓葬800余座</news_title>
            <news_source>新华网客户端</news_source>
            <news_time>8小时前</news_time>
            <news_contents>日前,记者从天津市文化遗产保护中心了解到,该中心近期在天津境内考古勘探发现古代墓葬800余座,据初步推测,墓葬的年代涵盖了宋、金、元至明清各个不同历史时期。此次...</news_contents>
        </news_list>
        <news_list>
            <news_title>天津:更多老年人实现“老有所养”</news_title>
            <news_source>潇湘晨报</news_source>
            <news_time>7小时前</news_time>
            <news_contents>天津北方网讯:中午11时半,西青区精武镇付村村民刘松棠,准时来到村里的康养中心,中心内设的老人家食堂内已经有不少乡亲在用餐。付村老人家食堂,是西青区精武镇首...</news_contents>
        </news_list>
    </city_news>
    <city_brief_information>
        <city_name>天津</city_name>
        <brief_intro>天津市，简称津，是中华人民共和国直辖市、国家中心城市和中国北方最大沿海开放城市。天津位于华北平原的海河各支流交汇处，东临渤海，北依燕山；有海河在城中蜿蜒而过，跨越海河的各式桥梁形成了“一桥一景”的景致。</brief_intro>
        <brief_intro_html>&lt;p&gt;&lt;b&gt;天津市&lt;/b&gt;，简称&lt;b&gt;津&lt;/b&gt;，是中华人民共和国直辖市、国家中心城市和中国北方最大沿海开放城市。天津位于华北平原的海河各支流交汇处，东临渤海，北依燕山；有海河在城中蜿蜒而过，跨越海河的各式桥梁形成了“一桥一景”的景致。&lt;/p&gt;</brief_intro_html>
    </city_brief_information>
    <city_position>
        <city_name>天津</city_name>
        <city_center>117.190182,39.125596</city_center>
        <city_center_longitude>117.190182</city_center_longitude>
        <city_center_latitude>39.125596</city_center_latitude>
    </city_position>
    <city_weather>
        <city_name>天津</city_name>
        <current_weather>晴</current_weather>
        <current_temp>17</current_temp>
        <today_temp_low>10</today_temp_low>
        <today_temp_high>21</today_temp_high>
        <current_aqi>117</current_aqi>
        <current_aqi_str>轻度污染</current_aqi_str>
    </city_weather>
</mashup>
```
