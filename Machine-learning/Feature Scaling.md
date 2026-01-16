# Feature Scaling

## Leading

A technique called feature scaling that will enable gradient descent to run much faster.

## Process

1. Start by taking a look at the relationship between the size of a feature, that is how big are the numbers for that feature, and the size of its associated parameter.

2. Let's look at how you can implement feature scaling to take features that take on very different ranges of values and scale them to have comparable ranges of value to each other.

3. Feature Scaling

   1. Dividing by the maximum

      e.g. 300 ≤ $x_1$ ≤ 2000 $\;\;\;$ 0 ≤ $x_2$ ≤ 5

      then:
      $x_{1,scaled} = \frac{x_1}{2000}$ $\;\;\;$ $x_{2,scaled} = \frac{x_2}{5}$

      Result:
      0.15 ≤ $x_{1,scaled}$ ≤ 1 $\;\;\;$ 0 ≤ $x_{2,scaled}$ ≤ 1

   2. Mean Normalization

      1. start with the original features, and then rescale them so that both of them are centered around 0.

      2. so where as before, they only had values greater than 0, now they have both negative and positive values, but maybe usually between negative 1 and plus 1.

      3. to calculate the mean normalization of $x_1$, first find the average, also called the mean of $x_1$ on your training set. And let's call this mean $\mu_1$.

      4. Example: 300 ≤ $x_1$ ≤ 2000 $\;\;\;$ 0 ≤ $x_2$ ≤ 5

      then:
      $x_1 = \frac{x_1 - \mu _1}{2000-300}$ $\;\;\;$ $x_2 = \frac{x_2 - \mu _2}{5-0}$

      Result:
      $-0.18≤ x_1 ≤ 0.82 \;\;\; -0.46 ≤ x_2 ≤ 0.54$

   3. Z-score Normalization

      1. Denotion: standard deviation $\sigma$

      2. Example: 300 ≤ $x_1$ ≤2000 $\;\;\;$ 0 ≤ $x_2$ ≤5

      then:
      $x_1 = \frac{x_1 - \mu_1}{\sigma_1}\;\;\;x_2 = \frac{x_2 - \mu_2}{\sigma_2}$

      Result:
      -0.67 ≤ $x_1$ ≤3.1 $\;\;\;$ -1.6 ≤ $x_2$ ≤ 1.9

# Conclusion

1. When you have different features that take on very different ranges of values, it can cause gradient descent to run slowly.

2. But scaling the different features so they all take on comparable range of values can speed up gradient descent significantly.

3. As a rule of thumb, when performing feature scaling, you might want to aim for getting the features to range from maybe anywhere around -1 to somwhere around 1 for each feature $x_j$. (i.e.) aim for about $-1 ≤ x_j ≤ 1$ for each feature $x_j$

4. But these values -1 and 1 can be a little bit loose. So if the features range from -3 and 3 or from -0.3 to 0,3 or from 0 to 3 or from -2 to 0,5. They are all acceptable and it is OK if you do not rescale them.

5. However, if the range is like -100 ≤ $x_i$ ≤ 100 ， thn you'd better rescale this feature $x_i$ so that it ranges from something closer to -1 and 1. Similarly, if you have a feature $x_j$ that takes on really small values, say between -0.001 and 0.001 (e.g.) , then these values are so small. That may also means you should rescale them.

6. To recap, there's almost never any harm to carrying out feature rescaling, so when in doubt, just carry it out !

7. By using this skill, you will often be able to get gradient descent to run much faster. So that is the feature scaling , and with or without feature rescaling, when you run gradient descent, how can you probably know and check if gradient descent is really working ? If it is finding you the global minimum or something close to it ? Next we will take a look at how to recognize if gradient descent is converging. What's more, it will lead us to a discussion of how to choose a good learning rate for gradient descent.
