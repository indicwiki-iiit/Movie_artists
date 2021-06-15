from selenium import webdriver
import time
import pickle 
import pandas as pd



PATH = "/Users/sameersanam/chromedriver"
driver = webdriver.Chrome(PATH)


p = pickle.load(open('oscar_wiki_id2.pkl','rb'))
wiki = p['wiki_id'].tolist()

l = []
url = "https://www.wikidata.org/wiki/{}"
for i in wiki:

    url = "https://www.wikidata.org/wiki/{}".format(i)
    print(i)
    driver.get(url)
    time.sleep(1)
   
    

    #gender
    try:
        gender = driver.find_element_by_id("P21").text
    except:
        gender=""
    try:
        name = driver.find_element_by_id("P735").text
    except:
        name=""


    #citizenship
    try:
        citizen = driver.find_element_by_id("P27").text
    except:
        citizen = ""
    
    #spouse info
    try:
        spouse = driver.find_element_by_id("P26").text
    except:
        spouse=""

   


    # father mother child
    try:
        father = driver.find_element_by_id("P22").text
    except:
        father=""
    try:
        mother = driver.find_element_by_id("P25").text
    except:
        mother=""
    try:
        child = driver.find_element_by_id("P40").text
    except:
        child=""
    



    #siblings of the actor
    try:
        sibling = driver.find_element_by_id("P3373").text
    except:
        sibling=""



            



    #languages spoken
    try:
        languages_spoken = driver.find_element_by_id("P1412").text
    except:
        languages_spoken=""




#     #work period(start) and end
    try:
        work_period_start = driver.find_element_by_id("P2031").text

    except:
        work_period_start = ""
    try:
        work_period_end = driver.find_element_by_id("P2032").text

    except:
        work_period_end = ""
    




    # #ethnic group
    try:
        ethnic_group = driver.find_element_by_id("P172").text
    #     print(ethnic_group)
    except:
        ethnic_group = ""



    #relatives
    try:
        relatives = driver.find_element_by_id("P1038").text
    except:
        relatives = ""





    # #name in native language
    try:
        name_in_native_language = driver.find_element_by_id("P1559").text
    except:
        name_in_native_language = ""





    # #native language
    try:
        native_language = driver.find_element_by_id("P103").text
    except:
        native_language = ""




    # #family name
    try:
        family_name = driver.find_element_by_id("P734").text
    except:
        family_name = ""
    
    

    
    #pob dob dod
    try:
        pob = driver.find_element_by_id("P19").text
    except:
        pob = ""
    try:
        dob = driver.find_element_by_id("P569").text
    except:
        dob = ""
    try:
        dod = driver.find_element_by_id("P570").text
    except:
        dod = ""
    
    
    
    #filmo debutnam image
    try:
        filmo = driver.find_element_by_id("P1283").text
    except:
        filmo = ""
    try:
        debut_name = driver.find_element_by_id("P2318").text
    except:
        debut_name = ""
    try:
        image = driver.find_element_by_id("P18").text
    except:
        image = ""
    
    
    
    #alsoknownbyname alternatename nickname  
    try:
        also_known_ny_name = driver.find_element_by_id("P2561").text
    except:
        also_known_ny_name = ""
    try:
        alternate_name = driver.find_element_by_id("P4970").text
    except:
        alternate_name = ""
    try:
        nick_name = driver.find_element_by_id("P1449").text
    except:
        nick_name = ""
    try:
        birth_name = driver.find_element_by_id("P1477").text
    except:
        birth_name = ""
    
    
    
    
    #occupation commonscategory
    try:
        occupation = driver.find_element_by_id("P106").text
    except:
        occupation = ""
    try:
        commons_category = driver.find_element_by_id("P373").text
    except:
        commons_category = ""
    
    
    
    
    #
    try:
        viaf_id = driver.find_element_by_id("P214").text
    except:
        viaf_id = ""
    try:
        gnd_id = driver.find_element_by_id("P227").text
    except:
        gnd_id = ""
    try:
        icaid = driver.find_element_by_id("P244").text
    except:
        icaid = ""
    try:
        worldcat_id = driver.find_element_by_id("P7859").text
    except:
        worldcat_id = ""
    try:
        allmovie_id = driver.find_element_by_id("P2019").text
    except:
        allmovie_id = ""
    try:
        allocine_id = driver.find_element_by_id("P1266").text
    except:
        allocine_id = ""
    try:
        csf_id = driver.find_element_by_id("P2605").text
    except:
        csf_id = ""
    try:
        facebook_id = driver.find_element_by_id("P2013").text
    except:
        facebook_id = ""
    try:
        freebase_id = driver.find_element_by_id("P646").text
    except:
        freebase_id = ""
    try:
        insta_id = driver.find_element_by_id("P2003").text
    except:
        insta_id = ""
    try:
        kinopisk_id = driver.find_element_by_id("P2604").text
    except:
        kinopisk_id = ""
    try:
        port_id = driver.find_element_by_id("P2435").text
    except:
        port_id = ""
    try:
        quora_id = driver.find_element_by_id("P4411").text
    except:
        quora_id = ""
    try:
        twitter_id = driver.find_element_by_id("P2002").text
    except:
        twitter_id = ""
    try:
        imdb_id = driver.find_element_by_id("P345").text
    except:
        imdb_id = ""
    



   



    # #signature
    try:
        signature = driver.find_element_by_id("P109").text
        # print(signature)
    except:
        signature = ""
    
    a = [imdb_id,url,name,gender,citizen,spouse,father,mother,child,sibling,languages_spoken,work_period_start,work_period_end,ethnic_group,relatives,name_in_native_language,native_language,family_name,pob,dob,dod,filmo,debut_name,image,signature,also_known_ny_name,alternate_name,nick_name,birth_name,occupation,commons_category,viaf_id,gnd_id,icaid,worldcat_id,allmovie_id,allocine_id,csf_id,facebook_id,freebase_id,insta_id,kinopisk_id,port_id,quora_id,twitter_id]
    l.append(a)
    

df = pd.DataFrame(l, columns=['imdb_id','wiki_id','name' ,'gender','citizen','spouse','father','mother','child','sibling','languages_spoken','work_period_start','work_period_end','ethnic_group','relatives','name_in_native_language','native_language','family_name','pob','dob','dod','filmo','debut_name','image','signature','also_known_ny_name','alternate_name','nick_name','birth_name','occupation','commons_category','viaf_id','gnd_id','icaid','worldcat_id','allmovie_id','allocine_id','csf_id','facebook_id','freebase_id','insta_id','kinopisk_id','port_id','quora_id','twitter_id'])
print(df)
pd.read_csv
df.to_csv("/Users/sameersanam/m/oscar_wiki.csv")