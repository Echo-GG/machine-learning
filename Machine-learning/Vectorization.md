# Vectorization

## Parameters and Features

$\vec{w} = [w_1\; w_2\; w_3]$ $\;$(n = 3)

b is a number

$\vec{x} = [x_1\;x_2\;x_3]$

```py
import numpy as np
w = np.array([1.0,2.5,-3.3])
b = 4
x = np.array([10,20,30])

# Linear Algebra : count from 1
# Code : count from 0
```

Without vectorization

$f_{\vec{w},b}(\vec{x}) = w_1 x_1 + w_2 x_2 + w_3 x_3 + b$

```py
f = w[0] * x[0] + w[1] * x[1] + w[2] * x[2] + b
```

$f_{\vec{w},b}(\vec{x}) = (\sum_{j=1}^{n} w_j x_j) + b$

```py
f = 0
for j in range (0,n):
    f = f + w[j] * x[j]
f = f + b
```

Vectorization

$f_{\vec{w},b}(\vec{x}) = \vec{w} · \vec{x} + b$

```py
f = np.dot(w,x) + b
```

## Analysis

Let's take a deeper look at how a vectorized implementation may work on your computer behind the scenes.

1. Without Vectorization

   1. A for loop like this runs without vectorization. So if j ranges from 0 to 15 , this piece of code performs operations one after another.

   2. On the first time step. it first operates on the values at index 0.

   3. At the next time step, it calculates values corresponding to index 1 and so on until the 15th step, where it computes that.

   4. In other words, it calculates these computations one step at a time, one step after another.

e.g.

```py
for j in range(0,16):
    f = f + w[j] * x[j]
```

2. With Vectorization

   1. In contrast, this function in numpy is implemented in the computer hardware with vectorization. So the computer can get all values of the vectors w and x in a single step.

   2. It multiplies each pair of w and x with each other all at the same time in parallel.

   3. Then after that, the computer takes these 16 numbers and uses specialized hardware to add them all together very efficiently, rather than needing to carry out distinct additions one after another to add up these 16 numbers.

   4. This means that code with vectorization can perform calculations in much less time than code without vectorization.

   5. And this matters more when you're running learning algorithms on large data sets or trying to train large models, which is often the case with machine learning.
