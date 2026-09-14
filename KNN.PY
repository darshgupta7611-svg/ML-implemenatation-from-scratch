import numpy as np
train = np.array([
    [15, 3],  
    [20, 4],  
    [10, 2],
    [25, 4]  
])
test = np.array([
    [12, 2],  
    [18, 3],
    [22, 4]  
])
y = np.array([[250, 340, 180, 420]])

def KNN(train, test, y,K):
    ok = []
    for i in test:
        s = []
        for k in train:
            l = np.sum((i - k) ** 2)
            d = np.sqrt(l)
            s.append(d)
        op = np.argsort(s)
        ok.append(op)
    w = []
    for i in ok:
        w.append(i[:K])
    m = []
    for i in w:
        k = []
        for p in i:
            R = y.ravel()[p]
            k.append(R)
        m.append(np.mean(k))

    return print(m)
KNN(train, test, y,2)