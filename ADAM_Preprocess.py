# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:11:38 2020

@author: MA
"""

import os
join = os.path.join
import argparse
import shutil

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", required=False, help="input path")
    parser.add_argument("--save_path", default="./input_preprocess", help="save path")
    args = parser.parse_args()
    
    input_path = args.input_path
    save_path = args.save_path
    
    if os.path.exists(save_path) is False:
        os.mkdir(save_path)



    shutil.copyfile(join(join(input_path, "pre"),"TOF.nii.gz"), join(save_path, 'TOF_0000.nii.gz'))
    print(" preprocess finished!")
    
if __name__ == "__main__":
    main()