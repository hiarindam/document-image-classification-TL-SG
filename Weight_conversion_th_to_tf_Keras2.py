import os
import numpy as np

from keras import backend as K
# from keras.utils.layer_utils import convert_all_kernels_in_model
from keras.applications import VGG16 


K.set_image_data_format('channels_first')
th_dim_model = VGG16(include_top=True, weights=None, input_shape=(3,224,224), pooling=None, classes=16) # Create your theano model here with TH dim ordering

K.set_image_data_format('channels_last')
tf_dim_model = VGG16(include_top=True, weights=None, input_shape=(224,224,3), pooling=None, classes=16) # Create your tensorflow model with TF dimordering here

model_weights = ['vgg16_weights_th_dim_ordering_th_kernels_right_body_82.17_0.00002.h5',
                'vgg16_weights_th_dim_ordering_th_kernels_left_body_85.21_0.000025.h5',
                'vgg16_weights_th_dim_ordering_th_kernels_Holistic_91.11.h5',
                'vgg16_weights_th_dim_ordering_th_kernels_header_86_0.00002.h5',
                'vgg16_weights_th_dim_ordering_th_kernels_Footer_81.24_0.00002.h5'] # Add names of theano model weight file paths here.
                     # These weights are assumed to be for  theano backend
                     # (th kernels) with th dim ordering!


"""
No need to edit anything below this. Simply run the script now after
editing the above 3 inputs.
"""


def shuffle_rows(original_w, nb_last_conv, nb_rows_dense):
    ''' Note :
    This algorithm to shuffle dense layer rows was provided by Kent Sommers (@kentsommer)
    in a gist : https://gist.github.com/kentsommer/e872f65926f1a607b94c2b464a63d0d3
    '''
    converted_w = np.zeros(original_w.shape)
    count = 0
    for index in range(original_w.shape[0]):
        if (index % nb_last_conv) == 0 and index != 0:
            count += 1
        new_index = ((index % nb_last_conv) * nb_rows_dense) + count
        #print("index from " + str(index) + " -> " + str(new_index))
        converted_w[index] = original_w[new_index]

    return converted_w


first_dense = True
nb_last_conv = 0

dirpath = "tf-kernels-channels-last-dim-ordering/"
if not os.path.exists(dirpath):
    os.makedirs(dirpath)

# Converts (theano kernels, th dim ordering) to (tensorflow kernels, tf dim ordering)
K.set_image_dim_ordering('th')
for weight_fn in model_weights:
    th_dim_model.load_weights(weight_fn) # th-kernels-th-dim
    #convert_all_kernels_in_model(th_dim_model) # tf-kernels-th-dim // ALREADY DONE BY KERAS!

    count_dense = 0
    for layer in th_dim_model.layers:
        if layer.__class__.__name__ == "Dense":
            count_dense += 1

    if count_dense == 1:
        first_dense = False # If there is only 1 dense, no need to perform row shuffle in Dense layer

    print("Nb layers : ", len(th_dim_model.layers))

    for index, th_layer in enumerate(th_dim_model.layers):
        if th_layer.__class__.__name__ in ['Conv1D',
                                           'Conv2D',
                                           'Conv3D',
                                           'AtrousConvolution1D'
                                           'AtrousConvolution2D',
                                           'Conv2DTranspose',
                                           'SeparableConv2D',
                                           'DepthwiseConv2D',
                                           ]:
            weights = th_layer.get_weights() # tf-kernels-th-dim
            #weights[0] = weights[0].transpose((2, 3, 1, 0)) // ALREADY DONE BY KERAS!
            tf_dim_model.layers[index].set_weights(weights) # tf-kernels-tf-dim

            nb_last_conv = th_layer.filters # preserve last number of convolutions to use with dense layers // UPDATED from nb_filters
            print("Converted layer %d : %s" % (index + 1, th_layer.name))
        else:
            if th_layer.__class__.__name__ == "Dense" and first_dense:
                weights = th_layer.get_weights()
                nb_rows_dense_layer = weights[0].shape[0] // nb_last_conv

                print("Magic Number 1 : ", nb_last_conv)
                print("Magic nunber 2 : ", nb_rows_dense_layer)

                weights[0] = shuffle_rows(weights[0], nb_last_conv, nb_rows_dense_layer)
                tf_dim_model.layers[index].set_weights(weights)

                first_dense = False
                print("Shuffled Dense Weights layer and saved %d : %s" % (index + 1, th_layer.name))
            else:
                tf_dim_model.layers[index].set_weights(th_layer.get_weights())
                print("Saved layer %d : %s" % (index + 1, th_layer.name))

  
    tf_dim_model.save_weights("tf-kernels-channels-last-dim-ordering/%s" % weight_fn, overwrite=True)
    print("Done tf-kernels-channels-last-dim-ordering %s" % weight_fn)