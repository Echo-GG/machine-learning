# Gradient Descent for Multiple Regression

## Leading

We've learnt about gradient descent about multiple linear regression and also vectorization. Let's put it all together to implement gradient descent for multiple linear regression with vectorization.

## Previous Notation

### Parameters

$w_1, ··· ,w_n$

b

### Model

$f_{\vec{w},b}(\vec{x}) = w_1 x_1 + ··· + w_n x_n + b$

### Cost Function

$J(w_1, ··· , w_n, b)$

### Gradient Descent

repeat{

$w_j = w_j - \alpha \frac{\partial{J(w_1,···,w_n,b)}}{\partial w_{j}}$

b = b - $\alpha \frac{\partial{J(w_1,···,w_n,b)}}{\partial b}$
}

## Vector Notation

### Parameters

$\vec{w} = [w_1\; ···\; w_n]$ (vector of length n)

b (still a number)

### Cost Function

$J(\vec{w},b)$

### Gradient Descent

repeat{

$w_j = w_j - \alpha \frac{\partial{J(\vec{w},b)}}{\partial {\vec{w}_{j}}}$

$b = b - \alpha \frac{\partial{J(\vec{w},b)}}{\partial b}$

}

##### One feature

repeat{

$w = w - \alpha \frac{1}{m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)})-y^{(i)})x^{(i)}$

（$ \frac{\partial{J(w,b)}}{w} = \frac{1}{m} \sum _{i=1}^{m} (f_{w,b}(x^{(i)})-y^{(i)})x^{(i)}$）

$b = b - \alpha \frac{1}{m}\sum _{i=1}^{m}(f_{w,b}(x^{(i)}) - y^{(i)})$

(simultaneously update w,b)

}

#### n features (n ≥ 2)

repeat{

$w_1 = w_1 - \alpha \frac{1}{m} \sum _{i=1}^{m} (f_{\vec{w},b}(\vec{x}^{(i)})-y^{(i)})x_1^{(i)}$

($\frac{\partial{J(\vec{w},b)}}{\partial{w_1}} = \frac{1}{m}\sum _{i=1}^{m}(f_{\vec{w},b}(\vec{x}^{(i)})-y^{(i)})x_1^{(i)}$)

···

$w_n = w_n - \alpha \frac{1}{m} \sum _{i=1}^{m} (f_{\vec{w},b}(\vec{x}^{(i)})-y^{(i)})x_n^{(i)}$

$b = b - \alpha \frac{1}{m} \sum _{i=1}^{m} (f_{\vec{w},b}(\vec{x}^{(i)})-y^{(i)})$

(simultaneously update $w_j (for\; j = 1, ··· , n) \;and \;b$)

}

## An alternative to gradient descent

### Normal equation

1. Only for linear regression

2. Solve for w,b without iterations

### Disadvantages

1. Doesn't generalize to other learning algorithms.

2. Slow when number of features is large (> 10,0000)

### What you need to know

1. Normal equation method may be used in machine learning libraries that implement linear regression.

2. Gradient descent is the recommended method for finding parameters w,b.
