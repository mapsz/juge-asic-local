# Imports
import scapy.all as scapy
import requests
from requests.auth import HTTPDigestAuth
import time
import fake_useragent
import json
from rich.console import Console
from rich.table import Table
import sys
import os
import asyncio
import aiohttp
from tkinter import *
from tkinter import ttk

# # Master
# tkMaster  = Tk()
# tkMaster.title('PythonGuides')
# tkMaster.geometry('800x600')

# # Device Table
# tkDeviceTable = ttk.Treeview(tkMaster, selectmode='browse')
# tkDeviceTableScrollbar = ttk.Scrollbar(tkMaster, orient="vertical", command=tkDeviceTable.yview)
# tkDeviceTable.configure(yscrollcommand=tkDeviceTableScrollbar.set)
# tkDeviceTableScrollbar.pack(side='right', fill='y')
# tkDeviceTable.pack(side='right', fill='y')


# tkDeviceTable['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')

# tkDeviceTable.column("#0", width=0,  stretch=NO)
# tkDeviceTable.column("player_id",anchor=CENTER, width=80)
# tkDeviceTable.column("player_name",anchor=CENTER,width=80)
# tkDeviceTable.column("player_Rank",anchor=CENTER,width=80)
# tkDeviceTable.column("player_states",anchor=CENTER,width=80)
# tkDeviceTable.column("player_city",anchor=CENTER,width=80)

# tkDeviceTable.heading("#0",text="",anchor=CENTER)
# tkDeviceTable.heading("player_id",text="Id",anchor=CENTER)
# tkDeviceTable.heading("player_name",text="Name",anchor=CENTER)
# tkDeviceTable.heading("player_Rank",text="Rank",anchor=CENTER)
# tkDeviceTable.heading("player_states",text="States",anchor=CENTER)
# tkDeviceTable.heading("player_city",text="States",anchor=CENTER)

# tkDeviceTable.pack()

# i=0
# while 1:
#   tkDeviceTable.insert(parent='',index='end',iid=i,text='',
#   values=(i,'Ninja','101','Oklahoma', 'Moore'))
#   tkMaster.update()
#   tkMaster.update_idletasks()    
#   time.sleep(0.3)
#   i+=1

  
# tkMaster.mainloop()


#Async porn
# asyncio.run(main())
# await asyncio.sleep(0.5)
# async def someFunction():
# task = asyncio.create_task(someFunction())
# print(task.result())

