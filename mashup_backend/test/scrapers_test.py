from marshmallow.soa.information_fetcher.baidu_city_gdp import baidu_gdp_with_city_name  # The code to test
from marshmallow.soa.information_fetcher.baidu_city_news import baidu_news_with_city_name # The code to test
from marshmallow.soa.information_fetcher.wikipedia_city_brief_information import get_wikipedia_city_brief_information  # The code to test
import json
import unittest  # The test framework
import testcases.scrapers_testcases
import time

class Test_TestScraper(unittest.TestCase):

    def test_baidu_city_gdp(self):
        for testcase in testcases.scrapers_testcases.scraper_testcases:
            print(testcase)
            # self.assertTrue(baidu_gdp_with_city_name(testcase))
            _, test_json_str = baidu_gdp_with_city_name(testcase)
            self.assertTrue(json.loads(test_json_str))
            time.sleep(1.5)

    def test_baidu_city_news(self):
        for testcase in testcases.scrapers_testcases.scraper_testcases:
            print(testcase)
            # self.assertTrue(baidu_news_with_city_name(testcase))
            _, test_json_str = baidu_news_with_city_name(testcase)
            self.assertTrue(json.loads(test_json_str))
            time.sleep(1.5)


    def test_wikipedia_city_brief_information(self):
        for testcase in testcases.scrapers_testcases.scraper_testcases:
            print(testcase)
            # self.assertTrue(get_wikipedia_city_brief_information(testcase))
            _, test_json_str = get_wikipedia_city_brief_information(testcase)
            self.assertTrue(json.loads(test_json_str))


if __name__ == '__main__':
    unittest.main()
