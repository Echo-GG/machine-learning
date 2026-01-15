# Multiple Features

## Notations

1. x<sub>j</sub> = $j^{th}$ feature

2. n = number of features

3. $\vec{x}^{(i)}$ = features of $i^{th}$ training example

4. x<sub>j</sub>$^{i}$ = value of feature j in $i^{th}$ training example

## Comparison

### Model:

Previously: $f_{w,b}(x) = wx + b$

Now: $f*{w,b}(x) = w*{1}x*{1} + w*{2}x*{2} + w*{3}x*{3} + ··· + w*{n}x\_{n} + b $

### Rewrite:

1.  Parammeters of the model

    1. $\vec{w} = [w_1 w_2 w_3 ... w_n]$

    2. b is a number

    3. $\vec{x} = [x_1 x_2 x_3 ... x_n]$

2.  $f_{\vec{w},b}(\vec{x}) = \vec{w}·\vec{x} + b = w_1 x_1 + w_2 x_2 + w_3 x_3 + ··· + w_n x_n + b$
