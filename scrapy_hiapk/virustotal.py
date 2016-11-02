# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import simplejson
import urllib
import urllib2
import time
import json
import os
class virustotal():
    def report(self,md5,path):
        print("report")
        print(md5)
        url = "https://www.virustotal.com/vtapi/v2/file/report"
        parameters = {"resource": " ","apikey": "e83d749addb188c2742ce86849e31704731a06d6331136a40b0be573265d2db7"}
        parameters["resource"]=md5
        print(parameters)
        data = urllib.urlencode(parameters)
        proxy = urllib2.ProxyHandler({'https': 'proxy-ty.mcu.edu.tw:3128'})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)
        req = urllib2.Request(url, data)
        time.sleep(10)
        response = urllib2.urlopen(req)
        result=json.load(response)
        print("RESULT")
        print (result)
        print("PATH")
        print (path)
        filename=md5+".apk"
        os.system("mv C:/Users/mcu/Documents/android_apk/"+path+" C:/Users/mcu/Documents/android_apk/full/"+filename)
        positives=result["positives"]
        if positives>5:
            command="mv C:/Users/mcu/Documents/android_apk/full/"+filename+" C:/Users/mcu/Documents/android_apk/android_problem/"+filename
            os.system(command)
        else:
            filename=md5+".apk"
            command="mv C:/Users/mcu/Documents/android_apk/full/"+filename+" C:/Users/mcu/Documents/android_apk/android_normal/"+filename
            os.system(command)