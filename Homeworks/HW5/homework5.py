## COMP1730/6730 S2 2017 - Homework 5

## I did this homework by myself.
## Xinlin Li u6460036
## 8/30/2017

## Modify the following function definition so that it computes and
## returns the correct answer to the homework problem. (The statement
## "return 0" is just a placeholder: you should of course modify it.)
def interpolate(x, y, x_test):
    for i in range(0, len(x)):  # find the closest sample point in x sequence
        if x[i] >= x_test:  # x[i-1](x_below) < x'< x[i](x_above)
            a = (y[i] - y[i - 1]) / (x[i] - x[i - 1])  # y = a*x + b
            b = y[i - 1] - a * x[i - 1]
            y_test = a * x_test + b
            return y_test

## REMEMBER THAT THIS FILE (WHEN YOU SUBMIT IT) MUST NOT CONTAIN ANYTHING
## OTHER THAN YOUR FUNCTION DEFINITION AND COMMENTS. You can (and should)
## use docstrings to document your functions, but a docstring should only
## be used inside a function definition, an then only at the very beginning
## of the function suite. Everywhere else you should use comments.
