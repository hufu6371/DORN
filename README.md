# DORN: Deep Ordinal Regression Network for Monocular Depth Estimation

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
3. Download our pretrained models:
For [KITTI]
```
mv DORN_KITTI_CVPR18.zip $DORN_ROOT/models
cd $DORN_ROOT/models
unzip DORN_KITTI_CVPR18.zip 
```
