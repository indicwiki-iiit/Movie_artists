from selenium import webdriver
import time
import pickle
import pandas as pd


PATH = "C:\Program Files (x86)\chromedriver"
driver = webdriver.Chrome(PATH)
wiki=pickle.load(open('oscar2k.pkl','rb'))
imdb= wiki['imdb_id'].tolist()
l=[]
k=0
data={}
for i in imdb:
    k=k+1
    if(k<=588):
        continue
    url = "https://www.imdb.com/name/{}/awards?ref_=nm_ql_2".format(i)
    driver.get(url)
    #time.sleep(3)
    c = driver.find_elements_by_class_name("awards")
    
    x=[]
    y=[]
    s=[]
    v=[]

    try:
        for t in c:
            trs = t.find_elements_by_tag_name("tr")
            
            for j in trs:
                a,b,d,e=0,"","",""
                try:
                    a = j.find_element_by_class_name("award_year").text #year
                except:
                    a = " "
                try:
                    b = j.find_element_by_class_name("award_outcome").find_element_by_tag_name("b").text
                except:
                    b=" "
                try:
                    d = j.find_element_by_class_name("award_category").text
                except:
                    d=" "
                try:
                    e = j.find_element_by_class_name("award_description").text
                except:
                    e = " "
                    
    # f = c.find_element_by_class_name("title_year")
                
                #l=a+","b
                x.append(a)
                y.append(b)
                s.append(e)
                v.append(d)
                
                
            #x.append(f)
            
            #print(x)
            #f=[]
    
    
    except:
        print("EXCEPTION!!!!!")

    #data[i]=x
    '''for z in x:
        print(z)
        df = pd.DataFrame(z[:],columns=['Year_Of_The_Award','Award_Outcome','Award_Category','Award_Description','IMDBid'])
        print(df)'''
    a = i
    try:
        w=driver.find_element_by_class_name("desc").text
    except:
        w=" "
    sam = [w,x,y,v,s,a]
    l.append(sam)    
    df = pd.DataFrame(l,columns=['No_Awards','Year_Of_The_Award','Award_Outcome','Award_Category','Award_Description','IMDBid'])
    print(k)
    df.to_csv(r'C:\Users\yasha\myenv_name\MovieArtist\oscar_awards2k_2.csv',index='False')
#print(data)
# for i in filmo_row_odd:
#         year = i.find_element_by_class_name("year_column")
#         movie_name = i.find_element_by_tag_name("b")
#  print(year.text, movie_name.text)+"award_outcome"+"award_category"+"award_description"+"title_year"