# a = """
#   STATUS=S,When=1645185475,Code=11,Msg=Summary,Description=cgminer 4.10.0|SUMMARY,Elapsed=4484245,GHS 5s=553.61,GHS av=477.92,Found Blocks=0,Getworks=181142,Accepted=615041,Rejected=824,Hardware Errors=3793420,Utility=8.23,Discarded=2576669,Stale=12,Get Failures=4,Local Work=4178400,Remote Failures=2,Network Blocks=29995,Total MH=2143090353.0000,Work Utility=495884.54,Difficulty Accepted=37011587072.00000000,Difficulty Rejected=49545216.00000000,Difficulty Stale=0.00000000,Best Share=260968212167,Device Hardware%=0.0102,Device Rejected%=0.1337,Pool Rejected%=0.1337,Pool Stale%=0.0000,Last getwork=1645185474|
#   STATUS=S,When=1645185475,Code=70,Msg=CGMiner stats,Description=cgminer 4.10.0|CGMiner=4.10.0,Miner=1.0.1.3,CompileTime=Sun Jan 14 00:00:57 CST 2018,Type=Antminer L3+ Blissz v1.02|STATS=0,ID=L30,Elapsed=4484245,Calls=0,Wait=0.000000,Max=0.000000,Min=99999999.000000,GHS 5s=553.610,GHS av=477.92,miner_count=4,frequency=425,frequency1=425,frequency2=425,frequency3=425,frequency4=425,volt1=3,volt2=3,volt3=3,volt4=3,watt1=201,watt2=201,watt3=201,watt4=201,fan_num=2,fan1=2166,fan2=2220,temp_num=4,temp1=48,temp2=47,temp3=39,temp4=40,temp2_1=56,temp2_2=57,temp2_3=49,temp2_4=49,temp31=0,temp32=0,temp33=0,temp34=0,temp4_1=0,temp4_2=0,temp4_3=0,temp4_4=0,temp_max=48,Device Hardware%=-0.0000,no_matching_work=3793420,chain_acn1=72,chain_acn2=72,chain_acn3=72,chain_acn4=72,chain_acs1= oooooooo oooooooo oooooooo oooooooo oooooooo ooooooxx xxxxxxxx xxxooooo oooooooo,chain_acs2= oooooooo oooooooo oooooooo oooooooo oooooooo oooooooo oxxxxxxx xxxxxooo oooooooo,chain_acs3= oooooooo oooooooo oooooooo ooooooxo oooooooo oooooooo oooooooo oooooooo oooooooo,chain_acs4= oooooooo oooooooo oooooooo oooxxxxx xxxxxxxo oooooooo oooooooo oooooooo ooooooxo,chain_hw1=1494,chain_hw2=127132,chain_hw3=1101955,chain_hw4=2562839,chain_rate1=138.80,chain_rate2=137.19,chain_rate3=138.77,chain_rate4=138.84|
#   STATUS=S,When=1645185475,Code=7,Msg=3 Pool(s),Description=cgminer 4.10.0|POOL=0,URL=stratum+tcp://172.65.204.210:3333,Status=Alive,Priority=0,Quota=1,Long Poll=N,Getworks=181098,Accepted=614943,Rejected=824,Discarded=2576511,Stale=11,Get Failures=4,Remote Failures=2,User=Eduard773.s03,Last Share Time=0:00:19,Diff=65.5K,Diff1 Shares=144638377,Proxy Type=,Proxy=,Difficulty Accepted=37009358848.00000000,Difficulty Rejected=49545216.00000000,Difficulty Stale=0.00000000,Last Share Difficulty=65536.00000000,Has Stratum=true,Stratum Active=true,Stratum URL=172.65.204.210,Has GBT=false,Best Share=260968212167,Pool Rejected%=0.1337,Pool Stale%=0.0000|POOL=1,URL=stratum+tcp://47.91.67.214:443,Status=Alive,Priority=1,Quota=1,Long Poll=N,Getworks=23,Accepted=0,Rejected=0,Discarded=0,Stale=0,Get Failures=0,Remote Failures=0,User=Eduard773.s03,Last Share Time=0,Diff=16.4K,Diff1 Shares=0,Proxy Type=,Proxy=,Difficulty Accepted=0.00000000,Difficulty Rejected=0.00000000,Difficulty Stale=0.00000000,Last Share Difficulty=0.00000000,Has Stratum=true,Stratum Active=false,Stratum URL=,Has GBT=false,Best Share=0,Pool Rejected%=0.0000,Pool Stale%=0.0000|POOL=2,URL=stratum+tcp://47.91.67.214:25,Status=Alive,Priority=2,Quota=1,Long Poll=N,Getworks=21,Accepted=98,Rejected=0,Discarded=162,Stale=1,Get Failures=0,Remote Failures=0,User=Eduard773.s03,Last Share Time=56:36:23,Diff=32.8K,Diff1 Shares=7885,Proxy Type=,Proxy=,Difficulty Accepted=2228224.00000000,Difficulty Rejected=0.00000000,Difficulty Stale=0.00000000,Last Share Difficulty=32768.00000000,Has Stratum=true,Stratum Active=false,Stratum URL=,Has GBT=false,Best Share=25489890,Pool Rejected%=0.0000,Pool Stale%=0.0000|
# """

# a = a.split(',')

# print(data)

# sys.exit()

