'''
Damn, Not Working :-(
'''

import numpy as np
import matplotlib.pyplot as plt
from itertools import product
from sklearn.decomposition import PCA as RandomizedPCA # 
from sklearn.datasets import fetch_openml
from sklearn.utils import shuffle

#use all digits
mnist = fetch_openml('mnist_784', version=1, cache=True)

X_train, y_train = mnist.data[:10000] / 255., mnist.target[:10000]

X_train, y_train = shuffle(X_train, y_train)
X_train, y_train = X_train[:5000], y_train[:5000]  # lets subsample a bit for a first impression

print('y_train[1000]= ', y_train)

pca = RandomizedPCA(n_components=3)
fig, plot = plt.subplots()
fig.set_size_inches(50, 50)
plt.prism()

X_transformed = pca.fit_transform(X_train)
plot.scatter(X_transformed[:, 0], X_transformed[:, 1], c=y_train)
plot.set_xticks(())
plot.set_yticks(())

#plt.tight_layout()
plt.savefig("mnist_pca.png")
