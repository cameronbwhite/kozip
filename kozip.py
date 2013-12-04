#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# this script supports shift-jis and euc-kr encodings (basically, Microsoft's Korean and Japanese encoding.)

# reference:    

    #if sys.version_info < (3, 0):
        
        #info.filename =  bytes(info.filename,lang).encode('utf-8')
    #else:
        #info.filename =  info.filename.decode(lang).encode('utf-8')
# that bit of code was given to me by slaveriq on the jupiter broadcasting irc. I'll make tha the base of the future rewrite.

import sys, os, zipfile

def unzip(file, dir, lang):
    if dir is None:
        dir = os.path.splitext(file)[0]
        os.mkdir(dir)
    else:
        os.mkdir(dir)

    if lang == None:
        lang = 'euc-kr'
    elif lang == jap:
        lang = "shift-jis"
    elif lang == kor:
        lang == 'euc-kr'
    else:
        print("please choose 'kor' or 'jap' as languages.")
        exit()

    zfobj = zipfile.ZipFile(file)
    for info in zfobj.infolist():
        #info.filename =  info.filename.decode(lang).encode('utf-8')
        
        zfobj.extract(info, dir)
        printing="extracting "

        print(printing+info.filename)

if __name__ == '__main__':
    argc = len(sys.argv)

    if argc == 1:
        print('Usage: {0} file [exdir] [lang]'.format(sys.argv[0]))
    elif argc == 2:
        unzip(sys.argv[1], None, None)
    elif argc == 3:
        unzip(sys.argv[1], sys.arv[2], None)
    elif argc == 4:
        unzip(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print('Usage: {0} file [exdir] [lang]'.format(sys.argv[0]))
