# Document Image Classification with Intra-Domain Transfer Learning and Stacked Generalization of Deep Convolutional Neural Networks
Contributors: [Arindam Das](https://scholar.google.co.in/citations?user=W8DTl_gAAAAJ&hl=en), [Saikat Roy](https://scholar.google.co.in/citations?user=dSs0DfoAAAAJ&hl=en), [Ujjwal Bhattacharya](https://scholar.google.co.in/citations?user=dcbu4SEAAAAJ&hl=en), [S.K. Parui](https://scholar.google.co.in/citations?user=RJh451AAAAAJ&hl=en)

This research work has been made available [here](https://arxiv.org/abs/1801.09321).

This page is published with intention to provide source code and region based pre-trained models for document image classification or document structure learning.<Enter>

Please cite our work if you find it useful for you research. <Enter>
  
```
@article{dic2018tlsg,
  title={Document Image Classification with Intra-Domain Transfer Learning and Stacked Generalization of Deep Convolutional Neural Networks},
  author={Das, Arindam and Roy, Saikat and Bhattacharya, Ujjwal},
  journal={arXiv preprint arXiv:1801.09321},
  year={2018}
}
```

# Dataset
[RVL-CDIP](http://www.cs.cmu.edu/~aharley/rvl-cdip/) has been used to validate the proposed methodology. This dataset consists of 400000 scanned grayscale images distributed among 16 categories. Also this collection is subdivided into training, validation and test sets each containing 320000, 40000 and 40000 images respectively.

# Proposed Architecture
<p align="center">
  <img src="https://github.com/hiarindam/document-image-classification-TL-SG/blob/master/IMG_Flowchart.png"  width="700" height="700">
</p>

# Experimental Results
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

# Pre-trained Models
Will be published soon...

# References
[1] A. W. Harley, A. Ufkes, and K. G. Derpanis, “Evaluation of deep convolutional nets for document image classification and retrieval,” in _Document Analysis and Recognition (ICDAR), 2015 13th International Conference on_. IEEE, 2015, pp. 991–995.<Enter>
  
[2] C. Tensmeyer and T. Martinez, “Analysis of convolutional neural networks for document image classification,” _arXiv preprint arXiv:1708.03273_, 2017.<Enter>

[3] G. Csurka, D. Larlus, A. Gordo, and J. Almazan, “What is the right way to represent document images?” _arXiv preprint arXiv:1603.01076_, 2016.<Enter>

[4] M. Z. Afzal, A. K¨olsch, S. Ahmed, and M. Liwicki, “Cutting the error by half: Investigation of very deep cnn and advanced training strategies for document image classification,” _arXiv preprint arXiv:1704.03557_, 2017.<Enter>

[5] Andreas Kölsch, Muhammad Zeshan Afzal, Markus Ebbecke, Marcus Liwicki, "Cutting the Error by Half: Investigation of Very Deep CNN and Advanced Training Strategies for Document Image Classification", _arXiv preprint arXiv:1704.03557_, 2017.<Enter>
