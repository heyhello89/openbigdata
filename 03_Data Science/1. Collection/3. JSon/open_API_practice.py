import json

print("데이터 분석을 시작합니다.")
count = 0

with open("빅데이터_naver_news.json", encoding="utf-8") as json_data:
    json_data_load = json.load(json_data)
    json_data_string = json.dumps(json_data_load)
    jsonResult = json.loads(json_data_string)

null_count=1
org_link_list=[]
for jsonResult_instance in jsonResult:
    try:
        org_link_list.append(jsonResult_instance['org_link'].split('/')[2])
    except:
        print("'org_link'가 없는 기사를 발견했습니다.")
        null_count+=1

domain_count=0
domain_list=[]
for domain_instance in org_link_list:
    for domain_target in org_link_list:
        if domain_instance==domain_target:
            domain_count+=1
    domain_list.append((domain_instance,domain_count))
    domain_count=0

domain=list(set(domain_list))
domain_sorted=reversed(sorted(domain, key=lambda domain: domain[1]))

print("<네이버 검색 빅데이터 분석>\n검색어: 이명박\n전체 도메인 수: %d\n전체 건수: %s\n부정확한 데이터수: %s\n\n- 도메인 별 뉴스 기사 분석"%(len(domain),len(jsonResult)-null_count,null_count))
for domain in domain_sorted:
    print("%s: %s건"%(domain[0], domain[1]))