# Method of moments for geometric random variable

The expectation for a geometric random variable with parameter p is given by:

![](https://render.githubusercontent.com/render/math?math=\mathbb{E}(X)=\frac{1}{p})

Let's see if you can use the method of moments to estimate the value of the parameter p.  This exercise is similar to the previous one that you completed for  the Bernoulli random variable.  As in that exercise, the aim is for you to write a code to investigate how the method of moments estimator for the parameter of a Geometric random variable depends on the number of samples that it is computed from.  To complete the exercise you will need to

1. Finish the  function `geometric`. This function should take a single argument `p`. It should return a Geometric random variable from a distribution with parameter `p`. 
2. Set the first element of the list called `indices` equal to 1, the second element of the list called `indices` to 2 and so on.
3. Set the first element of the list called `estimator` equal to an estimate of the parameter of the distribution that is calculated by generating 1 geometric random variable with parameter `pval`, the second element of the list `estimator` equal to an estimate of the parameter of the distribution that is calculated by generating 2 geometric random variables with parameter `pval`, set the third element of the list called `estimator` equal to an estimate of the parameter of the distribution that is calculated by generating 3 geometric random variables with parameter `pval` and so on until you have computed an estimate of the parameter of the distribution from 200 geometric random variables. 

When your code is complete a graph will be generated.  The red dots are the values of the method of moments estimator for the parameter of the distribution you sampled from.  The black dashed line is then the true value of the parameter.  You should see that the estimator converges to the true value of the parameter.
