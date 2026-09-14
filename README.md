# Machine Learning From Scratch

A collection of machine learning algorithms implemented from scratch to develop a deeper understanding of their underlying mathematics, logic, and implementation.

The focus of this repository is on understanding how algorithms work internally rather than simply using their library implementations.

## Projects

| Algorithm           | Implementation | Dataset / Verification     |
| ------------------- | -------------- | -------------------------- |
| Gradient Descent    | From scratch   | California Housing         |
| K-Nearest Neighbors | From scratch   | Verified with scikit-learn |

More implementations will be added as I continue learning.

## Approach

For each algorithm, I follow:

```text
Understand → Derive → Implement → Test → Verify
```

I first study the underlying concept and mathematics, implement the algorithm independently, test it, and then verify the results where appropriate.

## Current Implementations

### Gradient Descent

A manual implementation of Gradient Descent for Linear Regression.

**Includes:**

* Mean Squared Error
* Gradient calculation
* Weight updates
* Bias updates
* Learning rate
* Loss tracking

**Dataset:** California Housing

### K-Nearest Neighbors

A manual implementation of KNN classification.

**Includes:**

* Euclidean distance
* Nearest-neighbor selection
* K-value handling
* Majority voting
* Classification

**Verification:** Compared against scikit-learn's `KNeighborsClassifier`

## Technologies

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn

## Goal

The goal of this repository is to build a practical understanding of machine learning by implementing algorithms independently and working through the mathematics and logic behind them.

The implementations are primarily for learning and experimentation.

## Progress

* [x] Gradient Descent
* [x] K-Nearest Neighbors
* [ ] More algorithms


