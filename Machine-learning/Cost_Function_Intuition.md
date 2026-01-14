# Cost Function Intuition

## A short conclusion

To recap, here's what we've seen about the cost function so far.

1. You want to fit a straight line to the training data, so you have this model:
   $f_{w,b}(x) = wx + b$

2. And here, the model's paremeters are w and b.

3. Now depending on the values chosen for these parameters, you will get different straight lines. And you want to find values for w and b so that the straight line fits the training data well.

4. To measure how well a choice of w and b fits the training data, you have a cost function J:
   $J(w,b) = \frac{1}{2m}\sum_{i=1}^{m}(\hat{y}^{(i)}-y^{(i)})^2$

5. And what the cost function J does is, it measures the difference between the model's predictions and the actual true values for y.

6. Linear Regression will try to find values for w and b that make J of w and b as small as possible.

7. So our goal is to minimize J as a function of w and b

$\underset{w,b}{minimize}\;J(w,b)$

## Visualization

using a simplified version of the linear regression model: $f_{w}(x) = wx$

You can think of this as taking the original model on the left and getting rid of the parameter b, or setting the parameter b equal to zero, so it just goes away from the equation. So f is now just w times x. So you now have just one parameter w. The cost function looks similar as before:
$J(w) = \frac{1}{2m}\sum_{i=1}^{m}(f_{w}(x^{(i)})-y^{(i)})^2$

Our goal becomes finding the value for w that minimizes j of w.

$\underset{w}{minimize}\;J(w)$

To see this visually, it's a line passes through the origin here.

> > Note:

    1.  It is not easy to display all the related pictures, and we can just search it when we need it. For the beginners, let's skip this part of notes and focous on the following algorithms.(e.g. Gradient Descent)

    2.  Maybe there's a need to start a specific topic on drawing a graph using matplotlib.pylot and numpy in python. We will discuss this in the no longer future on purpose.
