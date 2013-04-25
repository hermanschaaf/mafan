"""
This file allows you to separately download large dictionary 
files for use with Mafan, if you would find it necessary.

These files can be rather large, so they don't come with the 
default mafan distribution.
"""
import os
import urllib2

from os.path import basename
from urlparse import urlsplit

def url2name(url):
    return basename(urlsplit(url)[2])


def download(url, localFileName = None, localDirName = None):
    """
    Utility function for downloading files from the web 
    and retaining the same filename.
    """
    localName = url2name(url)
    req = urllib2.Request(url)
    r = urllib2.urlopen(req)
    if r.info().has_key('Content-Disposition'):
        # If the response has Content-Disposition, we take file name from it
        localName = r.info()['Content-Disposition'].split('filename=')
        if len(localName) > 1:
          localName = localName[1]
          if localName[0] == '"' or localName[0] == "'":
              localName = localName[1:-1]
        else:
          localName = url2name(r.url)
    elif r.url != url: 
        # if we were redirected, the real file name we take from the final URL
        localName = url2name(r.url)
    if localFileName: 
        # we can force to save the file as specified name
        localName = localFileName
    if localDirName:
        # we can also put it in some custom directory
        if not os.path.exists(localDirName):
          os.makedirs(localDirName)
        localName = os.path.join(localDirName, localName)

    f = open(localName, 'wb')
    f.write(r.read())
    f.close()


def download_traditional_word_list():
  """
  Download Jieba big dictionary for splitting and classifying 
  both traditional and simplified Chinese texts.
  """

  url = 'https://raw.github.com/fxsjy/jieba/master/extra_dict/dict.txt.big'
  download(url, localDirName='data')

if __name__ == '__main__':
  confirm = raw_input("You are about to download all dictionary files. Could be up to 50MB in total. Are you sure?\n (y/n) ")
  if confirm == 'y' or confirm == 'yes':
      download_traditional_word_list()