#Loop
async def mainLoop():
  async with aiohttp.ClientSession() as session: 
  
    #Functions
    def aSearchIndex(arr,value,key):
      i = 0
      while i < len(arr):
        if(arr[i].get(key) == value): return i
        i+=1
      return -1

    def toFixed(numObj, digits=0):
        numObj = float(numObj)
        return f"{numObj:.{digits}f}"

    def printTable(data):

      if(data.get('ip') == None): data['ip'] = 'None'
      if(data.get('type') == None): data['type'] = 'None'
      if(data.get('error') == None): data['error'] = 'None'
      if(data.get('hr') == None): data['hr'] = 'None'
      if(data.get('temp') == None): data['temp'] = 'None'
      if(data.get('pool') == None): data['pool'] = 'None'
      if(data.get('worker') == None): data['worker'] = 'None'
      if(data.get('uptime') == None): data['uptime'] = 'None'

      if(len(data['type']) > 20): data['type'] = data['type'][:18]

      print(
        data['ip'] +"\t"+ 
        data['type'] +"\t\t\t"+ 
        data['error'] +"\t"+ 
        data['hr'] +"\t"+ 
        data['temp'] +"\t"+
        data['pool'] +"\t"+
        data['worker'] +"\t"+
        data['uptime']
      )

    def printRichTable(datas):
      #Table
      table = Table(show_header=True, header_style="bold magenta")

      #Table Header
      table.add_column("IP", style="dim")
      table.add_column("Type")
      table.add_column("Error", justify="right")
      table.add_column("HR", justify="right")
      table.add_column("Temp", justify="right")
      table.add_column("Pool", justify="right")
      table.add_column("Worker", justify="right")
      table.add_column("Uptime", justify="right")

      for data in datas:
        if(data.get('ip') == None): data['ip'] = 'None'
        if(data.get('type') == None): data['type'] = 'None'
        if(data.get('error') == None): data['error'] = 'None'
        if(data.get('hr') == None): data['hr'] = 'None'
        if(data.get('temp') == None): data['temp'] = 'None'
        if(data.get('pool') == None): data['pool'] = 'None'
        if(data.get('worker') == None): data['worker'] = 'None'
        if(data.get('uptime') == None): data['uptime'] = 'None'
        data['type'] = str(data['type'])
        if(len(data['type']) > 20): data['type'] = data['type'][:18]

        table.add_row(
          data['ip'], data['type'], data['error'], data['hr'], data['temp'], data['pool'], data['worker'], data['uptime']
        )
      
      clear()
      console.print(table)

    def clear():
      print(chr(27) + "[2J")

    def checkDone(task, text):
      try:
        task.result()
        print(text + ' task done')
        return True
      except Exception:
        return False

    async def fetch(url, headers = False):
      
      if headers == False:    
        headers = ""

      async with session.get(url, verify_ssl=False, headers=headers) as r:
        await r.read()
        return r

    async def fetchPost(url, params = []):
      
      if headers == False:    
        headers = ""

      async with session.post(url, verify_ssl=False, data=headers) as r:
        await r.read()
        return r

    

    #Classes
    class Gui():
      #Property
      tkMaster = 0
      tkDeviceTable = 0
      oldList = []

      #Init
      def __init__(self):
        # Master
        self.tkMaster  = Tk()
        self.tkMaster.title('Asic')
        self.tkMaster.geometry('800x600')

        # Device Table
        self.tkDeviceTable = ttk.Treeview(self.tkMaster, selectmode='browse')
        tkDeviceTableScrollbar = ttk.Scrollbar(self.tkMaster, orient="vertical", command=self.tkDeviceTable.yview)
        self.tkDeviceTable.configure(yscrollcommand=tkDeviceTableScrollbar.set)
        tkDeviceTableScrollbar.pack(side='right', fill='y')
        self.tkDeviceTable.pack(side='right', fill='y')
        self.tkDeviceTable['columns'] = ['ip', 'type', 'model', 'error', 'hr', 'temp', 'pool', 'worker', 'uptime']

        self.tkDeviceTable.column("#0", width=0,  stretch=NO)
        self.tkDeviceTable.heading("#0",text="",anchor=CENTER)

        #Set headers
        for item in self.tkDeviceTable['columns']:
          anchor = CENTER
          width = 80
          if(item == 'ip'): 
            anchor = E
            width = 100
          if(item == 'hr'): 
            width = 180
          if(item == 'model'): 
            width = 50
          self.tkDeviceTable.column(item, anchor=anchor, width=width)
          self.tkDeviceTable.heading(item, text=item,anchor=anchor)

        self.tkDeviceTable.pack()

        self.update()

      def update(self):
        for item in list.list:  
          # Get id
          id = self.idFromIp(item['ip'])
          # Set values
          values = []
          for value in self.tkDeviceTable['columns']:
            value_dict = ""
            if item.get(value) != None:
              value_dict = item.get(value)
            values.append(value_dict)
          # Delete
          try:self.tkDeviceTable.delete(id)
          except:pass
          # Add
          if(item.get('model')) != None:
            self.tkDeviceTable.insert(
              parent='',
              index='end',
              iid=id,
              text='',
              values=(values)
            ) 

        self.tkMaster.update()
        self.tkMaster.update_idletasks()

      def idFromIp(self, ip):
        return ip.replace('192.168', '').replace('.', '')

    class List():
      #Property
      list = []

      #Init
      def __init__(self):
        pass
      
      #Methods
      def setByIp(self, ip, key, value):
            
        i = aSearchIndex(self.list,ip,"ip")
        if(i == -1): return False;

        self.list[i][key] = value

      def getByIp(self, ip):
        return self.list[aSearchIndex(self.list, ip, 'ip')]

    class Delay():


      def __init__(self, n, _as):
        self.networkDelay = n
        self.asicSearchDelay = _as

      #Network  
      networkDelay = 30
      networkDoneAt = 0
      def network(self):
        return (time.time() - self.networkDoneAt) > self.networkDelay

      def nextNetwork(self):
        if(self.networkDoneAt == 0): return 0
        left = self.networkDoneAt - (time.time() - self.networkDelay)
        if(left < 0): return 0
        return toFixed(left,0)

      def networkDone(self):
        self.networkDoneAt = time.time()
      
      #Asic Search
      asicSearchDelay = 30
      asicSearchDoneAt = 0
      def asicSearch(self):
        return (time.time() - self.asicSearchDoneAt) > self.asicSearchDelay

      def nextAsicSearch(self):
        if(self.asicSearchDoneAt == 0): return 0
        left = self.asicSearchDoneAt - (time.time() - self.asicSearchDelay)
        if(left < 0): return 0
        return toFixed(left,0)

      def asicSearchDone(self):
        self.asicSearchDoneAt = time.time()

    class Network():
        
      list = []
      ip = ""
      timeout = 5

      def __init__(self, ip):
        self.ip = ip

      def scan(self):
        ip = self.ip
        arp_packet = scapy.ARP(pdst=ip)
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_broadcast_packet = broadcast_packet/arp_packet
        answered_list = scapy.srp(arp_broadcast_packet, timeout=self.timeout, verbose=False)[0]
        client_list = []

        # Make List
        for element in answered_list:
          client_dict = {
              "ip": element[1].psrc, 
              "mac": element[1].hwsrc,
              "check_at": time.time()
            }  
          client_list.append(client_dict)

        self.list = client_list

    class Types():
          
      sessionTimeout = 5
      delay = 180
          
      def __init__(self):
        pass
                
      async def setType(self):

        #Get ready ip
        ip = False
        for item in list.list:
          if item.get('typeSetAt') == None or (item.get('typeSetAt') + self.delay) < time.time(): 
            ip = item['ip']

        #stop if no ip
        if(ip == False): return False

        #Set type set
        list.setByIp(ip,"typeSetAt",time.time())
        
        # async with aiohttp.ClientSession() as session:
        type = ""
        error = False
        try:
          r = await fetch("http://" + ip)
          text = await r.text(encoding="utf-8")
          status = r.status
          headers = r.headers
        except Exception as e:
          error = True
          type = str(e);  


        #Find Type
        if error == False:
          if status == 200:            
            # InnoSilicon
            if text.find('<title>AsicMiner</title>') != -1: 
              type = 'Innosilicon'
            # Lua Login
            elif text.find('<a style="color: black; font-family: arial, helvetica, sans-serif;" href="/cgi-bin/luci">LuCI - Lua Configuration Interface</a>') != -1:
              type = ('Lua')
            elif text.find('<form class="pure-form">') != -1 or text.find('true;\ngetObj("Frm_Password").disabled') != -1:
              type = ('Router')
            else :
              type =  'Unknown device'          
          elif status == 401:
            #AntMiner
            if headers['WWW-Authenticate'].find('antMiner') != -1: 
              type = "AntMiner"
            else :
              type =  '401 Unknown device'     
          
          else:  
            type =  str(r.status)

        
        print(ip + " - " +type)
        
        list.setByIp(ip,"type",type)
      
    class Asic():
          
      sessionTimeout = 5
      delay = 60

      def __init__(self):
        pass

      async def update(self):

        typeList = ['AntMiner']

        #Get ready ip
        ip = False
        for item in list.list:
          if(
              item.get('type') != None and 
              item.get('type') in typeList and 
              (
                item.get('updateAt') == None or 
                (item.get('updateAt') + self.delay) < time.time()
              ) 
            ):
              ip = item['ip']
              type = item.get('type')

        #stop if no ip
        if(ip == False): return False

        # Set update
        list.setByIp(ip,"updateAt",time.time())

        if(type == "AntMiner"):
          asyncio.create_task(antMiner.update(ip))

    class AntMiner():

      sessionTimeout = 5
      session = False
          
      def __init__(self):
        #Start Session
        self.session = requests.Session()

      async def update(self, ip):
        #Get request
        print("Update AntMiner " + ip)
        r = self.session.get('http://' + ip + "/cgi-bin/get_status_api.cgi", auth=HTTPDigestAuth('root', 'root')) 
        text = r.text

        #Set Model
        self.setModel(text, ip)
        item = list.getByIp(ip)
        if(item.get('model') == None or item['model'] == False):
          list.setByIp(ip, 'model', False)
          print('====No Model=====')
          print(text)
          print('================')
          return False
        
        #Set Data
        self.setData(text, ip)

      def setModel(self, text, ip):
        if text.find('L3+') != -1:
          list.setByIp(ip, 'model', 'L3+')
          return True

        if text.find('S17+') != -1:
          list.setByIp(ip, 'model', 'S17+')

        if text.find('S17 Pro') != -1:
          list.setByIp(ip, 'model', 'S17 Pro')

        if text.find('T17') != -1:
          list.setByIp(ip, 'model', 'T17')

        return False

      def setData(self, text, ip):

        text = text.split(',')

        data = {}
        #Get from text
        for item in text:
          # Full HS
          if item.find('GHS 5s=') != -1:
            data['fullHR'] = item.replace('GHS 5s=', '')
            data['fullHR'] = str(toFixed(data['fullHR'], 1))
            list.setByIp(ip, 'fullHR', data['fullHR'])
          # Hashboard HS
          if item.find('chain_rate') != -1:    
            val = item.split('=')[1]
            if val.find('|') != -1:
              val = val.split('|')[0]
            if val == "": val = 0
            if data.get('hashboardsHR') == None:
              data['hashboardsHR'] = []            
            val = str(toFixed(val, 1))
            data['hashboardsHR'].append(val)

        # HR
        data['hr'] = ""
        # Full HR
        if data.get('fullHR') != None:
          data['hr'] = data['fullHR']

        # Boards
        if data.get('hashboardsHR') != None:
          if(len(data['hashboardsHR']) > 0):
            # Add space
            if(data['hr'] != ""): data['hr'] += " | "
            # Add boards
            first = True
            for hash in data['hashboardsHR']:
              if(first == False): data['hr'] += "/"
              data['hr'] += hash
              first = False

                
        # print(data['fullHR'])
        # print(data['hashboardsHR'])
        # print(data['hr'])

        list.setByIp(ip, 'hr', data['hr'])

    class Api():

      link = "http://a0638279.xsph.ru/in/l3"
      delay = 5*60
      stack = 10      
      
      def __init__(self):
        pass

      async def send(self):

        #Get ready ip
        ip = False
        toSend = []
        count = 0
        for item in list.list:
          if count > self.stack: 
            break
          if (
            item.get('model') != None and item['model'] != False and
            (item.get('apiSendAt') == None or (item.get('apiSendAt') + self.delay) < time.time())
            and item['model'] == "L3+"
          ):
            toSend.append(item) 
            count += 1

        #Stop if no ip
        if(len(toSend) == 0): return False

        #Set time
        for item in toSend:
          list.setByIp(item['ip'], "apiSendAt", time.time())

        # To Json
        toSend = json.dumps(toSend)

        # Log To File
        f = open("lastApiSend.txt", "w")
        f.write(toSend)
        f.close()

        # Send
        try:
          r = await fetch(self.link + "?data=" + toSend)
        except Exception as e:
          pass

        

    #Setup
    start = time.time()
    console = Console()
    delay = Delay(60, 30)
    
    list = List();
    network = Network('192.168.88.0/24')
    types = Types()
    asic = Asic()  
    api = Api()  

    antMiner = AntMiner()


    gui = Gui()
    gui.update()

    #Main loop
    while 1:
        
      #Network
      if(delay.network()):
        print('Do Network Scan')

        #Scan
        network.scan()

        print(network.list)

        # Add to Global list
        for item in network.list:
          if aSearchIndex(list.list,item["ip"],"ip") == -1: list.list.append(item)

        #Set done
        print('Found - ' + str(len(list.list)))
        delay.networkDone()
        
      
      if(len(list.list) > 0):

        #Asic Search
        asyncio.create_task(types.setType())

        #Asic Update
        asyncio.create_task(asic.update())

        #Api send
        if(time.time() - start > 60):
          asyncio.create_task(api.send())
        

      gui.update()
      await asyncio.sleep(0.1)


asyncio.run(mainLoop())
  

# if __name__ == '__main__':
#   MyApp().run()


    # def build(self):
    #     return Label(text='Hello world')

while 1:
  time.sleep(1)

sys.exit()




def InnoDecode(summary, ip, mac):

  if(summary.get('DEVS') == None):
    print('no devs')
    return 0


  # Get from hash boards
  hr = "/"
  temp = "/"
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
