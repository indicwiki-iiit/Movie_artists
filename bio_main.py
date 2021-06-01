from selenium import webdriver
import time
import pickle
import pandas as pd


PATH = "/Users/sameersanam/chromedriver"
driver = webdriver.Chrome(PATH)

p = pickle.load(open("moviesDF.pkl", "rb"))
imdb_list = p['imdbidLabel'][0:2].tolist()
l = []
url = "https://www.imdb.com/name/{}/bio?ref_=nm_ov_bio_sm"
for i in imdb_list:
    url = "https://www.imdb.com/name/{}/bio?ref_=nm_ov_bio_sm".format(i)
    driver.get(url)

    a = driver.find_element_by_id("overviewTable").text
# print(a)

# "https://www.imdb.com/name/{}/bio?ref_=nm_ov_bio_sm"
# b = driver.find_element_by_class_name("soda odd").text
# print(b)

    b = driver.find_element_by_tag_name("p").text
    c = i
# print(b)
# driver.quit

#reference
# print("if you have any query you can refer through this link")
# print("https://www.imdb.com/name/nm1659141/")
    sam = [a,b,c]
    l.append(sam)


df = pd.DataFrame(l,columns=['INTRO','Biography','IMDBid'])
print(df)
pd.read_csv
df.to_csv("/Users/sameersanam/m/do.csv")