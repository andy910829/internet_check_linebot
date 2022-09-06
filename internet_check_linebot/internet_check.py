import requests
import json

with open('urllist.json') as f:
    data = json.load(f)

localhost = []
area = []
encrypt_host = []
    

def datatoarray(data):
    global localhost,area,encrypt_host
    for i in range(len(data)):
        localhost.append(data[i]['host'])
        area.append(data[i]['name'])
        encrypt_host.append(data[i]['encrypt_host'])
    
def connection_check(i):
    try:
        global localhost,area,encrypt_host
        r = requests.get(f"https://netflow.ntut.edu.tw/home/network/ping?encrypt_host={encrypt_host[i]}")
        check = r.text
        #print(localhost[i], area[i], r.status_code, r.text)
        if check == 'false':
            return localhost[i], area[i], r.status_code, r.text
        else:
            return 'None','None','None','None'
    except TimeoutError:
        return localhost[i], area[i], r.status_code, r.text


def main():
    datatoarray(data)
    global localhost
    for i in range(197):
        ip,name,status,ping = connection_check(i)
        if ip != 'None':
            print(ip,name,status,ping)


def main2():
    ans = ''
    datatoarray(data)
    for i in range(197):
        ip,name,status,ping = connection_check(i)
        print(i)
        if ip != 'None':
            ans  = ans  + name + '--目前網路無法使用'+ '\n'
    return ans


if __name__ == '__main__':
    main()


