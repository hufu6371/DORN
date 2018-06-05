import cv2
import caffe
import numpy as np
import scipy.io as sio
import argparse
import os
import pdb

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--filename', type=str, default='./data/NYUV2/demo_01.png', help='path to an image')
parser.add_argument('--outputroot', type=str, default='./result/NYUV2', help='output path')

caffe.set_mode_gpu()
caffe.set_device(0)
net = caffe.Net('models/NYUV2/deploy.prototxt', 'models/NYUV2/cvpr_nyuv2.caffemodel', caffe.TEST)
pixel_means = np.array([[[103.0626, 115.9029, 123.1516]]])

def depth_prediction(filename):
    img = cv2.imread(filename, 1)
    img = img.astype(np.float32)
    H = img.shape[0]
    W = img.shape[1]
    img -= pixel_means
    img = cv2.resize(img, (353, 257), interpolation=cv2.INTER_LINEAR)
    data = img.copy()
    data = data[None, :]
    data = data.transpose(0,3,1,2)
    blobs = {}
    blobs['data'] = data
    net.blobs['data'].reshape(*(blobs['data'].shape))
    forward_kwargs = {'data': blobs['data'].astype(np.float32, copy=False)}
    net.forward(**forward_kwargs)
    pred = net.blobs['decode_ord'].data.copy()
    pred = pred[0,0,:,:] - 1.0
    pred = pred/25.0 - 0.36
    pred = np.exp(pred)
    ord_score = cv2.resize(pred, (W, H), interpolation=cv2.INTER_LINEAR)
    return ord_score
    #ord_score = ord_score*256.0

args = parser.parse_args()
depth = depth_prediction(args.filename)
depth = depth/10.0
depth = depth*255.0
depth = depth.astype(np.uint8)
img_id = args.filename.split('/')
img_id = img_id[len(img_id)-1]
img_id = img_id[0:len(img_id)-4]
if not os.path.exists(args.outputroot):
    os.makedirs(args.outputroot)
cv2.imwrite(str(args.outputroot + '/' + img_id + '_pred.png'), depth)






