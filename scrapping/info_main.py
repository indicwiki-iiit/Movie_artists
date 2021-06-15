from selenium import webdriver
import time
import pickle
import pandas as pd

PATH = "/Users/sameersanam/chromedriver"
driver = webdriver.Chrome(PATH)
p = pickle.load(open("moviesDF.pkl", "rb"))
imdb_list = p['imdbidLabel'][:2].tolist()
l = []
url = "https://www.imdb.com/name/{}/"
for i in imdb_list:
    url = "https://www.imdb.com/name/{}/".format(i)
    driver.get(url)
#     print(url)
    try:
        a = driver.find_element_by_class_name("header").text
    except:
        a = ""
#     print("name: ",a.text)

        #for printing actor profession
    try:    
        b = driver.find_element_by_id("name-job-categories").text
    except:
        b = ""
#   print("profession: ",b.text)

        #date of birth for actor
    try:
        d = driver.find_element_by_id("name-born-info").text
    except:
        d = ""
#     print(d.text)
    m = url

        #alternate name of the actor
    try:
        e = driver.find_element_by_id("details-akas").text
        # print(e.text)
    except:
        e = ""

        #height of the actor
    try:
        f = driver.find_element_by_id("details-height").text
        # print(f.text)
    except:
        f = ""
        #actor star sign
    try:
        g = driver.find_element_by_id("dyk-star-sign").text
        # print(g.text)
    except:
        g = ""
    sam = [a,b,d,m,e,f,g]
    l.append(sam)

df = pd.DataFrame(l, columns=['Name','Profession/Occupation','Date_Of_Birth','IMDBid','Alternate_Name','Height','Star_Sign'])
print(df)
df.to_csv("/Users/sameersanam/m/info.csv")