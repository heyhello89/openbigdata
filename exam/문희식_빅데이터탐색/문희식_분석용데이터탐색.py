import urllib.request
import datetime
import json
import re
import operator

access_key="1JUdQNlvEneBvGD546ShDvW7mVdVA%2Bd9k%2F7y7CkSgw%2BoERiCt5x3vzDE1qPZGP7uNJ0DL2EiKurdGZRV5ZuuUQ%3D%3D"
# access_key='B2rbAM30hFkQ4NAql1fjpFmE9tcdUluLmFF%2BBGWuBAdiWGWwpCuoZh2tDMVnF3S0TPxLhQW8LiLdURM7%2FZSJqw%3D%3D'
def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success"%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s"%(datetime.datetime.now(),url))
        return None


def getNatVisitor(yyyymm,nat_cd,ed_cd):
    end_point="http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"
    parameters = "?_type=json&serviceKey="+access_key
    parameters+="&YM="+yyyymm
    parameters+="&NAT_CD="+nat_cd
    parameters+="&ED_CD="+ed_cd
    url=end_point+parameters
    retData = get_request_url(url)
    if(retData == None):
        return None
    else:
        return json.loads(retData)

def main():
    with open('.\\national_code.txt','r',encoding='utf8') as infile :
        national_code_list=list(map(lambda x: x.rstrip().replace(' ',''), infile.readlines()))

    national_code_list[0]="000=미상"
    national_code_str=str(national_code_list)
    national_code_str=national_code_str[1:-1]
    national_code_str=national_code_str.replace('\'','').replace(',','').replace('=','')
    p=re.compile("(\d{3})([\w]*)\s")
    national_code_dic={}
    national_code_str_list=p.findall(national_code_str)
    national_list=open('문희식_빅데이터탐색_고려사항.txt','w',encoding='utf8')
    national_list.write('빅데이터 수집 년/월 : 2017년 12월\n사용한 국가 리스트\n')
    for i in range(0,50):
        national_code_dic[national_code_str_list[5*i+2][1]]=national_code_str_list[5*i+2][0]
        national_list.write(national_code_str_list[5*i+2][1]+'\n')
    national_list.close()

    jsonResult=[]
    ed_cd='E'
    log_file = open('문희식_수행로그.txt','w',encoding='utf8')
    for i in national_code_dic.values():
        national_code=str(i)
        jsonData=getNatVisitor('201712',national_code,ed_cd)
        try:
            if (jsonData['response']['header']['resultMsg']=='OK') :
                krName= jsonData['response']['body']['items']['item']['natKorNm']
                krName=krName.replace(' ','')
                iTotalVisit=jsonData['response']['body']['items']['item']['num']
                print('%s_%s:%s' %(krName,'201712',iTotalVisit))
                log_file.write('%s Url Request Success\t%s_%s:%s\n' %(datetime.datetime.now(),krName,'201712',iTotalVisit))
                jsonResult.append({'nat_name':krName,"nat_cd":national_code,'yyyymm':'201712','visit_cnt':iTotalVisit})
        except:
            print(national_code)
    log_file.close()

    visit_rank={}
    data_result=[]
    for i in range (len(jsonResult)):
        try:
            visit_rank[jsonResult[i]['nat_name']]+=int(jsonResult[i]['visit_cnt'])
        except:
            visit_rank[jsonResult[i]['nat_name']]=int(jsonResult[i]['visit_cnt'])
    visit_rank_sorted=sorted(visit_rank.items(), key=operator.itemgetter(1),reverse=True)

    for i in range(len(visit_rank_sorted)):
        data_result.append({'rank':i+1, 'nation':visit_rank_sorted[i][0], 'count':visit_rank_sorted[i][1]})
        if visit_rank_sorted[i][1]==visit_rank_sorted[i-1][1]:
            data_result[i]['rank']=data_result[i-1]['rank']

    with open('문희식_수행결과.json','w',encoding='utf8') as outfile :
        retJson= json.dumps(data_result,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

if __name__ == '__main__':
    main()