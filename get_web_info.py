#script:
#Script:    Get Web Info
#Desc:      Performs forensic analysis on a webpage
#           Gets URLs found from Webpage
#           Gets phone numbers and Hash from webpage
#Author:    David McCahon (40214392)
import sys
from webpage_getlinks import print_links
from email_analysis import analyse
from webpage_analysis import webOutput, crack
from file_hash import hash_compare, dir_hash
from file_download import file_download



def main():
    #Searching information
    sys.argv.append('http://www.soc.napier.ac.uk/~40001507/CSN08115/cw_webpage')
    passwordDic = (r'C:\Users\david\OneDrive\Documents\Digital_Security\yr2\Python\coursework_files/dict.txt')
    searchDir = (r'C:\temp\coursework\\')
    badHashes = (r'C:\Users\david\OneDrive\Documents\Digital_Security\yr2\Python\coursework_files\badHashes.txt')
    #sys.argv.append('https://www.facebook.com')
    #Find ips and email addresses
    analyse(sys.argv[1])
    print ""
    #Dictionary cracks passwords found on webpage
    crack(sys.argv[1], passwordDic)
    print ""
    #Gets urls from webpage
    print_links(sys.argv[1])
    #Gets Phone numbers & 
    #Gets files from webpage
    print ""
    webOutput(sys.argv[1])
    print ""
    #Shows successful file downloads
    file_download(sys.argv[1], searchDir)
    print ""
    #Compares downloded hashes to dictionary
    hash_compare(searchDir, badHashes)



     # Check args
    if len(sys.argv) != 2:
        print '[-] Usage: webpage_get URL'
        return
    

if __name__ == '__main__':
    main()
