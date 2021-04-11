from time import sleep
from celery import shared_task
from bs4 import BeautifulSoup
from lottoAPI.models import *
import requests
import json




@shared_task
def create_gov_thai():
    print('Creating data..')
    req = requests.get('https://lotto.postjung.com', headers={'User-Agent': 'Mozilla/5.0'})
    bs = BeautifulSoup(req.content, 'html.parser')
    title = bs.find_all('div', attrs={'class':'sptitle'})[0].get_text()[0:19]
    date = bs.find_all('div', attrs={'class':'sptitle'})[0].get_text()[22:42]
    FirstPrize = bs.find_all('div', attrs={'class':'xres'})[0].get_text()
    ThreeFront = bs.find_all('div', attrs={'class':'xres'})[2].get_text()[0:3]
    ThreeFrontTwo = bs.find_all('div', attrs={'class':'xres'})[2].get_text()[3:6]
    ThreeUnderTwo = bs.find_all('div', attrs={'class':'xres'})[3].get_text()[3:6]
    TwoUnder = bs.find_all('div', attrs={'class':'xres'})[1].get_text()
    
    print({'title':title, 'date':date, 'FirstPrize':FirstPrize, 'ThreeFront':ThreeFront, 'ThreeFrontTwo':ThreeFrontTwo, 'ThreeUnder':ThreeUnder, 'ThreeUnderTwo':ThreeUnderTwo, 'TwoUnder':TwoUnder})

    gov_thai.objects.create(
        title=title,
        date=date,
        FirstPrize=FirstPrize,
        ThreeFront=ThreeFront,
        ThreeFrontTwo=ThreeFrontTwo,
        ThreeUnder=ThreeUnder,
        ThreeUnderTwo=ThreeUnderTwo,
        TwoUnder=TwoUnder,
    )

    sleep(5)
    
    
@shared_task
def update_gov_thai():
    print('Updating data..')
    req = requests.get('https://lotto.postjung.com', headers={'User-Agent': 'Mozilla/5.0'})
    bs = BeautifulSoup(req.content, 'html.parser')
    title = bs.find_all('div', attrs={'class':'sptitle'})[0].get_text()[0:19]
    date = bs.find_all('div', attrs={'class':'sptitle'})[0].get_text()[22:42]
    FirstPrize = bs.find_all('div', attrs={'class':'xres'})[0].get_text()
    ThreeFront = bs.find_all('div', attrs={'class':'xres'})[2].get_text()[0:3]
    ThreeFrontTwo = bs.find_all('div', attrs={'class':'xres'})[2].get_text()[3:6]
    ThreeUnder = bs.find_all('div', attrs={'class':'xres'})[3].get_text()[0:3]
    ThreeUnderTwo = bs.find_all('div', attrs={'class':'xres'})[3].get_text()[3:6]
    TwoUnder = bs.find_all('div', attrs={'class':'xres'})[1].get_text()
    
    data = {'title':title, 'date':date, 'FirstPrize':FirstPrize, 'ThreeFront':ThreeFront, 'ThreeFrontTwo':ThreeFrontTwo, 'ThreeUnder':ThreeUnder, 'ThreeUnderTwo':ThreeUnderTwo, 'TwoUnder':TwoUnder}
    gov_thai.objects.filter(date=date).update(**data)

    sleep(5)

create_gov_thai()
if True:
    sleep(5)
    update_gov_thai()


@shared_task
def create_lao_vip():
    print('Creating lao VIP data...')
    req = requests.get('https://www.laosviplot.com/result')
    bs = BeautifulSoup(req.content, 'html.parser')
    json_data = json.loads(str(bs.text))
    numOne = json_data['lotto_0']
    numTwo = json_data['lotto_1']
    numThree = json_data['lotto_2']
    numFour = json_data['lotto_3']
    numFive = json_data['lotto_4']
    title = ('หวยลาวVIP')
    Five = numOne + numTwo + numThree + numFour + numFive
    Four = numOne + numTwo + numThree + numFour
    Three = numOne + numTwo + numThree
    Two = numOne + numTwo
    date = json_data['date']
    
    print({'title':title, 'Five':Five, 'Four':Four, 'Three':Three, 'Two':Two, 'date':date})

    lao_vip.objects.create(
        title=title,
        Five=Five,
        Four=Four,
        Three=Three,
        Two=Two,
        date=date
    )
    
    sleep(15)
    
@shared_task
def update_lao_vip():
    print('Updating lao VIP data...')
    req = requests.get('https://www.laosviplot.com/result')
    bs = BeautifulSoup(req.content, 'html.parser')
    json_data = json.loads(str(bs.text))
    numOne = json_data['lotto_0']
    numTwo = json_data['lotto_1']
    numThree = json_data['lotto_2']
    numFour = json_data['lotto_3']
    numFive = json_data['lotto_4']
    title = ('หวยลาวVIP')
    Five = numOne + numTwo + numThree + numFour + numFive
    Four = numOne + numTwo + numThree + numFour
    Three = numOne + numTwo + numThree
    Two = numOne + numTwo
    date = json_data['date']
    
    data= {'title':title, 'Five':Five, 'Four':Four, 'Three':Three, 'Two':Two, 'date':date}
    lao_vip.objects.filter(date=date).update(**data)


create_lao_vip()
if True:
    sleep(15)
    update_lao_vip()


@shared_task
def create_lao_lotto():
    print('Creating lao lotto data...')
    req = requests.get('https://www.ruay.info/%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%AB%E0%B8%A7%E0%B8%A2%E0%B8%A5%E0%B8%B2%E0%B8%A7/')
    bs = BeautifulSoup(req.content, 'html.parser')
    title = bs.find_all('strong')[1].get_text()
    date = bs.find_all('span')[15].get_text()
    Four = bs.find_all('strong')[3].get_text()
    Three = bs.find_all('strong')[6].get_text()
    Two = bs.find_all('strong')[7].get_text()
    
    print({'title':title, 'Four':Four, 'Three':Three, 'Two':Two, 'date':date})
    
    lao_lotto.objects.create(
        title=title,
        Four=Four,
        Three=Three,
        Two=Two,
        date=date
    )
    
    sleep(15)


@shared_task
def update_lao_lotto():
    print('Updating lao lotto data...')
    req = requests.get('https://www.ruay.info/%E0%B8%95%E0%B8%A3%E0%B8%A7%E0%B8%88%E0%B8%AB%E0%B8%A7%E0%B8%A2%E0%B8%A5%E0%B8%B2%E0%B8%A7/')
    bs = BeautifulSoup(req.content, 'html.parser')
    title = bs.find_all('strong')[1].get_text()
    date = bs.find_all('span')[15].get_text()
    Four = bs.find_all('strong')[3].get_text()
    Three = bs.find_all('strong')[6].get_text()
    Two = bs.find_all('strong')[7].get_text()
    
    data = ({'title':title, 'Four':Four, 'Three':Three, 'Two':Two, 'date':date})
    lao_lotto.objects.filter(date=date).update(**data)

create_lao_lotto()
if True:
    sleep(15)
    update_lao_lotto()
    