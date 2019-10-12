# Examples of scrapping with beautifulsoup

from bs4 import BeautifulSoup
import os
import re
import time


# wget the sap status file, execute every 5 minutes with celery
wget_command = "wget -N salive.shtml"
os.system(wget_command)
 

with open ("salive.shtml") as fp:
    soup = BeautifulSoup(fp, "html.parser")
    tr = soup.find_all('td')
    #print tr
    tr1 = open("tr.html","w")
    tr1.write(str(tr)) # saves files with all trs from table
    tr1.close()

with open ("tr.html") as fp1:
    soup2 = BeautifulSoup(fp1, "html.parser")
 
    p20 = soup2.find_all(string='P20 Production ERP Logistics & Finance')[0] # find first return of list
   
    parentp20 = p20.parent() # parent of match
    running = parentp20[1].text # second element of list in text
    if running == "RUNNING1":
        print "OK"
    else:
       kill_command = "pwd"   
       os.system(kill_command)
