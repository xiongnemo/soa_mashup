xml_to_json_testcases = [
    ["""
<student>
    <stid>10213</stid>
    <info>
        <name>name</name>
        <sex>male</sex>
    </info>
    <course>
        <name>math</name>
        <score>90</score>
    </course>
</student>
""", """
{
    "student": {
        "stid": "10213",
        "info": {
            "name": "name",
            "sex": "male"
        },
        "course": {
            "name": "math",
            "score": "90"
        }
    }
}
"""
     ]]

json_to_xml_testcases = [
    ["""
{
    "student": {
        "course": {
            "name": "math",
            "score": "90"
        },
        "info": {
            "sex": "male",
            "name": "name"
        }, 
        "stid": "10213"
    }
}""", """<?xml version="1.0" encoding="utf-8"?>
<student><course><name>math</name><score>90</score></course><info><sex>male</sex><name>name</name></info><stid>10213</stid></student>"""]
]

dict_to_xml_testcases = [
    ["stock", {'name': 'GOOG', 'shares': 100, 'price': 490.1},
        """<stock><name>GOOG</name><shares>100</shares><price>490.1</price></stock>"""]
]
