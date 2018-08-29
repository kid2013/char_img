

import cv2 as cv
import numpy as np
import os, sys



def readfile2list(ifile):
    img_list = []
    with open(ifile, 'r') as lf:
        img_list = [l.strip() for l in lf]
    return img_list


def get_bg( bg_path ) :
    """
         get back image  list from directory bg_path
    Args
             bg_path : a directory only contains back ground images
    Return
              a list of back ground images

    """
    if bg_path is None :
        return []
    bg_list = readfile2list(bg_path)
    bg_img_list = []
    for ipath in bg_list :
        bg_img = cv.imread(ipath)
        bg_img_list.append(bg_img)
    return bg_img_list


def add_bg(image, bg_img_list) :
    """
       add back ground to the image

       Args
                image :   image to add back ground
                bg_img_list :  a list of back ground images

        Return
                an image with back ground added

    """
    img = image.copy()
    num = len(bg_img_list)
    idx = np.random.randint(num, size = 10)[0]
    bg_img = bg_img_list[idx].copy()
    bg_img = gamma_trans(bg_img, ga = 2)
    (h, w, _) = img.shape
    bg_img =  cv.resize(bg_img, (w, h))
    alpha = np.random.random_sample()*0.3 + 0.1
    img = img*(1-alpha) + bg_img*alpha
    return img.astype(np.uint8)

def gamma_trans(image,  ga = 100):
    """
           take gamma transform on the image

    """
    ga_list = [0.3, 0.5, 0.7, 0.9, 1.5, 2, 2.5, 3]
    idx = np.random.randint(8, size = 10)[0]
    img = image.copy()
    img = img.astype(np.float32)
    img /= 255.0
    if ga == 100 :
        img **= ga_list[idx]
    else :
        img **= ga
    img *= 255
    img = img.astype(np.uint8)
#    print 'gamma_trans  '  , ga_list[idx]
    return img


def erode_img(image) :
    img = image.copy()
    kernel = np.ones((3,3), np.uint8)
    # num = np.random.randint(1, 4, size = 10)[0]
    num = 1
    img = cv.erode(img, kernel, iterations = num)
#    print 'erode' , num
    return img


def dilate_img(image) :
    img = image.copy()
    kernel = np.ones((3,3), np.uint8)
    # num = np.random.randint(1, 4, size = 10)[0]
    num = 1
    img = cv.dilate(img, kernel, iterations = num)
#    print 'dilate' , num
    return img


def pers_trans(image):
    """
              take perspective transform on the image

    """
    offset_list = [10, 20, 30]
    idx1 = np.random.randint(3, size = 10)[0:2]
    idx2 = np.random.randint(3, size = 10)[2:4]
    idx3 = np.random.randint(3, size = 10)[4:6]
    idx4 = np.random.randint(3, size = 10)[6:8]
    offset1 = offset_list[idx1[0]]
    offset2 = offset_list[idx2[0]]
    offset3 = offset_list[idx3[0]]
    offset4 = offset_list[idx4[0]]
    img = image.copy()
    ori_shape = img.shape[:-1][::-1]
    img = cv.resize(img, (300, 300))
    pt1 = [[0, 0], [0, offset1], [offset1, 0]]
    pt2 = [[300, 0], [300-offset2, 0], [300, offset2]]
    pt3 = [[300, 300], [300, 300-offset3], [300-offset3, 300]]
    pt4 = [[0, 300], [offset4, 300], [0, 300-offset4]]
    pts0 = np.float32([[0, 0], [300, 0],   [300, 300], [0, 300]])
    pts1 = np.float32([pt1[idx1[1]], pt2[idx2[1]], pt3[idx3[1]], pt4[idx4[1]]])
    M = cv.getPerspectiveTransform(pts1, pts0)
    dst = cv.warpPerspective(img, M, (300, 300))
    dst = cv.resize(dst, ori_shape)
#    print 'pers_trans', offset1, offset2, offset3, offset4
    return dst


