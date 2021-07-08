import pickle
import ast
from re import X
import datetime
import pandas as pd
from jinja2 import Environment, FileSystemLoader 
# from datetime import datetime, timedelta
 

import io
# from anuvaad import Anuvaad
# telugu = Anuvaad('english-telugu')

#from google_trans_new import google_translator
#translator = google_translator()
#from textblob import TextBlob
#from deeptranslit import DeepTranslit
#trans = DeepTranslit('telugu').transliterate

#from genXML import tewiki, writePage
def cleank(sample):
    bad = ["'","[","]","'"]
    for i in bad:
        sample = sample.replace(i,'')
    x = sample.split(',')
    return(x)

def xldate_to_datetime(xldate):
	temp = datetime.datetime(1899, 12, 30)
	delta = datetime.timedelta(days=xldate)
	return temp+delta

#print(xldate_to_datetime(serialnumber))

#intro occ
introocc={

'Casting director':'',
'Location management':'',
'Musician':'',
'Casting':'కాస్టింగ్ డైరెక్టర్',
'Additional Crew':'',
'Editor':'ఎడిటింగ్',
'Editorial' : 'సంపాదకీయం',
'Art director':'ఆర్ట్ డైరెక్షన్',
'Art':'ఆర్ట్ డిపార్ట్మెంట్',
'Producer':'నిర్మాణం',
'Animation':'యానిమేషన్',
'Writer':'కథా రచన',
'Actor':'నటన',
'Actress':'నటన',
'Makeup':'మేకప్ ఆర్టిస్ట్',   
'Music':'సంగీతం',
'special effects':'స్పెషల్ ఎఫెక్ట్స్',
'Costume and Wardrobe':'కాస్ట్యూమ్ మరియు వార్డ్ రోబ్',
'Sound':'సౌండ్',
'Visual effects':'విసువల్ ఎఫెక్ట్స్',
'Script and Continuity':'స్క్రిప్ట్ అండ్ కంటిన్యూయిటీ',
'Composer':'సంగీత దర్శకత్వం',  
'Production manager':'ప్రోడక్షన్  మేనేజర్',
'Set decorator':'సెట్ డెకొరేషన్',
'Production designer':'ప్రొడక్షన్ డిజైనింగ్',
'Second Unit Director or Assistant Director':'సహాయ దర్శకత్వం',
'Comedian':'హాస్యనటన',
'Costume designer':'కాస్ట్యూమ్ డిజైనర్',
'Stunts':'స్టంట్స్',
'Soundtrack':'సౌండ్ ట్రాక్',
'Cinematographer':'ఛాయాగ్రహణం',
'Director':'దర్శకత్వం',

}


#career stuff
def occup_clean(sample,row):
	if(row.Gender.values[0]=='female' or row.Gender.values[0]=='transgender female'):
		d={
	'Editor':'ఎడిటర్',
	'Editorial':'సంపాదకీయురాలు',
	'Locationmanagement':'',
	'transgender female':'',
	'Musician':'',
	'Casting':'కాస్టింగ్ డైరెక్టర్',
	'Model':'',
	'AdditionalCrew':'',
	'Cricketer':'',
	'Politician':'',
	'Soundtrack':'సంగీత విభాగంలో ప్రదర్శకురాలి',
	'Cinematographer':'ఛాయాగ్రాహకురాలి',
	'Director':'దర్శకురాలి',
	'':'',
	'Artdirector':'కళా దర్శకురాలి',
	'Art':'అసిస్టెంట్ ఆర్ట్ డైరెక్టర్',
	'Producer':'నిర్మాత',
	'Animation':'అనిమేషన్ ఆర్టిస్ట్',
	'Writer':'కథా రచయిత',
	'Actor':'నటి',
	'Actress':'నటి',
	'Makeup':'మేకప్ ఆర్టిస్ట్',
	'Music':'గాయకురాలి',
	'Specialeffects':'స్పెషల్ ఎఫెక్ట్స్ ఆర్టిస్ట్',
	'CostumeandWardrobe':'వార్డ్రోబ్ డిజైనర్',
	'Sound':'సౌండ్ ఇంజినీర్',
	'Visualeffects':'విసువల్ ఎఫెక్ట్స్ ఆర్టిస్ట్',
	'ScriptandContinuity':'స్క్రిప్ట్ రైటర్',
	'Composer':'సంగీత దర్శకురాలి',
	'Productionmanager':'ప్రొడక్షన్ మేనేజర్',
	'Setdecorator':'సెట్ డెకరేటర్',
	'Productiondesigner':'ప్రొడక్షన్ డిజైనర్',
	'SecondUnitDirectororAssistantDirector':'సహాయ దర్శకురాలి',
	'Comedian':'హాస్యనటి',
	'Costumedesigner':'కాస్ట్యూమ్ డిజైనర్',
	'Stunts':'స్టంట్ డైరెక్టర్',
	'CameraandElectrical':'',
	'Castingdirector':'',
	'Transportation':''



	}
	else:
		d={
	'Editor':'ఎడిటర్',
	'Editorial':'సంపాదకీయుడి',
	'Locationmanagement':'',
	'Musician':'',
	'Casting':'కాస్టింగ్ డైరెక్టర్',
	'Model':'',
	'AdditionalCrew':'',
	'Cricketer':'',
	'Politician':'',
	'Soundtrack':'సంగీత విభాగంలో ప్రదర్శకుడి',
	'Cinematographer':'ఛాయాగ్రాహకుడి',
	'Director':'దర్శకుడి',
	'':'',
	'Artdirector':'ఆర్ట్ డైరెక్టర్',
	'Art' :'అసిస్టెంట్ ఆర్ట్ డైరెక్టర్',
	'Producer':'నిర్మాత',
	'Animation':'అనిమేషన్ ఆర్టిస్ట్',
	'Writer':'కథా రచయిత',
	'Actor':'నటుడి',
	'Makeup':'మేకప్ ఆర్టిస్ట్',
	'Music':'గాయకుడి' ,
	'Specialeffects':'స్పెషల్ ఎఫెక్ట్స్ ఆర్టిస్ట్',
	'CostumeandWardrobe':'వార్డ్రోబ్ డిజైనర్',
	'Sound':'సౌండ్ ఇంజినీర్',
	'Visualeffects':'విసువల్ ఎఫెక్ట్స్ ఆర్టిస్ట్',
	'ScriptandContinuity':'స్క్రిప్ట్ రైటర్',
	'Composer':'సంగీత దర్శకుడి',
	'Productionmanager':'ప్రొడక్షన్ మేనేజర్', 
	'Setdecorator':'సెట్ డెకరేటర్',
	'Productiondesigner':'ప్రొడక్షన్ డిజైనర్',
	'SecondUnitDirectororAssistantDirector':'సహాయ దర్శకుడి',
	'Comedian':'హాస్యనటుడి',
	'Costumedesigner':'కాస్ట్యూమ్ డిజైనర్',
	'Stunts':'స్టంట్ డైరెక్టర్',
	'CameraandElectrical':'',
	'Castingdirector':'',
	'Transportation':''



	}

	bad = ["'","[","]","'"," "]
	for i in bad:
		if(isinstance(sample,float)==False):
			sample = sample.replace(i,'')
	x = []
	if(isinstance(sample,float)==False):	
		x=sample.split(',')

	for i in range (0,len(x)):
		x[i]=d[x[i]]

	return(x)


