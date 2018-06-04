# DORN: Deep Ordinal Regression Network for Monocular Depth Estimation

### Introduction
The shared code is a Caffe implemention of our CVPR18 paper (DORN). The provided caffe is not our internal one. But one can still use it for evaluation. We provide the pretrained models for KITTI and NYUV2 here (See Tab. 3 and Tab.4 in our paper). Our method win the 1st prize on the Robust Vision Challange 2018. The codes have been tested successfully on CentOS release 6.9, Cuda 9.0.176, Tesla V100, Anaconda python 2.7. 

This code is only for research purpose.

### Installation
For installation, please follow the instruction of [Caffe](https://github.com/BVLC/caffe).

### Usage
1. Clone the respository:
```
git clone https://github.com/hufu6371/DORN.git
```
2. Build and link to pycaffe:
```
cd $DORN_ROOT
build pycaffe
export PYTHONPATH=$DORN_ROOT/python:$DORN_ROOT/pylayer:$PYTHONPATH
```
3. Download our pretrained models and put them in folder './models':
```
mv DORN_KITTI_CVPR18.zip $DORN_ROOT/models
cd $DORN_ROOT/models
unzip DORN_KITTI_CVPR18.zip
```
4. Demo (KITTI and NYUV2):  
```
python demo_kitti.py --filename=./data/KITTI/demo_01.png --outputroot=./result/KITTI
python demo_nyuv2.py --filename=./data/NYUV2/demo_01.png --outputroot=./result/NYUV2
```

### Scores on the evaluation servers
1. [KITTI](http://www.cvlibs.net/datasets/kitti/eval_depth.php?benchmark=depth_prediction)
2. [ScanNet](http://dovahkiin.stanford.edu/adai/)

### Citation
```
@inproceedings{FuCVPR18-DORN,
  TITLE = {{Deep Ordinal Regression Network for Monocular Depth Estimation}},
  AUTHOR = {Fu, Huan and Gong, Mingming and Wang, Chaohui and Batmanghelich, Kayhan and Tao, Dacheng},
  BOOKTITLE = {{IEEE Conference on Computer Vision and Pattern Recognition (CVPR)}},
  YEAR = {2018}
}
```