def gray_compre(image):
    """
             intensity compresses

    """
    p_list = [120, 140, 160, 180, 200, 220]
    c_list = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
    idx = np.random.randint(6, size = 10)
    img = image.copy().astype(np.float32)
    p = p_list[idx[0]]
    c = c_list[idx[-1]]
    b_arr = img > p
    img[b_arr] *=  c
    img[b_arr] += p*(1-c)
    img = img.astype(np.uint8)
#    print 'gray_compre', p, c
    return img

def crop(image):
    img =  image.copy()
    ori_shape = img.shape[:-1][::-1]
    img = cv.resize(img, (300, 300))
    x_s = y_s = [0, 15]
    x_idx  = np.random.randint(2, size = 10)[0]
    y_idx  = np.random.randint(2, size = 10)[9]
    x = x_s[x_idx]
    y = y_s[y_idx]
    l = 285
    img = img[x:x+l][y:y+l]
    img = cv.resize(img, ori_shape)
#    print 'crop', x, y
    return img


def motblur(image):
    img = image.copy()
    col = img.shape[1]
    offset = np.random.randint(low = 1, high = 3, size = 10)[0]
    l_r = np.random.randn(10)[0] > 0
    if l_r :
        tmp = img[:, :col-offset]
        img[:, offset:] = (img[:, offset:] + tmp) /2
    else :
        tmp = img[:, offset:]
        img[:,:col-offset] = ( img[:,:col-offset] + tmp ) / 2
#    print 'motblur', offset
    return img


def down_blur(image):
    img = image.copy()
    ori_shape = img.shape[:-1][::-1]
    (w, h) = ori_shape
    img = cv.resize(img, (w/2, h/2))
    img = cv.resize(img, (w*2, h *2))
    img = cv.resize(img, (w/2, h/ 2))
    img = cv.resize(img, ori_shape)
#    print 'down_blur'
    return img


def blur(image):
    """
           blur an image

    """
    img = image.copy()
    idx = np.random.randint(4, size = 10)[0]
    if idx == 0 :
        return motblur(img)
    elif idx == 1 :
        return down_blur(img)
    elif idx == 2 :
#        print 'blur'
        return cv.blur(img, (5, 5))
    else :
#        print 'gaussian blur'
        return cv.GaussianBlur(img, (5, 5), 0)


def GaussianNoise(image) :
    img = image.copy()
    mu = 0
    sigma = 0.01
    noise = np.random.normal(mu, sigma, img.shape)
    img = img.astype(np.float32)
    img /= 255.0
    img += noise
    img *= 255
    img = np.clip(img, 0, 255)
    img = img.astype(np.uint8)
#    print "Gauss"
    return img


def WriteNoise(image, x_cood, y_cood, noise) :
    img = image.copy()
    img = img.astype(np.float32)
    img /= 255.0
    x_low, x_high, y_low, y_high = 0, img.shape[0], 0, img.shape[1]
    for idx, x in enumerate(x_cood) :
        y = y_cood[idx]
        p = noise[idx]
        x_list = [x-1, x, x+1]
        y_list = [y-1, y, y+1]
        img[x, y] = p
        num = 9
        n_idx = np.random.randint(2, size = num)
        for i in xrange(num) :
            if n_idx[i] > 0 :
                x_i = x_list[ i / 3]
                y_i = y_list[ i % 3]
                if x_i >= x_low and x_i < x_high and y_i >= y_low and y_i < y_high :
                    if np.random.randn() > 0 :
                        img[x_i, y_i] = p
    img *= 255
    img = np.clip(img, 0, 255)
    img = img.astype(np.uint8)
    return img


def PeperNoise(image) :
    img = image.copy()
    (rows, cols) = img.shape[:-1]
    point_num = (rows * cols) / 60
    x_cood = np.random.randint(rows, size = point_num )
    y_cood = np.random.randint(cols, size = point_num )
    mu = 0.8; sigma = 0.03
    noise = sigma*np.random.random(point_num) + mu
    img = WriteNoise(img, x_cood, y_cood, noise)
