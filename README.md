# Document Image Classification with Intra-Domain Transfer Learning and Stacked Generalization of Deep Convolutional Neural Networks
Contributors: [Arindam Das](https://scholar.google.co.in/citations?user=W8DTl_gAAAAJ&hl=en), [Saikat Roy](https://scholar.google.co.in/citations?user=dSs0DfoAAAAJ&hl=en), [Ujjwal Bhattacharya](https://scholar.google.co.in/citations?user=dcbu4SEAAAAJ&hl=en), [S.K. Parui](https://scholar.google.co.in/citations?user=RJh451AAAAAJ&hl=en)

This research work has been made available [here](https://arxiv.org/abs/1801.09321).

This page is published with intention to provide region based pre-trained models for document image classification for document structure learning. For using weight matrices, please note that we used theano as the backend for all our experiments hence everything is ordered per theano's style.<Enter>

Please cite our work if you find it useful for you research. <Enter>

```
@inproceedings{das2018document,
  title={Document Image Classification with Intra-Domain Transfer Learning and Stacked Generalization of Deep Convolutional Neural Networks},
  author={Das, Arindam and Roy, Saikat and Bhattacharya, Ujjwal and Parui, Swapan K},
  booktitle={2018 24th International Conference on Pattern Recognition (ICPR)},
  pages={3180--3185},
  year={2018},
  organization={IEEE}
}
```
## Theano to Tensorflow Weight Convertor
There has been an ongoing issue by users unable to use (properly load) the weights in tensorflow using a convertor or otherwise since the version of theano and keras used for this project was pretty old (late 2017/early 2018). Please also look at the section on preprocessing the input. This section deals with weight conversion from theano to tensorflow. This particular module was developed by Auke Zijlstra (a.zijlstra@student.eur.nl) and although he was unable to replicate the exact results we had using this script, he did get things working. We provide excerpts from his communication with us on the usage of the script.

> "... Although I have not been able to fully replicate your results, I have been able to achieve 0.87 accuracy score on the RVL-CDIP test set using your holistic model weights with a Keras+tensorflow setup. My steps to convert your Theano ordered weights into Tensorflow ordering were as follows:
>
> * I downloaded your model weights and added the attribute ‘backend’ into the weight file, so that Keras is able to automatically convert the convolutional kernels when calling load_weights(). I assume this was needed because you saved your models using Keras 1.X. (source: https://stackoverflow.com/questions/47368466/keras-converting-convolutional-kernels-from-theano-to-tensorflow-oom/47378902#47378902)
> * I used (an edited version of) a script by titu1994 (source: https://github.com/titu1994/Keras-Classification-Models/blob/master/weight_conversion_theano.py) to shuffle the Dense weights layers, so that they match with the (last) converted convolutional layer. My main edits in this script were to disable the calls to convert_all_kernels_in_model() and the transposing of the convolutional layer weights, as these steps are already done by Keras 2.x upon calling load_weights(). The resulting script I have attached to this email, as it might help others that want to replicate your work."

Hopefully this gives a way forward for people having issues using our weights for newer versions of keras, theano, tensorflow and the like.

## Dataset
[RVL-CDIP](http://www.cs.cmu.edu/~aharley/rvl-cdip/) has been used to validate the proposed methodology. This dataset consists of 400000 scanned grayscale images distributed among 16 categories. Also this collection is subdivided into training, validation and test sets each containing 320000, 40000 and 40000 images respectively.

## Preprocessing
Please look at this [comment](https://github.com/hiarindam/document-image-classification-TL-SG/issues/4#issuecomment-446190710) to see a small example on how to preprocess the input for the networks.

## Proposed Architecture
<p align="center">
  <img src="https://github.com/hiarindam/document-image-classification-TL-SG/blob/master/IMG_Flowchart.png"  width="700" height="700">
</p>

## Experimental Results
<table>
<th> Performance Comparison with State-of-the-art Approaches</th>
<tr><td>

Method | Accuracy(%) | Comments
--- | --- | ---
Harley et al. [1]  | 89.90 | Document region based DCNN models with transfer learning
Tensmeyer et al. [2] | 89.31 | Spatial pyramidal pooling based AlexNet without transfer learning
Tensmeyer et al. [2] | 90.94 | Same model as above with increased image dimension (384X384) keeping aspect ratio same
Csurka et al. [3]  | 90.70 | GoogleNet with weights transferred from ImageNet
Afzal et al. [4] | 90.97 | VGG-16 with weights transferred from ImageNet
Kölsch et al. [5] | 90.05 | Weights transferred from ImageNet to VGG-16 and adding ELM in place of MLP
Proposed | 91.11 | VGG-16 model trained on holistic samples with weights transferred from ImageNet
Proposed | 92.21 | Inter and intra domain transfer learning on region based DCNNs and MLNN based stacking


</td></tr> </table>

## Pre-trained Models
Trained models in this publication have been made available [here](https://drive.google.com/open?id=1oFk0eytDn_M6LmdugI22JUV4nmnO5gIv). Please note that all weight matrices are formatted with theano as a background and not tensorflow. That also includes theano style input dimension ordering.

## References
[1] A. W. Harley, A. Ufkes, and K. G. Derpanis, “Evaluation of deep convolutional nets for document image classification and retrieval,” in _Document Analysis and Recognition (ICDAR), 2015 13th International Conference on_. IEEE, 2015, pp. 991–995.<Enter>
  
[2] C. Tensmeyer and T. Martinez, “Analysis of convolutional neural networks for document image classification,” _arXiv preprint arXiv:1708.03273_, 2017.<Enter>

[3] G. Csurka, D. Larlus, A. Gordo, and J. Almazan, “What is the right way to represent document images?” _arXiv preprint arXiv:1603.01076_, 2016.<Enter>

[4] M. Z. Afzal, A. K¨olsch, S. Ahmed, and M. Liwicki, “Cutting the error by half: Investigation of very deep cnn and advanced training strategies for document image classification,” _arXiv preprint arXiv:1704.03557_, 2017.<Enter>

[5] Andreas Kölsch, Muhammad Zeshan Afzal, Markus Ebbecke, Marcus Liwicki, "Cutting the Error by Half: Investigation of Very Deep CNN and Advanced Training Strategies for Document Image Classification", _arXiv preprint arXiv:1704.03557_, 2017.<Enter>
