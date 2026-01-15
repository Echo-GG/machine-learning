# Learning Rate

## Formula

w = w- $\alpha$ $\frac{\partial J(w,b)}{\partial w}$

## Assumptions

1. If $\alpha$ is too small:

   Gradient descent may be low.

2. If $\alpha$ is too large:

   Gradient descent may:

   - Overshoot, never reach minimum.
   - Fail to converge, diverge.

3. If the parameters have already brought us to a local minimum, the further gradient descent steps do absolutely nothing. It doesn't change the parameters, which is what we want because it keeps the solution at that local minimum.

# Conclusion:

Just to recap, as we get nearer a local minimum, gradient descent will automatically take smaller steps. And that's because as we approach the local minimum, the derivative automatically gets smaller, and that means the update steps also automatically get smaller. even if the learning rate $\alpha$ is kept at some fixed value. That is the gradient descent algorithm. We can use it to try to minimize any cost function J(e.g.). not just the mean squared error cost function that we're using for linear regression.

> > Note:

    1.  Next we're going to take the function J and set that back to be exactly the linear regression model's cost function, the mean squared error cost function that we had come with earlier.

    2.  Putting together gradient descent with this cost function, there comes the 1st. learning algorithm --- the linear regression algorithm.
