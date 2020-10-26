from marshmallow.soa.information_constructor.city_gdp import get_city_gdp # The code to test
from marshmallow.soa.information_constructor.city_news import get_city_news # The code to test
from marshmallow.soa.information_constructor.city_brief_information import get_city_brief_information  # The code to test
from marshmallow.soa.information_constructor.city_weather import get_tianqi_city_weather  # The code to test
from marshmallow.soa.information_constructor.city_position import get_amap_city_position  # The code to test
import json
import unittest  # The test framework
import testcases.scrapers_testcases
import time

class Test_TestScraper(unittest.TestCase):

    def test_baidu_city_gdp(self):
        for testcase in testcases.scrapers_testcases.scraper_testcases:
            print(testcase)
            temp_dict = get_city_gdp(testcase)
            self.assertTrue(temp_dict)
            print(temp_dict)
            time.sleep(1.5)

    def test_baidu_city_news(self):
        for testcase in testcases.scrapers_testcases.scraper_testcases:
            print(testcase)
            temp_dict = get_city_news(testcase)
            self.assertTrue(temp_dict)
            print(temp_dict)
            time.sleep(1.5)


    def test_wikipedia_city_brief_information(self):
        for testcase in testcases.scrapers_testcases.scraper_testcases:
            print(testcase)
            temp_dict = get_city_brief_information(testcase)
            self.assertTrue(temp_dict)
            print(temp_dict)
    
    def test_tianqi_city_weather(self):
        for testcase in testcases.scrapers_testcases.scraper_testcases:
            print(testcase)
            temp_dict = get_tianqi_city_weather(testcase)
            self.assertTrue(temp_dict)
            print(temp_dict)

    def test_amap_city_position(self):
        for testcase in testcases.scrapers_testcases.scraper_testcases:
            print(testcase)
            temp_dict = get_amap_city_position(testcase)
            self.assertTrue(temp_dict)
            print(temp_dict)


if __name__ == '__main__':
    unittest.main()
