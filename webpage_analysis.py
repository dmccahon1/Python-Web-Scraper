#Script:    webpage_analysis
#Desc:      Finds phone numbers, Hash and Cracks Hash Passwords from webpage
#Author:    David McCahon (40214392)

import sys
from webpage_get import wget
from email_analysis import txtget
import re, os
from file_hash import filehash_get, hash_get, word_hash

def phone_get(txt):
    '''Finds phone numbers within a webpage or file'''
    phone =[]                                                                   #Create list to store found phone numbers
    try:
        p = wget(txt)                                                               
        match = re.findall(r"\+44\(\d\)\d{3}\s?\d{3}\s?\d{4}", p)                   #Matches phone numbers based on +44(0)123 123 1234 or +44(0)1234567891
    except:
        match = re.findall(r"\+44\(\d\)\d{3}\s?\d{3}\s?\d{4}", open(txt, "r").read())
    match = set(match)                                                          #Removes duplicates
    match = list(match)
    phone = phone + match
    return phone


def file_get (txt):
    '''Finds png, jpeg, .docx and gif files from a webpage'''
    fileFound =[]                                                              #Creates list to store found files on webpage
    web = wget(txt)                                                            #Finds files in webpage, finds jpgs, gifs, bmp, php and docx
    image = re.findall(r"\<(img\ssrc.*.jpg)", web)          
    gif = re.findall(r"\<(img\ssrc.*.gif)", web)
    doc = re.findall(r"\<(a\shref.*.docx)", web)
    php = re.findall(r"\<(a\shref.*.php)", web)
    bmp = re.findall(r"\<(img\ssrc.*.bmp)", web)
    fileFound = fileFound + image + gif + doc + php + bmp                      #Empty lists to hold cleaned items and completed files
    lstCleansed = []                                                           #List to hold found files of their html tags
    fileList = []                                                              #List to hold cleaned files plus their url
	
    for item in fileFound:                                                     
        #remove tags, clean output        
        raw =re.sub(r'img\ssrc="|a\shref="',"", item)                          #Remove html tags
		#append cleaned item to list
        lstCleansed.append( raw );                                             #Add cleaned files to lstCleaned list
        #add url to filename with not present, allows for download from web
        if "https" not in doc and "http" not in raw:                           #If file url not present, add the file url, otherwise add found fileurl
            complete=txt+"/"+raw
            fileList.append(complete)
        else:
            fileList.append(raw)
    return fileList


def crack(txt, dictionary):
    '''Cracks passwords using a dictionary of possible passwords'''
    found = hash_get(txt)                                               #Get a list of hashes found on webpage
    poss = word_hash(dictionary)                                        #Hash every word in comparison dictionary
    cracked = set(poss).intersection(found)                             #If hash is in found & poss, then a match has been found
    print '[!]', len(cracked), 'Passwords have been found:'
    for match in cracked:
        if match in poss:
            print '   ', match
            print '    Password recovered: ',poss[match] ,'\n'
    return match

def webOutput(txt):
    '''Function solely for a cleanout of files and phones found'''
    fileGet = file_get(txt)
    phoneGet = phone_get(txt)
    print '[!]', len(phoneGet), 'Phone Numbers Found:'
    for line in phoneGet:
        print "    %s" % line
    print ""
    print '[!]', len(fileGet), 'Files Found:'
    for line in fileGet:
        print "    " + line
    
def main():
    sys.argv.append('http://www.soc.napier.ac.uk/~40001507/CSN08115/cw_webpage/')
    passDictionary = (r'C:\Users\david\OneDrive\Documents\Digital_Security\yr2\Python\coursework_files/dict.txt')
    crack(sys.argv[1], passDictionary)
    webOutput(sys.argv[1])
    file_get(sys.argv[1])
    print ""


if __name__ == '__main__':
    main()
