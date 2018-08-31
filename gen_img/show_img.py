"""

the main function of this file is to show image by index list in selected npz file


"""
# -*- coding: utf-8  -*-
import numpy as np
import os
import shutil
import string
import sys
import codecs
import cv2 as cv
import matplotlib.font_manager as mfm
import matplotlib.pyplot as plt
from config import common_cfg, show_img_cfg
import pdb



def show_img_by_idx(img_arr, idx_list , npz_file , index_name_list) :
    """
    this function is used to show a list of images stored in the npz file

    Args
             img_arr :   an numpy array of image with shape NxHxWxC, element type np.uint8
             idx_list :    a list of index for the seleted images, should be in  the range of 0, ... , N - 1
             npz_file:    a string object, the name of the file storing images on disk
             index_name_list:  a list of index-name pair of char, used to title the figure plotted

    """
    # pdb.set_trace()
    N = img_arr.shape[0]
    font_name = os.path.join(common_cfg['font_libs'], 'simkai.ttf')
    myfont = mfm.FontProperties(fname = font_name)
    for idx in idx_list :
        if idx < 0 or idx >= N :
            print 'index {0:5d} is out of range'.format(idx)
            # os.exit(1)
            continue


        print 'now print the {0:5d}-th image in file {1!s}.'.format(idx, str(npz_file))
        index_name = index_name_list[idx]
        index, name= string.split(index_name, u'_')
        index = int(index)
        # check index
        if index != idx :
            print  'image and char are miss aligned'
            continue
        img = img_arr[idx]
        shape = img.shape[:-1]
        plt.title(index_name, fontproperties =  myfont)
        plt.imshow(img, interpolation = 'bicubic', shape = shape)
        plt.show()
    #    cv.imwrite(str(index)+'.jpg', img)


if __name__ == '__main__' :
    npz_dir = os.path.join(common_cfg['results_dir'],  show_img_cfg['generation_name'])
    npz_file = show_img_cfg['generation_name'] + '.npz'
    idx_list = show_img_cfg['idx_list']
    # pdb.set_trace()
    print 'it takes a minute to load the numpy object...'
    #==========================================
    #    load the npz file here
    #==========================================
    img_arr = np.load(os.path.join(npz_dir, npz_file))['arr_0']
    #==========================================
    #    load the char index name file
    #==========================================
    file_path = os.path.join(npz_dir, common_cfg['char_index_name'])
    fr =  codecs.open(file_path, 'r', 'utf-8')
    index_name_list = [b.strip() for b in fr]
    fr.close()

    show_img_by_idx(img_arr, idx_list, npz_file, index_name_list)
