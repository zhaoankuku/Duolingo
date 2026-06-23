import requests
import csv


url='https://www.duolingo.com/api/1/courses/list'
headers={
        'cookie':'logged_out_uuid=fdc1a995-bdbd-4d87-8362-eaef1c331034; lang=en; duocsexp7=design_lab_web_duolingo_sans~control~; wuuid=28a9c235-7630-4f41-86b3-ff53a99fb7c8; tsl=1776840411199; lu=https://en.duolingo.com/register; initial_referrer=$direct; lr=; AWSALB=19Rmm3UvYEfDKPKv32nWwvmx2AVp5ziBa+QSvDFShLwZhcmWCKOrCNbtAZxKHzQxCJUANzz1H42Eh+uI3EpnV9/QK+6rWF76NmrwvFFw2Rw0PEjCJLAakOxG4pu9; AWSALBCORS=19Rmm3UvYEfDKPKv32nWwvmx2AVp5ziBa+QSvDFShLwZhcmWCKOrCNbtAZxKHzQxCJUANzz1H42Eh+uI3EpnV9/QK+6rWF76NmrwvFFw2Rw0PEjCJLAakOxG4pu9; _gcl_au=1.1.1445262853.1776840415; _ga_CSFDVCPQ4F=GS2.1.s1776840417$o1$g0$t1776840417$j60$l0$h0; _ga=GA1.2.2039925526.1776840417; _gid=GA1.2.264666965.1776840418; _fbp=fb.1.1776840418538.441134823277083843; g_state={"i_l":0,"i_ll":1776840419619,"i_b":"MrKRm7IWg/ntKf62T+XHjXCc6+AhPX3AZv0p5Enwqug","i_e":{"enable_itp_optimization":0},"i_et":1776840419619}; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Apr+22+2026+14%3A47%3A59+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202404.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=5ac4bce5-20b7-42b1-ab44-9f7aac3d1fbd&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fen.duolingo.com%2Fregister&groups=C0001%3A1%2CC0003%3A1%2CSPD_BG%3A1%2CC0002%3A1%2CC0004%3A1',
        'accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'
              }
response = requests.get(url, headers=headers)
contents=response.json()

with open('duolinguo.csv', 'a+', newline="", encoding='utf8') as f:
    header = ['learn_id', 'learning_name', 'num_learnning_str', 'number', 'from_language']
    writer = csv.writer(f)
    writer.writerow(header)

    for content in contents:
                learning_id = content['learning_language_id']
                from_language = content['from_language_name']
                learning_name = content['learning_language_name']
                num_learning_string = content.get('num_learners_string', '')
                number = content['num_learners']
                writer.writerow([learning_id,learning_name,num_learning_string,number,from_language])
                print(learning_id, learning_name, num_learning_string, number, from_language)

# print(contents)