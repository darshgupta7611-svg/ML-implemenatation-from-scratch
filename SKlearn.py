import numpy as np
from sklearn.neighbors import KNeighborsRegressor

train = np.array([
    [15, 3],
    [20, 4],
    [10, 2],
    [25, 4]
])

y = np.array([[250, 340, 180, 42000]])
# Flatten y for scikit-learn compatibility
y_1d = y.ravel()

test = np.array([
    [12, 2],
    [18, 3],
    [22, 4]
])

# KNN Regressor with n_neighbors=2 (or default 3/2 given small dataset)
knn = KNeighborsRegressor(n_neighbors=2)
knn.fit(train, y_1d)
predictions = knn.predict(test)

print("Predictions (n_neighbors=2):", predictions)