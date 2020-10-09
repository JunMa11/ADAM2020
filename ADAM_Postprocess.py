# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:11:38 2020

@author: MA
"""

import os
join = os.path.join
import argparse
import nibabel as nib
import numpy as np
import shutil

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", default="./seg_initial", help="input path")
    parser.add_argument("--save_path", required=False, help="save path")
    args = parser.parse_args()
    
    input_path = args.input_path
    save_path = args.save_path
    if os.path.exists(save_path) is False:
        os.mkdir(save_path)
        

    

    nii = nib.load(join(input_path, 'TOF.nii.gz'))
    seg = nii.get_fdata()
    num_voxels = np.sum(seg)
    print(" voxels:", np.sum(seg))
    if num_voxels<11:
        new_seg = np.zeros_like(seg)
        nib.save(nib.Nifti1Image(new_seg, nii.affine, nii.header), join(save_path, 'output.nii.gz'))
        
    else:
        shutil.copyfile(join(input_path, 'TOF.nii.gz'), join(save_path, 'output.nii.gz'))
    
if __name__ == "__main__":
    main()