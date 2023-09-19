import requests
import json
import time

# messagewithconfig = input("Enter message: ")

message = f'''پر سرعت
ss://6f892973-90de-41e5-bb42-5b47c1566079@31.192.239.20:17630?encryption=none&security=reality&sni=ftp.debian.org&fp=chrome&pbk=511Wl4VP_Hn8PW-uRpulv7EG4kXlOF71yPAKwTj9aXA&sid=3b638c73&spx=%2F&type=tcp&headerType=http&host=khamenei.ir#ftp.debian.org-iydehbbu
پرسرعت2 
vmess://6f892973-90de-41e5-bb42-5b47c1566079@31.192.239.20:17630?encryption=none&security=reality&sni=ftp.debian.org&fp=chrome&pbk=511Wl4VP_Hn8PW-uRpulv7EG4kXlOF71yPAKwTj9aXA&sid=3b638c73&spx=%2F&type=tcp&headerType=http&host=khamenei.ir#ftp.debian.org-iydehbbu
پرسرعت 3
vless://6f892973-90de-41e5-bb42-5b47c1566079@31.192.239.20:17630?encryption=none&security=reality&sni=ftp.debian.org&fp=chrome&pbk=511Wl4VP_Hn8PW-uRpulv7EG4kXlOF71yPAKwTj9aXA&sid=3b638c73&spx=%2F&type=tcp&headerType=http&host=khamenei.ir#ftp.debian.org-iydehbbu
پرسرعت 4
trojan://6f892973-90de-41e5-bb42-5b47c1566079@31.192.239.20:17630?encryption=none&security=reality&sni=ftp.debian.org&fp=chrome&pbk=511Wl4VP_Hn8PW-uRpulv7EG4kXlOF71yPAKwTj9aXA&sid=3b638c73&spx=%2F&type=tcp&headerType=http&host=khamenei.ir#ftp.debian.org-iydehbbu
سرعت عالی
trojan://6f892973-90de-41e5-bb42-5b47c1566079@31.192.239.20:17630?encryption=none&security=reality&sni=ftp.debian.org&fp=chrome&pbk=511Wl4VP_Hn8PW-uRpulv7EG4kXlOF71yPAKwTj9aXA&sid=3b638c73&spx=%2F&type=tcp&headerType=http&host=khamenei.ir#ftp.debian.org-iydehbbu
'''

config_count_vmess = message.count("vmess://")
config_count_vless = message.count("vless://")
config_count_trojan = message.count("trojan://")

countloop1 = config_count_trojan + config_count_vless + config_count_vmess

for z in range(1):
    zhh = message

for i in range(countloop1):
    if "vless://" in zhh or "vmess://" in zhh or "trojan://" in zhh or "ss://" in zhh:
        if "trojan://" in zhh:
            start_index = zhh.index("trojan://")
        elif "vmess://" in zhh:
            start_index = zhh.index("vmess://")
        elif "vless://" in zhh:
            start_index = zhh.index("vless://")
        elif "ss://" in zhh:
            start_index = zhh.index("ss://")
    else:
        zasasa = print("sakam")
    configwithad = zhh[start_index:]
    tag_index = configwithad.index("#")
    configwithnoad = configwithad[:tag_index]
    config = configwithnoad + "#OmidNework"
    ipforcheck = config.index("@")
    ip_index = config[ipforcheck:]
    remove_index = ip_index.index(":")
    remove = ip_index[:remove_index]
    configip = remove.replace("@", "")
    zhh = zhh.replace(configwithnoad, "")
    try:
        checkhost = f"https://check-host.net/check-ping?host={configip}&node=ir1.node.check-host.net&node=ir4.node.check-host.net&node=ir3.node.check-host.net"

        headerscheckhost = {
            'Accept': 'application/json',
        }

        responseidcheckhost = requests.get(url=checkhost, headers=headerscheckhost)
        responseidcodecheckhost = responseidcheckhost.text
        idgetcheckhost = json.loads(responseidcodecheckhost)
        request_id = idgetcheckhost['request_id']

        time.sleep(3)

        checkhostresult = f"https://check-host.net/check-result/{request_id}"
        responseping = requests.get(url=checkhostresult, headers=headerscheckhost, timeout=3)
        responsepingtxt = responseping.text
        responsepingjson = json.loads(responsepingtxt)

        ir1tehran1 = responsepingjson['ir1.node.check-host.net'][0][0][0]
        ir1tehran2 = responsepingjson['ir1.node.check-host.net'][0][1][0]
        ir1tehran3 = responsepingjson['ir1.node.check-host.net'][0][2][0]
        ir1tehran4 = responsepingjson['ir1.node.check-host.net'][0][3][0]

        ir4tabriz1 = responsepingjson['ir4.node.check-host.net'][0][0][0]
        ir4tabriz2 = responsepingjson['ir4.node.check-host.net'][0][1][0]
        ir4tabriz3 = responsepingjson['ir4.node.check-host.net'][0][2][0]
        ir4tabriz4 = responsepingjson['ir4.node.check-host.net'][0][3][0]

        ir3shiraz1 = responsepingjson['ir3.node.check-host.net'][0][0][0]
        ir3shiraz2 = responsepingjson['ir3.node.check-host.net'][0][1][0]
        ir3shiraz3 = responsepingjson['ir3.node.check-host.net'][0][2][0]
        ir3shiraz4 = responsepingjson['ir3.node.check-host.net'][0][3][0]

        allir = ir1tehran1 + " " + ir1tehran2 + " " + ir1tehran3 + " " + ir1tehran4 + " " + ir4tabriz1 + " " + ir4tabriz2 + " " + ir4tabriz3 + " " + ir4tabriz4 + " " + ir3shiraz1 + " " + ir3shiraz2 + " " + ir3shiraz3 + " " + ir3shiraz4


        tehran = ""
        tabriz = ""
        shiraz = ""


        if 'OK' in allir:
            print(config)
            if "OK" in ir1tehran1 or "OK" in ir1tehran2 or "OK" in ir1tehran3 or "OK" in ir1tehran4:
                tehran = "Tehran"
            if "OK" in ir4tabriz1 or "OK" in ir4tabriz2 or "OK" in ir4tabriz3 or "OK" in ir4tabriz4:
                tabriz = "Tabriz"
            if "OK" in ir3shiraz1 or "OK" in ir3shiraz2 or "OK" in ir3shiraz3 or "OK" in ir3shiraz4:
                shiraz = "Shiraz"
            print(tehran + " & " + tabriz + " & " + shiraz)
        else:
            a = 'a'
    except:
        error = "zzs"

