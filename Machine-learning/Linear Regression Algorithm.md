# Linear Regression Algorithm

1. Linear Regression Model

   $f_{w,b}(x) = wx + b$

2. Cost Function

   $J(w,b) = \frac{1}{2m}\sum*{i=1}^{m}(f*{w,b}(x^{(i)}) - y^{(i)})^{2} $

3. Gradient Descent Algorithm

   repeat until convergence {

   w = w - $\alpha$ $\frac{\partial J(w,b)}{\partial w}$

   b = b - $\alpha$ $\frac{\partial J(w,b)}{\partial b}$

   }

4. Derivative Parts

   1. $\frac{\partial J(w,b)}{\partial w}$

      $\frac{\partial J(w,b)}{\partial w} = \frac{1}{m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)}) - y^{(i)})x^{(i)}$

   2. $\frac{\partial J(w,b)}{\partial b}$
      $\frac{\partial J(w,b)}{\partial b}$ = $\frac{1}{m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)}) - y^{(i)})$

## Algorithm

repeat until convergence{
w = w - $\alpha$ $\frac{1}{m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)}) - y^{(i)})x^{(i)}$
b = b - $\alpha$ $\frac{1}{m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)}) - y^{(i)})$
}

(Update w and b simultaneously.)

## Issue

One issue we saw with gradient descent is that it can lead to a local minimum instead of a global minimum, where the global minimum means the point that has the lowest possible value for the cost function J out of all possible points.

The cost function does not and will never have multiple local minima. It has a single global minimum because of this bowl shape.

The technical term for this is that this cost function is a convex function. Informally, a convex function is a bow-shaped function, and it cannot have any local minima other than the single global minimum.

So when you implement gradient descent on a convex funciton, one nice property is that so long as your learning rate is chosen appropriately, it will always converge to the global minimum.

Later, we will see this algorithm in action.
