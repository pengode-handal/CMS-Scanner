#!/usr/bin/env python3
import json
from colorama import Fore
import requests

# Toggle to use tools installed in the system path instead of using from plugins
USE_PREINSTALLED_TOOLS = False
r = Fore.RED 
c = Fore.CYAN
g = Fore.GREEN
b = Fore.BLUE
def find_cms(url):
        count = 0
        try:
          res = requests.get('http://'+url)
        except:
          print(r+"Error")
        count = count + 1
        if "wp-content/themes/" in res.text or "powered by WordPress" in res.text:
            print(str(c+f"[+]{b}{count}. "+url + " ==> WordPress"))
        elif "Drupal.settings" in res.text or "sites/default" in res.text:
            print(str(c+f"[+]{b}{count}. "+url+" ==> Drupal"))
        elif "window.vBulletin" in res.text or "vBulletin_" in res.text:
            print(str(c+f"[+]{b}{count}. "+url+" ==> "+"vBulletin"))
        elif "Joomla!" in res.text or "joomla-script-" in res.text:
            print(str(c+f"[+]{b}{count}. "+url+" ==> Joomla"))
        elif "Mage.Cookies" in res.text:
          print(str(c+f"[+]{b}{count}. "+url+" ==> Magento"))
        elif "osCommerce" in res.text:
          print(str(c+f"[+]{b}{count}. "+url+" ==> osCommerce"))
        elif "prestashop" in res.text or "PrestaShop" in res.text:
          print(str(c+f"[+]{b}{count}. "+url+" ==> PrestaShop"))
        else:
          print(str(r+f"[!]{count}. "+url+" ==> Unknown"))
          
      
def getUrl(url):
    urls = []
    with open(url, "r") as ufile:
        allurl = ufile.readlines()
        for i in range(len(allurl)):
            urls.append(allurl[i].strip('\n'))
        return urls 
urll = str(input('list: '))
urls = getUrl(urll)
for link in urls:
  find_cms(link)