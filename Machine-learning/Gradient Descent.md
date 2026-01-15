# Gradient Descent

## Leading

It would be nicer if we had a more systematic way to find the values of w and b that result in the smallest possible cost, j of w,b. It turns out there's an algorithm called gradient descent that you can use to do that.

## General

Gradient descent is an algorithm that can be used to minimize any function.

## Outline

1. Start with some w,b (e.g. set w = 0, b = 0).

2. Keep changing w,b to reduce J(w,b).

3. Until we settle at or near a minimum. (may have more than 1 minimum.)

## Gradient Descent Algorithm (Mathematical expressions)

Repeat until convergence

w = w - $\alpha$ $\frac{\partial J(w,b)}{\partial w}$

b = b - $\alpha$ $\frac{\partial J(w,b)}{\partial b}$

1. $\alpha$ is called the learning rate (0< $\alpha$ <1)

2. $\frac{\partial J(w,b)}{\partial w}$ or $\frac{\partial J(w,b)}{\partial b}$ is called the (partial) derivative.

3. Simultaneously update w and b

   1. Correct: Simultaneous update

      tmp_w = w - $\alpha$ $\frac{\partial J(w,b)}{\partial w}$

      tmp_b = b - $\alpha$ $\frac{\partial J(w,b)} {\partial b}$

      w = tmp_w

      b = tmp_b

   2. Incorrect

      tmp_w = w - $\alpha$ $\frac{\partial J(w,b)}{\partial w}$

      w = tmp_w

      tmp_b = b - $\alpha$ $\frac{\partial J(w,b)} {\partial b}$

      b = tmp_b

> > Note:

    1.  As for the (partial) derivative , it's nothing new but what we've learnt in the course of calculus. No more explanation here.

    2.  We may focous our attention on the learning rate $\alpha$ which is more than 0 and less than 1.
