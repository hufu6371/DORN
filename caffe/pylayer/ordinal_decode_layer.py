import caffe
import numpy as np
import pdb

class OrdinalDecodeLayer(caffe.Layer):
               
    def setup(self, bottom, top):
        pass
        # check input pair
        #layer_params = yaml.load(self.param_str)
        #self._top_number = layer_params['top_number']

    def reshape(self, bottom, top):
        pass

    def forward(self, bottom, top):
        N = bottom[0].data.shape[0]
        C = bottom[0].data.shape[1]
        H = bottom[0].data.shape[2]
        W = bottom[0].data.shape[3]
        ord_labels = bottom[0].data.copy()
        decode_label = np.zeros((N, 1, H, W), dtype=np.float32)
        ord_num = C/2
        for i in xrange(ord_num):
            ord_i = ord_labels[:,2*i:2*i+2,:,:]
            decode_label = decode_label + np.argmax(ord_i, axis=1)
        top[0].reshape(*decode_label.shape)
        top[0].data[...] = decode_label.astype(np.float32, copy=False)

    def backward(self, top, propagate_down, bottom):
        pass
