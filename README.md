# Bloom classification without labels
This is the demo notebook for the paper "Towards Bloom’s Taxonomy Classification Without Labels", to appear at Conf. Artificial Intelligence in Education (AIED), 2021.

The paper explores the weakly-supervised learning approach to perform the question Bloom's level classification task without relying on the costly-to-obtain, mostly proprietary, ground-truth Bloom's level labels.

# dependencies
pandas 1.2.4

numpy 1.19.5

bs4 (beautifulsoup) 4.9.3

snorkel 0.9.6

textstat 0.7.0

sklearn 0.21.3

seaborn 0.11.1

# Usage
### demo
*The `demo` notebook* demonstrates a few examples of questions and how the weakly-trained classifier predicts Bloom labels compared to the fully-supervised classifier.

please see the code and comments therein.

### training
*The `train_demo` notebook* demonstrates how to set up the labeling functions, create and train a label model, 
and compares a classifier trained on the weakly labeled dataset (by the label model) with a classifier trained on the ground-truth label dataset.

Note that, because the dataset that we use in this work is not publicly available, we did not include a copy of the dataset in this repo. 
However, the notebook and the utility file provides detailed steps which help to adapt the code to your dataset. 
Please see the code and comments therein for usage.




