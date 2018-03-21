# Document Image Classification with Intra-Domain Transfer Learning and Stacked Generalization of Deep Convolutional Neural Networks
Contributors: [Arindam Das](https://scholar.google.co.in/citations?user=W8DTl_gAAAAJ&hl=en), [Saikat Roy](https://scholar.google.co.in/citations?user=dSs0DfoAAAAJ&hl=en), [Ujjwal Bhattacharya](https://scholar.google.co.in/citations?user=dcbu4SEAAAAJ&hl=en)

This research work has been made available [here](https://arxiv.org/abs/1801.09321).

This page is published with intention to provide source code and region based pre-trained models for document image classification.<Enter>

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

# Experimental Results
<table>
<th> Performance Comparison </th>
<tr><td>

Method | Accuracy(%) | Comments
--- | --- | ---
Harley et al. [1]  | 89.90 | Document region based DCNN models with transfer learning
Tensmeyer et al. [2] | 89.31 | Spatial pyramidal pooling based AlexNet without transfer learning
Tensmeyer et al. [2] | 90.94 | Same model as above with increased image dimension (384X384) keeping aspect ratio same
Csurka et al. [3]  | 90.70 | GoogleNet with weights transferred from ImageNet
Afzal et al. [4] | 90.97 | VGG-16 with weights transferred from ImageNet
Kolsch et al. [5] | 90.05 | Weights transferred from ImageNet to VGG-16 and adding ELM in place of MLP
Proposed | 91.11 | VGG-16 model trained on holistic samples with weights transferred from ImageNet
Proposed | 92.21 | Inter and intra domain transfer learning on region based DCNNs and MLNN based stacking


</td></tr> </table>

# Pre-trained Models
Will be published soon...
