# encoding=utf-8
import requests, datetime
from datetime import timedelta, date
from lxml import etree
import json
import random
from user_agents import agents
import re
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from browsermobproxy import Server


def get_parameter(date):
    '''获取重要的参数
    date:日期，格式示例：2016-05-13
    '''
    response = requests.get(url)
    tree = etree.HTML(response.content)
    pp = tree.xpath('''//body/script[1]/text()''')[0].split()
    CK_original = pp[3][-34:-2]
    url = 'http://flights.ctrip.com/booking/hrb-sha-day-1.html?ddate1=%s' % date
    CK = CK_original[0:5] + CK_original[13] + CK_original[5:13] + CK_original[14:]

    rk = pp[-1][18:24]
    num = random.random() * 10
    num_str = "%.15f" % num
    rk = num_str + rk
    r = pp[-1][27:len(pp[-1]) - 3]

    return rk, CK, r


def parseCookieFile(cookiefile):
    """Parse a cookies.txt file and return a dictionary of key value pairs
    compatible with requests."""

    cookies = {}
    with open(cookiefile, 'r') as fp:
        for line in fp:
            if not re.match(r'^\#', line):
                lineFields = line.strip().split('\t')
                if len(lineFields) > 6 and lineFields[0].__contains__('ctrip'):
                    cookies[lineFields[5]] = lineFields[6]
    print(cookies)
    return cookies


#cookies = parseCookieFile('cookies.txt')

headers = {
    'sec-fetch-mode': 'cors',
    'dnt': '1',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    # 6368c10578c6480bb1d6ce5c933ed13b
    # 'transactionid': 'dbd659bc13ea4618aee02ac7c296eae1',
    'transactionid': '73b2f7cd07824cbdbbffa578e66792e2',
    # 'cookie': '_abtest_userid=927b16eb-db31-46d8-b2b1-b9766d2a2fc5; _RSG=U.q5ukPyzR5VoK_oOgR1g9; _RDG=2839bd444e4cd225bb0afd8e112b1a82b8; _RGUID=56fdf19b-b817-4f9e-9a81-6ea632fd4c9f; _ga=GA1.2.1462029734.1557382347; UUID=77D7C491694C4A7483A5C0587E70812E; login_type=0; GUID=09031141110926314626; Corp_ResLang=en; __utma=1.1462029734.1557382347.1563251787.1563251787.1; __utmc=1; __utmz=1.1563251787.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); HotelCityID=659split%E5%AE%89%E5%90%89splitAnjisplit2019-7-17split2019-07-18split0; MKT_Pagesource=PC; login_uid=E058C6725DAF32DD8632AF51792C5EDC; cticket=E0DE51853A3FA2220205421F3B37B9254B3863E723AA1A008DCEFA902E0B559E; AHeadUserInfo=VipGrade=30&VipGradeName=%D7%EA%CA%AF%B9%F3%B1%F6&UserName=%BD%F0%D5%D1&NoReadMessageCount=1; ticket_ctrip=bJ9RlCHVwlu1ZjyusRi+ypZ7X2r4+yojvVuV/I2UYHOk5EYC3y8ub/EoVq9vtukxHX1RyT3q8Oc/XpVSMPlRXcAiSHL0Lg3DXUC7o7/eSqjjMk9b7dwbBgxcfH9WWghLViwolojiCsf5FSDJnTUKjiEWvx5ixW12UIoQPHR2QMRLPAsjOQheBChG/f7bCeLAnp7repjG2g/ExH3xf5bygjA67GheVazRn2iMxJa65V/H/+bTeevU1EqOaqhbIjtbkc2MjaOdvsPEnHTw8rtSrPn7xhe40UI704dyXyNBWXljPuFPgTEx6Q==; DUID=u=78A35AD1451F790E6B505EA91CE12D52C916733EF2E482E05C236A911B579966&v=0; IsNonUser=F; IsPersonalizedLogin=T; _RF1=115.211.74.232; gad_city=da954ff4e36a9d469dd99cc8e2bac817; _gid=GA1.2.16176248.1565158434; Session=SmartLinkCode=U1449755&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; Union=OUID=&AllianceID=880279&SID=1449755&SourceID=&Expires=1565839616577; DomesticUserHostCity=SHA%7c%c9%cf%ba%a3; appFloatCnt=3; FlightIntl=Search=[%22SHA|%E4%B8%8A%E6%B5%B7(SHA)|2|SHA|480%22%2C%22FRA|%E6%B3%95%E5%85%B0%E5%85%8B%E7%A6%8F(FRA)|250|FRA|120%22%2C%222019-08-30%22%2C%22%22%2C[[%22FRA|%E6%B3%95%E5%85%B0%E5%85%8B%E7%A6%8F(FRA)|250|FRA|120%22%2C%22ALG|%E9%98%BF%E5%B0%94%E5%8F%8A%E5%B0%94(ALG)|1271|ALG|60%22%2C%222019-09-03%22]%2C[%22ALG|%E9%98%BF%E5%B0%94%E5%8F%8A%E5%B0%94(ALG)|1271|ALG|60%22%2C%22SHA|%E4%B8%8A%E6%B5%B7(SHA)|2|SHA|480%22%2C%222019-09-12%22]]]; _jzqco=%7C%7C%7C%7C%7C1.638869469.1557382347575.1565239898917.1565241449409.1565239898917.1565241449409.0.0.0.126.126; __zpspc=9.27.1565239898.1565241449.2%233%7Cd3upggnd18hyak.cloudfront.net%7C%7C%7C%7C%23; _bfi=p1%3D10320672929%26p2%3D101023%26v1%3D253%26v2%3D252; _bfa=1.1557382344603.38da7e.1.1565234813695.1565239893712.27.254; _bfs=1.4',
    # 'sign': '62c0079dfb64ee77eb9418fac5c93dd0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'accept': 'application/json',
    'cache-control': 'no-cache',
    'authority': 'flights.ctrip.com',
    # 'referer': 'https://flights.ctrip.com/international/search/multi-sha-fra-fra-alg-alg-sha?depdate=2019-08-30_2019-09-03_2019-09-12&cabin=y_s&adult=1&child=0&infant=0',
    'sec-fetch-site': 'same-origin',
    'origin': 'https://flights.ctrip.com',
}

