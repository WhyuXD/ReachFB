#-------------------------------------->
#     *recode mulu pleer 
#-------------------------------------->
#     *Coding by WahyuDin Ambia
#     *Name tool ReachFB <--- don't remove name ReachFB
#     *version 1.0

#---  JALANKAN TOOLS
if __name__=="__main__":
       import os, sys, shutil, subprocess 
	if sys.version_info.major != 3: # cek versi python 
		exit("\n\t\x1b[0m type: python Reach.py \n")
	
	# Don't delete the --> coox <-- file, you will get an error
	coox = ("rm -rf data/indo.txt && rm -rf data/english.txt && rm -rf data/pengguna.txt")
	try: # install module
		import requests 
	except ImportError:
		print ('\n\t\x1b[0m $ install module requests ...\n')
		os.system("python -m pip install --upgrade pip && pip install requests")
		os.system(coox)
	try:
		import bs4 
	except ImportError:
		print ('\n\t\x1b[0m $ install module bs4 ...\n')
		os.system("python -m pip install --upgrade pip && pip install bs4")
		os.system(coox)
	try:
		import mechanize 
	except ImportError:
		print ('\n\t\x1b[0m $ install module mechanize ...\n')
		os.system("python -m pip install --upgrade pip && pip install mechanize")
		os.system(coox)
	try:
		import concurrent.futures 
	except ImportError:
		print ('\n\t\x1b[0m $ install module futures ...\n')
		os.system("python -m pip install --upgrade pip && pip install futures")
		os.system(coox)
	try:
		import rich 
	except ImportError:
		print ('\n\t\x1b[0m $ install module rich ...\n')
		os.system("python -m pip install --upgrade pip && pip install rich")
		os.system(coox)
		
	try: # music mp3
		Share = open(os.devnull, "w")
		my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=Share,stderr=subprocess.STDOUT)
		Share.close()
		if my_music !=0:
			os.system('pkg install play-audio' )
			#os.system(coox)
	except FileNotFoundError:
		os.system('pkg install play-audio' )
		#os.system(coox)
			
	from xyz import *
	from wahyu.menu import wahyu_xd_ganteng_banget as onichan 
	from shutil import rmtree as lolichan
	runtah = [
		"wahyu/__pycache__",
		"log/__pycache__",
		"xd/__pycache__"
	]
	try:
		[lolichan(xz) for xz in runtah]
	except: 
		pass 
	os.system('git pull')
	os.system('clear')
	tulis(Panel(f"""
{Te}{O}Mohon maaf 🙏 script ini belum saya rilis, mohon bersabar😸:
 
 {O}facebook{M} : {H}facebook.com/WaGyoXD {P}(Wahyu XD)
 {O}whatsap{M}  :{H} +6283132458199
		""",style='#FF0022'))
		
