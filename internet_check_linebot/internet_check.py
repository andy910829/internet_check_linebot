import requests
import json
import time

with open('urllist.json') as f:
    data = json.load(f)


localhost = []
area = []
encrypt_host = []
    
class internet_check:
    def __init__(self):#初始化
        self.ans = ' ' 
        self.localhost = []
        self.area = []
        self.encrypt_host = []
        self.ip=' '
        self.name=' '
        self.status=' '
        self.ping =' '
        with open('urllist.json') as f:
            self.data = json.load(f)
        
    def datatoarray(self):                                              #轉換類型
        for i in range(len(self.data)):
            self.localhost.append(self.data[i]['host'])
            self.area.append(self.data[i]['name'])
            self.encrypt_host.append(self.data[i]['encrypt_host'])

    def connection_check(self):                                            #判斷連線成不成功 #
        try:
            for i in range(197):
                headers = {
                'user-agent' : 'Mozilla/5.0'
                }
                r = requests.get(f"https://netflow.ntut.edu.tw/home/network/ping?encrypt_host={self.encrypt_host[i]}", headers = headers )
                check = r.text
                # print(self.localhost[i], self.area[i], r.status_code, r.text)
                if check == 'false':   
                    self.ip = self.localhost[i]    
                    self.name = self.area[i]
                    self.status =   r.status_code    
                    self.ping = r.text                          #連線失敗
                    # return localhost[i], area[i], r.status_code, r.text
                    self.ans= self.ans+ self.area[i] + '--目前網路無法使用'+ '\n'
            # else:                                                       #連線正常
            #     return 'None','None','None','None'
            print('done')
        except TimeoutError:                                            #連線失敗
                # return localhost[i], area[i], r.status_code, r.text
                self.ans= self.ans+ area[i] + '--目前網路無法使用'+ '\n'

    def run(self): #轉類+確認+給出答覆
        self.datatoarray()
        self.connection_check()
    def store(self):#
        while True:
            self.run()
            time.sleep(300)



# if __name__ == '__main__':
#     main2()


# def test():
#     headers = {
#     'user-agent' : 'Mozilla/5.0'
#     }
#     r = requests.get("https://netflow.ntut.edu.tw/home/network/ping?encrypt_host=eyJpdiI6IjJyUGlVQ1NnRnQ3UkYwVEViak1uWVE9PSIsInZhbHVlIjoiaUdYemdnRGdKUDJnSkJLaU14anlQaGtxV0FOenFVaDc4YllPSVdBd0duST0iLCJtYWMiOiJlNDlkYjI5MzQ2ODEwNGNlYWIyNzg5Nzc4MGY0OGY4N2JmZjlmYzc1NDVlMGYwN2ZkNGE3NWY3ZjUyMWVlYjgxIn0=",  headers = headers)  
#     r.encoding = r.apparent_encoding
#     ans = '192.192.7.221'+ '臺大區網中心'
#     return ans

# def main2():
#     ans = ''
#     datatoarray(data)
#     for i in range(197):
#         ip,name,status,ping = connection_check(i)
#         print(i)
#         if ip != 'None':
#             ans  = ans  + name + '--目前網路無法使用'+ '\n'
#     print(ans)

# def main(i):
#     datatoarray(data)
#     global localhost
#     ip,name,status,ping = connection_check(i)
#     #if ip != 'None':
#     return ip,name,status,ping