test_xml_list = ["""<?xml version="1.0" encoding="utf-8"?>
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
</mashup>""","""<?xml version="1.0" encoding="utf-8"?>
<mashup>
    <city_gdp>
        <city_name>上海</city_name>
        <gdp>38155.32 亿元</gdp>
        <gdp_time>(2019年)</gdp_time>
    </city_gdp>
    <city_news>
        <city_name>上海</city_name>
        <news_count>10</news_count>
        <news_list>
            <news_title>上海举办首届逛马路节 挖掘后街经济 激发消费活力</news_title>
            <news_source>央视网</news_source>
            <news_time>59分钟前</news_time>
            <news_contents>央视网消息:上海市正在举办首届逛马路节,激发消费活力,活动持续到30日。 慢行的街区,创意的市集,首届逛马路节期间,大大小小的活动遍布6条上海小马路,让马路不仅...</news_contents>
        </news_list>
        <news_list>
            <news_title>全球艺场切入“上海时间”</news_title>
            <news_source>看看新闻Knews</news_source>
            <news_time>2020年10月15日 18:00</news_time>
            <news_contents>“全球艺场,上海时间”,第二届“上海国际艺术品交易月”10月15日至11月15日在徐汇滨江举行。第七届西岸艺术与设计博览会、第八届ART021上海廿一当代艺术博览会...</news_contents>
        </news_list>
        <news_list>
            <news_title>上海市城运大厅日前正式启用,李强今天实地调研!</news_title>
            <news_source>新民晚报</news_source>
            <news_time>2020年10月12日 18:57</news_time>
            <news_contents>市委书记李强今天上午(10月12日)在上海市城市运行管理中心调研城市运行“一网统管”建设时指出,“一网统管”事关超大城市安全有序运行,要深入贯彻落实习近平总书记...</news_contents>
        </news_list>
        <news_list>
            <news_title>除了上热搜,“上海名媛群”还带给人们这些疑惑</news_title>
            <news_source>观察者网</news_source>
            <news_time>2020年10月13日 19:06</news_time>
            <news_contents>【文/观察者网 严珊珊】这两天,一篇揭露上海“名媛”的观察记,在盛大开场后,于酒店双双否认中迅速转折,变成了一场疑似“自导自演”“挑动对立”的闹剧。 曾经令...</news_contents>
        </news_list>
        <news_list>
            <news_title>中国下一个“上海”,成都、苏州不被看好,最可能是这3座城市</news_title>
            <news_source>珊珊的旅行游记</news_source>
            <news_time>2020年10月24日 22:57</news_time>
            <news_contents>说到上海,我相信大家都知道上海是我国不让步的经济负责人,上海在国际上也有很大的声誉,这充分表明我国经济一直处于高速发展阶段,相信不久我国将会出现更多的城市,成...</news_contents>
        </news_list>
        <news_list>
            <news_title>“上海市青年五四奖章”拟表彰对象公示</news_title>
            <news_source>手机凤凰网</news_source>
            <news_time>2020年10月19日 17:47</news_time>
            <news_contents>夺取疫情防控和实现经济社会发展目标“双胜利”、创造新时代上海发展新奇迹贡献青春力量,上海市人力资源和社会保障局、共青团上海市委员会联合开展了“上海市青年五四...</news_contents>
        </news_list>
        <news_list>
            <news_title>上海这一罕见的环形马路,曾是有“殿、台、楼、阁”的老城墙?</news_title>
            <news_source>解放日报</news_source>
            <news_time>2020年10月13日 18:58</news_time>
            <news_contents>建起城墙,保护上海的繁荣 上海在13世纪末元代至元年间设县之后的260多年时间里,一直没有建造过城墙。探究原因,说法纷纭。如据许国兴、祖建平主编《老城厢—上海...</news_contents>
        </news_list>
        <news_list>
            <news_title>今晨上海S20外环高速两车追尾 造成1死1伤</news_title>
            <news_source>手机凤凰网</news_source>
            <news_time>2020年10月19日 14:29</news_time>
            <news_contents>凌晨5时左右,S20外环高速外圈靠近漕宝路出口匝道附近发生一起厢式货车追尾养护车辆的事故。记者了解到,该起事故造成现场施工人员一死一伤。 事故发生时,天还未亮,...</news_contents>
        </news_list>
        <news_list>
            <news_title>上海名媛群女孩回应说了什么 名媛群拼单是怎么回事</news_title>
            <news_source>站长之家</news_source>
            <news_time>2020年10月14日 08:58</news_time>
            <news_contents>上海名媛群女孩回应说了什么?日前一篇名为《我潜伏上海“名媛”群,做了半个月的名媛观察者》的网帖上了热搜。文中,作者号称花 500 元“入群费”,潜入魔都...</news_contents>
        </news_list>
        <news_list>
            <news_title>继静安区之后,苏州一县城有望“撤市设区”,距离仅有60公里</news_title>
            <news_source>旅行情报局</news_source>
            <news_time>2020年10月24日 15:30</news_time>
            <news_contents>上海市成立于1927年7月7日,归中央政府管理,也是中华人民共和国省级行政区,直辖市,国家中心城市,中国国际经济,金融,贸易,航运科技创新中心,上海市管辖下有着16个区...</news_contents>
        </news_list>
    </city_news>
    <city_brief_information>
        <city_name>上海</city_name>
        <brief_intro>上海市，简称沪，别称申，是中華人民共和國直轄市，中國的经济、金融、贸易和航运中心，世界著名的港口城市，是中国人口第二多的城市。上海位於中国东部弧形海岸线的正中间，长江三角洲最东部，东临东海，南濒杭州湾，西与江苏、浙江两省相接，北端的崇明岛处于长江入海口中，与周围的江苏、浙江、安徽三省多个城市共同构成世界级城市群长江三角洲城市群，是其重要的组成部分。
最晚在新石器時代，上海地區已經有先民聚居。春秋時代，上海由吳國管轄，戰國時代則是楚國領土。晋代，上海的人口聚集起來，初步发展为一个區域的渔港、盐产地和商贸集镇。唐代到元代，上海所属地区归华亭县、松江府管辖。明清两朝，已成较为繁荣的村落，棉纺织业发达。1843年，《南京条约》签订，正式开埠，上海作为指定通商五口之一，开始上海租界的历史，亦开启上海取得舉足輕重地位的历程。当时名苏淞太常道与上海县，從小聚落成為港口之後，得益独特的政治环境，上海经济凭借通商口岸，各方面得到空前迅速的发展，吸引江蘇、浙江、廣東、安徽、山東等周边省份及外国移民，成为中国乃至远东地区最大的都会至今。吸收江南地区附近传统的吴越文化与各地移民带入的多样文化，及開埠後的西方近现代文化融合，逐渐形成上海本地特有的海派文化。</brief_intro>
        <brief_intro_html>&lt;p&gt;&lt;b&gt;上海市&lt;/b&gt;，简称&lt;b&gt;沪&lt;/b&gt;，别称&lt;b&gt;申&lt;/b&gt;，是中華人民共和國直轄市，中國的经济、金融、贸易和航运中心，世界著名的港口城市，是中国人口第二多的城市。上海位於中国东部弧形海岸线的正中间，长江三角洲最东部，东临东海，南濒杭州湾，西与江苏、浙江两省相接，北端的崇明岛处于长江入海口中，与周围的江苏、浙江、安徽三省多个城市共同构成世界级城市群长江三角洲城市群，是其重要的组成部分。
最晚在新石器時代，上海地區已經有先民聚居。春秋時代，上海由吳國管轄，戰國時代則是楚國領土。晋代，上海的人口聚集起來，初步发展为一个區域的渔港、盐产地和商贸集镇。唐代到元代，上海所属地区归华亭县、松江府管辖。明清两朝，已成较为繁荣的村落，棉纺织业发达。1843年，《南京条约》签订，正式开埠，上海作为指定通商五口之一，开始上海租界的历史，亦开启上海取得舉足輕重地位的历程。当时名苏淞太常道与上海县，從小聚落成為港口之後，得益独特的政治环境，上海经济凭借通商口岸，各方面得到空前迅速的发展，吸引江蘇、浙江、廣東、安徽、山東等周边省份及外国移民，成为中国乃至远东地区最大的都会至今。吸收江南地区附近传统的吴越文化与各地移民带入的多样文化，及開埠後的西方近现代文化融合，逐渐形成上海本地特有的海派文化。&lt;/p&gt;</brief_intro_html>
    </city_brief_information>
    <city_position>
        <city_name>上海</city_name>
        <city_center>121.472644,31.231706</city_center>
        <city_center_longitude>121.472644</city_center_longitude>
        <city_center_latitude>31.231706</city_center_latitude>
    </city_position>
    <city_weather>
        <city_name>上海</city_name>
        <current_weather>晴</current_weather>
        <current_temp>18</current_temp>
        <today_temp_low>14</today_temp_low>
        <today_temp_high>20</today_temp_high>
        <current_aqi>51</current_aqi>
        <current_aqi_str>良</current_aqi_str>
    </city_weather>
</mashup>""","""
<?xml version="1.0" encoding="utf-8"?>
<mashup>
    <city_gdp>
        <city_name>北京</city_name>
        <gdp>35371.3亿元</gdp>
        <gdp_time>(2019年)</gdp_time>
    </city_gdp>
    <city_news>
        <city_name>北京</city_name>
        <news_count>10</news_count>
        <news_list>
            <news_title>这个信号来了!北京楼市稳了?</news_title>
            <news_source>新浪财经</news_source>
            <news_time>2020年10月16日 08:50</news_time>
            <news_contents>经过几年调整,北京住宅交易量在近期有所恢复。机构数据显示,今年5-9月份,北京二手住宅的月度网签量均超过1.6万套,处于2017年“317新政”以来的高点。新建住宅交易相...</news_contents>
        </news_list>
        <news_list>
            <news_title>北京“新增”一大型度假区,耗资上百亿,预计将于2021年试运营</news_title>
            <news_source>小酥带你去旅行</news_source>
            <news_time>2020年10月24日 17:14</news_time>
            <news_contents>说起北京,大家会想到什么呢,相信很多人的第一反应就是想到北京的旅游景点,北京的天安门,颐和园,长城等,都是享誉国内外的著名的旅游景区,而在北京,不仅有这些古建...</news_contents>
        </news_list>
        <news_list>
            <news_title>北京老年人口超370万 百岁老人突破千人</news_title>
            <news_source>央视网</news_source>
            <news_time>5小时前</news_time>
            <news_contents>《北京市老龄事业发展报告(2019)》日前发布,数据显示,北京市60岁及以上常住人口达到371.3万人,百岁老人突破千人。</news_contents>
        </news_list>
        <news_list>
            <news_title>北京惠民保最新产品和市场分析</news_title>
            <news_source>爱分享的培训师刘阳</news_source>
            <news_time>2020年10月19日 22:44</news_time>
            <news_contents>北京市委社会工委市民政局领导表示,“北京京惠保”作为首都城市定制保险,按照“政府指导、社会参与”的模式,作为惠及北京市民民生的专属保障,凸显了“普惠+实用”的定...</news_contents>
        </news_list>
        <news_list>
            <news_title>[北京您早]关爱老年人生活 让幸福感满人心</news_title>
            <news_source>央视网</news_source>
            <news_time>8小时前</news_time>
            <news_contents>新闻 [北京您早]关爱老年人生活 让幸福感满人心简介45 新闻栏目推荐 首页|全站地图  中央广播电视总台央视网版权所有</news_contents>
        </news_list>
        <news_list>
            <news_title>北京一荒凉的城中村,租客在不断的减少,却等不到拆迁</news_title>
            <news_source>向导小蚂</news_source>
            <news_time>2020年10月24日 12:32</news_time>
            <news_contents>很多的人在去到北京之后,最先想到的问题就是居住地。 在这样的一座城市之中,想找到一处便宜的地方居住是不容易的,和跟多对这里不熟悉的人员,看到这里最先考虑...</news_contents>
        </news_list>
        <news_list>
            <news_title>北京京惠保谁能买?附相关问题解答</news_title>
            <news_source>北京本地宝</news_source>
            <news_time>2020年10月19日 17:17</news_time>
            <news_contents>北京本地宝频道提供北京京惠保谁能买?附相关问题解答有关的信息,北京京惠保谁能买?答:北京市范围内的基本医疗保险(含北京市城镇职工、城乡居民、公费医疗)参保人...</news_contents>
        </news_list>
        <news_list>
            <news_title>北京扫黑除恶战果:王海民、王海深犯罪集团覆灭</news_title>
            <news_source>北京日报客户端</news_source>
            <news_time>2020年10月19日 07:23</news_time>
            <news_contents>王海民、王海深团伙落网后,北京市公安局纪委对15名涉案民警分别处以政务处分、行政告诫、批评教育等处理,并追究了5名领导干部的队伍管理责任。针对落实扫黑除恶专项...</news_contents>
        </news_list>
        <news_list>
            <news_title>北京女人有多美?看这篇就够了</news_title>
            <news_source>过客的憧憬</news_source>
            <news_time>2020年10月14日 07:09</news_time>
            <news_contents>北京,简称“京”,是中华人民共和国的首都,是全国的政治中心、文化中心,是世界著名古都和现代化国际城市。北京是中国四大古都之一。北京是一座有着三千多年历史的古...</news_contents>
        </news_list>
        <news_list>
            <news_title>北京耗资30亿的公园,被称昌平“小颐和园”,门票仅30却略显惨淡</news_title>
            <news_source>游侠许志远</news_source>
            <news_time>2020年10月21日 09:38</news_time>
            <news_contents>从明清时期开始,北京诞生出了许多具有标志性的皇家园林式公园,我们熟知的圆明园,颐和园等都是那个时期的精华,所以很多人认为去看北京的公园一定要去看具有历史底蕴的...</news_contents>
        </news_list>
    </city_news>
    <city_brief_information>
        <city_name>北京</city_name>
        <brief_intro>北京市，通称北京，简称“京”，是中華人民共和國的首都及直辖市，是中國的政治、文化、科技和国际交往中心，是世界人口第三多的城市和人口最多的首都，具有重要的国际影响力。北京位於華北平原的西北边缘，背靠燕山，有永定河流经老城西南，毗邻天津市、河北省，为京津冀城市群的重要组成部分。</brief_intro>
        <brief_intro_html>&lt;p&gt;&lt;b&gt;北京市&lt;/b&gt;，通称&lt;b&gt;北京&lt;/b&gt;，简称“&lt;b&gt;京&lt;/b&gt;”，是中華人民共和國的首都及直辖市，是中國的政治、文化、科技和国际交往中心，是世界人口第三多的城市和人口最多的首都，具有重要的国际影响力。北京位於華北平原的西北边缘，背靠燕山，有永定河流经老城西南，毗邻天津市、河北省，为京津冀城市群的重要组成部分。&lt;/p&gt;</brief_intro_html>
    </city_brief_information>
    <city_position>
        <city_name>北京</city_name>
        <city_center>116.405285,39.904989</city_center>
        <city_center_longitude>116.405285</city_center_longitude>
        <city_center_latitude>39.904989</city_center_latitude>
    </city_position>
    <city_weather>
        <city_name>北京</city_name>
        <current_weather>晴</current_weather>
        <current_temp>17</current_temp>
        <today_temp_low>7</today_temp_low>
        <today_temp_high>19</today_temp_high>
        <current_aqi>131</current_aqi>
        <current_aqi_str>轻度污染</current_aqi_str>
    </city_weather>
</mashup>""","""<?xml version="1.0" encoding="utf-8"?>
<mashup>
    <city_gdp>
        <city_name>湛江</city_name>
        <gdp>3064.72亿元</gdp>
        <gdp_time>(2019年)</gdp_time>
    </city_gdp>
    <city_news>
        <city_name>湛江</city_name>
        <news_count>10</news_count>
        <news_list>
            <news_title>湛江市局部署做好特防期信访维稳安保工作</news_title>
            <news_source>潇湘晨报</news_source>
            <news_time>3小时前</news_time>
            <news_contents>【来源:湛江市政府】 声明:转载此文是出于传递更多信息之目的。若有来源标注错误或侵犯了您的合法权益,请作者持权属证明与本网联系,我们将及时更正、删除,谢谢。 </news_contents>
        </news_list>
        <news_list>
            <news_title>「最新通报」10月24日,湛江市无新增!</news_title>
            <news_source>潇湘晨报</news_source>
            <news_time>8小时前</news_time>
            <news_contents>2020年10月24日0至24时,湛江市无新增确诊病例,无新增无症状感染者。 截至10月24日24时,湛江市累计报告新冠肺炎确诊病例30例(其中境外输入确诊病例8例),累计报告...</news_contents>
        </news_list>
        <news_list>
            <news_title>湛江公安破获盗销耕牛案,10头耕牛派出所招认领</news_title>
            <news_source>腾讯网</news_source>
            <news_time>3小时前</news_time>
            <news_contents>日前,廉江市公安局石城派出所拉回了10头大小不一的黄牛,“安置”在辖区某农场,正陆续被失主领回。这是近日侦破的盗牛案中追回的耕牛,为群众挽回直接经济损失20余...</news_contents>
        </news_list>
        <news_list>
            <news_title>“广东湛江一夜宵店一群手持棍棒年轻人在屋里乱打后转头就走...</news_title>
            <news_source>界面新闻</news_source>
            <news_time>2020年10月24日 13:58</news_time>
            <news_contents>广东省湛江市公安局官微10月24日通报,近日,网上转发标题为“广东湛江一夜宵店一群手持棍棒年轻人在屋里乱打后转头就走”的短视频被网民朋友广泛关注,湛江市公安局...</news_contents>
        </news_list>
        <news_list>
            <news_title>2020年湛江富豪榜出炉!首富身价达310亿元!</news_title>
            <news_source>得嗲</news_source>
            <news_time>1小时前</news_time>
            <news_contents>苏萌,广东省湛江市雷州人,高德置地集团董事长。2020年3月20日,苏萌以100亿元人民币财富名列《2020胡润全球房地产富豪榜》第191位。高德置地集团成立于1995年,是一...</news_contents>
        </news_list>
        <news_list>
            <news_title>省委巡视组仅进入10天,广东湛江三名官员被查!</news_title>
            <news_source>网易新闻</news_source>
            <news_time>18小时前</news_time>
            <news_contents>湛江市纪委监委10月23日下午18时通报称,廉江市委教育工委书记、廉江市教育局党组书记、局长叶春涉嫌严重违纪违法,目前正接受湛江市纪委监委纪律审查和监察调查。此...</news_contents>
        </news_list>
        <news_list>
            <news_title>湛江:粤西首个获批设立的省实验室动工</news_title>
            <news_source>央广网</news_source>
            <news_time>2020年10月24日 23:51</news_time>
            <news_contents>央广网湛江10月24日消息(记者郭翔宇 通讯员梁妃忠)记者从湛江相关部门获悉,10月23日上午,湛江湾实验室龙王湾研发基地一期工程开工仪式举行。 据悉,湛江湾实验室是粤...</news_contents>
        </news_list>
        <news_list>
            <news_title>做振兴湛江的“打工人”</news_title>
            <news_source>湛江新闻网</news_source>
            <news_time>8小时前</news_time>
            <news_contents>在新时代,“打工人”就是奋斗者、建设者,我们要做振兴湛江的“打工人”。不仅要体现劳动之美的奋斗底色,也要展现创造之美的价值升华。争当优秀的“打工人”,就...</news_contents>
        </news_list>
        <news_list>
            <news_title>网传“湛江一群手持棍棒年轻人在一夜宵店乱打后离开” !警方回应...</news_title>
            <news_source>网易新闻</news_source>
            <news_time>2020年10月24日 20:47</news_time>
            <news_contents>近日,网上转发标题为“广东湛江一夜宵店一群手持棍棒年轻人在屋里乱打后转头就走”的短视频被网民朋友广泛关注。湛江公安局对此高度重视,迅速在全市范围内展开核查...</news_contents>
        </news_list>
        <news_list>
            <news_title>秋风送凉,湛江人这些动作有点暖</news_title>
            <news_source>得嗲</news_source>
            <news_time>45分钟前</news_time>
            <news_contents>近日,在湛江站里 有三名行动不便的旅客 计划乘坐K158次前往长沙 客运员梁广福看到后 立即上前抱起坐在轮椅上的大爷 安全送达相应的位置上 并引导另两位乘客通过...</news_contents>
        </news_list>
    </city_news>
    <city_brief_information>
        <city_name>湛江</city_name>
        <brief_intro>湛江市，简称湛，别称港城，旧称广州湾（），是中华人民共和国广东省下辖的地级市，广东省域副中心城市，北部湾 及粤西城镇群中心城市，地处中国大陆最南端的雷州半岛，广东、广西、海南三省（区）交汇处，东北邻茂名市，西北接广西壮族自治区玉林市、北海市，东濒南海，南隔琼州海峡与海南岛相望，西临北部湾，现辖4个市辖区、3个县级市、2个县，市人民政府驻赤坎区。</brief_intro>
        <brief_intro_html>&lt;p&gt;&lt;b&gt;湛江市&lt;/b&gt;，简称&lt;b&gt;湛&lt;/b&gt;，别称&lt;b&gt;港城&lt;/b&gt;，旧称&lt;b&gt;广州湾&lt;/b&gt;（），是中华人民共和国广东省下辖的地级市，广东省域副中心城市，北部湾 及粤西城镇群中心城市，地处中国大陆最南端的雷州半岛，广东、广西、海南三省（区）交汇处，东北邻茂名市，西北接广西壮族自治区玉林市、北海市，东濒南海，南隔琼州海峡与海南岛相望，西临北部湾，现辖4个市辖区、3个县级市、2个县，市人民政府驻赤坎区。&lt;/p&gt;</brief_intro_html>
    </city_brief_information>
    <city_position>
        <city_name>湛江</city_name>
        <city_center>110.364977,21.274898</city_center>
        <city_center_longitude>110.364977</city_center_longitude>
        <city_center_latitude>21.274898</city_center_latitude>
    </city_position>
    <city_weather>
        <city_name>湛江</city_name>
        <current_weather>阴</current_weather>
        <current_temp>23</current_temp>
        <today_temp_low>20</today_temp_low>
        <today_temp_high>26</today_temp_high>
        <current_aqi>49</current_aqi>
        <current_aqi_str>优</current_aqi_str>
    </city_weather>
</mashup>""",]