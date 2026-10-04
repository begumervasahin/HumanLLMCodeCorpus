import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
b1 = pd.read_csv('Admission_Predict.csv')
b2 = b1.iloc[:,1:8].values
b3 = b1.iloc[:,8].values
for i in range(0,400):
    if(b3[i]>=0.5):
        b3[i]=1
    else:
        b3[i]=0
from sklearn.cross_validation import train_test_split
b6,b7,Y_train,b4 = train_test_split(b2,b3,test_size=0.2,random_state=0)
from sklearn.preprocessing import StandardScaler
b5 = StandardScaler()
b6 = b5.fit_transform(b6)
b7 = b5.transform(b7)
from sklearn.decomposition import PCA
b8 = PCA(n_components = 2)
b6 = b8.fit_transform(b6)
b7 = b8.transform(b7)
b9 = b8.explained_variance_ratio_
from sklearn.tree import DecisionTreeClassifier
b10 = DecisionTreeClassifier(criterion='entropy',random_state=0)
b10.fit(b6,Y_train)
b11 = b10.predict(b7)
from sklearn.metrics import confusion_matrix
b12 = confusion_matrix(b4,b11)
from matplotlib.colors import ListedColormap
X_set,b13 = b7,b4
X1,b14 = np.meshgrid(np.arange(b15=X_set[:,0].min()-1,stop=X_set[:,0].max()+1,step=0.01),
                  np.arange(b15 = X_set[:,1].min()-1,stop=X_set[:,1].max()+1,step=0.01))
plt.contourf(X1,b14,b10.predict(np.array([X1.ravel(),b14.ravel()]).T).reshape(X1.shape),b16 = 0.75,cmap=ListedColormap(('red','green')))
plt.xlim(X1.min(),X1.max())
plt.ylim(b14.min(),b14.max())
for i,j in enumerate(np.unique(b13)):
    plt.scatter(X_set[b13 = =j,0],X_set[b13==j,1],
                b17 = ListedColormap(('red','green'))(i),label=j)
plt.title('Decision Tree Classifier(Test set)')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend()
plt.show()