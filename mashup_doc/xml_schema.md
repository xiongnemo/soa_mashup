# XML Schema

Here defines what XML Schema my Mashup backend use.

``` xml
<xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="mashup">
    <xs:complexType>
      <xs:sequence>
        <xs:element name="city_gdp">
          <xs:complexType>
            <xs:sequence>
              <xs:element type="xs:string" name="city_name"/>
              <xs:element type="xs:string" name="gdp"/>
              <xs:element type="xs:string" name="gdp_time"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name="city_news">
          <xs:complexType>
            <xs:sequence>
              <xs:element type="xs:string" name="city_name"/>
              <xs:element type="xs:integer" name="news_count"/>
              <xs:element name="news_list" maxOccurs="10" minOccurs="10">
                <xs:complexType>
                  <xs:sequence>
                    <xs:element type="xs:string" name="news_title"/>
                    <xs:element type="xs:string" name="news_source"/>
                    <xs:element type="xs:string" name="news_time"/>
                    <xs:element type="xs:string" name="news_contents"/>
                  </xs:sequence>
                </xs:complexType>
              </xs:element>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name="city_brief_information">
          <xs:complexType>
            <xs:sequence>
              <xs:element type="xs:string" name="city_name"/>
              <xs:element type="xs:string" name="brief_intro"/>
              <xs:element type="xs:string" name="brief_intro_html"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name="city_position">
          <xs:complexType>
            <xs:sequence>
              <xs:element type="xs:string" name="city_name"/>
              <xs:element type="xs:string" name="city_center"/>
              <xs:element type="xs:float" name="city_center_longitude"/>
              <xs:element type="xs:float" name="city_center_latitude"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name="city_weather">
          <xs:complexType>
            <xs:sequence>
              <xs:element type="xs:string" name="city_name"/>
              <xs:element type="xs:string" name="current_weather"/>
              <xs:element type="xs:integer" name="current_temp"/>
              <xs:element type="xs:integer" name="today_temp_low"/>
              <xs:element type="xs:integer" name="today_temp_high"/>
              <xs:element type="xs:integer" name="current_aqi"/>
              <xs:element type="xs:string" name="current_aqi_str"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```