params = (
    ('v', '0.025567854220195585'),
)

data = '{"flightWayEnum":"MT","arrivalProvinceId":2,"arrivalCountryName":"\u4E2D\u56FD","infantCount":0,"cabin":"Y_S","cabinEnum":"Y_S","departCountryName":"\u4E2D\u56FD","flightSegments":[{"departureDate":"2019-08-30","arrivalProvinceId":10121,"arrivalCountryName":"\u5FB7\u56FD","departureCityName":"\u4E0A\u6D77","departureCityCode":"SHA","departureCountryName":"\u4E2D\u56FD","arrivalCityName":"\u6CD5\u5170\u514B\u798F","arrivalCityCode":"FRA","departureCityTimeZone":480,"arrivalCountryId":28,"timeZone":480,"departureCityId":2,"departureCountryId":1,"arrivalCityTimeZone":120,"departureProvinceId":2,"arrivalCityId":250},{"departureDate":"2019-09-03","arrivalProvinceId":11548,"arrivalCountryName":"\u963F\u5C14\u53CA\u5229\u4E9A","departureCityName":"\u6CD5\u5170\u514B\u798F","departureCityCode":"FRA","departureCountryName":"\u5FB7\u56FD","arrivalCityName":"\u963F\u5C14\u53CA\u5C14","arrivalCityCode":"ALG","departureCityTimeZone":120,"arrivalCountryId":6,"timeZone":120,"departureCityId":250,"departureCountryId":28,"arrivalCityTimeZone":60,"departureProvinceId":10121,"arrivalCityId":1271},{"departureDate":"2019-09-12","arrivalProvinceId":2,"arrivalCountryName":"\u4E2D\u56FD","departureCityName":"\u963F\u5C14\u53CA\u5C14","departureCityCode":"ALG","departureCountryName":"\u963F\u5C14\u53CA\u5229\u4E9A","arrivalCityName":"\u4E0A\u6D77","arrivalCityCode":"SHA","departureCityTimeZone":60,"arrivalCountryId":1,"timeZone":60,"departureCityId":1271,"departureCountryId":6,"arrivalCityTimeZone":480,"departureProvinceId":11548,"arrivalCityId":2}],"childCount":0,"segmentNo":1,"adultCount":1,"extensionAttributes":{},"transactionID":"dbd659bc13ea4618aee02ac7c296eae1","directFlight":false,"departureCityId":2,"isMultiplePassengerType":0,"flightWay":"M","arrivalCityId":2,"departProvinceId":2}'

