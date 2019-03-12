# Script:   webpage_get.py
# Script:   webpage get
# Desc:     Fetches data and urls from a webpage.
# Author:   David McCahon
# Created:  Oct, 16
#
import sys, urllib
import re
        
def wget(url):
    '''Gets url and displays webpage content'''
    # open url like a file, based on url instead of filename
    try:
        webpage = urllib.urlopen(url)                                       #Open url 
        page_contents = webpage.read()                                      #get webpage contents
        http_code = webpage.code                                            #Get htp code
        return page_contents
        
    except:
        raise

def print_links(page):
    """Find all hyperlinks on a webpage assed in as input and print"""
    # regex to match on hyperlinks, returning 3 grps,
    # links[1] being the link itself
    cont = wget(page)                                                     #Get contents of webpage
    links = re.findall(r'\<a.*href\=.*(?:http|https)\:.+', cont)          #Find urls in webpage by their html tags
    links = set(links)                                                  #Remove duplicates
    print '[!]', str(len(links)), 'Hyperlinks found:'
    for link in links:
        url = re.sub(r'<.*?"','', link)                                   #Remove html tags from urls to give clean output
        url = re.sub('".*?<.*?>',"", url)
        print '   ', url
        

def main():
    # temp testing url argument
    sys.argv.append('http://www.soc.napier.ac.uk/~40001507/CSN08115/cw_webpage')
    print_links(sys.argv[1])

    # Check args
    if len(sys.argv) != 2:
        print '[-] Usage: webpage_get URL'
        return

    # Get and analyse web page
    #print wget(sys.argv[1])

if __name__ == '__main__':
	main()
