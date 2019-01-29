# DORN: Deep Ordinal Regression Network for Monocular Depth Estimation

### Paper

#### [H. Fu, M. Gong, C. Wang, K. Batmanghelich and D. Tao: Deep Ordinal Regression Network for Monocular Depth Estimation. IEEE Conference on Computer Vision and Pattern Recognition (CVPR) 2018.](https://arxiv.org/abs/1806.02446)


### Introduction
The shared code is a Caffe implemention of our CVPR18 paper (DORN). The provided Caffe is not our internal one. But one can still use it for evaluation. We provide the pretrained models for KITTI and NYUV2 here (See Tab. 3 and Tab.4 in our paper).  The code has been tested successfully on CentOS release 6.9, Cuda 9.0.176, Tesla V100, Anaconda python 2.7, Cudnn 7.0. 

Our method won the 1st prize in [Robust Vision Challange 2018](http://www.robustvision.net/index.php). We ranked 1st place on both [KITTI](http://www.cvlibs.net/datasets/kitti/eval_depth.php?benchmark=depth_prediction) and [ScanNet](http://dovahkiin.stanford.edu/adai/). Slides can be downloaded [here](https://drive.google.com/file/d/1d2b8rNk4Mxc5dBDrj8lOStKxGVwMXoq7/view?usp=sharing).

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
1. [KITTI](https://drive.google.com/open?id=180QRn5su1Yf5d-WNqE0jELPNuOpQMjNR)
2. [NYUV2](https://drive.google.com/file/d/1PkxkzWwZthjnJGtaPlTS5qTrj-Tka7eX/view?usp=sharing)

### Scores on the evaluation servers
1. [KITTI](http://www.cvlibs.net/datasets/kitti/eval_depth.php?benchmark=depth_prediction)
2. [ScanNet](http://dovahkiin.stanford.edu/adai/)

### Results on ScanNet
The evaluation scripts and the groundtruth depth maps for KITTI and NYU Depth v2 are contained in the zip files. You may also need to download the predictions from [Eigen et al.](https://cs.nyu.edu/~deigen/depth/) for the center cropping used in our evaluation scripts.
1. [ScanNet](https://drive.google.com/file/d/12EB_UrmNQZj8VvEUVVxwl1VBQFPB9hdv/view?usp=sharing)
2. [KITTI](https://drive.google.com/open?id=18z_FpbHWmU-tX19n2FWQMwpzCmuuOsMb)
3. [NYU Depth v2](https://drive.google.com/open?id=1uRqOkCbJLwHWyx4oz19N6MQgrOSZQo6H)

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


