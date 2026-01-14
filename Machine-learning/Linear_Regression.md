# Linear Regression Model

## Terminology

1. Traning set

Data used to train the model.

## Notation:

1. x = "input" variable / feature.

2. y = "output" variable / "target" variable.

3. m = number of training examples.

4. (x,y) = single training example.

5. (x<sup>(i)</sup>,y<sup>(i)</sup>) = i <sup>th</sup> training example

   1. "i" means index. (1<sup>st</sup>,2<sup>nd</sup>,3<sup>rd</sup>...)

   2. x<sup>(2)</sup> ≠ x$^2$ not exponent

## Process

1. To train the model, you feed the training set, both the input features and the output targets, to your learning algorithm.

2. Then your supervised learning algorithm will produce some function.

   1. We denote the function as lowercase "f", where f stands for function.

   2. Historically, this funciton used to be called a hypothesis.

3. The job of f is to take the new input x and output an estimate or a prediction.

   1. x -> f -> "y-hat" ($\hat y$)`.

   2. In manchine learning, the convention is that y-hat is the estimate or the prediction for y.

   3. The function f is called the model.

   4. x is called the input or the input feature, and the output of the model is the prediction y-hat.

   5. The model's prediciton is the estimated value of y ($\hat y$).

   6. When the symbol is just the letter y, then that refers to the target, which is the actual true value in the training set.

   7. In contrast, y-hat is an estimate. It may or may not be the actual true value.

## Representation of the function (f)

f<sub>w,b</sub>(x) = wx + b

f(x) = wx + b

Linear regression with one variable.

Univariate linear regression.

# comment

This is the linear regression and in order to make it work, one of the most important things that is required to do is construct a cost function.
