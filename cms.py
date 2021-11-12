#!/usr/bin/env python3

#Buatan Babwa,  gpp mau di ganti, babwa kn baik xixixi
#tapi lebih baik buat sendiri biar bisa puas

from colorama import Fore
import requests
from requests.exceptions import ConnectionError

r = Fore.RED 
c = Fore.CYAN
g = Fore.GREEN
b = Fore.BLUE
def find_cms(url):
        count = 0
        try:
          try:
            if 'http' in url:
              pass
            else:
              urlll = "http://"+url
              res = requests.get(urlll)
          except:
            res = requests.get("https://"+url)

          count += 1
          if "wp-content/themes/" in res.text or "powered by WordPress" in res.text:
              print(str(c+f"[+]{b}{count}. "+url + " ==> WordPress"))
          elif "Drupal.settings" in res.text or "sites/default" in res.text:
              print(str(c+f"[+]{b}{count}. "+url+" ==> Drupal"))
          elif "window.vBulletin" in res.text or "vBulletin_" in res.text:
              print(str(c+f"[+]{b}{count}. "+url+" ==> "+"vBulletin"))
          elif "Joomla!" in res.text or "joomla-script-" in res.text:
              print(str(c+f"[+]{b}{count}. "+url+" ==> Joomla"))
          elif "Mage.Cookies" in res.text or "skin/frontend" in res.text:
            print(str(c+f"[+]{b}{count}. "+url+" ==> Magento"))
          elif "osCommerce" in res.text:
            print(str(c+f"[+]{b}{count}. "+url+" ==> osCommerce"))
          elif "prestashop" in res.text or "PrestaShop" in res.text:
            print(str(c+f"[+]{b}{count}. "+url+" ==> PrestaShop"))
          elif "/cmsms" in res.text:
            print(str(c+f"[+]{b}{count}. "+url+" ==> CMS Made Simple"))
          elif "theme/image.php" in res.text or "moodle-block_navigation-navigation" in res.text:
            print(str(c+f"[+]{b}{count}. "+url+" ==> Moodle"))
          elif "mediawiki.page.startup" in res.text or "mediawiki.legacy.wikibits" in res.text:
            print(str(c+f"[+]{b}{count}. "+url+" ==> Media Wiki"))
          else:
            print(str(r+f"[!]{count}. "+url+" ==> Unknown"))
        except ConnectionRefusedError:
          print(r+url+" ==> Connection Refused Error")
          pass
        except ConnectionError:
          print(r+url+" ==> Conection Error")
          pass
        except:
          print(r+url+" ==> REFUSED")
          pass
          
      
def getUrl(url):
    urls = []
    with open(url, "r") as ufile:
        allurl = ufile.readlines()
        for i in range(len(allurl)):
            urls.append(allurl[i].strip('\n'))
        return urls 
urll = str(input('File list: '))
urls = getUrl(urll)
for link in urls:
  find_cms(link)
