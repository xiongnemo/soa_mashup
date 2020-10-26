const { Table } = require("element-ui");
const { xml2js } = require("xml-js");

exports.install = function(Vue, options) {
    Vue.prototype.$soa_city_position = function(city_name, amap_center) { //全局函数1
        var httpRequest_city_position = new XMLHttpRequest();
        var city_position_base_url =
            "http://127.0.0.1:5000/city_position?city_name=";
        httpRequest_city_position.open(
            "GET",
            city_position_base_url + city_name,
            true
        );
        httpRequest_city_position.send();
        httpRequest_city_position.onreadystatechange = function() {
            if (
                httpRequest_city_position.readyState == 4 &&
                httpRequest_city_position.status == 200
            ) {
                var json = httpRequest_city_position.responseText;
                var city_position_element = document.getElementById(
                    "soa_city_position_answer"
                );
                var city_position = JSON.parse(json);
                city_position_element.textContent = city_position["city_center"];
                amap_center.pop()
                amap_center.pop()
                amap_center.push(city_position["city_center_longitude"])
                amap_center.push(city_position["city_center_latitude"])
                    // amap_center.values = [city_position["city_center_longitude"], city_position["city_center_latitude"]].values
                console.log(amap_center)
            }
        };
    };
    Vue.prototype.$soa_city_weather = function(city_name) { //全局函数2
        var httpRequest_city_weather = new XMLHttpRequest();
        var city_weather_base_url =
            "http://127.0.0.1:5000/city_weather?city_name=";
        httpRequest_city_weather.open(
            "GET",
            city_weather_base_url + city_name,
            true
        );
        httpRequest_city_weather.send();
        httpRequest_city_weather.onreadystatechange = function() {
            if (
                httpRequest_city_weather.readyState == 4 &&
                httpRequest_city_weather.status == 200
            ) {
                var json = httpRequest_city_weather.responseText;
                var city_weather = JSON.parse(json);
                var city_weather_element = document.getElementById(
                    "soa_city_weather_answer_weather"
                );
                city_weather_element.textContent = city_weather["current_weather"];
                var city_weather_element = document.getElementById(
                    "soa_city_weather_answer_temp"
                );
                city_weather_element.textContent = city_weather["current_temp"];
                var city_weather_element = document.getElementById(
                    "soa_city_weather_answer_temp_high"
                );
                city_weather_element.textContent = city_weather["today_temp_high"];
                var city_weather_element = document.getElementById(
                    "soa_city_weather_answer_temp_low"
                );
                city_weather_element.textContent = city_weather["today_temp_low"];
                var city_weather_element = document.getElementById(
                    "soa_city_weather_answer_aqi"
                );
                city_weather_element.textContent = city_weather["current_aqi"];
                var city_weather_element = document.getElementById(
                    "soa_city_weather_answer_aqi_str"
                );
                city_weather_element.textContent = city_weather["current_aqi_str"];
            }
        };
    };
    Vue.prototype.$soa_city_brief_information = function(city_name) { //全局函数3
        var httpRequest_city_brief_information = new XMLHttpRequest();
        var city_brief_information_base_url =
            "http://127.0.0.1:5000/city_brief_information?city_name=";
        httpRequest_city_brief_information.open(
            "GET",
            city_brief_information_base_url + city_name,
            true
        );
        httpRequest_city_brief_information.send();
        httpRequest_city_brief_information.onreadystatechange = function() {
            if (
                httpRequest_city_brief_information.readyState == 4 &&
                httpRequest_city_brief_information.status == 200
            ) {
                var json = httpRequest_city_brief_information.responseText;
                var city_brief_information_element = document.getElementById(
                    "soa_city_brief_information_answer"
                );
                var city_brief_information = JSON.parse(json);
                city_brief_information_element.textContent = city_brief_information["brief_intro"];
            }
        };
    };
    Vue.prototype.$soa_city_news = function(city_name, news_data) { //全局函数4
        var httpRequest_city_news = new XMLHttpRequest();
        var city_news_base_url =
            "http://127.0.0.1:5000/city_news?city_name=";
        httpRequest_city_news.open(
            "GET",
            city_news_base_url + city_name,
            true
        );
        var temp
        httpRequest_city_news.send();
        httpRequest_city_news.onreadystatechange = function() {
            if (
                httpRequest_city_news.readyState == 4 &&
                httpRequest_city_news.status == 200
            ) {
                var json = httpRequest_city_news.responseText;
                // var city_news_element = document.getElementById(
                //     "soa_city_news_answer"
                // );
                var city_news = JSON.parse(json);
                var city_news_list = city_news["news_list"].splice(0, 8);
                city_news_list.forEach((element) => {
                    news_data.push({
                        news_title: element.news_title,
                        news_contents: element.news_contents,
                        news_source: element.news_source,
                        news_time: element.news_time,
                    });
                });
            }
        };
        return temp
    };
    Vue.prototype.$soa_city_gdp = function(city_name) { //全局函数5
        var httpRequest_city_gdp = new XMLHttpRequest();
        var city_gdp_base_url =
            "http://127.0.0.1:5000/city_gdp?city_name=";
        httpRequest_city_gdp.open(
            "GET",
            city_gdp_base_url + city_name,
            true
        );
        httpRequest_city_gdp.send();
        httpRequest_city_gdp.onreadystatechange = function() {
            if (
                httpRequest_city_gdp.readyState == 4 &&
                httpRequest_city_gdp.status == 200
            ) {
                var json = httpRequest_city_gdp.responseText;
                var city_gdp = JSON.parse(json);
                var city_gdp_element = document.getElementById(
                    "soa_city_gdp_answer_gdp"
                );
                city_gdp_element.textContent = city_gdp["gdp"];
                var city_gdp_element = document.getElementById(
                    "soa_city_gdp_answer_year"
                );
                console.log(city_gdp["gdp_time"])
                city_gdp_element.textContent = city_gdp["gdp_time"];
            }
        };
    };
    Vue.prototype.$soa_mashup_test = function(amap_center, news_data) { //全局函数6
        var httpRequest_mashup = new XMLHttpRequest();
        var mashup_base_url =
            "http://127.0.0.1:5000/test";
        httpRequest_mashup.open(
            "GET",
            mashup_base_url,
            true
        );
        httpRequest_mashup.send();
        httpRequest_mashup.onreadystatechange = function() {
            if (
                httpRequest_mashup.readyState == 4 &&
                httpRequest_mashup.status == 200
            ) {
                var response = httpRequest_mashup.responseText;
                var test = document.getElementsByClassName("grid-content");
                for (let index = 0; index < test.length; index++) {
                    const element = test[index];
                    element.style.visibility = "visible";
                }
                var test = document.getElementsByClassName("amap-copyright");
                test[0].style.visibility = "visible";
                var test = document.getElementById("soa-header");
                test.textContent = "Now Testing..";
                parser = new DOMParser();
                xmlDoc = parser.parseFromString(response, "text/xml");
                var convert = require('xml-js');
                // console.log(xmlDoc)
                // console.log(xmlDoc.getElementsByTagName("news_list"));
                var response_json = convert.xml2json(response, { compact: true, spaces: 4 })
                var response_dict = JSON.parse(response_json);
                console.log(response_dict);

                var city_position_element = document.getElementById(
                    "soa_city_position_answer"
                );
                // city position
                var city_position = response_dict["mashup"]["city_position"];
                console.log(city_position);
                city_position_element.textContent = city_position["city_center"]["_text"];
                amap_center.pop()
                amap_center.pop()
                amap_center.push(parseFloat(city_position["city_center_longitude"]["_text"]))
                amap_center.push(parseFloat(city_position["city_center_latitude"]["_text"]))
                    // city weather
                var city_weather = response_dict["mashup"]["city_weather"];
                console.log(city_weather);
                var city_weather_element = document.getElementById(
                    "soa_city_weather_answer_weather"
                );
                city_weather_element.textContent = city_weather["current_weather"]["_text"];
                var city_weather_element = document.getElementById(
                    "soa_city_weather_answer_temp"
                );
                city_weather_element.textContent = city_weather["current_temp"]["_text"];
                var city_weather_element = document.getElementById(
                    "soa_city_weather_answer_temp_high"
                );
                city_weather_element.textContent = city_weather["today_temp_high"]["_text"];
                var city_weather_element = document.getElementById(
                    "soa_city_weather_answer_temp_low"
                );
                city_weather_element.textContent = city_weather["today_temp_low"]["_text"];
                var city_weather_element = document.getElementById(
                    "soa_city_weather_answer_aqi"
                );
                city_weather_element.textContent = city_weather["current_aqi"]["_text"];
                var city_weather_element = document.getElementById(
                    "soa_city_weather_answer_aqi_str"
                );
                city_weather_element.textContent = city_weather["current_aqi_str"]["_text"];
                // city brief information
                var city_brief_information_element = document.getElementById(
                    "soa_city_brief_information_answer"
                );
                var city_brief_information = response_dict["mashup"]["city_brief_information"];
                console.log(city_brief_information);
                city_brief_information_element.textContent = city_brief_information["brief_intro"]["_text"];
                // city news
                var city_news_list = response_dict["mashup"]["city_news"]["news_list"];
                console.log(city_news_list);
                city_news_list.forEach((element) => {
                    news_data.push({
                        news_title: element.news_title._text,
                        news_contents: element.news_contents._text,
                        news_source: element.news_source._text,
                        news_time: element.news_time._text,
                    });
                });
                // city GDP
                var city_gdp = response_dict["mashup"]["city_gdp"];
                console.log(city_gdp["city_gdp"])
                var city_gdp_element = document.getElementById(
                    "soa_city_gdp_answer_gdp"
                );
                city_gdp_element.textContent = city_gdp["gdp"]["_text"];
                var city_gdp_element = document.getElementById(
                    "soa_city_gdp_answer_year"
                );
                city_gdp_element.textContent = city_gdp["gdp_time"]["_text"];
            }
        };
    };
    Vue.prototype.$soa_mashup = function(city_name, amap_center, news_data, main_page) { //全局函数7
        main_page.loading = true;
        var httpRequest_mashup = new XMLHttpRequest();
        var mashup_base_url =
            "http://127.0.0.1:5000/mashup?city_name=";
        httpRequest_mashup.open(
            "GET",
            mashup_base_url + city_name,
            true
        );
        httpRequest_mashup.send();
        httpRequest_mashup.onreadystatechange = function() {
            if (
                httpRequest_mashup.readyState == 4 &&
                httpRequest_mashup.status == 200
            ) {
                var response = httpRequest_mashup.responseText;
                if (response === '<?xml version="1.0" encoding="utf-8"?>\n<you>idiot</you>') {
                    console.log("not good");
                    var test = document.getElementsByClassName("grid-content");
                    for (let index = 0; index < test.length; index++) {
                        const element = test[index];
                        element.style.visibility = "hidden";
                    }
                    var test = document.getElementsByClassName("amap-copyright");
                    test[0].style.visibility = "hidden";
                    main_page.$notify.error({
                        title: 'Fetch Error',
                        message: 'Something wrong happened on backend\'s side or your input is somehow wrong.\n Check your input and try again.',
                    });
                    var test = document.getElementById("soa-header");
                    test.textContent = ":/";
                } else {
                    var test = document.getElementsByClassName("grid-content");
                    for (let index = 0; index < test.length; index++) {
                        const element = test[index];
                        element.style.visibility = "visible";
                    }
                    var test = document.getElementsByClassName("amap-copyright");
                    test[0].style.visibility = "visible";
                    var test = document.getElementById("soa-header");
                    test.textContent = city_name;
                    parser = new DOMParser();
                    xmlDoc = parser.parseFromString(response, "text/xml");
                    var convert = require('xml-js');
                    // console.log(xmlDoc)
                    // console.log(xmlDoc.getElementsByTagName("news_list"));
                    var response_json = convert.xml2json(response, { compact: true, spaces: 4 })
                    var response_dict = JSON.parse(response_json);
                    console.log(response_dict);

                    var city_position_element = document.getElementById(
                        "soa_city_position_answer"
                    );
                    // city position
                    var city_position = response_dict["mashup"]["city_position"];
                    console.log(city_position);
                    city_position_element.textContent = city_position["city_center"]["_text"];
                    amap_center.pop()
                    amap_center.pop()
                    amap_center.push(parseFloat(city_position["city_center_longitude"]["_text"]))
                    amap_center.push(parseFloat(city_position["city_center_latitude"]["_text"]))
                        // city weather
                    var city_weather = response_dict["mashup"]["city_weather"];
                    console.log(city_weather);
                    var city_weather_element = document.getElementById(
                        "soa_city_weather_answer_weather"
                    );
                    city_weather_element.textContent = city_weather["current_weather"]["_text"];
                    var city_weather_element = document.getElementById(
                        "soa_city_weather_answer_temp"
                    );
                    city_weather_element.textContent = city_weather["current_temp"]["_text"];
                    var city_weather_element = document.getElementById(
                        "soa_city_weather_answer_temp_high"
                    );
                    city_weather_element.textContent = city_weather["today_temp_high"]["_text"];
                    var city_weather_element = document.getElementById(
                        "soa_city_weather_answer_temp_low"
                    );
                    city_weather_element.textContent = city_weather["today_temp_low"]["_text"];
                    var city_weather_element = document.getElementById(
                        "soa_city_weather_answer_aqi"
                    );
                    city_weather_element.textContent = city_weather["current_aqi"]["_text"];
                    var city_weather_element = document.getElementById(
                        "soa_city_weather_answer_aqi_str"
                    );
                    city_weather_element.textContent = city_weather["current_aqi_str"]["_text"];
                    // city brief information
                    var city_brief_information_element = document.getElementById(
                        "soa_city_brief_information_answer"
                    );
                    var city_brief_information = response_dict["mashup"]["city_brief_information"];
                    console.log(city_brief_information);
                    city_brief_information_element.textContent = city_brief_information["brief_intro"]["_text"];
                    // city news
                    var city_news_list = response_dict["mashup"]["city_news"]["news_list"];
                    console.log(city_news_list);
                    city_news_list.forEach((element) => {
                        news_data.push({
                            news_title: element.news_title._text,
                            news_contents: element.news_contents._text,
                            news_source: element.news_source._text,
                            news_time: element.news_time._text,
                        });
                    });
                    // city GDP
                    var city_gdp = response_dict["mashup"]["city_gdp"];
                    console.log(city_gdp["city_gdp"])
                    var city_gdp_element = document.getElementById(
                        "soa_city_gdp_answer_gdp"
                    );
                    city_gdp_element.textContent = city_gdp["gdp"]["_text"];
                    var city_gdp_element = document.getElementById(
                        "soa_city_gdp_answer_year"
                    );
                    city_gdp_element.textContent = city_gdp["gdp_time"]["_text"];
                    main_page.loading = false;
                }
            }
        }
    };
};