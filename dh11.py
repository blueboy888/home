#!/usr/bin/env python
#coding=utf8
import commands
#import requests
import re
#import json
#import time
from time import strftime, sleep

while True:
	text = commands.getoutput( 'sudo /home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_DHT_Driver/Adafruit_DHT 11 4' )
	#print "dht_11: ", text
	if "Temp" in text: #检测结果中是否正确获取到Temp 关键字 没有就循环执行获取温度的命令
	 break
	#print "循环中..."
	sleep (1) #暂停1秒

m = re.findall(r'\s\d{2}\s',text) #正则抓取温度湿度值
#print m[0], m[1]
wd = m[0] .replace(" ", "") #替换空格 只获取数值
sd = m[1] .replace(" ", "")

print strftime("%Y-%m-%d/%H:%M:%S,"),wd,",",sd
"""
print "温度：", wd
print "湿度：", sd


#wd_data = {"timestamp": strftime("%Y-%m-%dT%H:%M:%S"), "value": wd}
#sd_data = {"timestamp": strftime("%Y-%m-%dT%H:%M:%S"), "value": sd}
wd_data = {"value": wd} #简单格式温度
sd_data = {"value": sd} #简单格式湿度
print wd_data #打印上传温度
print sd_data #打印上传湿度
headers = {"U-ApiKey": "248539436f514c0e71d75da3fa80f5a7"} #yeelink apikey

url = r"http://api.yeelink.net/v1.0/device/11889/sensor/19191/datapoints" #DH11温度
r = requests.post(url, data=json.dumps(wd_data), headers=headers) #DH11温度

url = r"http://api.yeelink.net/v1.0/device/11889/sensor/19192/datapoints" #DH11湿度
r = requests.post(url, data=json.dumps(sd_data), headers=headers) #DH11湿度

pi = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( "'C", '' )
pi_data = {"value": pi} 
url = r"http://api.yeelink.net/v1.0/device/11889/sensor/20187/datapoints" #PI 温度
r = requests.post(url, data=json.dumps(pi_data), headers=headers) #PI 温度
print pi
print pi_data
"""
