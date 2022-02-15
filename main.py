# Imports
import scapy.all as scapy
import requests
import time
import fake_useragent
import json
from rich.console import Console
from rich.table import Table
import sys
import os

#sys.exit();

#Data
console = Console()

#Fucntions
def clear():
  print(chr(27) + "[2J")

def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_broadcast_packet = broadcast_packet/arp_packet
    answered_list = scapy.srp(arp_broadcast_packet, timeout=1, verbose=False)[0]
    client_list = []

    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)

    return client_list

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def InnoDecode(summary, ip, mac):

  if(summary.get('DEVS') == None):
    print('no devs')
    return 0


  # Get from hash boards
  hr = "/";
  temp = "/";
  for item in summary['DEVS']:
    hr += str(toFixed(item['Hash Rate'],1)) + '/'
    temp += str(item['Temperature']) + '/'
      

  data = {
    "ip" : str(ip),
    "type" : '2t2', #@@@ todo
    "error" : '0',  #@@@ todo
    "hr" : str(toFixed(summary['TotalHash']['Hash Rate'], 1)) + " " + str(hr), 
    "temp" : str(temp), 
    "pool" :  '0',  #@@@ todo
    "worker" :  '0',  #@@@ todo 
    "uptime" :  '0'  #@@@ todo
  }

  return data;

def printTable(data):{

  print(
    data['ip'] +"\t"+ 
    data['type'] +"\t"+ 
    data['error'] +"\t"+ 
    data['hr'] +"\t"+ 
    data['temp'] +"\t"+
    data['pool'] +"\t"+
    data['worker'] +"\t"+
    data['uptime']
  )
  
  
}

#Console Output
output = {
  "header": ["IP", "type", "Error", "HR", "Temp", "Pool", "Worker", "Uptime"],
}


#Table
table = Table(show_header=True, header_style="bold magenta")

#Table Header
table.add_column("IP", style="dim", width=12)
table.add_column("Type")
table.add_column("Error", justify="right")
table.add_column("HR", justify="right")
table.add_column("Temp", justify="right")
table.add_column("Pool", justify="right")
table.add_column("Worker", justify="right")
table.add_column("Uptime", justify="right")


#console.print(table)
# clear()
# console.print(table)


# options = get_arguments()
result_list = scan('192.168.0.0/24')

session = requests.Session();
header = {
  'user-agent': fake_useragent.UserAgent().random
}


for item in result_list:

  r = 0
  try:
    r = session.get("http://" + item["ip"], verify=False, timeout=5, headers=header)
  except requests.ConnectTimeout as e:
    print(' - no http')
    continue
  except Exception as e:
    print(str(e))
    continue
  
  if r.status_code == 200: 

    # InnoSilicon
    if r.text.find('<title>AsicMiner</title>') != -1: 
      print(' - InnoSilicon')

      # Post Login
      innoSession = requests.Session();
      header['user-agent'] = fake_useragent.UserAgent().random
      header['Authorization'] = ""
      innoLoginR = innoSession.post("http://" + item["ip"] + "/api/auth", verify=False, timeout=60, headers=header, data={'username': 'admin','password': 'admin'})
      
      # Decode
      innoLoginR = json.loads(innoLoginR.text)

      # Check Success
      if(innoLoginR.get('success') != None):
        if(innoLoginR['success'] == False):
          print(innoLoginR)
        else:
          header['Authorization'] = "Bearer " + innoLoginR['jwt']
          innoSummaryR = innoSession.post("http://" + item["ip"] + "/api/summary", verify=False, timeout=60, headers=header)
          innoSummary = json.loads(innoSummaryR.text);
          # innoSummary = innoSummaryR.text;
          print(str(innoSummary['success']))
          # time.sleep(3000)

          if(innoSummary.get('success') != None):
            data = InnoDecode(innoSummary, item["ip"], item["mac"]);
            # table.add_row(
            #   data['ip'], data['type'], data['error'], data['hr'], data['temp'], data['pool'], data['worker'], data['uptime']
            # )
            # clear()
            # console.print(table)
            if(data != 0):
              printTable(data)

    # Lua Login
    elif r.text.find('<a style="color: black; font-family: arial, helvetica, sans-serif;" href="/cgi-bin/luci">LuCI - Lua Configuration Interface</a>') != -1:
      print(' - Lua Login')
    elif r.text.find('<form class="pure-form">') != -1:
      print(' - router')
    elif r.text.find('true;\ngetObj("Frm_Password").disabled') != -1:
      print(' - router')
    else :
      print(' - unknown device')
      # print(r.text)
      # time.sleep(9999)
  else:        
    print('bad status - ' + str(r.status_code))
    # print(r.text)
    time.sleep(3)
  
  








print("done")
while 1:
	time.sleep(3)
