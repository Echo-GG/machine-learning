# Cost Function

## General

The cost function will tell us how well the model is doing so that we can try to get it to do better.

## Target

1. To find w,b that make $\hat y$<sup>(i)</sup> is close to y<sup>(i)</sup> for all (x<sup>(i)</sup>,y<sup>(i)</sup>).

2. To reach this target, let's first take a look at how to measure how well a line fits the training data.

3. To do that, we are going to construct our cost function.

## Process

1. The cost function takes the prediction y hat and compares it to the target y by taking y hat minus y. This difference is called the error. We are measuring how far off the prediction is from the target.

2. Next, let's compute the square of this error. Also we are going to want to compute this term for different training examples in the training set. For example, we'll compute this squared error term.

   ($\hat y$<sup>(i)</sup> - y<sup>(i)</sup>)<sup>2</sup>

3. Finally, we want to measure the error across the entire training set. In particular, let's sum up the squared errors like this. We will sum from i equals 1,2,3 all the way up to m.
   $\sum_{i=1}^{m}(\hat{y}^{(i)}-y^{(i)})^2$

   1. m = number of training examples

   2. m is larger and your cost function will calculate a bigger number since it's summing over more examples. So to build a cost function that doesn't automatically get bigger as the training set size gets larger, by convention, we will compute the average squared error instead of the total squared error. And we do that by dividing m like this.

   $\frac{1}{m}\sum_{i=1}^{m}(\hat{y}^{(i)}-y^{(i)})^2$

   3. By convention, the cost function that machine learning people use actually divides bt 2 times m. The extra division by 2 is just meant to make some of our later calculations a little bit neater. Hwever, the cost function still works whether you include this division by 2 or not. So this expression right here is the cost function, and we're going to write J of WB to refer to the cost function. This is also called the squared error cost function, and it's called this because you're taking the square of these error terms.

   $J(w,b) = \frac{1}{2m}\sum_{i=1}^{m}(\hat{y}^{(i)}-y^{(i)})^2$

   4. And because of $\hat y^{(i)}$ = f<sub>w,b</sub>(x<sup>(i)</sup>), we can also write J(w,b) as $J(w,b) = \frac{1}{2m}\sum_{i=1}^{m}(f_{w,b}(x^{(i)})-y^{(i)})^2$
