#!coding: utf-8

import os
from PIL import Image

def get_pic_list():
	dirpath = os.path.dirname(os.path.abspath(__file__))
	files = os.listdir(dirpath+"/images/prof/new/")
	return files,dirpath

def conv_to_grayscale(infile, outfile):
    try:
        Image.open(infile).convert('L').save(outfile)
    except:
        print('cannot convert %s' % infile)

def main():
	p_list,dirpath=get_pic_list()
	for p in p_list:
	    conv_to_grayscale(dirpath+"/images/prof/new/"+p,dirpath+"/images/prof/"+p)

if __name__ == "__main__":
    main()