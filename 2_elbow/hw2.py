'''------------------------
| Import Required Modules |
------------------------'''
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from yellowbrick.cluster import KElbowVisualizer
import numpy as np

'''-------------------
| Generate Test Data |
-------------------'''
X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0)

'''-----------------
| Determine Best K |
-----------------'''
model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,15))
visualizer.fit(X)
visualizer.show()

'''---------------
| Generate Model |
---------------'''
kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit_predict(X)

'''--------------
| Assign Labels |
--------------'''
from scipy.stats import mode
labels = np.zeros_like(clusters)
for i in range(4):
    # this is similar to another for loop to check every element of clusters
    # group all the elements of clusters == i, then assign these elements to mask
    mask = (clusters == i)
    labels[mask] = mode(y_true[mask])[0]
    
print(labels.shape)
print(labels)

'''----------------
| Assess Accuracy |
----------------'''
from sklearn.metrics import accuracy_score
accuracy_score(y_true, labels)

'''-----------------
| Confusion Matrix |
-----------------'''
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.metrics import confusion_matrix

mat = confusion_matrix(y_true, labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False,
            xticklabels=[0, 1, 2, 3],
            yticklabels=[0, 1, 2, 3])
plt.xlabel('true label')
plt.ylabel('predicted label');
