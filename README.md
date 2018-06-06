# DORN: Deep Ordinal Regression Network for Monocular Depth Estimation

### Paper

H. Fu, M. Gong, C. Wang, K. Batmanghelich and D. Tao: Deep Ordinal Regression Network for Monocular Depth Estimation. IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2018.


### Introduction
The shared code is a Caffe implemention of our CVPR18 paper (DORN). The provided Caffe is not our internal one. But one can still use it for evaluation. We provide the pretrained models for KITTI and NYUV2 here (See Tab. 3 and Tab.4 in our paper).  The code has been tested successfully on CentOS release 6.9, Cuda 9.0.176, Tesla V100, Anaconda python 2.7, Cudnn 7.0. 

Our method won the 1st prize in [Robust Vision Challange 2018](http://www.robustvision.net/index.php). We achieved 1st place ranking on both [KITTI](http://www.cvlibs.net/datasets/kitti/eval_depth.php?benchmark=depth_prediction) and [ScanNet](http://dovahkiin.stanford.edu/adai/). 

KITTI
![KITTI](https://github.com/hufu6371/DORN/blob/master/DORN_Server_Scores/KITTI.jpeg)

ScanNet
![ScanNet](https://github.com/hufu6371/DORN/blob/master/DORN_Server_Scores/ScanNet.jpeg)


Robust Vision Challange 2018
![Robust Vision Challange 2018](https://github.com/hufu6371/DORN/blob/master/DORN_Server_Scores/ROB.jpeg)

This code is only for research purposes. If you use the provided Caffe, you may also need to follow the instructions of [DeepLab v2](https://bitbucket.org/aquariusjay/deeplab-public-ver2) and [PSPNet](https://github.com/hszhao/PSPNet).

### Installation
See [Caffe](https://github.com/BVLC/caffe) for installation.

### Usage
1. Clone the respository:
```
git clone https://github.com/hufu6371/DORN.git
```
2. Build and link to pycaffe:
```
cd $DORN_ROOT
edit Makefile.config
build pycaffe
export PYTHONPATH=$DORN_ROOT/python:$DORN_ROOT/pylayer:$PYTHONPATH
```
3. Download our pretrained models:
```
mv cvpr_kitti.caffemodel $DORN_ROOT/models/KITTI/
mv cvpr_nyuv2.caffemodel $DORN_ROOT/models/NYUV2/
```
4. Demo (KITTI and NYUV2):  
```
python demo_kitti.py --filename=./data/KITTI/demo_01.png --outputroot=./result/KITTI
python demo_nyuv2.py --filename=./data/NYUV2/demo_01.png --outputroot=./result/NYUV2
```

### Pretrained models
1. [KITTI](https://drive.google.com/file/d/1twncRAsez7wqCnMTO5yZ1rHtXashu5OD/view?usp=sharing)
2. [NYUV2](https://drive.google.com/file/d/1a1gr1VNBDRDxj2F77x-wzycQC_ZJuKxT/view?usp=sharing)

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
### Contact
Huan Fu: hufu6371@uni.sydney.edu.au


