import marshmallow.common.utils.xml    # The code to test
import unittest # The test framework
import testcases.xmlutils_testcases

class Test_TestXMLOperation(unittest.TestCase):
    def test_xml_to_json(self):
        for testcase in testcases.xmlutils_testcases.xml_to_json_testcases:
            self.assertEqual(marshmallow.common.utils.xml.xml_to_json(testcase[0].strip()), testcase[1].strip())

    def test_json_to_xml(self):
        for testcase in testcases.xmlutils_testcases.json_to_xml_testcases:
            self.assertEqual(marshmallow.common.utils.xml.json_to_xml(testcase[0].strip()), testcase[1].strip())

    def test_dict_to_xml(self):
        for testcase in testcases.xmlutils_testcases.dict_to_xml_testcases:
            self.assertEqual(marshmallow.common.utils.xml.dict_to_xml(testcase[0], testcase[1]), testcase[2].strip())


if __name__ == '__main__':
    unittest.main()