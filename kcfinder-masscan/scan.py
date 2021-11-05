import colorama
import requests
import argparse
import time
from colorama import Fore
b = '\033[34;1m'
g = Fore.LIGHTGREEN_EX
c = Fore.LIGHTCYAN_EX
r = Fore.LIGHTRED_EX
w = Fore.LIGHTWHITE_EX

logo = f"""{b}
       _  __    _____ _           _                        
      | |/ /___|  ___(_)_ __   __| | ___ _ __   
      | ' // __| |_  | | '_ \ / _` |/ _ \ '__| 
      | . \ (__|  _| | | | | | (_| |  __/ |    
      |_|\_\___|_|   |_|_| |_|\__,_|\___|_|   
{r}                                                                
==================Information=====================
||Tools     : KcFinder MasScan                  ||
||Author    : Kenzawa/Babwa                     ||
||help      : CLI Python3                       ||
||github    : https://github.com/pengode-handal ||
==================Information=====================
"""
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='Put URL')
parser.add_argument('-l', '--list', help='File Contain URL')
parser.add_argument('-s', '--save', help='If Result Wan\'t To Be Saved')
parser.add_argument('-t', '--TimeOut', help='time out - default: 5')
parser.add_argument('-v', '--version', action='version', version='0.2.1')

args = parser.parse_args()

def getUrl(url):
    urls = []
    with open(url, "r") as ufile:
        allurl = ufile.readlines()
        for i in range(len(allurl)):
            urls.append(allurl[i].strip('\n'))
        return urls

def scan(url, timer=5):
    target = url
    #mengecek prokotol
    target = target.replace('https://', '')
    target = target.replace('http://', '')
    tar_list = target.split('/')
    for tar in tar_list:
        if tar == '':
            tar_list.remove(tar)
    target = '/'.join(tar_list)
    url = 'http://' + target
    if args.TimeOut:
        timer = args.TimeOut
    wl = getUrl('list')
    for i in wl:
        www = url+i
        try:
          get = requests.get(url=www)
        except:
          www = 'https://'+target+i 
          get = requests.get(www)
        if get.status_code == 404:
            pass
        elif get.status_code == 302:
            print(g+'[*] '+c+url+r+' ==> Redirected - '+www)
        elif get.status_code == 200:
            print(b+'[+] '+url+c+' ==> Found!! - '+www)
            if args.save:
                logger(pika=www, nma=args.save)
            else:
                pass
        elif get.status_code == 403:
            pass
        elif get.status_code == 500:
            pass
        else:
            print(b+'[+] '+w+url+r+' ==> Not Found')
def logger(pika, nma):
    file = open(str(nma) + ".txt", "a")
    file.write(str(pika))
    file.write("\n")    
    file.close()

print(logo)

if args.url:
    start = time.time()
    print(w+"##########{}RESULT{}{}###########".format(b, c, w))

    scan(args.url)
    stop = time.time()
    print('Finished in {} second'.format(int(stop - start)))
elif args.list:
    urll = getUrl(args.list)
    start = time.time()
    print(w+"##########{}RESULT{}{}###########".format(b, c, w))
    for link in urll:
            scan(link)
    stop = time.time()
    print('Finished in {} second'.format(int(stop - start)))