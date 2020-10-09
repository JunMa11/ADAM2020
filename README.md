# README

> 1st Place Solution to MICCAI 2020 ADAM Challenge in Segmentation Task.

## Step 1. Prepare input data and running environment

Put input data into the folder `input`. The folder structure should be 

```python
input
——10001
————orig
——————struct.nii.gz
——————...
————pre
——————TOF.nii.gz # we only use the preprocessed TOF data
——————...
```

Run 

> python 3.7.6; pytorch 1.5.0; cuda 10.1

```python
cd nnUNet
pip install -e .
cd ..
# preprocess
python ADAM_Preprocess.py --input_path ./input
cd nnUNet/nnunet
```

## Step 2. Inference

Download the trained models: [link](https://pan.baidu.com/s/176J6mS8dx89Nbht5EaeYEg ) (PW: b9oo), and put it in the `ADAM2020/nnUNet/nnunet/TrainedModels/nnUNet/3d_fullres`

Run

```python
nnUNet_predict -i ../../input_preprocess -o ../../seg_initial -m 3d_fullres -t Task600_ADAM --disable_tta
cd ../../
```

```python
# postprocess
python ADAM_Postprocess.py --save_path ./output
```

The final segmentation results are in the folder `output`.

