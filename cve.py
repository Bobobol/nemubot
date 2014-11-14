import urllib.request
from bs4 import BeautifulSoup
import pprint
from hooks import hook
from more import Response

nemubotversion = 3.4

def help_tiny():
  return "CVE description"

def help_full():
  return "No help "


@hook("cmd_hook", "cve")
def get_cve_desc(msg):
  DESC_INDEX = 17
  BASEURL_MITRE = 'http://cve.mitre.org/cgi-bin/cvename.cgi?name='

  search_url = BASEURL_MITRE + msg.cmds[1]
 # print (search_url)
  url = urllib.request.urlopen(search_url)
  soup = BeautifulSoup(url)
#print (soup)
  desc = soup.body.findAll('td')
  i = 0
  return Response(desc[DESC_INDEX].text, msg.channel)

