# Gradient Descent From Scratch

A simple implementation of **Gradient Descent from scratch using Python and NumPy**.

The goal of this project was to understand how Gradient Descent works mathematically and implement it without relying on machine-learning libraries for the optimization algorithm.

## What I Built

In this project, I implemented Gradient Descent to find the optimal parameters for a linear regression model.

The basic idea is:

1. Make predictions using the current parameters.
2. Calculate the error.
3. Calculate the gradients of the loss function.
4. Update the parameters in the direction that reduces the loss.
5. Repeat this process until the model converges.

## Mathematics

The model used is:

`y = wx + b`

The Mean Squared Error loss is:

`J(w,b) = (1/n) Σ(y_pred - y)²`

The parameters are updated using:

`w = w - learning_rate × dw`

`b = b - learning_rate × db`

where `dw` and `db` are the gradients of the loss with respect to the weight and bias.

## Technologies Used

- Python
- NumPy
- Matplotlib
- Google Colab

## What I Learned

Through this project, I learned:

- How Gradient Descent actually works
- How derivatives are used to optimize a model
- How weights and bias are updated
- How the learning rate affects optimization
- How the loss changes during training
- How to implement a basic ML algorithm without using `sklearn`

## Project Structure

```text
gradient-descent-scratch/
│
├── gradient_descent.ipynb
└── README.md
