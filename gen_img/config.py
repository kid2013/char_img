# -*- coding: utf-8 -*-
"""
                                    important !!!
         this file contains  ALL configurations to produce npz file and show image

"""

import os
import pygame
import pdb

try:
    import pygame.freetype as freetype
except ImportError:
    print ("No FreeType support compiled")
    sys.exit ()

#==================================================
#                             font style
#==================================================
STYLES = {
    "style_normal"          :        freetype.STYLE_NORMAL,
    "style_underline"    :        freetype.STYLE_UNDERLINE,
    "style_oblique"         :        freetype.STYLE_OBLIQUE,
    "style_strong"           :        freetype.STYLE_STRONG,
    "style_wide"                 :        freetype.STYLE_WIDE,
    "style_default"         :        freetype.STYLE_DEFAULT
}


#==================================================
#
#                            common configuration
#
#==================================================
common_cfg = {
    #   font libs
    'font_libs' : '/home/algo/char_gen/RS_CHR01/resources/font_libs/',
    #   directory in which to write and read results of  generation
    'results_dir' : '/home/algo/char_gen/RS_CHR01/outputs/gbk2',
    #    file records all char index and name
    'char_index_name' : 'char_index_name.txt',
}


#==================================================
#
#                            configuration for gen_npz.py
#
#                                 attributes to produce char images
#                                 detailed explanation can be seen in function write_config  below
#
#==================================================

gen_npz_cfg = {

    # color is in (r, g, b) format
    'bg_color' : [(255, 255, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)],
    'fg_color' : [(0, 0, 0), (0, 0, 255), (0, 255, 0), (255, 0, 0)],
    # 'screen_color' : (255, 0, 0),
    # size should not be to large
    #'screen_size' :  (64, 64),
    'screen_size' :  (32, 32),
    'font' :  [ 'msyh.ttc', 'NotoSansCJK-Regular.ttc', 'simfang.ttf', 'simhei.ttf', 'simkai.ttf'],
    #'font_size' : (32, 32),
    'font_size' : (28, 28),
    # 'pos_x' : [0,  16,  32],
    'pos_x' : [2,  16,  32],
    # 'pos_y' : [0,  16,  32],
    'pos_y' : [2,  16,  32],
    'rotate' : 0,
    'style' :  ['style_normal', 'style_oblique', 'style_strong', 'style_wide', 'style_default'],
    # img_op is a string list, each string represents one transformation
    'img_op' : ['None',   'noise'],
    #   name for current generation
    'cur_generation_name' : 'GBK_',
}


#==================================================
#
#                            configuration for show_img.py
#
#==================================================
show_img_cfg = {

    #   index list, image at these indexes will be shown
    'idx_list' : range(20000, 20010),
    #   name for  generation to show
    'generation_name' : 'GBK_0000'
}


#==================================================
#
#                            configuration for gen_list.py
#
#==================================================
gen_list_cfg = {
    # char set source file to generate char_list
    'char_source_file' : '/home/algo/char_gen/RS_CHR01/emb_chars/chars/GBK.list',
}


#==================================================
#                             this function is  used to
#                             write configuration for one generation in a txt file
#==================================================

def write_config(args_dict, file_name) :
    """
    write configuration in file_name

    Args :
                 args_dict : configuration given by a dictionary
                 file_name : file name to write
    """
    bg_color = args_dict['bg_color']
    fg_color = args_dict['fg_color']
    screen_size = args_dict['screen_size']
    font = args_dict['font']
    font_size = args_dict['font_size']
    pos_x = args_dict['pos_x']
    pos_y = args_dict['pos_y']
    rotate = args_dict['rotate']
    style = args_dict['style']
    img_op = args_dict['img_op']
    char_file_name = os.path.basename(gen_list_cfg['char_source_file'])
    # pdb.set_trace()
    with open(file_name, 'w') as fw :
        wrt_str   =  '#################################################\n'  + \
              ' this is the configuration for the generated {!s}.npz file  '.format(args_dict['cur_generation_name']) + '\n' + \
              ' char file is : {!s}'.format(char_file_name) + '\n' + \
              '#################################################\n' + \
              '###  font backgroud color  ###' + '\n' + \
              'bg_color: {0:4d}, {1:4d}, {2:4d}'.format(bg_color[0], bg_color[1], bg_color[2]) + '\n' + \
              '###  font foreground color  ###' + '\n' + \
              '###  note that font foreground color should be same with canvas color  ###' + '\n' + \
              'fg_color: {0:4d}, {1:4d}, {2:4d}'.format(fg_color[0], fg_color[1], fg_color[2]) + '\n' + \
              '###  canvas size in pixel  ###' + '\n' + \
              'screen_size: {0:4d}, {0:4d}'.format(screen_size[0], screen_size[1]) + '\n' + \
              '### font name  ###' +'\n' + \
              'font: {!s}'.format(str(font)) + '\n' + \
              '###  font size in pixel  ###' + '\n' + \
              'font_size: {0:4d}, {0:4d}'.format(font_size[0], font_size[1]) + '\n' + \
              '###  char top-left x coordinate  ###' + '\n' + \
              'pos_x: {0:4d}'.format(pos_x) + '\n' + \
              '###  char top-left y coordinate  ###' + '\n' + \
              'pos_y: {0:4d}'.format(pos_y) + '\n' + \
              '###  rotation of the char in degree  ###' + '\n' + \
              'rotate: {0:4d}'.format(rotate) + '\n' + \
              '###  style for the font  ###' + '\n' + \
              'style: {!s}'.format(str(style)) + '\n' + \
              '### image operation taken on the char image  ###' + '\n' + \
              'img_op: {!s}'.format(str(img_op)) + '\n' + \
              '#################################################\n'
        fw.write(wrt_str)