#经济舱：cabin=y_s 公务舱cabin=c
first_base_url = 'https://flights.ctrip.com/international/search/multi-sha-alg-alg-fra-fra-sha?depdate=%s_%s_%s&cabin=y_s&adult=1&child=0&infant=0'


def test_sample_request():
    session = requests.session()
    session.headers = {"hearders": random.choice(agents)}
    base_url = "https://flights.ctrip.com/international/search/api/search/batchSearch"
    url = base_url
    payload = '{"flightWayEnum": "MT", "arrivalProvinceId": 2, "arrivalCountryName": "中国", "infantCount": 0, "cabin": "Y_S", "cabinEnum": "Y_S", "departCountryName": "中国", ' \
              '"flightSegments": [{"departureDate": "2019-09-11", "arrivalProvinceId": 11548, "arrivalCountryName": "阿尔及利亚", "departureCityName": "上海", "departureCityCode": "SHA", "departureCountryName": "中国", "arrivalCityName": "阿尔及尔", "arrivalCityCode": "ALG", "departureCityTimeZone": 480, "arrivalCountryId": 6, "timeZone": 480, "departureCityId": 2, "departureCountryId": 1, "arrivalCityTimeZone": 60, "departureProvinceId": 2, "arrivalCityId": 1271}, ' \
              '{"departureDate": "2019-09-21", "arrivalProvinceId": 10121, "arrivalCountryName": "德国", "departureCityName": "阿尔及尔", "departureCityCode": "ALG", "departureCountryName": "阿尔及利亚", "arrivalCityName": "法兰克福", "arrivalCityCode": "FRA", "departureCityTimeZone": 60, "arrivalCountryId": 28, "timeZone": 60, "departureCityId": 1271, "departureCountryId": 6, "arrivalCityTimeZone": 120, "departureProvinceId": 11548, "arrivalCityId": 250}, ' \
              '{"departureDate": "2019-09-25", "arrivalProvinceId": 2, "arrivalCountryName": "中国", "departureCityName": "法兰克福", "departureCityCode": "FRA", "departureCountryName": "德国", "arrivalCityName": "上海", "arrivalCityCode": "SHA", "departureCityTimeZone": 120, "arrivalCountryId": 1, "timeZone": 120, "departureCityId": 250, "departureCountryId": 28, "arrivalCityTimeZone": 480, "departureProvinceId": 10121, "arrivalCityId": 2}], "childCount": 0, "segmentNo": 1, "adultCount": 1, "extensionAttributes": {}, "transactionID": "92114bccf31d4c3dad93cfc979476315", "directFlight": false, "departureCityId": 2, "isMultiplePassengerType": 0, "flightWay": "M", "arrivalCityId": 2, "departProvinceId": 2}'

    headers['user-agent'] = random.choice(agents)
    response = requests.post(url, headers=headers, params=params, data=payload.encode('utf-8'))
    print(response.status_code)
    print(response.content)
    file = open("resp_content.html", "w")
    file.write(response.text)
    file.close()


day_formate = '%Y-%m-%d'


def update_pay_load_depart_date(depart_date1, depart_date2, depart_date3, pay_load):
    f_json = json.loads(pay_load)
    f_json['flightSegments'][0]['departureDate'] = depart_date1.strftime(day_formate)
    f_json['flightSegments'][1]['departureDate'] = depart_date2.strftime(day_formate)
    f_json['flightSegments'][2]['departureDate'] = depart_date3.strftime(day_formate)
    return json.dumps(f_json, ensure_ascii=False)


