import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


#아카데미 남우주연상 수상작
def academy_men():

    data = requests.get('https://pedia.watcha.com/ko-KR/staffmades/603', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    lis = soup.select('#root > div > div.css-1fgu4u8 > section > section > div > div > ul>li ')
    academy_men_list=[]

    for li in lis:
        link = 'https://pedia.watcha.com' +  li.find('a')['href']
        title = li.select_one('div.css-ixy093 > div.css-niy0za').text.strip()
        star = li.select_one('div.css-ixy093 > div.css-m9i0qw').text
        img = li.select_one('div.css-1qmeemv > div > img')['src']
        academy_men_dict ={
            'link': link,
            'title': title,
            'star': star,
            'img': img
        }
        academy_men_list.append(academy_men_dict)
    return academy_men_list


#전주국제영화제 수상작
def jeonju():

    data = requests.get('https://pedia.watcha.com/ko-KR/staffmades/135', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    lis = soup.select('#root > div > div.css-1fgu4u8 > section > section > div > div > ul>li ')
    jeonju_list=[]

    for li in lis:
        link = 'https://pedia.watcha.com' + li.find('a')['href']
        title = li.select_one('div.css-ixy093 > div.css-niy0za').text.strip()
        star = li.select_one('div.css-ixy093 > div.css-m9i0qw').text
        img = li.select_one('div.css-1qmeemv > div > img')['src']
        academy_men_dict ={
            'link': link,
            'title': title,
            'star': star,
            'img': img
        }
        jeonju_list.append(academy_men_dict)

    return jeonju_list


#베니스영화제 황금사자상 수상작
def venice_film():
    data = requests.get('https://pedia.watcha.com/ko-KR/staffmades/610', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    lis = soup.select('#root > div > div.css-1fgu4u8 > section > section > div > div > ul>li ')
    gold_lion_list=[]

    for li in lis:
        link = 'https://pedia.watcha.com' + li.find('a')['href']
        title = li.select_one('div.css-ixy093 > div.css-niy0za').text.strip()
        star = li.select_one('div.css-ixy093 > div.css-m9i0qw').text
        img = li.select_one('div.css-1qmeemv > div > img')['src']
        gold_lion_dict ={
            'link': link,
            'title': title,
            'star': star,
            'img': img
        }
        gold_lion_list.append(gold_lion_dict)

    return gold_lion_list


#아카데미 촬영상 수상작
def academy_film():
    data = requests.get('https://pedia.watcha.com/ko-KR/staffmades/581', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    lis = soup.select('#root > div > div.css-1fgu4u8 > section > section > div > div > ul>li ')
    academy_film_list=[]

    for li in lis:
        link = 'https://pedia.watcha.com' + li.find('a')['href']
        title = li.select_one('div.css-ixy093 > div.css-niy0za').text.strip()
        star = li.select_one('div.css-ixy093 > div.css-m9i0qw').text
        img = li.select_one('div.css-1qmeemv > div > img')['src']
        academy_film_dict ={
            'link': link,
            'title': title,
            'star': star,
            'img': img
        }
        academy_film_list.append(academy_film_dict)

    return academy_film_list


#아카데미 여우조연상 수상작
def academy_women():
    data = requests.get('https://pedia.watcha.com/ko-KR/staffmades/4708', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    lis = soup.select('#root > div > div.css-1fgu4u8 > section > section > div > div > ul>li ')
    academy_women_list=[]

    for li in lis:
        link = 'https://pedia.watcha.com' + li.find('a')['href']
        title = li.select_one('div.css-ixy093 > div.css-niy0za').text.strip()
        star = li.select_one('div.css-ixy093 > div.css-m9i0qw').text
        img = li.select_one('div.css-1qmeemv > div > img')['src']
        academy_women_dict ={
            'link': link,
            'title': title,
            'star': star,
            'img': img
        }
        academy_women_list.append(academy_women_dict)

    return academy_women_list