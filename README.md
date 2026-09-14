# K-Nearest Neighbors From Scratch

A from-scratch implementation of the K-Nearest Neighbors (KNN) algorithm using Python and NumPy.

## Overview

KNN makes predictions by finding the training samples closest to a given data point.

The basic process is:

1. Calculate the distance between the new point and training points.
2. Sort the points by distance.
3. Select the `K` nearest neighbors.
4. Examine their labels.
5. Predict using majority voting.

For Euclidean distance:

```text
distance = sqrt(sum((x1 - x2)^2))
```

## Implementation

The implementation includes:

* Euclidean distance calculation
* Distance comparison
* Nearest-neighbor selection
* K-value handling
* Majority voting
* Classification predictions

## Verification

The from-scratch implementation was **rechecked against scikit-learn's `KNeighborsClassifier`**.

The predictions from both implementations were compared to verify that the manually implemented algorithm was working correctly.

## Tech Stack

* Python
* NumPy
* Scikit-learn

## Key Learning

This project helped me understand:

* How KNN makes predictions
* How distance is calculated
* How the nearest neighbors are selected
* How the value of `K` affects predictions
* How majority voting is used for classification
* How to implement KNN without relying on a pre-built classifier

## Project Status

Completed.

Implemented from scratch and verified against scikit-learn.
