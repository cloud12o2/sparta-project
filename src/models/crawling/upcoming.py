import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# daum영화 넷플리스 공개예정작
def netflix_newly():
    data = requests.get('https://movie.daum.net/premovie/netflix?flag=Y', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    all_li = soup.select('#mainContent>div>div.box_movie>ul>li')

    netflix_newly_list = []

    for li in all_li:
        title = li.select_one('div.thumb_cont>strong>a').text
        open_date = li.select_one('div>span>span').text.strip()
        img = li.select_one('div>img')['src']
        href_find = li.find(class_='thumb_item')['href']
        link = "https://movie.daum.net/" + href_find

        netflix_newly_dict = {
            'title': title,
            'open_date': open_date,
            'img': img,
            'link': link
        }
        netflix_newly_list.append(netflix_newly_dict)

    return netflix_newly_list




# daum영화 왓챠 개봉예정작
def daum_watcha_newly():
    data = requests.get('https://movie.daum.net/premovie/watcha?flag=Y', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    all_li = soup.select('#mainContent>div>div.box_movie>ul>li')

    daum_watcha_newly_list = []

    for li in all_li:
        title = li.select_one('div.thumb_cont>strong>a').text
        open_date = li.select_one('div>span>span').text.strip()
        img = li.select_one('div>img')['src']
        href_find = li.find(class_='thumb_item')['href']
        link = 'https://movie.daum.net' + href_find

        daum_watcha_newly_dict = {
            'title': title,
            'open_date': open_date,
            'img': img,
            'link': link
        }
        daum_watcha_newly_list.append(daum_watcha_newly_dict)

    return daum_watcha_newly_list



# yes24영화 개봉예정작
def yes24_newly():
    data = requests.get('https://movie.yes24.com/MovieInfo/PromotionMovie', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    all_li = soup.select(
        '#wrap>div.container>div.content>div.movie_area>div>div.movie_rank_cont>div.comming_box>div.movie_info_card')

    yes24_newly_list = []

    for li in all_li:
        title = li.select_one('div.mv_info>p.mv_tit').text.replace(" ", "").replace("\n", "").replace("\r", "").strip("12345")
        open_date = li.select_one('div.mv_info>p.mv_txt').text.replace("\n", "")
        img = li.select_one('div.img_thumb>img')['src']

        yes24_newly_dict = {
            'title': title,
            'open_date': open_date,
            'img': img,
        }
        yes24_newly_list.append(yes24_newly_dict)

    return yes24_newly_list
