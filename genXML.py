import string
import random
from hashlib import sha1
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

tewiki = '''<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.10/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.10/ http://www.mediawiki.org/xml/export-0.10.xsd" version="0.10" xml:lang="te">
	<siteinfo>
		<sitename>tewiki</sitename>
		<dbname>indicwiki</dbname>
		<base>https://tewiki.iiit.ac.in/index.php/%E0%B0%AE%E0%B1%8A%E0%B0%A6%E0%B0%9F%E0%B0%BF_%E0%B0%AA%E0%B1%87%E0%B0%9C%E0%B1%80</base>
		<generator>MediaWiki 1.34.0</generator>
		<case>first-letter</case>
		<namespaces>
			<namespace key="-2" case="first-letter">మీడియా</namespace>
			<namespace key="-1" case="first-letter">ప్రత్యేక</namespace>
			<namespace key="0" case="first-letter" />
			<namespace key="1" case="first-letter">చర్చ</namespace>
			<namespace key="2" case="first-letter">వాడుకరి</namespace>
			<namespace key="3" case="first-letter">వాడుకరి చర్చ</namespace>
			<namespace key="4" case="first-letter">Project</namespace>
			<namespace key="5" case="first-letter">Project చర్చ</namespace>
			<namespace key="6" case="first-letter">దస్త్రం</namespace>
			<namespace key="7" case="first-letter">దస్త్రంపై చర్చ</namespace>
			<namespace key="8" case="first-letter">మీడియావికీ</namespace>
			<namespace key="9" case="first-letter">మీడియావికీ చర్చ</namespace>
			<namespace key="10" case="first-letter">మూస</namespace>
			<namespace key="11" case="first-letter">మూస చర్చ</namespace>
			<namespace key="12" case="first-letter">సహాయం</namespace>
			<namespace key="13" case="first-letter">సహాయం చర్చ</namespace>
			<namespace key="14" case="first-letter">వర్గం</namespace>
			<namespace key="15" case="first-letter">వర్గం చర్చ</namespace>
			<namespace key="120" case="first-letter">Item</namespace>
			<namespace key="121" case="first-letter">Item talk</namespace>
			<namespace key="122" case="first-letter">Property</namespace>
			<namespace key="123" case="first-letter">Property talk</namespace>
			<namespace key="482" case="first-letter">Config</namespace>
			<namespace key="483" case="first-letter">Config talk</namespace>
			<namespace key="710" case="first-letter">TimedText</namespace>
			<namespace key="711" case="first-letter">TimedText talk</namespace>
			<namespace key="828" case="first-letter">మాడ్యూల్</namespace>
			<namespace key="829" case="first-letter">మాడ్యూల్ చర్చ</namespace>
			<namespace key="2300" case="first-letter">Gadget</namespace>
			<namespace key="2301" case="first-letter">Gadget talk</namespace>
			<namespace key="2302" case="case-sensitive">Gadget definition</namespace>
			<namespace key="2303" case="case-sensitive">Gadget definition talk</namespace>
			<namespace key="2600" case="first-letter">Topic</namespace>
			<namespace key="3022" case="first-letter">Tewiki</namespace>
			<namespace key="3023" case="first-letter">Tewiki talk</namespace>
		</namespaces>
	</siteinfo>\n'''


def sha36(page_id):
	page_id = str(page_id).encode('utf-8')
	sha16 = sha1(page_id).hexdigest()
	sha10 = int(sha16, 16)
	chars = []
	alphabets = string.digits + string.ascii_lowercase
	while sha10 > 0:
		sha10, r = divmod(sha10, 36)
		chars.append(alphabets[r])
	
	return ''.join(reversed(chars))

def addPage(title, page_id, username, user_id, wikitext):
    page_length = len(wikitext)
    time = datetime.now().strftime("%Y-%m-%dT%H-%M-%SZ")
    sha_text = sha36(page_id)
    page = """
	<page>
		<title>{}</title>
		<ns>0</ns>
		<id>{}</id>
		<revision>
			<id>{}</id>
			<timestamp>{}</timestamp>
			<contributor>
				<username>{}</username>
				<id>{}</id>
			</contributor>
			<comment>xmlpage created</comment>
			<model>wikitext</model>
			<format>text/x-wiki</format>
			<text xml:space="preserve" bytes="{}">
{}
			</text>
            <sha1>{}</sha1>
		</revision>
	</page>
""".format(title, page_id, page_id, time, username, user_id, page_length, wikitext, sha_text)
	
    return page