def print_flight_info(d_date, pay_load):
    url = "https://flights.ctrip.com/international/search/api/search/batchSearch"

    headers['user-agent'] = random.choice(agents)
    response = requests.post(url, headers=headers, data=pay_load.encode('utf-8'))
    # print(response.status_code)
    file = open('fl_data/'+datetime.datetime.today().strftime('%m%d')+"resp_content" + d_date.strftime('%m-%d') + ".json", "w")
    file.write(response.text)
    file.close()
    info = json.loads(response.text, encoding='utf-8')

    cpi = info['data']['cheapestFlightItinerary']
    fb = ''
    for f in cpi['flightSegments']:
        fb += f['airlineName']
    print(d_date.strftime(day_formate), '\t航班号', cpi['itineraryId'], 'price:\t',

          cpi['priceList'][0]['adultPrice'] + cpi['priceList'][0]['adultTax'], '\t', '')
    # chespt_price=info['data']['cheapestFlightItinerary']['priceList'][0]
    # print('%s\t航班:%s\t价格%s'%(date.strftime('%m-%d'),info['data']['cheapestFlightItinerary']['itineraryId'],chespt_price['adultPrice']+chespt_price['adultTax']))


def get_search_cr(url):
    #   GlobalSearchCriteria ={"adultCount":1,"childCount":0,"infantCount":0,"flightWay":"M","cabin":"Y_S","extensionAttributes":{},"transactionID":"6368c10578c6480bb1d6ce5c933ed13b","flightSegments":[{"departureCityCode":"SHA","arrivalCityCode":"FRA","departureCityName":"上海","departureDate":"2019-08-30","departureCountryId":1,"departureCountryName":"中国","departureProvinceId":2,"departureCityId":2,"arrivalCountryId":28,"arrivalCountryName":"德国","arrivalCityName":"法兰克福","arrivalProvinceId":10121,"arrivalCityId":250,"departureCityTimeZone":480,"arrivalCityTimeZone":120,"timeZone":480},{"departureCityCode":"FRA","arrivalCityCode":"ALG","departureCityName":"法兰克福","departureDate":"2019-09-03","departureCountryId":28,"departureCountryName":"德国","departureProvinceId":10121,"departureCityId":250,"arrivalCountryId":6,"arrivalCountryName":"阿尔及利亚","arrivalCityName":"阿尔及尔","arrivalProvinceId":11548,"arrivalCityId":1271,"departureCityTimeZone":120,"arrivalCityTimeZone":60,"timeZone":120},{"departureCityCode":"ALG","arrivalCityCode":"SHA","departureCityName":"阿尔及尔","departureDate":"2019-09-12","departureCountryId":6,"departureCountryName":"阿尔及利亚","departureProvinceId":11548,"departureCityId":1271,"arrivalCountryId":1,"arrivalCountryName":"中国","arrivalCityName":"上海","arrivalProvinceId":2,"arrivalCityId":2,"departureCityTimeZone":60,"arrivalCityTimeZone":480,"timeZone":60}],"directFlight":false};

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    json_str = soup.head.find_all('script')[-1].text.replace('GlobalSearchCriteria =', '').replace(';', '').strip()
    print('search_cr\t', json_str)
    print(json.loads(json_str)['transactionID'])
    return json.loads(json_str)


def deep_search(needles, haystack):
    found = {}
    if type(needles) != type([]):
        needles = [needles]

    if type(haystack) == type(dict()):
        for needle in needles:
            if needle in haystack.keys():
                found[needle] = haystack[needle]
            elif len(haystack.keys()) > 0:
                for key in haystack.keys():
                    result = deep_search(needle, haystack[key])
                    if result:
                        for k, v in result.items():
                            found[k] = v
    elif type(haystack) == type([]):
        for node in haystack:
            result = deep_search(needles, node)
            if result:
                for k, v in result.items():
                    found[k] = v
    return found


