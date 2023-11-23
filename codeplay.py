# -*- coding: utf-8 -*-

#import RPi.GPIO as GPIO

from gtts import gTTS
import pygame
import sys
import time

import talkmo
import sm1
import sm2
import RGBm

import requests
from bs4 import BeautifulSoup

import random

RGBm.setcolor(100, 0, 0)
time.sleep(1)
RGBm.setcolor(0, 100, 0)
time.sleep(1)
RGBm.setcolor(0, 0, 100)
time.sleep(1)
RGBm.setcolor(10, 50, 50)

testmod = 1

time = [0.5, 1, 2, 3, 4]
degree = [4, 5, 6, 7, 8, 9, 10, 11]

while True:
	d = choice(degree)
	t = choice(time)
	sm1.servo(d)
	time.sleep(t)
	sm2.servo(d)
	time.sleep(t)

ser.stop()        
ser2.stop()            


GPIO.cleanup() 



while testmod == 0:
   site=requests.get('https://weather.naver.com/rgn/townWetr.nhn?naverRgnCd=02830400')
   source=BeautifulSoup(site.text, 'html.parser')


   issue=source.select('.today_weather .weather_area')

   data1 = []
   for title in issue:
      data1.append(title.get_text())

   #print(data1)

   out_tem = ((data1[0])[6:8])

   #--------------------------------
   '''
   issue=source.select('.sub_info .lv2')

   data1 = []
   for title in issue:
      data1.append(title.get_text())
   out_dust = ((data1[0])[5:7])
   #------------------------------------
   issue=source.select('.sub_info .lv3')

   data1 = []
   for title in issue:
      data1.append(title.get_text())

   out_dust2 = ((data1[0])[5:7])

   #----------------------------------

   out_tem_s = ""
   if int(out_tem) > -10000:
      out_tem_s = "지구 멸망"

   print("\n바깥온도 : %s\n미세먼지 : %s\n초미세먼지 : %s\n" % (out_tem_s, out_dust, out_dust2))

   '''
   print("\n온도 : %s" % out_tem)

   #talkman = ("현재 온도는 %s도 입니다." % out_tem)
   talkmo.talk2("현재 온도는 %s도 입니다." % out_tem)
   
   time.sleep(5)
   #sm1.my_left()
   sm1.servo(7.5)
   time.sleep(1)
   sm2.servo(7.5)
   time.sleep(1)

   sm1.servo(12.5)
   time.sleep(1)
   sm2.servo(12.5)
   time.sleep(1)

   # sm1.servo(4)
   # sm2.servo(4)
   # time.sleep(1)

   # sm1.servo(7.5)
   # sm2.servo(7.5)
   # time.sleep(1)