def getData(row):

	def split1(sample):
		f = ["''"]
		for i in f:
			z=f.remove('')
		return(z)

	def listToString(s):
		str1=""
		if(isinstance(s,float)==False):

			str1 = ', '.join([str(elem) for elem in s])
		else:
			str1 = 1.0
		return(str1)

	def clean(sample):
		bad = ["'","[","]","'"," ","^"]
		for i in bad:
			if(i=='^'):
				sample = sample.replace(i,' ')
			else:
				sample = sample.replace(i,'')
			
		x=sample.split(',')
		return(x)
	def clean1(sample):
		bad = ["'","[","]","'","^"," " " "]
		if(isinstance(sample,float)==False):
			for i in bad:
				if(i=='^'):
					sample = sample.replace(i,' ')
				else:
					sample = sample.replace(i,'')
		x = []
		if(isinstance(sample,float)==False):
			x=sample.split(',')
		return(x)
	def clearyear(sample):
		bad = [","]
		if(isinstance(sample,float)==False):
			for i in bad:
				# sample = sample.replace(i,' ')
				sample = sample.replace(i,'')
		x = []
		return(x)
	def spaceclean(sample):
		bad = ["'","[","]","'","^"," " " "," "]
		if(isinstance(sample,float)==False):
			for i in bad:
				if(i=='^'):
					sample = sample.replace(i,' ')
				else:
					sample = sample.replace(i,'')
		x = []
		if(isinstance(sample,float)==False):
			x=sample.split(',')
		return(x)
	def filmoclean(sample):
		bad = [",^'",",^[",',^"',"^"]
		for i in bad:
			if i==",^[":
				sample = sample.replace(i,",[")
			elif i==",^'":
				sample = sample.replace(i,",'")
			elif i==',^"':
				sample = sample.replace(i,',"')
			elif i=='^':
				sample = sample.replace(i,' ')
			

			

		x=sample
		return(x)
	def num(sample):
		sam=int(sample)
		return(sam)
	#def sep(sample):
	#	sample=list[sample]
	#	sepi=sample.split(',')
	#	return(sepi)
	

	occup1_num=int(row.occup1_num.values[0])
	occup2_num=int(row.occup2_num.values[0])
	occup3_num=int(row.occup3_num.values[0])
	occup4_num=int(row.occup4_num.values[0])

	Name=row.Name.values[0]
	if(isinstance(Name, float)==False):
		Name=Name
	else:
		Name=1.0
	Citizenship=row.Citizenship.values[0]
	#print(type(Citizenship))
	#lenc=len(Citizenship)
	#print(lenc)
	#print(Citizenship)
	lenc=0
	if(isinstance(Citizenship, float)==False):
		#Citizenship=listToString(Citizenship)
		#print(Citizenship)
		#print(type(Citizenship))
		#citi=[]
		#for i in range(0,lenc):
		Citizenship=Citizenship
		citi=Citizenship.split(',')
		lenc=len(citi)
		
	else:
		Citizenship=1.0
	#print(Citizenship)
	#print(citi)
	#print(lenc)
	
	filmo_occupation=row.filmo_occupation.values[0]
	if(isinstance(filmo_occupation,float)==False):
		filmo_occupation=clean1(filmo_occupation)
	else:
		filmo_occupation = 1.0

	'''bad = ["'","[","]","'"]
	res=[]
	if(isinstance(filmo_occupation, float)==False):
		for i in bad:
			filmo_occupation = filmo_occupation.replace(i,'')
		res=filmo_occupation.split(',')
	#print(res)
	filmocc=[]
	for i in res:
		if(isinstance(i, float)==False):
			filmocc.append(i)
		else:
			filmocc=1.0'''
	

	debut_films=row.debut_films.values[0]
	if(isinstance(debut_films, float)==False):
		debut_films = clean1(debut_films)
	else:
		debut_films = 1.0

	print(debut_films)
	#print(type(debut_films))
	debut_filmsf=[]
	if(isinstance(debut_films, float)==False and debut_films!=['']):
		debut_filmsf.append(debut_films[0])
		debut_filmsf.append(debut_films[1])
	else:
		debut_films=1.0
	#print(debut_filmsf)
	#print(str(TextBlob('Hyderabad Blues').translate(to='te')))
	#print(trans('Hyderabad Blues')[0]['pred'])
	latest_films=row.latest_films.values[0]
	if(isinstance(latest_films, float)==False):
		latest_films = clean(latest_films)
	else:
		latest_films = 1.0
	latest_filmsf=[]
	if(isinstance(latest_films, float)==False and latest_films!=['']):
		latest_filmsf.append(latest_films[0])
		latest_filmsf.append(latest_films[1])
	else:
		latest_films=1.0


	filmo_all_film_ocupations = row.English_filmo_all_film_ocupations.values[0]
	if(isinstance(filmo_all_film_ocupations,float)==False):
		filmo_all_film_ocupations=occup_clean(filmo_all_film_ocupations,row)
		# filmo_all_film_ocupations = filmo_all_film_ocupations
		print('hi',filmo_all_film_ocupations)
		lenf=len(filmo_all_film_ocupations)
		print('yash',lenf)
	else:
		filmo_all_film_ocupations = 1.0
		lenf = 1.0
