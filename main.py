from render29 import getData
from genXML import addPage, tewiki
import pickle
from jinja2 import Environment, FileSystemLoader 
moviesDF = pickle.load(open('/Users/sameersanam/m/telengfin6_7.pkl', 'rb'))
ids = moviesDF.IMDBid.tolist()
ids =ids[0:1000:50]
username = "Movieartists"
user_Id = "18104"
page_id = 9000001
XML = tewiki
for i, movieId in enumerate(ids):
    row  = moviesDF.loc[moviesDF['IMDBid']==movieId]
    artists = getData(row)
    file_loader = FileSystemLoader('/Users/sameersanam/m/new')
    env = Environment(extensions=['jinja2.ext.loopcontrols'],loader=file_loader)
    template = env.get_template('template29 (1).j2')
    text = template.render(artists)
    text = text.replace('&','&amp;')
    text = text.replace('<','&lt;')
    text = text.replace('>','&gt;')
    text = text.replace('"','&quot;')
    text = text.replace("'",'&apos;')
    XML = XML+addPage(artists["Name"],page_id,username,user_Id,text)
    page_id+=1
XML = XML+'</mediawiki>'
a = open("artists.xml","w")
a.write(XML)
a.close()