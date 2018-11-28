# implement-Collaborative-Deep-Learning-for-Recommender-Systems

implement this paper "Collaborative Deep Learning for Recommender Systems" by python

Collaborative Deep Learning (CDL) (Wang, H., Wang, N., & Yeung, D. Y. (2015, August). Collaborative deep learning for recommender systems. In Proceedings of the 21th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 1235-1244). ACM.)

-----------------------------------------------------------------------------

## Introduction
This paper combine Collaborative filtering and stacked Denoising Autoencoder together. The original author implement by python and c++. And update the parameter by ALS algorithm . 
I implement this paper by tensorflow and try two method to update the parameter (1)ALS (2)gradient decent

You can download the [slide](https://drive.google.com/file/d/1EtnYFQyRSd6A24NIniJtE_U5bm6f4-lZ/view?usp=sharing) for more detail information.

## dataset
The dataset is from CiteULike . You can download it from the original author's website [here](http://www.wanghao.in/publication.html)

## usage
   
   CDL_tf.ipynb  - train CDL by gradient decent
   <br>
   CDL.ipynb - train CDL by ALS