if __name__ == "__main__":
    # test_sample_request()
    # print('test pass')
    min_depart_date = datetime.datetime.strptime('2019-08-30', day_formate)
    max_depart_date = datetime.datetime.strptime('2019-09-30', day_formate)
    range_one_days = 10
    range_two_days = 4
    pay_load = '{"flightWayEnum":"MT","arrivalProvinceId":2,"arrivalCountryName":"中国","infantCount":0,"cabin":"Y_S","cabinEnum":"Y_S","departCountryName":"中国","flightSegments":[{"departureDate":"2019-08-30","arrivalProvinceId":11548,"arrivalCountryName":"阿尔及利亚","departureCityName":"上海","departureCityCode":"SHA","departureCountryName":"中国","arrivalCityName":"阿尔及尔","arrivalCityCode":"ALG","departureCityTimeZone":480,"arrivalCountryId":6,"timeZone":480,"departureCityId":2,"departureCountryId":1,"arrivalCityTimeZone":60,"departureProvinceId":2,"arrivalCityId":1271},{"departureDate":"2019-09-03","arrivalProvinceId":10121,"arrivalCountryName":"德国","departureCityName":"阿尔及尔","departureCityCode":"ALG","departureCountryName":"阿尔及利亚","arrivalCityName":"法兰克福","arrivalCityCode":"FRA","departureCityTimeZone":60,"arrivalCountryId":28,"timeZone":60,"departureCityId":1271,"departureCountryId":6,"arrivalCityTimeZone":120,"departureProvinceId":11548,"arrivalCityId":250},{"departureDate":"2019-09-12","arrivalProvinceId":2,"arrivalCountryName":"中国","departureCityName":"法兰克福","departureCityCode":"FRA","departureCountryName":"德国","arrivalCityName":"上海","arrivalCityCode":"SHA","departureCityTimeZone":120,"arrivalCountryId":1,"timeZone":120,"departureCityId":250,"departureCountryId":28,"arrivalCityTimeZone":480,"departureProvinceId":10121,"arrivalCityId":2}],"childCount":0,"segmentNo":1,"adultCount":1,"extensionAttributes":{},"transactionID":"92114bccf31d4c3dad93cfc979476315","directFlight":false,"departureCityId":2,"isMultiplePassengerType":0,"flightWay":"M","arrivalCityId":2,"departProvinceId":2}'
    while (min_depart_date < max_depart_date):
        # print('出发时间', min_depart_date.strftime(day_formate))

        depart_date2 = min_depart_date + timedelta(days=range_one_days)
        depart_date3 = depart_date2 + timedelta(days=range_two_days)
        first_ur = first_base_url % (
            min_depart_date.strftime(day_formate),
            (min_depart_date + timedelta(days=range_one_days)).strftime(day_formate),
            (depart_date2 + timedelta(days=range_two_days)).strftime(day_formate))
        print('first_ur:',first_ur)

        # 设置浏览器选项
        options = webdriver.ChromeOptions()

        # 把chrome设置成无界面模式
        options.add_argument('--headless')
        options.add_experimental_option('w3c', True)

        caps = DesiredCapabilities.CHROME
        caps['loggingPrefs'] = {'performance': 'ALL'}
        caps['goog:loggingPrefs'] = {'performance': 'ALL'}

        browser = webdriver.Chrome(options=options, desired_capabilities=caps)
        browser.get(first_ur)
        browser.implicitly_wait(5)
        raw_logs = browser.get_log('performance')

        logs = [json.loads(log['message'])['message'] for log in raw_logs]
        # print(logs)
        sign = deep_search(['sign', 'transactionID'], logs)
        # print('sign:\t', sign['sign'])
        # print('transactionID:\t', sign['transactionID'])
        with open('performance.json', 'w', encoding='utf-8') as f:
            json.dump(logs, f, ensure_ascii=False)

        # search_cr = get_search_cr(first_ur)
        headers['transactionid'] = sign['transactionID']
        headers['sign'] = sign['sign']
        pay_load = update_pay_load_depart_date(min_depart_date, depart_date2, depart_date3, pay_load)
        # print('pay_load:\t',pay_load)
        print_flight_info(min_depart_date, pay_load)
        min_depart_date = min_depart_date + timedelta(days=1)