config_count_ss = zhh.count("ss://")

if "ss://" in zhh:
    for z in range(config_count_ss):
        start_index = zhh.index("ss://")
        configwithad = zhh[start_index:]
        tag_index = configwithad.index("#")
        configwithnoad = configwithad[:tag_index]
        config = configwithnoad + "#OmidNework"
        ipforcheck = config.index("@")
        ip_index = config[ipforcheck:]
        remove_index = ip_index.index(":")
        remove = ip_index[:remove_index]
        configip = remove.replace("@", "")
        zhh = zhh.replace(configwithnoad, "")
        try:
            checkhost = f"https://check-host.net/check-ping?host={configip}&node=ir1.node.check-host.net&node=ir4.node.check-host.net&node=ir3.node.check-host.net"

            headerscheckhost = {
                'Accept': 'application/json',
            }

            responseidcheckhost = requests.get(url=checkhost, headers=headerscheckhost)
            responseidcodecheckhost = responseidcheckhost.text
            idgetcheckhost = json.loads(responseidcodecheckhost)
            request_id = idgetcheckhost['request_id']

            time.sleep(3)

            checkhostresult = f"https://check-host.net/check-result/{request_id}"
            responseping = requests.get(url=checkhostresult, headers=headerscheckhost, timeout=3)
            responsepingtxt = responseping.text
            responsepingjson = json.loads(responsepingtxt)

            ir1tehran1 = responsepingjson['ir1.node.check-host.net'][0][0][0]
            ir1tehran2 = responsepingjson['ir1.node.check-host.net'][0][1][0]
            ir1tehran3 = responsepingjson['ir1.node.check-host.net'][0][2][0]
            ir1tehran4 = responsepingjson['ir1.node.check-host.net'][0][3][0]

            ir4tabriz1 = responsepingjson['ir4.node.check-host.net'][0][0][0]
            ir4tabriz2 = responsepingjson['ir4.node.check-host.net'][0][1][0]
            ir4tabriz3 = responsepingjson['ir4.node.check-host.net'][0][2][0]
            ir4tabriz4 = responsepingjson['ir4.node.check-host.net'][0][3][0]

            ir3shiraz1 = responsepingjson['ir3.node.check-host.net'][0][0][0]
            ir3shiraz2 = responsepingjson['ir3.node.check-host.net'][0][1][0]
            ir3shiraz3 = responsepingjson['ir3.node.check-host.net'][0][2][0]
            ir3shiraz4 = responsepingjson['ir3.node.check-host.net'][0][3][0]

            allir = ir1tehran1 + " " + ir1tehran2 + " " + ir1tehran3 + " " + ir1tehran4 + " " + ir4tabriz1 + " " + ir4tabriz2 + " " + ir4tabriz3 + " " + ir4tabriz4 + " " + ir3shiraz1 + " " + ir3shiraz2 + " " + ir3shiraz3 + " " + ir3shiraz4


            tehran = ""
            tabriz = ""
            shiraz = ""


            if 'OK' in allir:
                print(config)
                if "OK" in ir1tehran1 or "OK" in ir1tehran2 or "OK" in ir1tehran3 or "OK" in ir1tehran4:
                    tehran = "Tehran"
                if "OK" in ir4tabriz1 or "OK" in ir4tabriz2 or "OK" in ir4tabriz3 or "OK" in ir4tabriz4:
                    tabriz = "Tabriz"
                if "OK" in ir3shiraz1 or "OK" in ir3shiraz2 or "OK" in ir3shiraz3 or "OK" in ir3shiraz4:
                    shiraz = "Shiraz"
                print(tehran + " & " + tabriz + " & " + shiraz)
            else:
                a = 'a'
        except:
            z = "z"
else:
    error = 'error'