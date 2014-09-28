#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'gersonda'
import os
import sys
import requests
from bs4 import BeautifulSoup
from re import sub
import string
import time

fileName = open("C:/Users/gersonda/Dropbox/Github/DirectoryScraper/Directory_Out/Non_Fellow_Links.txt", 'r')
outFile = open("C:/Users/gersonda/Dropbox/Github/DirectoryScraper/Directory_Out/NonFellow.csv", 'w')
for line in fileName:
    print(line)
    # line = fileName.readline()
    doctorFirstName = ""
    doctorMiddleName = ""
    doctorLastName = ""
    city = ""
    state = ""
    zip = ""
    html_string = requests.get(line, stream=True).text.encode('utf-8', 'ignore')
    #print(line)
    html_soup = BeautifulSoup(html_string)
    payload = html_soup.td.td
    #print(payload)
    ws_payload = payload.p
    bold = ws_payload.b.extract()
    print(str(ws_payload.get_text()).strip())
    doctorArray = str(ws_payload.get_text()).strip().split(" ")
    doctorFirstName = doctorArray[0]
    doctorVar = len(doctorArray)
    if doctorVar == 2:
        doctorLastName = doctorArray[1]
    if doctorVar == 3:
        doctorMiddleName = doctorArray[1]
        doctorLastName = doctorArray[2]
    ws_payload = payload.p.next_sibling.next_sibling
    bold = ws_payload.b.extract()
    breakers = ws_payload.br.extract()
    practiceName = unicode(ws_payload.get_text()).strip().split("\n")[0]
    print(practiceName)
    if "army" not in practiceName.lower():
        try:
            ws_payload = payload.p.next_sibling.next_sibling.next_sibling.next_sibling
            bold = ws_payload.b.extract()
            breakers = ws_payload.br.extract()
            ws_payload = ws_payload.get_text().strip().split("\n")
            ws_payload = ws_payload[1].strip().split(" ")
            print(ws_payload)
            zip = ws_payload.pop()
            state = ws_payload.pop()
            city = ' '.join(ws_payload)
        except IndexError:
            print('Data element not found')
    outString = str(
        doctorFirstName + "," + doctorMiddleName + "," + doctorLastName + "," + city + "," + state + "," + zip + "\n")
    print(outString)
    outFile.write(outString)
    time.sleep(1)