#intro
	engfilmo_all_film_occ = row.English_filmo_all_film_ocupations.values[0]
	intro_filmo=[]
	lennew = 1
	lenintro= -1
	careercsentence = []
	lencareer = -1
	infoocup = []
	if(isinstance(engfilmo_all_film_occ,float)==False):
		engfilmo_all_film_occ=clean1(engfilmo_all_film_occ)
		for i in range(0,len(engfilmo_all_film_occ)):
			for key in introocc:
				if(engfilmo_all_film_occ[i]==key):
					careercsentence.append(introocc[key])
					infoocup.append(introocc[key])
					
				
				elif(engfilmo_all_film_occ[i]==''):
					pass
	
		print('thu',careercsentence)
		infoocup = str(infoocup).replace("[",'')
		infoocup = str(infoocup).replace("]",'')
		infoocup = str(infoocup).replace("'",'')
		# infoocup = clearyear(infoocup)
		print('lit',infoocup)
		lencareer = len(careercsentence)
		print('set',lencareer)
		engfilmo_all_film_occ1=[]
		
		if(isinstance(engfilmo_all_film_occ,float)==False):	
			lenin=len(engfilmo_all_film_occ)
			for i in range(1,lenin):
				engfilmo_all_film_occ1.append(engfilmo_all_film_occ[i])
				#print(engfilmo_all_film_occ1)
			lennew=len(engfilmo_all_film_occ1)
			if(lennew==0):
				lennew=1.0
			else:	
			#print(lennew)
				for i in range(0,lennew):
					for key in introocc:
						if(engfilmo_all_film_occ1[i]==key):
							intro_filmo.append(introocc[key])
						elif(engfilmo_all_film_occ1[i]==''):
							pass
			
				print('dead',intro_filmo)
		
				# lenintro = len(intro_filmo)
			lenintro = len(intro_filmo)
			print('dude',lenintro)
			
		else:
			intro_filmo=1.0
			lennew=1.0
			lenintro = 1.0
			careercsentence = 1.0





	# bad = ["'","[","]","'"," "]
	'''for i in bad:
		filmo_all_film_ocupations = filmo_all_film_ocupations.replace(i,'')
	resa=filmo_all_film_ocupations.split(',')
	print(resa)
	resa = list(filter(None, resa))
	#print(resa)
	lenresa=len(resa)
	k=resa[0]
	resa.remove(k)
	#print(resa)
	lenf=len(resa)
	#print(lenf)
	#print(lenresa)
	filmoccall=[]
	for i in resa:
		if(isinstance(i, float)==False):
			try:
				filmoccall.append(str(TextBlob(i).translate(to='te')))
			except:
				pass
		else:
			filmoccall=1.0'''
	#print(filmoccall)
	#print(filmoccall[0])
	#lenf=len(filmoccall)
	#print(lenf)
	#lenfirstocc=len(filmoccall[0])
	#print(lenfirstocc)


	lenalter=0
	Alternate_Name=row.Alternate_Name.values[0]
	if(isinstance(Alternate_Name, float)==False):
		Alternate_Name=Alternate_Name
		alter=Alternate_Name.split(',')
		lenalter=len(alter)
	else:
		Alternate_Name=1.0

	lenn=0
	Native_language=row.Native_language.values[0]
	native=[]
	if(isinstance(Native_language, float)==False):
		Native_language=Native_language
		native=Native_language.split(',')
		lenn=len(native)
	else:
		Native_language=1.0


	lenl=0
	Languages_spoken=row.Languages_spoken.values[0]
	if(isinstance(Languages_spoken, float)==False):
		Languages_spoken=Languages_spoken
		Lang=Languages_spoken.split(',')
		lenl=len(Lang)
	else:
		Languages_spoken=1.0
	#print(Languages_spoken)
	#print(Lang)
	#print(lenl)


	Actor_POB=row.Actor_POB.values[0]
	if(isinstance(Actor_POB, float)==False):
		Actor_POB=Actor_POB
	else:
		Actor_POB=1.0

	Birthname=row.Birthname.values[0]
	if(isinstance(Birthname, float)==False):
		Birthname=Birthname
	else:
		Birthname=1.0

	Father_Name=row.Father_Name.values[0]
	if(isinstance(Father_Name, float)==False):
		Father_Name=Father_Name
	else:
		Father_Name=1.0

	Mother_Name=row.Mother_Name.values[0]
	if(isinstance(Mother_Name, float)==False):
		Mother_Name=Mother_Name
	else:
		Mother_Name=1.0

	lensib=0
	wiki_siblings=row.wiki_siblings.values[0]
	if(isinstance(wiki_siblings, float)==False):
		wiki_siblings=wiki_siblings
		sib=wiki_siblings.split(',')
		lensib=len(sib)
	else:
		wiki_siblings=1.0

	lenspouse=0
	wiki_spouse_name=row.wiki_spouse_name.values[0]
	wiki_spouse_namef=[]
	if(isinstance(wiki_spouse_name, float)==False):
		wiki_spouse_name=wiki_spouse_name
		spous=wiki_spouse_name.split(',')
		lenspouse=len(spous)
		wiki_spouse_namef=spous[lenspouse-1]
		#print(wiki_spouse_namef)
	else:
		wiki_spouse_name=1.0




	Child_Name=row.Child_Name.values[0]
	if(isinstance(Child_Name, float)==False):
		Child_Name=Child_Name
	else:
		Child_Name=1.0

	wiki_family_name=row.wiki_family_name.values[0]
	if(isinstance(wiki_family_name, float)==False):
		wiki_family_name=wiki_family_name
	else:
		wiki_family_name=1.0

	lenrela=0
	Relatives=row.Relatives.values[0]
	if(isinstance(Relatives, float)==False):
		Relatives=Relatives
		rela=Relatives.split(',')
		lenrela=len(rela)
	else:
		Relatives=1.0
	alpha=['-','/','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	wiki_DOB=row.wiki_DOB.values[0]
	print('hi',type(wiki_DOB))
	wiki_DOB_year=wiki_DOB
	flag=0
	if(isinstance(wiki_DOB, float)==False):
		#if(isinstance(wiki_DOB,str)==False):
		for i in alpha:
			if(type(wiki_DOB)!=int and type(wiki_DOB)!=datetime.datetime):
				if(wiki_DOB.find(i)):
					flag=1
					break
				else:
					flag=0
					break
		print('flag',flag)
		if(flag==1):
			wiki_DOB=wiki_DOB
			print("wiki"+wiki_DOB)
			if(wiki_DOB=="20 century" or wiki_DOB=="19 century"):
				wiki_DOB_year=1.0
			
			elif "-" in wiki_DOB:
				
				wiki_DOB_year=wiki_DOB[0:4]	
				print('year'+wiki_DOB_year)
			else:	
				wiki_DOB_year=wiki_DOB[-4:]
				print('yes'+wiki_DOB_year)
			
			
			
		elif(int(wiki_DOB)>1700 and int(wiki_DOB)<2020):
			wiki_DOB=wiki_DOB
			wiki_DOB_year=wiki_DOB
			
		else:
			wiki_DOB=xldate_to_datetime(wiki_DOB)
			wiki_DOB=wiki_DOB.strftime("%Y-%m-%d")
			print(wiki_DOB)
			print(type(wiki_DOB))
		#else:
		#	wiki_DOB=wiki_DOB
		#wiki_DOB_year=xldate_to_datetime(wiki_DOB)
			wiki_DOB_year=xldate_to_datetime(wiki_DOB_year)
			wiki_DOB_year=wiki_DOB_year.strftime("%Y")
			print(wiki_DOB_year)
		
	else:
		wiki_DOB=1.0
		wiki_DOB_year=1.0
	

	alpha=['-','/','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	DOD=row.DOD.values[0]
	print(type(DOD))
	DOD_year=DOD
	flag=0
	if(isinstance(DOD, float)==False):
		#if(isinstance(wiki_DOB,str)==False):
		
		for i in alpha:
			if(type(DOD)!=int):
				if(DOD.find(i)):
					flag=1
					break
				else:
					flag=0
					break

		if(flag==1):
			DOD=DOD
			if(DOD=="20 century" or DOD=="19 century"):
				DOD_year=1.0
			elif(DOD.find("-")):
				DOD_year=DOD[0:3]	
			else:	
				DOD_year=DOD[-4:]
		elif(int(DOD)>1700 and int(DOD)<2020):
			DOD=DOD
			DOD_year=DOD	
		else:
			DOD=xldate_to_datetime(DOD)
			DOD=DOD.strftime("%Y-%m-%d")
			# print(DOD)
			print(type(DOD))
		#else:
		#	wiki_DOB=wiki_DOB
		#wiki_DOB_year=xldate_to_datetime(wiki_DOB)
			DOD_year=xldate_to_datetime(DOD_year)
			DOD_year=DOD_year.strftime("%Y")
			print(DOD_year)
		
	else:
		DOD=1.0
		DOD_year=1.0
	present_date = datetime.date.today()
	present_date=present_date.strftime('%Y-%m-%d')
	#print(present_date)

	#infostuff

	# Name_in_native_languageinfo=row.Name_in_native_language.values[0]
	# if(isinstance(Name_in_native_languageinfo, float)==False):
	# 	Name_in_native_languageinfo=Name_in_native_languageinfo
	# else:
	# 	Name_in_native_languageinfo=1.0

	Genderinfo=row.Gender.values[0]
	if(isinstance(Genderinfo, float)==False):
		Genderinfo=Genderinfo
	else:
		Genderinfo=1.0

	filmo_occupationinfo=row.wiki_occupation.values[0]
	#res = filmo_occupation.strip('][').split(',')
	'''occ=""
	for i in range(0,len(res)):
		if(i==len(res)-1):
			c=res[i].strip("'")
			occ=occ+c+"."
		else:
			c=res[i].strip("'")
			occ=occ+c+" ," '''
	'''bad = ["'","[","]","'"]
	for i in bad:
		filmo_occupationinfo = filmo_occupation.replace(i,'')
	res=filmo_occupationinfo.split(',')
	#print(res)
	for i in range(0,len(res)):
		if(i==len(res)-1):
			occ=occ+res[i]+"."
		else:
			occ=occ+res[i]+" ,"

	if(isinstance(filmo_occupationinfo, float)==False):
		filmo_occupationinfo=TextBlob(occ.strip('')).translate(to='te')
		filmo_occupationinfo=filmo_occupationinfo.split(',')
	else:
		filmo_occupationinfo=1.0'''


	Star_Sign=row.Star_Sign.values[0]
	if(isinstance(Star_Sign, float)==False):
		Star_Sign=Star_Sign
	else:
		Star_Sign=1.0

	Height=row.Height.values[0]
	if(isinstance(Height, float)==False):
		Height=Height
	else:
		Height=1.0

	Ethnic_group=row.Ethnic_group.values[0]
	if(isinstance(Ethnic_group, float)==False):
		Ethnic_group=Ethnic_group
	else:
		Ethnic_group=1.0

	Work_period_start=row.Work_period_start.values[0]
	if(isinstance(Work_period_start, float)==False):
		#if(isinstance(Work_period_start,str)==False):
		if(int(Work_period_start)>1700 and int(Work_period_start)<2020):
			Work_period_start=Work_period_start
			work_startyear=Work_period_start
		else:	
			Work_period_start=xldate_to_datetime(Work_period_start)
			work_startyear=Work_period_start.strftime("%Y")
		#else:
			#Work_period_start=Work_period_start
			#work_startyear=Work_period_start.split('-')
			#work_startyear=work_startyear[2]
	else:
		Work_period_start=1.0
		work_startyear=1.0

	Work_period_end=row.Work_period_end.values[0]
	if(isinstance(Work_period_end, float)==False):
		if(int(Work_period_end)>1700 and int(Work_period_end)<2020):
			Work_period_end=Work_period_end
		else:
			Work_period_end=xldate_to_datetime(Work_period_end)		
		#if(isinstance(Work_period_end,str)==False):
		#Work_period_end=xldate_to_datetime(Work_period_end)
		#else:
		#Work_period_end=Work_period_end
	else:
		Work_period_end=1.0	

	Image=row.New_image.values[0]
	if(isinstance(Image, float)==False):
		Image=Image
	else:
		Image=1.0

	Signature_image=row.Signature_image.values[0]
	if(isinstance(Signature_image, float)==False):
		Signature_image=Signature_image
	else:
		Signature_image=1.0




	#career stuff
	
	debut_filmseng=row.English_debut_films.values[0]
	if(isinstance(debut_filmseng, float)==False):
		debut_filmseng = clean1(row.English_debut_films.values[0])
	else:
		debut_filmseng = 1.0
	debut_filmst=row.debut_films.values[0]
	if(isinstance(debut_filmst,float)==False):
		debut_filmst=clean1(debut_filmst)
	else:
		debut_filmst = 1.0

	English_filmo_all_film_ocupations=row.English_filmo_all_film_ocupations.values[0]
	if(isinstance(English_filmo_all_film_ocupations,float)==False):
		occuplen=len(occup_clean(English_filmo_all_film_ocupations,row))
	else:
		occuplen = 1.0

	latest_filmseng=row.English_latest_films.values[0]
	if(isinstance(latest_filmseng, float)==False):
		latest_filmseng=clean1(row.English_latest_films.values[0])
	else:
		latest_filmseng=1.0
	latest_filmst=row.latest_films.values[0]
	if(isinstance(latest_filmst,float)==False):
		latest_filmst = clean1(latest_filmst)
	else:
		latest_filmst =1.0

	#filmo awards stuff
	Year_Of_The_Award=row.Year_Of_The_Award.values[0]
	if(isinstance(Year_Of_The_Award, float)==False):
		Year_Of_The_Award=clean(Year_Of_The_Award)
	else:
		Year_Of_The_Award=1.0

	Award_Outcome=row.Award_Outcome.values[0]
	if(isinstance(Award_Outcome, float)==False):
		Award_Outcome=clean(Award_Outcome)
	else:
		Award_Outcome=1.0

	Award_Category=row.Award_Category.values[0]
	Award_Categoryeng=row.English_Award_Category.values[0]
	if(isinstance(Award_Category, float)==False):
		award=clean1(Award_Category)
		award1=clean1(Award_Categoryeng)
		Award_Category=award
		Award_Categoryeng=award1
	else:
		Award_Category=1.0
		Award_Categoryeng=1.0

	Award_Description=row.Award_Description.values[0]
	Award_Descriptioneng=row.English_Award_Description.values[0]
	if(isinstance(Award_Description, float)==False):
		desc=clean1(Award_Description)
		if(isinstance(Award_Descriptioneng, float)==False):
			desc1=clean1(Award_Descriptioneng)
			Award_Descriptioneng = desc1
		Award_Description = desc
		
	else:
		Award_Description = 1.0
		Award_Descriptioneng=1.0

	No_of_Awards=row.No_of_Awards.values[0]
	Award_Now=[1.0,1.0]
	Award_Non=[1.0,1.0]
	if(isinstance(No_of_Awards,float)==False):
		temp=No_of_Awards.split(',')
		# print(temp)
		Award_Now=temp[0].split(' ')
		print(Award_Now)
		
		Award_Non=temp[1].split(' ')
		# print(Award_Now[0])
		# print(Award_Non[0])
		# if(isinstance(No_of_Awards,float)==False):
		# 	No_of_Awards = No_of_Awards
	else:
		No_of_Awards = 1.0


	filmo1=[]
	filmo1_1=[]

	if(isinstance(row.occup1_films.values[0],float)==False):
		filmo1=ast.literal_eval(filmoclean(row.occup1_films.values[0]))

		# print(filmo1)
		#t = open("x.txt","w")
		#t.write(str(filmo1))
		filmo1_1=ast.literal_eval(row.English_occup1_films.values[0])
	'''if(isinstance(filmo1,float)==False):
		filmo1=filmo1.split(',')
		filmlen=len(filmo1)
		print(filmlen)
		filmo1_1=filmo1_1.split(',')
		print(filmo1_1)
	else:
		filmo1=1.0
		filmo1_1=1.0	'''			


	filmo2=[]
	filmo2_1=[]
	if(isinstance(row.occup2_films.values[0],float)==False):
		filmo2=ast.literal_eval(filmoclean(row.occup2_films.values[0]))
		filmo2_1=ast.literal_eval(row.English_occup2_films.values[0])
	'''if(isinstance(filmo2,float)==False):
		filmo2=filmo2.split(',')
		filmlen=len(filmo2)
		filmo2_1=filmo2_1.split(',')
	else:
		filmo2=1.0
		filmo2_1=1.0'''


	filmo3=[]
	filmo3_1=[]
	if(isinstance(row.occup3_films.values[0],float)==False):
		filmo3=ast.literal_eval(filmoclean(row.occup3_films.values[0]))
		filmo3_1=ast.literal_eval(row.English_occup3_films.values[0])
	'''if(isinstance(filmo3,float)==False):
		filmo3=filmo3.split(',')
		#print(filmo3)
		filmlen=len(filmo3)
		filmo3_1=filmo3_1.split(',')
	else:
		filmo3=1.0
		filmo3_1=1.0'''	

	filmo4=[]
	filmo4_1=[]
	if(isinstance(row.occup4_films.values[0],float)==False):
		filmo4=ast.literal_eval(filmoclean(row.occup4_films.values[0]))
		filmo4_1=ast.literal_eval(row.English_occup4_films.values[0])
	'''if(isinstance(filmo4,float)==False):
		filmo4=filmo4.split(',')
		filmlen=len(filmo4)
		filmo4_1=filmo4_1.split(',')
	else:
		filmo4=1.0
		filmo4_1=1.0'''
	
	filmo_occupationfilmo=row.filmo_all_film_ocupations.values[0]
	print(filmo_occupationfilmo)
	if(isinstance(filmo_occupationfilmo,float)==False):
		print(filmo_occupationfilmo)
		filmo_all_film_ocupations_filmo=spaceclean(filmo_occupationfilmo)
		print('space',filmo_all_film_ocupations_filmo)
		# print(filmo_occupationfilmo)
		# print(type(filmo_all_film_ocupations_filmo))    
		latest_films_filmo=spaceclean(row.latest_films.values[0])
		#latest_films_filmo=latest_films_filmo.replace('^',' ')
		debut_films_filmo=spaceclean(row.debut_films.values[0])
		#debut_films_filmo=debut_films_filmo.replace('^',' ')
	else:
		filmo_occupationfilmo=1.0
		filmo_all_film_ocupations_filmo = 1.0
		latest_films_filmo  = 1.0
		debut_films_filmo = 1.0
	

	# print(data['occup1_num'])
	if(isinstance(row.occup1_films.values[0],float)==False):
		if(occup1_num>=10):
			sam = len(row.occup1_films.values[0][0:len(filmo1)])
		else:
			sam = len(row.occup1_films.values[0][0:occup1_num])
		# print(filmo1)
		
	else:
		sam=1.0

	if(isinstance(row.occup2_films.values[0],float)==False):
		if(occup2_num>=10):
			san = len(row.occup2_films.values[0][0:len(filmo2)])
		else:
			san = len(row.occup2_films.values[0][0:occup2_num])
		# print(filmo2)
	else:
		san=1.0

	if(isinstance(row.occup3_films.values[0],float)==False):
		if(occup3_num>=10):
			ran = len(row.occup3_films.values[0][0:len(filmo3)])
			
		else:
			ran = len(row.occup3_films.values[0][0:occup3_num])
		
	else:
		ran=1.0

	if(isinstance(row.occup4_films.values[0],float)==False):
		if(occup4_num>=10):
			man = len(row.occup4_films.values[0][0:len(filmo4)])
		else:
			man = len(row.occup4_films.values[0][0:occup4_num])
	else:
		man=1.0


	# print(len(data['Year_Of_The_Award']))
	if(isinstance(Year_Of_The_Award,float)==False):
		if(len(Year_Of_The_Award)>=10):
			length = len(Year_Of_The_Award[0:])
		else:
			length = len(Year_Of_The_Award)



	else:
		length = 1
	
	Knownfor = row.Knownfor.values[0]
	if(isinstance(row.Knownfor.values[0],float)==False):
		Knownfor = ast.literal_eval(row.Knownfor.values[0])
		Knownforlength = len(Knownfor)
		for i in range(0,Knownforlength):
		
			Knownfor[i][2] = Knownfor[i][2].strip('(')
			Knownfor[i][2] = Knownfor[i][2].strip(')')

	else:
		Knownfor = 1.0
		Knownforlength = 1.0
	print('gang',Knownfor)
	
	
	print(Knownforlength)








	# Data dictionary 
	data = {
		#{%- macro infobox(Image,Name, Name_in_native_language, Birthname, Alternate_Name, wiki_DOB,DOD,Actor_POB, Gender,Citizenship, wiki_occupation,
		#Work_period_start,Work_period_end,Height,Star_Sign,Ethnic_group,wiki_spouse_name,Child_Name,Father_Name, Mother_Name,wiki_siblings,Relatives,Signature_image) -%}
		'Name':Name,
		'Nameeng':row.English_Name.values[0],
		'filmo_occupation': filmo_occupation,
		'filmo_all_film_ocupations':filmo_all_film_ocupations,
		'Citizenship':str(Citizenship),
		'lenf':lenf,
		'lenl':lenl,
		'lenc':lenc,
		'lenn':lenn,
		'lenalter':lenalter,
		'lensib':lensib,
		#'lenfirstocc' :lenfirstocc,
		'Gender':row.Gender.values[0],
		'Native_language': Native_language,
		'Languages_spoken':Languages_spoken,
		# 'Name_in_native_language': row.Name_in_native_language.values[0],
		'native':native,
		'debut_filmsip': debut_filmseng,
		'latest_filmsip': latest_filmseng,
        'debut_filmsf':debut_filmsf,
		'latest_filmsf':latest_filmsf,
		'present_date':present_date,
		'occup1_num': occup1_num,
		'occup2_num': occup2_num,
		'occup3_num': occup3_num,
		'occup4_num': occup4_num,
		'work_startyear':work_startyear,
		'intro_filmo':intro_filmo,
		'lennew':lennew,
		#{% macro personal_life(Name,Gender,wiki_DOB,Actor_POB,Birthname,Alternate_Name,Father_Name,
		#Mother_Name,wiki_siblings,wiki_family_name,Relatives,wiki_spouse_name,Child_Name,DOD) %}
		'wiki_DOB': str(wiki_DOB),
		'Actor_POB': Actor_POB,
		'Birthname': Birthname,
		'Alternate_Name': Alternate_Name,
		'Father_Name': Father_Name,
		'Mother_Name': Mother_Name,
		'wiki_siblings':wiki_siblings,
		'wiki_family_name': wiki_family_name,
		'Relatives': Relatives,
		'lenrela':lenrela,
		'wiki_spouse_namef': str(wiki_spouse_namef),
		#'wiki_spouse_name':wiki_spouse_name,
		'Child_Name': Child_Name,
		'DOD': str(DOD),
		'DOD_year':str(DOD_year),
		#{% macro infobox(IMDB_id,Image,Name, Name_in_native_language, Birthname, Alternate_Name, wiki_DOB,DOD,Actor_POB, Gender,Citizenship, wiki_occupation,
		#Work_period_start,twitterid,instaid,wiki_family_name,Work_period_end,Height,Star_Sign,Ethnic_group,wiki_spouse_name,Child_Name,Father_Name, Mother_Name,Wiki_commons_category,wiki_siblings,Relatives,Signature_image) %}
		'IMDB_id':row.IMDBid.values[0],
		'Image':Image,
		# 'Name_in_native_languageinfo': Name_in_native_languageinfo,
		'twitterid':row.twitterid.values[0],
		'instaid':row.instaid.values[0],
		'Actor_POB': Actor_POB,
        'Genderinfo':Genderinfo,
		'Signature_image':Signature_image,
		'Work_period_start':Work_period_start,
		'Wiki_commons_category':row.Wiki_commons_category.values[0],
		'Work_period_end':Work_period_end,
		'wiki_occupation': filmo_occupationinfo,
		'Height': Height, 
		'Star_Sign': Star_Sign,
		'Ethnic_group': Ethnic_group,
		'wiki_spouse_name': wiki_spouse_name,

		#{%- macro career(IMDB_id,name,wiki_data_id,occup,occup1_num,occup2_num,occup3_num,occup4_num,debut_films,debut_filmseng,latest_films,latest_filmseng,Gender,occuplen) -%}
		
		'wiki_data_id':row.wiki_data_id.values[0],
		'occuplen':len(occup_clean(row.English_filmo_all_film_ocupations.values[0],row)),
		'occup': filmo_all_film_ocupations,
		'English_occup':clean1(row.English_filmo_all_film_ocupations.values[0]),
		'English_filmo_all_film_ocupations': clean1(row.English_filmo_all_film_ocupations.values[0]),
		'debut_films':debut_filmst,
		'debut_filmseng':debut_filmseng,
		'latest_filmseng':latest_filmseng,
		'latest_films': latest_filmst,
		'facebookid':row.facebookid.values[0],
        #{{- filmo(filmo_occupation,filmo_all_film_ocupations,latest_films,occup1_num,occup1_films,occup2_num,occup2_films,occup3_num,occup3_films,occup4_num,occup4_films,occup1_filmseng,occup2_filmseng,occup3_filmseng,occup4_filmseng,debut_films) -}}
        #{{- data(No_of_Awards) -}}
        #{{- n(Name) -}}
        #{{- awards(Year_Of_The_Award,Award_Outcome,Award_Category,Award_Categoryeng,Award_Description) -}}
		'Award_Now':Award_Now,
		'Award_Non':Award_Non,
        'Year_Of_The_Award':Year_Of_The_Award,
        'Award_Outcome':Award_Outcome,
        'Award_Category':Award_Category,
        'Award_Categoryeng':Award_Categoryeng,
        'Award_Description':Award_Description,
        'Award_Descriptioneng':Award_Descriptioneng,
        'No_of_Awards':No_of_Awards,
        'occup1_films':filmo1,
        'occup1_filmseng':filmo1_1,
        'occup2_films':filmo2,
        'occup2_filmseng':filmo2_1,
        'occup3_films':filmo3,
        'occup3_filmseng':filmo3_1,
        'occup4_films':filmo4,
        'occup4_filmseng':filmo4_1,
        'filmo_occupationfilmo':filmo_occupationfilmo,
        'filmo_all_film_ocupations_filmo':filmo_all_film_ocupations_filmo,
        'latest_films_filmo':latest_films_filmo,
        'debut_films_filmo':debut_films_filmo,
        'sam':sam,
        'san':san,
        'ran':ran,
        'man':man,
        'length':length,
		'wiki_DOB_year':wiki_DOB_year,
		'Knownfor': Knownfor,
		'Knownforlength': Knownforlength,
		'lenintro':lenintro,
		'careercsentence':careercsentence,
		'lencareer':lencareer,
		'infoocup' :infoocup
		



	}
	return data
def main():
	file_loader = FileSystemLoader('/Users/sameersanam/m/new')
	#env = Environment(loader=file_loader)
	env = Environment(extensions=['jinja2.ext.loopcontrols'],loader=file_loader)
	#env = Environment(loader=file_loader)
	template = env.get_template('template29 (1).j2')
	moviesDF =pickle.load(open('/Users/sameersanam/m/telengfin7_7.pkl', 'rb'))
	#id=moviesDF.loc[1]
	#data=getData(id)
	#text=template.render(data)




	ids = moviesDF.IMDBid.tolist()
	ids =ids[849:850] #remove this to generate articles for all movies
#1345 ra
	# Initiate tfile object
	# fobj = io.open('movies.xml', 'w',encoding="utf-8")
	# fobj.write(tewiki+'\n')

	for i, movieId in enumerate(ids):
		row = moviesDF.loc[moviesDF['IMDBid']==movieId]
		text = template.render(getData(row))

		#writePage(text, fobj)

		# print(i)
		# print(text, '\n')
		t = open("x.txt","w")
		t.write(text)
	
		


	#fobj.write('</mediawiki>')
	#fobj.close()

if __name__ == '__main__':
	main()
	
	
