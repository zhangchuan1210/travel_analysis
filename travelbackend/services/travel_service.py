import re
import time
import urllib
import requests
from bs4 import BeautifulSoup


class TravelService:
    def __init__(self, url='', city_id='', sight_id=''):
        self.url = url
        self.city_id = city_id
        self.sight_id = sight_id

    def get_place(self, url):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        response = requests.get(url=url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        soup1 = soup.select('.city-selector-tab-main-city')  # .cf a[href^="/place"]
        citys = []
        for i in range(1, len(soup1)):
            province = soup1[i].select('.city-selector-tab-main-city-title')[0].get_text()
            city = soup1[i].find_all('a', class_='city-selector-tab-main-city-list-item')
            city_tag = []
            for tag in city:
                city_info_title = tag['title']
                city_tag_item = tag['href'].split('/')[-1].replace('.html', '')
                city_tag.append(city_tag_item)
                with open('D:\\project\\pythonProject\\tourism_scraper\\province_info.csv', 'a+',
                          encoding='utf-8-sig') as f:
                    f.write(province + ',' + city_tag_item + ',' + city_info_title + '\n')
            citys.append(city_tag)
            print(province, citys)
        return citys

    def get_sight_info(self, url):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        response = requests.get(url=url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        soup1 = soup.select('.cardListBox_box__lMuWz .sightItemCard_box__2FUEj')
        # Extract city name
        city_name_soup = soup.find('h2', class_='headerBarModule_district_name__jtn7Q')
        if city_name_soup:
            city_name = city_name_soup.contents[0].strip()
            print(city_name)
            for i in range(len(soup1)):
                link = soup1[i].select('.titleModule_name__Li4Tv a')[0]
                href = link['href']
                parts = href.split('/')
                city_id = parts[4]  # shanghai2
                sight_id = parts[5].split('.')[0]  # 3739
                sight_name = link.get_text()  # 南京路步行街
                print(city_name, city_id, sight_id, sight_name)
                self.get_comment(city_id, sight_id)
                # Write city and sight id into CSV file
                with open('D:\\project\\pythonProject\\tourism_scraper\\city_sight.csv', 'a+',
                          encoding='utf-8-sig') as f:
                    f.write(str(i) + ',' + city_name + ',' + city_id + ',' + sight_name + ',' + sight_id + '\n')
                try:
                    price_str = soup1[i].select('.bottomModule_box__dHx0U .priceView_real-price-view__l7J6R')[
                        0].get_text()  # priceView_real-price-view__l7J6R
                    if '免费' in price_str:
                        price = '0'
                    else:
                        price = re.search(r'¥(\d+)', price_str)
                        if price is not None:
                            price = price.group(1)
                        else:
                            price = ''
                    print(city_id, sight_id, price)
                    with open('D:\\project\\pythonProject\\tourism_scraper\\sight_price.csv', 'a+',
                              encoding='utf-8-sig') as f:
                        f.write(city_id + ',' + sight_id + ',' + price + '\n')
                except IndexError as e:
                    print("An error occurred: {e}")
                try:
                    soupTemp = soup1[i].select('.commentInfoModule_box__msDjT')
                    heat_score = soupTemp[0].find('span', class_='commentInfoModule_heat-score_value__J8p3b').text
                    rating_score = soupTemp[0].find('span',
                                                    class_='commentInfoModule_comment-score_value__iUsa8').text
                    review_count = soupTemp[0].find_all('span', class_='commentInfoModule_comment-text__UBk1F')[
                        -1].text.strip('条点评')
                    if '万' in review_count:
                        review_count_num = float(review_count.replace('万', '')) * 10000
                    else:
                        review_count_num = int(review_count)
                    with open('D:\\project\\pythonProject\\tourism_scraper\\sight_comments_info.csv', 'a+',
                              encoding='utf-8-sig') as f:
                        f.write(city_id + ',' + sight_id + ',' + heat_score + ',' + rating_score + ',' + str(
                            review_count_num) + '\n')
                    with open('D:\\project\\pythonProject\\tourism_scraper\\sight_detail.csv', 'a+',
                              encoding='utf-8-sig') as f:
                        f.write(
                            str(i) + ',' + city_id + ',' + sight_id + ',' + sight_name + ',' + heat_score + ',' + str(
                                review_count_num) + ',' + rating_score + '\n')
                except AttributeError as e:
                    print("An error occurred: {e}")
            time.sleep(0.1)

    def get_info(url, city_id, provice_name):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        response = requests.get(url=url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        infor = soup.select('.list_mod2')
        # Loop to extract data
        for i in range(len(infor)):
            sight_id = infor[i].select('.rdetailbox dl dt a')[0]["href"].replace('.', '/').split("/")[7]  # 获取景点 id
            name = infor[i].select('.rdetailbox dl dt a')[0]["title"]  # 获取景点名称
            rank_1 = infor[i].select('.rdetailbox dl dt s')[0].get_text()  # 获取排名信息
            # rank = re.sub("\D", "", rank_1)  # 利用正则表达式提取数字部分作为排名
            rank = 3
            score_1 = infor[i].select('.score')[0].get_text()
            if score_1 == "暂无评分":
                score = str(-1)
            else:
                # score = str(int(re.sub(r"\D", "", score_1)) / 10)
                score = 55
            comm_1 = infor[i].select('.recomment')[0].get_text()
            # comm = re.sub(r"\D", "", comm_1)
            comm = 222
            print(provice_name, city_id, sight_id, name, score, comm, rank)
            with open(r'./data/sight_detail_info.csv', 'a+', encoding='utf-8-sig') as f:
                f.write(
                    provice_name + ';' + city_id + ';' + sight_id + ';' + name + ';' + score + ';' + comm + ';' + rank + '\n')
            time.sleep(1)

    def get_price(city_name):
        global sum_
        url = 'https://travelsearch.fliggy.com/index.htm?searchType=product&keyword=' + urllib.request.quote(
            city_name)
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        response = requests.get(url=url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        soup1 = soup.select('.price')
        for i in range(len(soup1)):
            soup2 = soup1[i].get_text()[0:]
            sum_ = float(soup2)
            avg = sum_ / len(soup1)
            with open('./data/sight_price.csv', 'a+', encoding='utf-8-sig') as f:
                f.write(city_name + ',' + str(avg) + '\n')
        for i in range(13, 17):
            url = 'https://you.ctrip.com/months/' + str(i) + '.html'
            response = requests.get(url=url, headers=headers)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            soup1 = soup.select('.city-name')
            soup2 = soup.select('.opts>.been')
            soup3 = soup.select('.opts>.want')
            # season1=season[i-13]
            season1 = '22222'
            for i in range(len(soup1)):
                recommend_name = soup1[i].next_element
                recommend_opts = soup2[i].next_element
                recommend_want = soup3[i].next_element
                print(recommend_name, recommend_opts, recommend_want)
                with open('./data/recommend_data.csv', 'a+', encoding='utf-8-sig') as f:
                    f.write(season1 + ',' + recommend_name + ',' + recommend_opts + '\n')

    def get_comment(city_id, sight_id):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }
        url = 'https://you.ctrip.com/sight/' + city_id + '/' + sight_id + '.html'
        response = requests.get(url=url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        soup1 = soup.select('.commentModuleRef .commentModule .commentList .commentItem')
        for i in range(len(soup1)):
            try:
                comment_user = soup1[i].select('.userName')[0].text
                comment_score_match = re.search('(\d+)分', soup1[i].select('.averageScore')[0].text)
                if comment_score_match:
                    score = comment_score_match.group(1)
                comment_detail = soup1[i].select('.commentDetail')[0].text
                comment_date = soup1[i].select_one('.commentTime').get_text(strip=True).split('IP属地')[0].strip()
                print(comment_user, score, comment_date, comment_detail)
                with open('D:\\project\\pythonProject\\tourism_scraper\\sight_comment.csv', 'a+',
                          encoding='utf-8-sig') as f:
                    f.write(
                        city_id + '&;' + sight_id + '&;' + comment_user + '&;' + score + '&;' + comment_date + '&;' + comment_detail + '\n' + '\n')
            except IndexError as e:
                print('an error occured:{e}')
