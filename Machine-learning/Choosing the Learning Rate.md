# Choosing the Learning Rate

## Leading

Our learning algorithm will run much better with an appropriate choice of learning rate $\alpha$.

If it's too small, it would run very slowly. And if it's too large, it may not even converge.

Let's start by taking a look at how we can choose a good learning rate for our model.

## Explanation

### Problem Statement

If you plot the cost for a number of iterations and notice that the cost sometimes goes up and sometimes goes down, you should take that as a clear sign that gradient descent is not working properly. This could mean that there's a bug in the code, or sometimes it could mean that yor learning rate is too large.

### Solution

To fix this, you can use a smaller learning rate. So then your updates may start here and go down a little bit and down a bit, and will hopefully consistently decrease until it reaches the global minimum.

### Other Cases

Sometimes you may see that the cost consistently increases after each iteration.This is also likely due to a learning rate that is too large, and it could be addressed by choosing a smaller learning rate.

But learning rates like this could also be a sign of a possible bug in the code. For example, if we wrongly wrote $w_1 = w_1 + \alpha d_1$ to $w_1 = w_1 + \alpha d_1$, then this could result in the cost consistently increasing at each iteration. And this is because adding the derivative term(e.g. $d_1$) moves your cost J further from the global minimum instead of closer.

# Conclusion

1. One debugging tip for a correct implementation of gradient descent is that with a small enough learning rate $\alpha$, the cost function should decrease on every single iteration. So if gradient descent isn't working, one thing we usually do is to just set $\alpha$ to be a very, very small number and see if that causes the cost to decrease on every iteration.

2. If even with alpha set to a very small number, J doesn't decrease on every single iteration but instead sometimes increases, then that usually means there's a bug somewhere in the code.

3. Note that setting $\alpha$ to be really, really small is meant here as a debugging step, and a very, very small value of $\alpha$ is not going to be the most efficient choice for actually training your learning algorithm. One important trade-off is that if your learning rate is too small, then gradient descent can take a lot of iterations to converge.

4. So while we're actually running a gradient descent, we'll usually try a range of values for the learning rate $\alpha$. So we might start by trying a learning rate of 0.001, and we might also try a learning rate that's 10 times as large, say 0.01 and 0.1 and so on. And for each choice of $\alpha$, we might run gradient descent just for a handful of iterations, and plot the cost function J as a function of the number of iterations.(the graph we have discussed in the former chapter.)

5. After trying a few different values, we might then pick the value of $\alpha$ that seems to decrease the learning rate rapidly, but also consistently.

6. In fact, what we actually do is try a range of values like this. After trying 0.001, we'll then increase the learning rate threefold yo 0.003. And after that, we'll try 0.01, which is again about three times as large as 0.003. So these are roughly trying out gradient descent with each value of $\alpha$ being roughly three times bigger than the previous value.

7. So what we'll do is try a range of values until we found a value that's too small. And then also make sure we found a value that's too large. And we'll slowly try to pick the largest possible learning rate, or just something slightly smaller than the largest reasonable value that we found. When we do that, it usually gives us a good learning rate for our model.
