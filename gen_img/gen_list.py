#coding:utf-8

import os, sys
import pdb
from config import  gen_list_cfg



def get_all_char_list():
    """
             this function reads a char set from a file and produces 
             a list of char 

    """
    # pdb.set_trace()
    #=========================================
    #                          char set file
    #=========================================
    file0 = gen_list_cfg['char_source_file']
    char_str0 = read(file0).replace('\n', '').replace(' ', '').replace('\r', '')
    #=========================================
    #                          add the 'space'   char
    #=========================================
    char_str0 =  u' ' +  char_str0
    char_list = list(char_str0)
    return char_list


def read(txtfile):
    txtfile = UNICODE(txtfile)
    f = open(txtfile, 'r')
    txt = f.read()
    f.close()
    txt = UNICODE(txt)
    txt = remove_BOM(txt.encode('utf-8'))
    txt = txt.decode('utf-8')
    return txt

def UNICODE(str):
    if type(str).__name__ == 'unicode':
        return str
    try:
        decode = str.decode('utf-8')
    except:
        try: decode = str.decode('gbk')
        except: decode = ''
    return decode

def check_BOM(str):
    length = len(str)
    if length >= 3:
        if str[0:3] == '\xef\xbb\xbf':
            return True
    return False

def remove_BOM(str):
    if check_BOM(str):
        return str[3:]
    return str



if __name__ == '__main__' :
    # file0 = 'chn.txt'
    # file1 = 'eng.txt'
    get_all_char_list()
