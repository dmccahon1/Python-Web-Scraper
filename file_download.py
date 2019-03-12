#Script:    File Comparison
#Script     File Download   
#Desc:      Download a file from URL to specified directory
#Author:    David McCahon(40214392)
#Reference: http://stackoverflow.com/questions/19602931/basic-http-file-downloading-and-saving-to-disk-in-python
#

from webpage_analysis import file_get
import sys
import os
from email_analysis import wget



def file_download(file_url, directory):
    '''Downloads files found on webpage and writes to given directory'''
    #Gets the filenames and urls from a dictionary
    if not os.path.exists(directory):    #If directory doesnt exist, then create directory
        os.makedirs(directory)
    downSuccess = []
    
    try:
        print "[!]  Downloading files to: "+directory
        for filename in file_get(file_url):
            #print filename
            cleanFile = os.path.basename(filename)      #Strip urls of their filename
            with open(directory+cleanFile, 'wb') as location:             #Opens directory plus filename to be written to as binary
                location.write(wget(filename))                            #Writes contents of file to directory
                downSuccess.append(location)
        print "     %s" % len(downSuccess)+" Files have been successfully downloaded"
        
    except:
        print "Failure to download file %s" % cleanFile
        

def main():
    sys.argv.append(r'http://www.soc.napier.ac.uk/~40001507/CSN08115/cw_webpage')
    searchDirectory = ("C://temp//coursework//")
                  
    file_download(sys.argv[1], searchDirectory)

    #check args
if __name__ == '__main__':
    main()


    
