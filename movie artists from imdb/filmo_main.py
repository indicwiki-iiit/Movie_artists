from bs4 import BeautifulSoup
import requests
import pandas as pd
import pickle 
import time

p = pickle.load(open("oscar2k.pkl","rb"))
imdb_list = p['imdb_id'].tolist()


url_common = 'https://www.imdb.com/name/{}/'

IMDb_ids, occupations, all_film_ocupations,latest_films, debut_films = [], [], [], [],[]
occup1_num, occup1_films, occup2_num, occup2_films, occup3_num, occup3_films, occup4_num, occup4_films = [], [], [], [], [], [], [], []
occups = [occup1_num,occup1_films,occup2_num,occup2_films,occup3_num,occup3_films,occup4_num,occup4_films]
# count = 0
for i in imdb_list:
    time.sleep(3)
    url = url_common.format(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    IMDb_ids.append(i)
    # if count==10:
        
    #     break
    # count+=1
    occupation = soup.find('div',id="name-job-categories")
    print(i)

    # print("profession: ", occupation.text)
    try:
        main_occ = occupation.text.strip().split("|")
    except:
        main_occ = ""
    for t in range(len(main_occ)):
        try:
            main_occ[t]=main_occ[t].strip()
        except:
            main_occ[t] = ""
    occupations.append(main_occ)
    try:
        filmography = soup.find('div', id='filmography')
    except:
        filmography = ""
    try:
     filmo_heads = filmography.find_all('div', {'class': 'head'})
    except:
        filmo_heads  = ""
    try:
        filmo_categories = filmography.find_all('div', {'class': 'filmo-category-section'})
    except:
        filmo_categories = ""
    # print(len(filmo_heads), len(filmo_categories))

    temp = 4
    
    roles = []
    for head in filmo_heads:
        role = head.find('a').text
        roles.append(role)
        temp -= 1
        if temp == 0: break
    # print(roles)
    all_film_ocupations.append(roles)
    latest,debut = [],[]
    temp = 0
    for category in filmo_categories:
        listi = []
        filmo_rows = category.find_all('div', {'class': 'filmo-row'})
        # print('total movies', len(filmo_rows))
        occups[temp*2].append(len(filmo_rows))
        temp1,temp_latest,temp_debut = 10,0,0
        # k = 0
        for film in filmo_rows:
            # if k==10:
            #     break
            # k+=1
            try:
                year = film.find('span', {'class': 'year_column'}).text.strip()
            except:
                year = "-1"
            a_tag = film.find('a')
            movie_name = a_tag.text.strip()
            movie_id = a_tag['href'].split("/")[-2]
            # print(year, movie_name, movie_id)
            if temp_latest == 0:
                latest.append([year, movie_name, movie_id])
                temp_latest+=1
            if temp1 != 0:
                # dicti[movie_id]=[year, movie_name]
                listi.append([year, movie_name, movie_id])
            if temp_debut == len(filmo_rows) - 1:
                debut.append([year, movie_name, movie_id])
            temp1 -= 1
            temp_debut += 1
        # print(latest_films,debut_films)
        occups[(temp * 2) + 1].append(listi)
        temp += 1
        if temp == 4: break
    if (4-temp) !=0:
        for num in range(temp,4):
            occups[num*2].append(0)
            occups[(num * 2) + 1].append([])
    latest_films.append(latest)
    debut_films.append(debut)

# print(latest_films)
dictionary = {'IMDb_id': IMDb_ids, 'occupation': occupations, 'all_film_ocupations': all_film_ocupations, 'latest_films': latest_films, 'debut_films': debut_films,'occup1_num': occup1_num, 'occup1_films': occup1_films, 'occup2_num': occup2_num, 'occup2_films': occup2_films, 'occup3_num': occup3_num, 'occup3_films': occup3_films,'occup4_num':occup4_num,'occup4_films':occup4_films}
# df = pd.DataFrame(dictionary)
df = pd.DataFrame.from_dict(dictionary, orient='index')
df = df.transpose()
print(df)
pd.read_csv
df.to_csv("filmo_oscar.csv")