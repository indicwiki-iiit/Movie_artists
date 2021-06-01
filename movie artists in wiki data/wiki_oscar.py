import wptools
import pickle
import pandas as pd

wiki=pickle.load(open('oscar2k.pkl','rb'))
name_list=wiki['name'].tolist()
#print(type(name_list[0]))
k=0
l=[]
for i in name_list:
	k=k+1
	print(k)
	page=wptools.page(i)
	try:
		page.get_query()
	except:
		print("Exception")
	#page.get_query()
	wiki_id='NULL'
	try:
		wiki_id=page.data['wikibase']
	except:
		print("no Wikibase")
	l.append(wiki_id)
	print(wiki_id)

print(l)
df = pd.DataFrame(l,columns=['wiki_id'])
df.to_csv(r'C:\Users\yasha\myenv_name\MovieArtist\oscar_wikiid2k.csv',index='False')