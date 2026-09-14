# Gradient Descent From Scratch

A from-scratch implementation of Gradient Descent for Linear Regression using NumPy, tested on the California Housing dataset.

## Overview

This project implements Gradient Descent manually to understand how a linear regression model learns its parameters by minimizing a loss function.

The model predicts:

```text
y_pred = Xw + b
```

and minimizes Mean Squared Error (MSE).

The parameters are updated iteratively using:

```text
w = w - learning_rate * dw
b = b - learning_rate * db
```

## Implementation

The implementation includes:

* Linear Regression
* Mean Squared Error
* Gradient calculation
* Weight updates
* Bias updates
* Learning rate
* Iterative optimization
* Loss tracking

The gradients are calculated using vectorized NumPy operations:

```text
dw = (-2 / n) * X.T @ (y - y_pred)
db = (-2 / n) * sum(y - y_pred)
```

## Dataset

The model was trained and tested using the **California Housing dataset**.

The dataset contains information about housing districts in California, with the target representing the median house value.

## Results

The implementation was trained using Gradient Descent and evaluated on the California Housing dataset.

The training process was also monitored using the loss over iterations to observe convergence.

## Tech Stack

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

## Key Learning

This project helped me understand:

* How Gradient Descent minimizes a loss function
* How gradients control parameter updates
* The role of the learning rate
* How weights and bias change during training
* Vectorized gradient calculations using NumPy
* How optimization behaves on a real-world dataset

## Project Status

Completed.

Implemented Gradient Descent from scratch and tested on the California Housing dataset.

