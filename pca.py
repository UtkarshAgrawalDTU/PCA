#Make sure you scale your data using StandardScaler before calling this function!

import numpy as np

def PCA(X, ncomp = 0, critical = 0.9999):
    m = X.shape[0]
    n = X.shape[1]
    Sigma = np.zeros(shape = (n,n))
    for i in range(m):
        Sigma += np.dot(np.transpose(X[i,:]), X[i, :])
    
    u, s, vh = np.linalg.svd(Sigma, full_matrices=True)
    
    find = False
    k = 1
    sumdiag = 0
    
    for i in range(n):
        sumdiag += s[i]
    
    sumk = 0
    while find == False :
        sumk += s[k-1]
        
        if sumk/sumdiag >= critical:
            find = True
        else:
            k+=1
    
    if ncomp != 0:
        k = ncomp
    
    else:
        ured = u[:, 0:k]

    X_red = np.dot(X_scaled, ured)
    return X_red
