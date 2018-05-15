from lxml import etree
import urllib2

ns={"Atom" : "http://www.w3.org/2005/Atom"}
parser=etree.XMLParser()
tree=etree.parse(urllib2.urlopen('https://api.flickr.com/services/feeds/photos_public.gne?tags=sevilla'),parser)
for node in tree.xpath('//Atom:entry/Atom:title', namespaces=ns) :
   print node.text

