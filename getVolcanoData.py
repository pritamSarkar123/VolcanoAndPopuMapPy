from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd

myUrl='http://volcano.oregonstate.edu/volcano_table'
pageObj=urlopen(myUrl)
pageRawHtml=pageObj.read()
pageObj.close()

pageData=soup(pageRawHtml,'html.parser')

container1=pageData.find("div",{"class":"view-display-id-page_4"})
containerO=container1.find_all("tr",{"class":"odd"})
containerE=container1.find_all("tr",{"class":"even"})

volcanoList=[]
def addEvens():
    items={}
    for container in containerE:
        items["Name"]=container.find("td",{"class":"views-field-title"}).text.strip()
        items["Country"]=container.find("td",{"class":"views-field-field-location-value"}).text.strip()
        items["Type"]=container.find("td",{"class":"views-field-field-vtype-value"}).text.strip()
        items["Lat"]=container.find("td",{"class":"views-field-field-latitude-value"}).text.strip()
        items["Lon"]=container.find("td",{"class":"views-field-field-longitude-value"}).text.strip()
        items["Elv"]=container.find("td",{"class":"views-field-field-elevation-value"}).text.strip()
        volcanoList.append(dict(items))
    for v in volcanoList:
        if v["Lat"]=='' or v['Lon']=='' or v["Elv"]=='':
            volcanoList.remove(v)
        else:
            v["Lat"]=float(v["Lat"])
            v["Lon"]=float(v["Lon"])
            v["Elv"]=float(v["Elv"])

def addOdds():
    items={}
    for container in containerO:
        items["Name"]=container.find("td",{"class":"views-field-title"}).text.strip()
        items["Country"]=container.find("td",{"class":"views-field-field-location-value"}).text.strip()
        items["Type"]=container.find("td",{"class":"views-field-field-vtype-value"}).text.strip()
        items["Lat"]=container.find("td",{"class":"views-field-field-latitude-value"}).text.strip()
        items["Lon"]=container.find("td",{"class":"views-field-field-longitude-value"}).text.strip()
        items["Elv"]=container.find("td",{"class":"views-field-field-elevation-value"}).text.strip()
        volcanoList.append(dict(items))
    for v in volcanoList:
        if v["Lat"]=='' or v['Lon']=='' or v["Elv"]=='':
            volcanoList.remove(v)
        else:
            v["Lat"]=float(v["Lat"])
            v["Lon"]=float(v["Lon"])
            v["Elv"]=float(v["Elv"])
addEvens()
addOdds()

volcanos=pd.DataFrame(volcanoList)

volcanos.to_csv('volcanos.csv',index=0)

