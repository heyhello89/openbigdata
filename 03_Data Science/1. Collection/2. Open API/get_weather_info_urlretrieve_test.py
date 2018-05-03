import urllib.request
import datetime
import json

nx='89'
ny='91'

now_date=datetime.datetime.now()
# get_date=now_date-datetime.timedelta(hours=1)


def get_request_url(url):
    req=urllib.request.urlretrieve(url, '기상정보.json')
    print(req)


def getWeatherResult(nx, ny):
    base="http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData?"
    base_date=datetime.datetime.strftime(now_date, '%Y%m%d')
    base_time=datetime.datetime.strftime(now_date, '%H%M')
    type='json'
    pageNo='1'
    numOfRows='100'
    serviceKey='VNH7QeBnhzad%2B45QS4DMbIvJp0s%2Fx2iY9vdKxLYJJJEHMFFHDLr8HZJHuPgfjWRTg22OklmBOuSWznNeJktguQ%3D%3D'

    parameters = "base_date=%s&base_time=%s&nx=%s&ny=%s&_type=%s&ServiceKey=%s&pageNo=%s&numOfRows=%s"%(base_date,base_time,nx,ny,type,serviceKey,pageNo,numOfRows)
    url=base+parameters
    print(url)
    get_request_url(url)

getWeatherResult(89, 91)
