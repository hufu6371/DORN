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
3. Download our pretrained models and put them in folder './models':
```
mv DORN_KITTI_CVPR18.zip $DORN_ROOT/models
cd $DORN_ROOT/models
unzip DORN_KITTI_CVPR18.zip
```
4. Demo:   
For KITTI:
```
python demo_kitti.py --filename=./data/KITTI/demo_01.png --outputroot=./result/KITTI
```
  For NYUV2:  
```
python demo_nyuv2.py --filename=./data/NYUV2/demo_01.png --outputroot=./result/NYUV2
```


