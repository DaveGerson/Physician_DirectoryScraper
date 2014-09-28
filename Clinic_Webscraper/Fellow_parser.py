__author__ = 'gerson64'

import re
regexTrainedFellows= r'(\w*)\s([A-Z]\.\s|[A-Z]\.[A-Z]\.\s|)(\w*)?\W\s.*'

fileName = open("C:/Users/gerson64/Desktop/Dropbox Sync/Dropbox/Github/DirectoryScraper/Directory_Out/Fellow_Data.txt", 'r')
outFileName = open("C:/Users/gerson64/Desktop/Dropbox Sync/Dropbox/Github/DirectoryScraper/Directory_Out/Fellow_Data_parsed.txt", 'w')

for line in fileName:
    firstname=''
    middleInitial=''
    lastName=''
    city=''
    state=''
    splitline=line.split('~')
    nameLine = re.search(regexTrainedFellows,splitline[0])
    if nameLine:
        firstname = nameLine.group(1).strip()
        #print(firstname)
        middleInitial = nameLine.group(2).strip()
        #print(middleInitial)
        lastName = nameLine.group(3).strip()
        #print(lastName)
        try:
            locationArray=splitline[1].split(',')
            try:
                city=locationArray[0].strip()
                #print(city)
            except IndexError:
                pass
            try:
                state=locationArray[1].translate(None, '\n').strip()
                #print(state)
            except IndexError:
                pass
        except IndexError:
            pass
        outString = str(firstname + "," + middleInitial + "," + lastName + "," + city + "," + state+"\n")
        print(outString)
        outFileName .write(outString)


