# Script: file_hash.py
# Script: file_hash
# Desc:   Module which contains general hash usage functions
#         Generate file hash signature for files, and word per file
#         Finds hashes in a webpage or file
#         Hash files found in an entire directory and compare found hashes to a dictionary of hashes
# Author: David McCahon
# Reference: http://stackoverflow.com/questions/16193521/typeerror-expected-string-or-buffer
#

import sys, os
import hashlib
import re
import email_analysis
from webpage_get import wget
import email_analysis


def file_hash(filename):
    """prints a hex hash signature of the file passed in as arg"""
    try:
        #open file

        # Generate Hash Signature
            content = f.read()                                       #Reads content of file
            gen = hashlib.md5(content).hexdigest()                   #Hashes the contents of file
            print "[!] Hashing file...", filename                    #Outputs filename and its hash
            print '[+] Hash Generated...', gen

    except Exception as err:
        print '[-]', str(err)


def word_hash(filename):
    """prints a hex hash signature for every word in a file"""
    try:
        # Read File
       with open(filename) as f:                                    
           d = {}                                                   #Create empty dictionary
           for line in f:                                           #For line in the file and for word in the file, split on space
                for w in line.split(" "):
                     hsh = hashlib.md5(w).hexdigest()               #Hash the word and add to dictionary as {hash : word}
                     d[hsh] = w
                return d

    except Exception as err:
        print '[-]', str(err)    
        
def hash_get(txt):
    '''Find hash within a webpage or file'''
    pwd =[]                                                        #Create empty list to store hashes
    try:
        web = wget(txt)
        match = re.findall(r"[a-fA-F\d]{32}", web)                 #Find hashes using regex of any word, any number of length 32
    except:
        match = re.findall(r"[a-fA-F\d]{32}", open(txt, "r").read())
    match = set(match)                                              #Remove the duplicates
    match = list(match)
    pwd = pwd + match
    return pwd

def filehash_get(txt):
    '''Find hash within a webpage or file'''
    hashFind =[]                                                     #Create empty list to hold found hashes
    try:
        match = re.findall(r"[a-fA-F\d]{32}", open(txt, "r").read()) #Find hashes in file by regex any word, any num of length 32
        match = set(match)                                           #Remove duplicates
        match = list(match)
        hashFind = hashFind + match
        return hashFind
    except Exception as err:
        print '[-]', str(err)

def dir_hash(directory):
    '''Hash every file in a directory'''
    my_dict = {}                                                    #Create empty dictionary to store hash : path
    dirFiles = os.listdir(directory)
    print "[!] Hashing downloaded files"
    for files in dirFiles:                                          #For each file in directory
        fpath = directory+"\\"+files                                #Create path by adding filename to directory
        try:
            with open(fpath, 'rb') as open_file:                    #Open filename via its path by reading binary
                a = open_file.read()
                a = hashlib.md5(a).hexdigest()                      #Hash contents of fine
                my_dict[a] = fpath.split('\\')[-1]                  #Add hash & path to dictionary
                print "    "+a+" : "+files
        except IOError:
            print "dir_hash error"
    print ""
    return my_dict

def hash_compare(directory, badDictionary):
    '''Compares found hashes against a dictionary of badHashes'''
    badHash = hash_get(badDictionary)                           #Take list of bad hashes found in dictionary
    dirHash = dir_hash(directory)                                   #Takes dictionary of hashes of files from directory
    badFiles = set(dirHash).intersection(badHash)                   #Finds intersection of list and dictionary, finding common values between both
    print ("[!] %s" % len(badFiles) + " Bad Files have been recovered")
    for badFile in badFiles:
        print "   ", badFile
        print "    FilePath: " +  directory +"\\"+ dirHash[badFile] + "\n"
        

def main():
    #Cases
    sys.argv.append('http://www.soc.napier.ac.uk/~40001507/CSN08115/cw_webpage/')
    searchDir = (r'C:\temp\coursework')
    badHashes = (r'C:\Users\david\OneDrive\Documents\Digital_Security\yr2\Python\coursework_files\badHashes.txt')
    dictionary = (r'C:\Users\david\OneDrive\Documents\Digital_Security\yr2\Python\coursework_files\dict.txt')

    #Test Functions
    word_hash(dictionary)
    print ""
    hash_compare(searchDir, badHashes)    
    print ""
    filehash_get(badHashes)
    print ""
    dir_hash(searchDir)

    # Check args
    if len(sys.argv) != 2:
        print '[-] usage: file_hash filename'
        sys.exit(1)


if __name__ == '__main__':
    main()

