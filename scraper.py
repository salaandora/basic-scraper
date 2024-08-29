import requests
from bs4 import BeautifulSoup

def tableRead (url):
    url = url
    page = requests.get(url)
    pContent = page.content
    

    pSoup = BeautifulSoup(pContent, 'html.parser')
    sDiv = pSoup.find('div', class_ = 'doc-content')
    sContent = sDiv.find_all('tr')

    del sContent[0]

    rowArr = []
    tableRowDict = {}

    for i in sContent:
        row = i.find_all('td')
        for j in row: 
            try:
                rowArr.append(int(j.text))
            except:
                rowArr.append(j.text)
        if rowArr[2] in tableRowDict:
            tableRowDict[rowArr[2]].append(rowArr)
        else:
            tableRowDict[rowArr[2]] = [rowArr]
        rowArr = []

    for i in sorted(tableRowDict):
        endstr=''
        count = 0
        for j in sorted(tableRowDict[i]):
            jc = j[0]
            diff = jc - count
            if j[0] == count:
                endstr += j[1]
                count += 1
            else:
                endstr += ' ' * (diff - 1)
                endstr += j[1]
                count += diff
        count = 0
        
        print(endstr)
        endstr = ''


tableRead("https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub")