#    print "pep"
    return img


def noise(image) :
    """
         add noise to an image

    """
    img = image.copy()
    idx  = np.random.randint(3, size = 10)[0]
    if idx == 0 :
        return GaussianNoise(img)
    elif idx == 1 :
        return PeperNoise(img)
    else :
        img = GaussianNoise(img)
        return  PeperNoise(img)


def line(image) :
    """
          add an virtual line to an image so that intensity on one side ot the line
               increases and the other side decreases

    """
    img = image.copy()
    slope_list =[3, 2, 1, 0, 0, 0.5, 0.33]
    slope_idx = np.random.randint(7, size = 10)[0]
    slope = slope_list[slope_idx]
    flag = np.random.randn() > 0
    if flag :
        slope *= -1
    (h, w) = img.shape[:-1]
    bias = -w*0.5 - slope*h*0.5 + np.random.randint(-3, 4, size = 10)[0]
    area = lambda x, y : x + slope*y + bias > 0
    if flag and slope == 0 :
        area = lambda x, y : y + bias > 0
    inc = np.random.randint(30, size = 10)[0]
    dec = np.random.randint(30, size = 10)[0]
    for i in xrange(h) :
        for j in xrange(w) :
            if area(i, j) >  0 :
                img[i, j] += inc
            else :
                img[i, j] -= dec
    img = img.astype(np.uint8)
#    print 'line' , slope, bias, inc, dec
    return img


def rotate_trans(image,  bg_list) :
    """
       rotate an image, fill with back ground image after rotation

    """
    img = image.copy()
    img += 5
    (w, h) = img.shape[:-1][::-1]
    angle = np.random.randint(-15, 16, size = 10)[0]
    M = cv.getRotationMatrix2D((w/2, h/2), angle, 1)
    dst = cv.warpAffine(img, M, (w, h))
    length = len(bg_list)
    idx = np.random.randint(length, size = 10)[0]
    bg = bg_list[idx]
    bg = cv.resize(bg, img.shape[:-1][::-1])
    bg += 5
    mask = dst == 0
    dst[mask] = bg[mask]
    dst -= 5
    dst = dst.astype(np.uint8)
#    print 'rotate', angle
    return dst


def mor_trans(image) :
    """
     morphsim transform

    """
    img = image.copy()
    case = np.random.randint(4, size = 10)[0]
    kernel = np.ones((3,3), np.uint8)
    if case == 0 :
        return cv.erode(img, kernel)
    elif case == 1 :
        return cv.dilate(img, kernel)
    elif case == 2 :
        img = cv.erode(img, kernel)
        return cv.dilate(img, kernel)
    else :
        img = cv.dilate(img, kernel)
        return cv.erode(img, kernel)

def is_single_color(image) :
    img = image.copy()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    sigma = np.std(img)
    return sigma < 1e-8


def img_trans(img, img_op,  bg_file = None, is_add = False):
    """
        take image transform based on the img_op parameter
    Args
             img:  on which to take image transform
             img_op : a string, transform type
    Return
             return an image with image transform taken on

    """
    bg_img_list = get_bg(bg_file)
    # img = cv.imread(img_file)
    if img is None :
            print 'image doesn\'t exist'
            return None
    # if is_single_color(img) :
    #     print 'image is single color'
    if is_add :
        img = add_bg(img, bg_img_list)
    if img_op == 'gamma' :
        img = gamma_trans(img)
    elif img_op == 'pers' :
        img = pers_trans(img)
    elif img_op == 'crop' :
        img = crop(img)
    elif img_op == 'blur' :
        img = blur(img)
    elif img_op == 'noise' :
        img = noise(img)
    elif img_op == 'line' :
        img =line(img)
    elif img_op == 'mor' :
        img = mor_trans(img)
    elif img_op == 'None' :
        pass
    else :
        print 'Not implemention'
    # cv.imwrite(img_file, img)
    return img



