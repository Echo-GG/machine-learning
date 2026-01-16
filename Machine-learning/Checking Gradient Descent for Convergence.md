# Checking Gradient Descent for Convergence

## Leading

1. When running gradient descent, how can we tell if it is converging ? That is to say, whether it is helping us to find parameters close to the global minimum of the cost function.

2. By learning to recognize what a well-running implementation of gradient descent looks like, we'll later be able to choose a good learning rate $\alpha$.

## Gradient Descent Rule

$w_j = w_j - \alpha \frac{\partial{J(\vec{w},b)}}{\partial{w_j}}$

$b = b - \alpha \frac{\partial{J(\vec{w},b)}}{\partial b}$

### comment

One of the key choices is the choice of the learning rate $\alpha$.

## Make sure gradient descent is working correctly

### Objective

$\underset{\vec a,b}{min}$$J(\vec{w},b)$

### Methods

1. Create a graph:

   X axis: iterations

   Y axis: $J(\vec{w},b)$

   **Attention:**

   1. $J(\vec{w},b)\;$should decrease after every iteration.

   2. Looking at the learning curve, we can try to spot whether or not gradient descent is converging.

   3. The number of iterations that gradient descent takes to converge can vary a lot between different applications. For example, in one application, it may converge after just 30 iterations. For a different application, it could take a thousand or a hundred thousand iterations. It turns out to be very difficult to tell in advance how many iterations gradient descent needs to converge, which is why we can create a graph like we mentioned before, a learning curve, to try to find out when we can stop training our particular model.

2. Automatic convergence test

   1. Let $\epsilon$ be $10^{-3}$.

   2. If $J(\vec{w},b)$ decreases by ≤ $\epsilon$ in one iteration, declare convergence.

   (found parameters $\vec w$,b to get close to global minimum.)

### Comparison

1. Convergence hopefully indicates that we found parameters $\vec w$ and b that are close to the minimum possible value of j.

2. Usually we find that choosing the right threshold $\epsilon$ is pretty difficult, so we actually tend to look at graphs like the former method's one rather than rely on automatic convergence tests (the latter method).

3. Looking at this sort of figure can tell you or give you some advanced warning if maybe gradient descent is not working correctly as well.

# Conclusion

We've already seen what the learning curve should look like when gradient descent is running well.

So the next question will come to how to choose an appropriate learning rate $\alpha$.
