# Week 1
# 1. Math Refresher
## Overview
* Order of Operations (PEMDAS)
* Scientific Notation
* Interval Notation
* Equation of a line
* Slope/Derivative
* Summations/Integrals
* Products
* Factorials

# 2. Data Basics
# Overview
* Defining the Research Question
    * Population
    * Observational Unit (Case)
    * Variables
* Data Matrices
* Types of Variables
    * Numerical / Quantitative
    * Cardinal / Ordinal
* Relationships between Variables 

# 3. Introduction to Data in Python
## Overview
* Python Variables
* Python Data Elements
* Python Iterables
* Numpy
* Pandas
* Python Functions
### Note:
* Python rounds to the nearest even integer on a tie

# 4. Data Collection
## Overview
* Study Design
* Sampling and Census
* Sources of Data
* Experimental Design
* Preparing for Data Collection


# 5. Summarizing Numerical Data
## Overview
* Central Tendency
* Skewness
* Variability
* Quantiles
* Parametric and Nonparametric interpretations


# 6. Visualizing Numerical Data
## Overview
* Intro to visualization in Python
* Rug plot
* Histogram
* Kernel Density Estimation (KDE) plot
* Box Plot
* Scatterplot
* Combined Plots
    * pairplot
    * joinplot
* Finalizing your plots


# Week 2
# 7. Summarizing Categorical Data
## Overview
* Tabular Summaries
* Bar Graph
* Pie Chart
## Categorical or Qualitative Data
* Class: Each category for classification of qualitative data
* Class Frequency: Number of observation falling into a particular class
* Class Relative Frequency ($ \hat{p} $)
* Class percentage

## Tables
* Contingency (Frequency) table
* Relative Frequency Table

## Graphs
* Bar graph
* Pie Chart

# 8. Introduction to Probability
## Overview
* Probability and Statistics
* Events
* Sets
* Venn Diagrams
* Rules of Probability

## Probability and Statistics
* Descriptive Statistics: sample data to describe something about the population
* Probability: assumptions of the population to infer about a sample

## Definitions
* Event: A specific set of possible outcomes of an experiment
* Simple Event: Set of a single possible outcome of an experiment
* Compound Event: Set of multiple simple events
* Sample Space: The set of all possible outcomes of an experiment
* $𝑝_𝑖$: The probability of the ith event in the sample space occurring
* $𝑃(𝐴)$ : The probability of any outcome in the event 𝐴𝐴 occurring

## What is Probability
Probability is a map of events from a sample space to the interval [0,1]
* probability of any event mus lie between 0 and 1
* total probability of entire sample space must equal 1

## Calculating Probability (Discrete Events)
## Sets
* Union
* Intersection
* Complement

## More Definitions
* Marginal Probability: one event  
    $ P(A=A_i) = P(A_i) = p_i $
* Joint Probability: two events  
    $ P((A=A_i)\cap(B=B_j))=P(A_i \cap B_j) = p_{i,j} $
* Disjoint (Mutually Exclusive): no overlap in events
* Collectively Exhaustive: events that cover entire sample space
* Partition: set of events that are both disjoint and collectively exhaustive
## Probability Rules
### Compliment
### Law of Total Probability
### Additive Rule
### Disjoint Events

# 9. Conditional Probability
## Overview
* What is Conditional Probability
* Calculating conditional probability
* Independence
* Multiplication Rule
* Bayes's Rule

## Conditional Probability
$ P(A|B) = \frac{P(A\cap B)}{P(B)} $

## Multiplication Rule
$ P(A|B)P(B) = P(A \cap B) $ as long as $ P(B) \ne 0 $

## Independence of Events
If and only if A and B are independent events,  
$ P(A|B) = P(A) $  
$ P(B|A) = P(B) $  
$ P(A \cap B) = P(A) \times P(B) $

## Bayes's Rule
$ P(B_i|A) = \frac{P(B_i)P(A|B_i)}{\sum_{j=1}^{k}P(B_j)P(A|B_j)} $


# 10. Counting Problems
## Overview
* What is a counting problem?
* Replacement
* Order
* Counting rules

## What are counting problem?
* Counting problems are defined by calculating the number of possible
outcomes of some process
* Examples:
    * There are 24 students in the class, and I split the class into groups of 4. How many different groups could you be a part of?
    * A raffle has 3 different prizes. 213 people bought tickets. How many ways can the prizes be divided up?

## Formulation
* $ n $ : population of possibilities
* $ r $ : size of the selection (always less than $ n $)
* Looking for total possible arrangements of size $r$ from $n$ possibilities
* Replacement
    * With: Any of the $n$ possibilities may be chosen repeatedly
* Order
    * Does order of select matter? (is HHT considered the same as HTH?)
## Counting rules
* see table in slides
* Permutation: without replacement, order matters 
* Combination: without replacement (typically), order doesn't matter 

# 11. Intro to Random Variables
## Overview
* Random Variables
* Discrete Random Variables
* Expectation
* Variance
* Continuous Random Variables
* Linear Combinations of Random Variables
* Other Probability Functions
## Random Variable
* A random variable (RV) is a mapping that assigns numerical values to the possible outcomes of an experiment such that each sample point is represented by a unique numerical value
## Discrete Random Variables
* discrete random variable: a random variable that assumes a countable number of values
* probability mass function (pmf): the function that maps outcomes to probabilities
## probability mass function (pmf)
* fully defines a distribution $ f(x) = P(X=x) $
## Cumulative Distribution Function (cdf)
* also fully defines a distribution
* partial sum $ F(x) = P(X \le x) $
## Expectation 
* The expected value or expectation $E(X)=\mu$ is the mean observation expected to be observed from a random variable
## Variance
* the variance $ (\text{Var}(X) = \sigma^2) $ is the expected squared deviation from the mean    
## Standard Deviation

## Continuous Random Variables
* assumes uncountable number of values
## Probability Density Function
## Cumulative Distribution Function
## Expectations of Continuous RVs
## Linear Combinations
* A linear combination of random variables $X$ and $Y$ can be written as $ aD + bY $ where $ a $ and $ b $ are any real numbers.  
* Expected Value: $ E(aX + bY) = aE(X) + bE(Y) = a\mu_X + b\mu_Y $ 
* Variance: $ \text{Var}(aX + bY) = a^2\text{Var}(X) + b^2 \text{Var}(Y) = a^2 \sigma_x^2 + b^2 \sigma_Y^2 $
* Standard Deviation: $ \sigma_{aX+bY} = \sqrt{a^2 \sigma_x^2 + b^2 \sigma_Y^2} $
## Other Probability Functions
* Percentile Point Function (ppf): inverse of the cdf - the input of the ppf is the desired quantile and the ppf gives you that quantile
* Survival Function (sf): (1 - cdf): $ x \rightarrow P(X > x) $
* Inverse Survival Function (isf): $  P(X > x) \rightarrow x  $
### Inverse Functions for Discrete Distributions
* interpretation is slightly different with discrete distributions
## Summary Table of Probability Functions
| **Function**          | **Input/Argument** | **Output**     |
|-----------------------|--------------------|----------------|
| pmf (discrete only)   | $ x $              | $ P(X = x) $   |
| pdf (continuous only) | $ x $              | $ f(x) $       |
| cdf                   | $ x $              | $ P(X \le x) $ |
| ppf                   | $ P(X \le x) $     | $ x $          |
| sf                    | $ x $              | $ P(X > x) $   |
| isf                   | $ P(X > x) $       | $ x $          |

# Week 3
# 12. Probability Distribution Families
## Overview
* Location Families
* Scale Families
* Location and Scale Families  

Families are groups of probability distributions with similar characteristics

## Location Families
$f(x-\mu)$

## Scale Families
$ \frac{1}{\sigma}f(\frac{x}{\sigma}) $


## Location and Scale Families
$ \frac{1}{\sigma}f(\frac{x - \mu}{\sigma}) $

# 13. Discrete Distributions
## Overview
* Uniform Distribution
* Bernoulli Distribution
* Geometric Distribution
* Binomial Distribution
* Poisson Distribution

## Discrete Uniform Distribution
* every outcome is equally probable

$ \mu = \frac{n+1}{2} $ 
$ \sigma^2 = \frac{n^2+1}{12} $

`scipy.stats.randint(k, low, high, loc=$𝜇$)`

## Bernoulli Distribution
Let an outcome of interest (“success”) be denoted
by $𝑋𝑋 = 1$ and any other outcome (“failure”) be
denoted by $𝑋𝑋 = 0$.  

In a Bernoulli trial, success occurs with probability $𝑝$.
The Bernoulli distribution represents a single Bernoulli trial.

$\mu = p$  
$\sigma^2 = 𝑝 (1 − p)$

`scipy.stats.bernoulli(k, p=𝑝, loc=𝜇)`


## Geometric Distribution

`scipy.stats.geom(k, p=𝑝, loc=𝜇)`

## Binomial Distribution
Now consider a fixed number 𝑛 of iid Bernoulli trials
are conducted. Let 𝑋 be the total number of
successes.

$\mu = np$  
$\sigma^2 = np (1 − p)$

`scipy.stats.binom(k, n=𝑛, p=𝑝, loc=𝜇)`


## Poisson Distribution
Let 𝑋 be the number of occurrences of some event
within a specific interval, where that events occurs
on average 𝜆 (lambda) times per interval

$𝑋~\text{Poisson}(\lambda)$

$\mu = \lambda$  
$\sigma^2 = \lambda$

`scipy.stats.poisson(k, mu=𝜆, loc=𝜇)`

# 13. Continuous Distributions - Part 1
## Overview
* Normal distribution
* Students $t$ distribution
* Chi Squared distribution
* F distribution

## Normal Distribution
𝑋~N (𝜇, 𝜎)  
$ f_{\mu,\sigma}(x) = \frac{1}{\sigma \sqrt{2\pi}}e^{-(\frac{(𝑥−𝜇)^2}{2\sigma^2})}$

𝜇𝜇 = 𝜇𝜇
𝜎𝜎2 = 𝜎𝜎2

`scipy.stats.norm(x, loc=𝜇, scale=𝜎)`

## Student's $t$-distribution
The $t$ distribution with 𝜈 = 𝑛 − 1 degrees of freedom
corrects for randomness in the observed variance of
a sample of size 𝑛. For large samples (𝑛 → ∞) this
converges to the standard normal distribution.


`scipy.stats.t(x, df=𝜈, loc=𝜇, scale=𝜎)`

## Chi-Squared Distribution
The sum of the squares of k independent random
variables 𝑍𝑍1, 𝑍𝑍2, … , 𝑍𝑍𝑘𝑘~𝑁𝑁 0,1 is itself a random
variable distributed 𝜒𝜒2 with k degrees of freedom.

`scipy.stats.chi2(x, df=𝑘, loc=𝜇, scale=𝜎)`

## F Distribution
The ratio of two independent 𝜒𝜒2-distributed random
variables divided by their degrees of freedom is a
random variable that is F distributed.

$r$ is the degrees of freedom

`scipy.stats.f(x, dfn=𝑟1, dfd=𝑟2, loc=𝜇, scale=𝜎)`

# 15. Continuous Distributions - Part 2
## Overview
* Lognormal Distribution
* Exponential Distribution
* Beta Distribution
* Uniform Distribution
* Other Distributions

## Lognormal Distribution
Lognormal is a common distribution when
something is approximately normally distributed but
can only take positive values.

Like the 𝜒2 distribution, it is derived from the
Standard Normal (Z)

Note that 𝜇 and 𝜎 are not the mean and standard
deviation for this distribution.

`scipy.stats.lognorm(x, s=𝜎, loc, scale)`


## Exponential Distribution
The exponential distribution is often used to model
time to failure in reliability modeling.
It is notable for having the memorylessness feature:
𝑃 (𝑋 > 𝑥1 + 𝑥2) = 𝑃(𝑋 > 𝑥2 | 𝑋 > 𝑥1)
What does this mean? It means the probability of
failure in the next 2 minutes is the same whether the
component has just been replaced or it has been
operating for 1000 hours.
In other words, it represents time between events
that occur with a constant rate – a “homogeneous
Poisson process”

`scipy.stats.expon(x, loc, scale)`

## Beta Distribution
Beta is a flexible distribution for values
between 0 and 1 – very useful for
applications where the RV is a proportion
Varying parameters α>0 and β>0 can
result in:
 Increasing distributions 𝛼𝛼 > 1, 𝛽𝛽 = 1
 Decreasing distributions (
)
𝛼𝛼 = 1, 𝛽𝛽 > 1
* U-shaped distributions 𝛼𝛼 < 1, 𝛽𝛽 < 1
* Unimodal distributions 𝛼𝛼 > 1, 𝛽𝛽 > 1
* Symmetric distributions $(\alpha = \beta)$

`scipy.stats.beta(x, a=𝛼, b=𝛽, loc, scale)`

## Uniform Distribution


`scipy.stats.uniform(x, loc, scale)`


## Other Distributions
* Weibull distribution
* A more flexible form of the exponential distribution used in reliability modeling
* Exponential is a special case of Weibull
* Gamma distribution
* Very flexible distribution used to approximate odd distributions
* Exponential and 𝜒𝜒2 are special cases of Gamma
* Cauchy distribution
* This distribution breaks everything. It has no finite mean or variance.
* Equivalent to the 𝑡𝑡 𝜈𝜈 = 1
* Double exponential (Laplace) distribution
* This is a symmetric version of the exponential distribution defined for all 𝑥𝑥 ≠ 0

# 16. Central Limit Theorem
## Overview
* Population distribution
* Sampling Distribution
* Central Limit Theorem (CLT)
* Example applications
* Simulations

## Population distribution
So far, we have mostly been talking about the population distribution
* Each case is a single observation
* Observational unit is one member of the population  

We want to make inferences on the parameters of the population distribution

## Sampling Distribution
The sampling distribution is the distribution of point estimates of the
population parameters
* Each case is a point estimate calculated from the sample
* Observational unit is one sample
* The sampling distribution is not observed unless the experiment is
repeated

Every sample will have some variability in point estimates, but it will be less
than that of the population

### Standard Error
The standard error about the mean is the standard deviation of the sampling distribution of sample means.
Given population standard deviation $\sigma$, the standard error is

$ \sigma_{\bar X} = \frac{\sigma}{\sqrt{n}}$

We can estimate this using a sample standard deviation

$ s_{\bar X} = \frac{s}{\sqrt{n}} = \sqrt{\sum_{i=1}^{n}\frac{(x_i - \bar x)^2}{n(n - 1)}} $


## Central Limit Theorem (CLT)  

Let $X_1, X_2, ..., X_n$ be a random sample from a distribution with mean $\mu$ and variance $\sigma^2$. If the sample size $n$ is sufficiently large, then 
* The sample mean $\bar X$ follows an approximate normal distribution with mean $\mu_{\bar X} = \mu$ and variance $\sigma_{\bar X}^2 = \frac{\sigma^2}{n}$. 

That is, the sampling distribution of the sample mean is approximately normally distributed **regardless of the distribution of the underlying random sample**. This includes discrete and  continuous distributions.
* Exception: distributions for which mean/variance do not exist.

The meaning of “sufficiently large” depends on the median, mean, and mode. If the distribution of $X_i$ is…
*  Symmetric, unimodal, and continuous  
    Sample size as small as 5-10 is sufficient
* Skewed, multimodal, or discrete  
    Sample size of 25-30 is typically sufficient
* Extremely skewed  
    Even larger samples may be required (rarely more than 100)

For binomial distribution, $np \ge 10$ and $n(1-p) \ge 10$.



## Example applications
See slides

## Simulations
See notebook

# Week 4 - Confidence Intervals and Hypothesis Tests

# 17. Confidence Intervals
Chapter 5.2-5.3, 7.1

This lesson covers confidence intervals and prediction intervals. The focus is on using the t distribution to infer a range of likely values for the population mean, but the concept is broadly applicable to other distributions and other parameters.

## Overview
* What is a confidence interval
* How to construct a confidence interval
* What assumptions are required?
* Python application
* Prediction intervals

## Standard Error
* standard error about the mean  
$ s_{\bar X} = \frac{s}{\sqrt{n}} = \sqrt{\sum_{i=1}^{n}\frac{(x_i - \bar x)^2}{n(n - 1)}} $

## What is a confidence interval
A 100(1-α)% Confidence Intervalis a range of values within which the true parameter value will fall for 100(1-α)% of gathered samples.  
In other words, if you built equivalent confidence intervals for 100 random samples from the same population, you would expect the true parameter to fall within 95 of those intervals.  
This is what it means to be, for example, 95% confident.

## How to construct a confidence interval
* Define your desired level of confidence (1−𝛼)
* Define the type of confidence interval
* Symmetric, asymmetric, one-sided
* Define the sampling distribution
* Any assumptions must be supported by data and sample size  

We’ll start by looking at symmetric CIs using a normal sampling distribution

### Margin of Error
### Confidence Interval about the Mean
$ ci = \bar x \pm \text{SEM} \times N_{PPF}(1 - \frac {\alpha}{2})$

### Inverse Function for Discrete Distributions
### Binomial CIs

## What assumptions are required?
* **Always**: Independent and identically distributed (iid) data collection
* Type of data: numerical or categorical
* Distribution: typicallynormal or t(CLT), but may be another distribution
* Sample size: must be sufficient to justify distributional assumption

## Python application


## Prediction intervals
A 100(1-α)% Prediction Interval is a range of values within which the next observation is expected to fall 100(1-α)% of the time.  
In other words, if you collected a random sample of 100 new data points from the same population, you would expect 95 of those observations to be within that interval.

$ ci = \bar x \pm \sqrt{\frac{1}{n}}s \times t_{PPF,v=n-1}(1 - \frac {\alpha}{2})$

$ pi = \bar x \pm  \sqrt{1+\frac{1}{n}}s \times t_{PPF,v=n-1}(1 - \frac {\alpha}{2})$



# 18. Hypothesis Test Formulation
Chapter 5.3, 7.1  

This lesson covers the fundamental of formulating a hypothesis test. We'll cover lots of different hypothesis tests in this course, but they all share the same general formulation. As always, spending the time to define the problem well is very valuable!

“If I had an hour to solve a problem I'd spend 55 minutes thinking about the problem and 5 minutes thinking about solutions.” ― Albert Einstein

## Overview
* What is a hypothesis test?
* Defining the hypotheses
* Choosing a test statistic
* Setting the significance level
* Defining the rejection region
* $p$-values: what are they good for?

## What is a hypothesis test?
A hypothesis test or significance test uses data to summarize the evidence about a hypothesis by comparing a point estimate of the parameter of interest to the value predicted by the hypothesis.  
So we have the following elements:  
* Hypothesis (null and alternative)
* Point estimate of parameter (test statistic)
* Predicted value of parameter (sampling distribution)
* Conclusion  

We also must consider assumptions under which a test is valid.

### Assumptions
Each type of hypothesis test requires varying assumptions pertaining to:  
* Type of data: numerical or categorical
* Distribution: depends on the hypothesis test
* Sample size: must be sufficient to justify distributional assumption  

And of course, they always assume independent and identically distributed (iid) data collection

## To build a Hypothesis Test
1. Define the hypotheses (null and alternative)
* Parameter of interest
* Left-, right-, or two-tailed
2. Choose the significance level (\alpha)
3. Choose a test statistic
4. Define the rejection region
* This may be in terms of test statistic or $p$-value
5. Calculate the test statistic and/or $p$-value
6. Make a conclusion

## Defining the Hypothesis
### Hypotheses - Null hypothesis
Hypothesis are formulated before analyzing the data.
The null hypothesis $(H_0)$ is a statement that a parameter takes a particular value. This will be assumed to be true, but it cannot be proved to be true.  
$H_0:\mu = \mu_0$  
$H_0:\sigma^2 = \sigma_0^2$  
$H_0:\pi = \pi_0$  

### Alternate Hypothesis
The alternative hypothesis $(H_a)$ states that a parameter falls in another range. This is usually a research hypothesis the investigator believes to be true. Data is collected to attempt to support this.  
May be one-sided or two-sided.

### Key Terms
* Rejection Region
* Non-rejection Region
* Critical Value

## Choosing a test statistic
We use data to calculate a test statistic, which summarizes how far the observed point estimate falls from the parameter value in $H_0$.  
This value is examined in terms of the assumed sampling distribution.  
Sampling distribution assumptions define the type of hypothesis test, based on factors such as
* Parameter of interest (mean, median, variance, proportion, distribution)
* Data collection method (paired observation, independence, sample size)

## Setting the significance level
* \alpha
## Defining the rejection region
## $p$-values: what are they good for?
* The $p$-value is the probability, presuming that $H_0$ is true, that a sample would be collected with a test statistic that equals the observed value or a value even more extreme in the direction predicted by $H_a$  
* Traditionally, p-values are used to choose between conclusions according to some pre-selected significance value $\alpha$, which represents the probability of a Type I Error (confidence is $1−\alpha$)

## Statistical Errors
* Type I (false positive)
* Type II (false negative)

## Example
* Grocery Store Checkout

## $p$-values: What are they bad for?
* how to use them


# 19. One-Sample Tests of Central Tendency
Chapter 6.1, 7.1  
This lesson covers one-sample tests of measures of central tendency: 

* Large-sample test about the mean (z test)
* One-sample test about the mean (t test)
* One-sample test about the median (Wilcoxon Signed Rank Sum test)
* One-sample test about the proportion (Binomial test)

**Important Note**: I used the stats.binom_test() function in this lesson. I noticed afterwards that this function has been deprecated. The recommended stats.binomtest() function has the following differences:

1. Input is appropriately k instead of x,
2. It returns an object instead of only a p-value, and
3. That returned object contains many useful outputs.  
The p-values should be identical between the two functions, and they both continue to function for now. The stats.binomtest().proportion_ci(confidence) now gives you the associated confidence interval (one-sided or two-sided), so that's a benefit of the new function.

## Overview
* Large-Sample Test about Mean/Proportion ($z$ test)
* One-Sample Test about Mean ($t$ test)
* One-Sample Test about Median (Wilcoxon Signed Rank Sum)
* One-Sample Test about Proportion (Binomial test)

* Fundamentally, hypothesis tests are the same
    * They test whether the evidence supports an alternative hypothesis
* Each test is based on different assumptions
    * Number of samples/treatments
    * Parameter of interest
    * Distributional assumptions
    * Sample size

## Large-Sample Test about Mean/Proportion ($z$ test)
### Assumptions
* Type of data – Numerical
* Randomization – Data gathered randomly (iid)
* Population distribution – Assumes population data distributed 𝑁𝑁𝜇𝜇,𝜎𝜎2, but test is robust to deviations thanks to Central Limit Theorem
    * A method is said to be robustwith respect to an assumption if it performs adequately even when that assumption is violated.
* Sample size –Used only for large sample sizes (think CLT)  𝑛𝑛≥30,𝑛𝑛𝑛𝑛>10,𝑛𝑛1−𝑝 >10
### Hypotheses
Null hypothesis: The mean is equal to some known value  
𝐻𝐻0:𝜇𝜇=𝜇𝜇0  
Alternative hypothesis: The mean is not equal to the known value in some way (depends on the research hypothesis)  
𝐻𝐻𝑎𝑎:𝜇𝜇<𝜇𝜇0,𝐻𝐻𝑎𝑎:𝜇𝜇>𝜇𝜇0,𝐻𝐻𝑎𝑎:𝜇𝜇≠𝜇𝜇0  

### Test Statistic
Assuming the population is distributed 𝑁𝑁𝜇𝜇,𝜎𝜎2, the sampling distribution is 𝑁𝑁𝜇𝜇,𝜎𝜎2𝑛𝑛. We’ll normalize our results to the sampling distribution.
The test statistic is then
𝑍𝑍=􀴤𝑋𝑋−𝜇𝜇0𝑆𝑆𝑆𝑆𝑆𝑆where𝑆𝑆𝑆𝑆𝑆𝑆=𝜎𝜎2𝑛𝑛=𝜎𝜎𝑛𝑛≈𝑠𝑠𝑛𝑛
### Conclusion
Rejection region varies on the alternative hypothesis.
### $p$-value
Presuming that 𝐻𝐻0 is true, the probability of observing a test statistic 𝑍𝑍 more extreme than the one observed 𝑧𝑧 is:  
If 𝐻𝐻𝑎𝑎:𝜇𝜇<𝜇𝜇0, 𝑝 =𝑃𝑃Z<z=𝑁𝑁𝐶𝐶𝐶𝐶𝐶 𝑧𝑧  
If 𝐻𝐻𝑎𝑎:𝜇𝜇>𝜇𝜇0, 𝑝 =𝑃𝑃Z>z=𝑁𝑁𝑆𝑆𝑆 𝑧𝑧  
If 𝐻𝐻𝑎𝑎:𝜇𝜇≠𝜇𝜇0, 𝑝=𝑃𝑃𝑍𝑍>𝑧𝑧=2×𝑁𝑁𝑆𝑆𝑆 𝑧𝑧   
### Example: General Social Survey (GSS)
### When (not) to use a z-test

## One-Sample Test about Mean ($t$ test)
### Assumptions
* Type of data – Numerical
* Randomization – Data gathered randomly (iid)
* Population distribution – Assumes population data distributed $N(\mu,\sigma^2)$, but test may be robust depending on actual distribution and sample size
* Sample size – Can be used for small sample size

### Hypotheses
Null hypothesis: The mean is equal to some known value  
𝐻𝐻0:𝜇𝜇=𝜇𝜇0  
Alternative hypothesis: The mean is not equal to the known value in some way (depends on the research hypothesis)  
𝐻𝐻𝑎𝑎:𝜇𝜇<𝜇𝜇0,𝐻𝐻𝑎𝑎:𝜇𝜇>𝜇𝜇0,𝐻𝐻𝑎𝑎:𝜇𝜇≠𝜇𝜇0 
### Test Statistic
### Conclusion
### P-value

## One-Sample Test about Median (Wilcoxon Signed Rank Sum)
### Assumptions
* Type of data –Quantitative
* Randomization –Data gathered randomly (iid)
* Population distribution –No assumptions
* Sample size –Can be used for small sample size
### Hypothesis
### Test Statistic
$W$
### Conclusion
### Why Wilcoxon?
First, to introduce you to non-parametric statistics, which don’t rely upon distributional assumptions and instead use fields such as order statisticsand the binomial distribution.  
Second, the Wilcoxon signed-rank sum test is a powerful non-parametric test analogous to the t-test. With small samples and highly skewed data, it is a great choice.


## One-Sample Test about Proportion (Binomial test)
### Assumptions
### Hypothesis
### Test Statistic
* sum of the bernoulli trials
### Conclusion


# 20. Sample Size and Power
Chapter 7.4  
This lesson covers the trade-offs in deciding on values for sample size, confidence/significance, and power. 

**Important Note**: I forgot to mention in the lesson that the Python input effect_size for sms.tt_solve_power() is not the difference to detect, but the difference to detect as a multiple of the standard deviation. I allude to this while discussion changing variance and changing detectable difference, but I forgot to state it plainly.

So, if the difference to detect is $\delta = 2$ and the variance is $\sigma^2 = 4$, then the effect_size would be $\frac{\delta}{\sigma} = \frac{2}{\sqrt{4}} = 1$.

Also, in contrast to other functions, the options for alternative are 'two-sided', 'larger', and 'smaller'.

## Risk-Based Experimental Design
* $\alpha$ is set to a value depending on the acceptable risk of a False Positive. We say we are $100(1 - \alpha)%$ confident in the result.  
* $\beta$ can also be set to a value depending on the acceptable risk of a False Negative specific to an alternative valueof the parameter of interest.
## Rod Manufacturing Example
* how many samples do need to take?
## What is "power"?
* $\alpha$ is significanve 
* $(1 - \alpha)$ is confidence
* $(1 - \beta)$ is power
## Determining Sample Size
* could use z-test and iterate up ... or
* Use python statsmodels.stats, give it three of four arguments and get the fourth as a response
    * Effect size ($\delta$) \*
    * Sample size ($n$)
    * Significance ($\alpha$)
    * Power ($1 - \beta$)  

\*Note that `effect_size` for `sms.tt_solve_power()` is as a multiple of the standard deviation. So `effect_size` = $ \frac{\delta}{\sigma}$ 

## Non-parametric note
* power is not well defined

## How can I increase power?
* Increase sample size
* decrease confidence (increase significance ($\alpha$))
* Increase Detectable Difference ($\delta$)
* Reduce Porcess Variance ($\sigma^2$)

## Recap
Power ($1-\beta$) is the probability of currectly rejecting


# 21. Two-Sample Test of Central Tendency
Chapter 6.2, 7.2, 7.3  

This lesson covers two-sample tests of measures of central tendency:  
* Paired-sample tests
* Independent 2-sample test about mean (2-sample independent t-test)
* Independent 2-sample test about median (Mann-Whitney U test)

## Overview
* Paired samples test
* Independent 2-sample test about mean (2-sample $t$ test)
* Independent 2-sample test about median (Mann-Whitney U test)

## Paired samples test
### Independent vs Paired Sampling
* Paired Samplesare equally sized samples for which data points can be matched in a way that may be expected to reduce variance
    * Samples are correlated somehow, typically using the same observational unit under differing conditions
* Independent samples are two, non-correlated samples, possibly of different sizes
### How to perform a paired test
Given observations $x_1, ..., x_n$ and $y_1, ..., y_n$
1. Let $d_i = x_i - y_i$.
2. Perform a one-sample test on $d_1, ..., d_n$.

## Independent 2-sample test about mean (2-sample $t$ test)
### Assumptions
* Type of data –Still quantitative
* Randomization –Data gathered randomly (iid)
* Population distribution –Assumes normality, but varies depending on
    * Pooled variance: Assumption that samples come from populations with the same variance (homoscedasticity)
    * Different variance: No such assumption (heteroscedasticity)
* Sample size –same concerns regarding Central Limit Theorem
### Hypotheses
 * the difference in the means is some hypethesized value
### Pooled Variance
If the variance of each sample is approximately equal, we can improve test precision by pooling the variance measure.

## Independent 2-sample test about median (Mann-Whitney U test)
### Nonparametric 2-sample test
* When we have ordinal data or cannot make distributional assumptions, we can use the Mann-Whitney U Test
    * Sometimes confusingly called the Wilcoxon Rank-Sum Test
* Null hypothesis: Distributions of both populations are equal
* Alternative hypothesis: Distributions are not equal

* Can be interpreted as a test of difference in medians.




# 22. Tests of Normality
This lesson covers graphical and analytical testing of normality, primarily to justify using that assumption in hypothesis tests and other statistical techniques. We will use QQ-plots, the Shapiro-Wilk test, and the Omnibus test. 

## WhyTest for Normality?
Most statistical tests we’ve discussed assume normality in data. That assumption won’t go away in the second half of the course.  
We must apply due diligence to confirm this assumption. Some strategies:
* Visual: QQ-Plots
* CDF Comparison Tests: Kolmogorov-Smirnov test, Lilliefors test, Anderson-Darling test, Shapiro-Wilk test
* Moment-based Tests: D’Agostino-Pearson Omnibus test  

Details on how these tests work are beyond the scope of this course, but let’s look at how to use them.

## When to Use Each Test
* Visual – **always**
* Shapiro-Wilk test – Small samples ($n<100$)
    * High power in even small samples
    * May be overly sensitive especially for large samples
* Omnibus test – Large samples ($n>100$)
    * Creates a test statistic from mean, variance, skewness, and kurtosis
    * Not overly sensitive for large samples
* Kolmogorov-Smirnov test –For distributions other than normal
    * Anderson-Darling can also be used.

## Visual Inspection
* QQ-plot - observed vs expected quantiles of distribution

## Python tests
* It is good practice to test normality computationally, especially for small samples, but remember that statistical significance is not the same as practical significance.
* Small samples: `stats.shapiro(data)`
* Large samples: `stats.normaltest(data)`
* Exponential, Logistic, Gumbel distributions:`stats.anderson((data-np.mean(data))/np.std(data, ddof=1)), dist=‘dist’)`
* Other distributions: `stats.kstest((data-np.mean(data))/np.std(data, ddof=1)), cdf=‘dist’)`
    * Note:‘dist’ should be any of the dist.*distributions, i.e., ‘norm’, ‘expon’, ‘binom’, etc.




# Week 5 
# 23. Tests of Variability
Last week we covered a lot of hypothesis tests focusing on measures of central tendency (mean, median, and proportion). For this lesson the focus is on hypothesis tests for variance, a measure of variability. Two tests are covered: the one-sample (chi-squared) test and the two-sample (F) test.

## Overview
* One-Sample Test of Variance ($\chi^2$ test)
* Two-Sample Test of Variance (F test)

## One-Sample Test of Variance ($\chi^2$ test)
### Assumptions
* Type of data –Quantitative
* Randomization –Data gathered randomly (iid)
* Population distribution –Assumes population data distributed 𝑁(𝜇,𝜎2)
* Sample size –May be used for any sample size, but normality is extra important for small samples
### Hypotheses
$H_0:\sigma^2 = \sigma_0^2$
### $\chi^2$ Distribution Review
* in the equeaitons $s$ is the observed sample stadard deviation and $\sigma$ is the hypothesized standard deviation
### Python Functions
* not built into Python, but instructor created functions for it. 
    * chi2_1samp_var_stats if you have summary statistics
    * chi2_1samp_var_data if you have raw data

### Critical observation calculation
* to find the value of the sample variance where you would reject the null hypothesis

## Two-Sample Test of Variance (F test)
### Assumptions
* Type of data –Quantitative
* Randomization –Data gathered randomly (iid)
* Population distribution –Assumes population data distributed normally
* Sample size –May be used for any sample size, but normality is extra important for small samples
### Hypothesis
$H_0:\sigma_1^2 = \sigma_2^2$
### F Distribution Review
### Python Functions
* not built into Python, but instructor created functions for it. 
    * F_2samp_var_stats if you have summary statistics
    * F_2samp_var_data if you have raw data



# 24. Analysis of Variance
Chapter 7.5

This lesson covers the Analysis of Variance (ANOVA) hypothesis test for equality of means across multiple groups. This is such a powerful test! The concepts of this lesson also apply very strongly to the second half of this course. If there is a lesson to pay close attention to, this is the one!
## Overview
* Introduction to Design of Experiments (DoE)
* One-Factor Experiments (One-Way ANOVA)
* Two-Factor Experiments (Two-Way ANOVA)
* Many-Factor Experiments

## Introduction to Design of Experiments (DoE)
### Observational study vs Designed experiment
Comparisons of two population means often result from *observational studies*, when outcomes are observed but factors aren’t controlled.  
In a *designed experiment*, researchers attempt to control the levels of one or many factors of interest to determine their effect on an outcome of interest.  
If factors are sufficiently controlled, this allows us to infer causal linkage
### Definitions
**Response Variable (Dependent Variable)**: Variable of interest to be measured in the experiment  
**Factors (Independent Variables)**: Variables whose effect on the response is of interest to the experimenter (may be qualitative or quantitative)  
* Factors are typically controlled but are measured even if control is impossible

**Levels (Factor Levels)**: Values of the factor(s) used in the experiment  
**Treatments**: The factor level combinations used in the experiment  
**Observational/Experimental Unit**: Object on which the response and factors are observed or measured.  

### Design of Experiments
The field of Design of Experiments details experimental designs that fully disentangle the effects of multiple factors for analysis.   
In a full factorialexperiment, all factors are varied across their levels in combination. This allows measurement of all effects and interactions.  
Example: Safety researchers are interested in braking reaction times while driving under impairments by sleeping pills and alcoholic drinks.  
* Response variable: Braking reaction time
* Factors: 2 –Pills and drinks
* Levels: 2 x 3 –Pills (Yes, No), Drinks (0, 2, 4)
* Treatments: 6 (Y0, Y2, Y4, N0, N2, N4)

Full factorial designs grow exponentially with factors/levels.
DoE provides techniques for reducing the size of factorial designs by assuming high-level interaction effects are negligible.  
We won’t get into those details in this class, but these experiments are designed to take best advantage of the strength of the Analysis of Variance (ANOVA) technique.  

## One-Factor Experiments (One-Way ANOVA)
### Assumptions
* Type of data –Numerical
* Randomization –Data gathered randomly (iid)
* Population distribution –Assumes population data distributed normally, with equal variance
* ANOVA is robust to deviations from normality
* Sample size –Must be one greater than the number of treatments at bare minimum.
### Hypotheses
Null hypothesis: The mean is equal for all treatments
ALternative: At least one is different
### Test Statistic: F
The ANOVA uses the F distribution following a similar logic to how we developed the F-test for variance.  
In the last F-test, $F = frac{s_1^2}{s_2^2}$. In the ANOVA, we’ll take the ratio $ \frac{MST}{MSE}$, where
* MST is the Mean Square for Treatment, and
* MSE is the Mean Square for Error.
#### Total Sum of Squares
Let $k$ be the number of treatments. Let $n_j$ be the number of observations for treatment $j$. Then we can calculate the total sum of squares(TSS) to be  

$TSS = \displaystyle\sum\limits_{j=1}^k \sum\limits_{i=1}^{n_j} (y_{ij} - \bar y)^2$

This is the numerator for the total sample variance calculation.

$ TSS = SST + SSE $  
where $SST$ is the sum of squares for treatments and $SSE$ is the sum of squares error.

$ SST = \displaystyle\sum\limits_{j=1}^k n_j(\bar y_j - \bar y)^2 $  
$ SSE = \displaystyle\sum\limits_{j=1}^k \sum\limits_{i=1}^{n_j} (y_{ij} - \bar y_j)^2 $

#### Mean Squares
We assume a model where $ Y = \mu_j + \epsilon $, where $\mu_j$ is the mean for the treatment $j$ and $\epsilon \sim N(0,\sigma^2)$, is the residual error.    
Sums of Squares (Treatment, Error, and Total) are then random variables in the scale family of the $\chi^2$ distribution (similar to $s^2$ in the F-test)  
The Mean Squares (Treatment, Error) are the Sum of Squares divided by their degrees of freedom.

$ \displaystyle MST = \frac{SST}{k-1} $

$ \displaystyle MSE = \frac{SST}{n-k} $

#### Test Statistic
$ F = \frac{MST}{MSE} \sim F(k-1,n-k) $

If $F > F_{ISF}(\alpha,r_1=k-1, r_2=n-k) $ then reject the null hypothesis.  
P-value:$p = P(F(k-1,n-k) > F) = F_{SF}(F,r_1=k-1, r_2=n-k) $

### One-Way ANOVA Table
see slides for reference table

## Two-Factor Experiments (Two-Way ANOVA)
* Earlier we saw a one-factor (three-level) experiment.
* We could test multiple factors at once instead.
    * Factor A: 𝑎𝑎levels
    * Factor B: 𝑏𝑏levels
    * Treatments: 𝑎𝑎×𝑏𝑏treatments
* Including all possible treatments yields a “full factorial design.”
### Total Sum of Squares
* The TSS (really the SST) is split into more parts for treatement A and B
### Two Way ANOVA Table
see slides for reference table


## Many-Factor Experiments
The same concept can be applied to larger experiments, but then you’re typically doing statistical modeling rather than hypothesis tests  
That’s the focus of the second half of this course!


 # 25. Multiple Comparisons
 Chapter 7.5.6  

 So the ANOVA told you that something was different... but which group was different? This lesson gives you the tools to appropriately do post-hoc (follow-up) analysis on the ANOVA to compare groups to one another. Techniques include the Bonferroni method, Bonferroni-Holm method, Tukey's HSD, and Tukey-Kramer. 

## Overview
* When would this be used?
* Bonferroni
* Bonferroni-Holm
* Tukey’s HSD / Tukey-Kramer

## When would this be used?
### Post-hoc Analysis
After conducting an ANOVA and rejecting the null hypothesis, we may be interested in doing pair-wise comparisons between groups.  
We do this by generating confidence intervals on the difference between each pair of groups  
For 𝑘𝑘treatments, there are 𝑐𝑐=𝑘𝑘𝑘𝑘−12pairs of means to compare.  
If we kept 𝛼𝛼steady for each comparison, our actual probability of a Type I error would balloon to 1−1−𝛼𝛼𝑐𝑐  

## Bonferroni
Bonferroni’s approach is quick and easy, but may be too conservative.  
Boole’s inequality: For events 𝐸𝐸1,𝐸𝐸2,…,𝐸𝐸𝑐𝑐in a sample space, the probability of at least one event occurring has the following inequality.  
𝑃𝑃𝐸𝐸1∪𝐸𝐸2∪⋯∪𝐸𝐸𝑐𝑐≤𝑃𝑃𝐸𝐸1+𝑃𝑃𝐸𝐸2+⋯+𝑃𝑃𝐸𝐸𝑐𝑐

Family Wise Error Rate vs individual $\alpha$

## Bonferroni-Holm
Holm updated Bonferroni to make it perform slightly better.  
This method tests pairs sequentially starting at the Bonferroni 𝛼𝛼, then increases 𝛼𝛼for each consecutive pair until the last pair is tested at the original 𝛼𝛼


## Tukey’sHSD/Tukey-Kramer
“Honest Significant Difference” is more advanced (and complicated) but generally gives tighter intervals than Bonferroni.  
* Tukey only works for equal 𝑛𝑛𝑖𝑖  
* Python implements Tukey-Kramer test when 𝑛𝑛𝑖𝑖is not equal  

sm.stats.multicomp.MultiComparison(data,groups).tukeyhsd(alpha).summary()



 # 26. Hypothesis Tests for Categorical Data
 Chapter 6.3-6.4  

 This lesson covers analysis of the outcomes of multinomial experiments, a generalization of the binomial experiment to more than 2 categories. 

## Overview
* Multinomial Experiments
* Chi-squared test for one-way multinomial experiments
* Contingency test for two-way multinomial experiments

## Multinomial Experiments
In week 2, we talked about the binomial experiment
* Experiment of 𝑛𝑛 iid Bernoulli trials
* There are 2 possible mutually exclusive outcomes to each trial: success (1) or failure (0)
* The probability of success is 𝑝𝑝  

The multinomial experimentextends that concept into multiple classes
* Experiment of 𝑛𝑛 iid trials
* There are 𝑘𝑘 possible mutually exclusive outcomes to each trial (classes, categories, or cells)
* The probability of each outcome is 𝑝𝑝𝑖𝑖 where Σ𝑖𝑖𝑝𝑝𝑖𝑖=1
* The random variable of interest is the vector 𝑛𝑛1,𝑛𝑛2,…,𝑛𝑛𝑘𝑘of cell counts, the number of observations of each class


## Chi-squared test for one-way multinomial experiments
A one-way (single variable) table is used to summarize outcomes from a multinomial experiment. It looks like a frequency table.  
For each of the categories of the multinomial variable (represented by cells in the table), counts are listed that result from the experiment.  
Classes are compared by the proportions of counts in each cell to the expected counts, according to some hypothesized proportions.  

### Assumptions
* Type of data –Qualitative
* Randomization –Data gathered randomly (iid)
* Population distribution –Assumes observed proportions are normally distributed(using the normal approximation to the binomial)
* Sample size –Sample size must be large. 𝑛𝑛𝑝𝑝𝑖𝑖,0>5for each 𝑖𝑖.
### Hypotheses
Null hypothesis: Every proportion is equal to some known value.  
Alternative hypothesis: At least one proportion is different
### Test Statistic
Assuming observed proportions are normally distributed, the sum of squared deviations divided by the expected number of observations is𝜒𝜒2 distributed.

## Contingency test for two-way multinomial experiments
Two-way contingency tables (aka cross-tabs) classify data from a multinomial experiment with two qualitative variables.  
This is used to examine relationships between the qualitative variables with respect to the experiment.  
We use 𝑅𝑅𝑖𝑖to denote row 𝑖𝑖and 𝐶𝐶𝑗𝑗to denote column 𝑗𝑗. 𝑛𝑛𝑖𝑖𝑖 is the cell count.  

Null hypothesis: The classifications are independent.
Alternative hypotheses: The classifications are dependent.
In this example, the null hypothesis is that Masters and PhD students get the same proportions of As and Bs. Alternative: they do not.

### Assumptions
* Type of data –Qualitative
* Randomization –Data gathered randomly (iid)
* Population distribution –Assumes observed proportions are normally distributed(using the normal approximation to the binomial)  
* Sample size –Sample size must be large. Expected cell count must be at least 5 for every cell.


---
---

## MIDTERM

---
---

# Week 6 - Ordinary Least Squares Regression
# 27. Probabilistic Models
This short lesson introduces probabilistic models and contrasts them with deterministic models. The focus of the remainder of this course is building probabilistic models. 

# 28. Least Squares Estimations
Chapter 8.1-8.2

The method of least squares estimation is the topic for this lesson! This is the foundation for everything we'll do in the next few weeks leading up to the final project.

# 29. Model Assumptions
Chapter 8.2.3 

It is vitally important that we check whether the assumptions are met for our probabilistic models, and this lesson covers examination of assumption for ordinary least squares regression models. Later in the course, we'll cover techniques for fixing deviations from our assumptions (except for i.i.d. assumption, which is beyond the scope of this course). 

**Errata**:  
For Assumption 1, we do still need to test that the mean error is zero for all values of x. This would not be the case if the relationship were not linear. I cover this in the Jupyter notebook for the lesson. So while examining the scatterplot in Assumption 2, look for trends in both mean and variance. We'll cover techniques for this later in the course.  
For Assumption 3, ignore the references to the Lilliefors test. I've simplified our approach to using only the two normality tests, Shapiro-Wilk and Omnibus, after comparing their performance. Also, QQ-plots should use line='45' rather than line='q'. This is correct in the notebook.


# 30. Inferences About Slope
Chapter 8.4

The focus of this lesson is hypothesis testing on the slope of the least squares regression line. Why? Because if we can say the slope is not zero, then we can say that there is a relationship (correlation - the topic of next lesson). 


# 31. Coefficients of Correlation and Determination
Chapter 8.2

The focuses of this lesson are the coefficient of correlation ($r$) and coefficient of determination ($r^2$). This also comes with a free hypothesis test! 


# 32. Estimation and Prediction Intervals
Chapter 8.2

Remember confidence and prediction intervals? In this lesson we cover their analogues using probabilistic models: estimation and prediction intervals. 



---
# Week 7 -  Multiple Linear Regression
This week's material is focus on Multiple Linear Regression, an extension of the OLS modeling that we did last week into multiple independent variables.
# 33. Multiple Regression
Chapter 9.1

In this lesson, we'll extend the concept of simple linear regression to the use of multiple independent (predictor) variables. 

## Multiple Regression Models
Multiple regression expands upon simple linear regression to include multiple independent variables to predict the response variable
The general form is now  
$ y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_k x_k +\epsilon $

Interpretation remains consistent
* $\beta_0$ is still the y-intercept (when $x_1, x_2, ..., x_k =0$)
* $\beta_i$ is still the effect of independent variable $x_i$ on response variable $y$    
These models can also allow for “higher-order” relationships, e.g.,  
$ x_2 = (x_1)^2 $  
$ x_3 = \ln(x_1) $ 


The random error component 𝜖𝜖still has the same assumptions
1.The mean of 𝜖𝜖is zero and constant
2.Variance of 𝜖𝜖is equal to 𝜎𝜎2and constant
3.The distribution of 𝜖𝜖~𝑁𝑁0,𝜎𝜎2
4.Each observed 𝜖𝜖𝑖𝑖is independent (iid)


## Six Steps to Multiple Regression Modeling
1. Hypothesize the deterministic component
2. Use sample data to estimate unknown parameters
3. Estimate the standard deviation of random error term
4. Check assumptions on error term and modify model as needed
5. Statistically evaluate the utility of the model
6. When satisfied that the model is useful, apply it

## Method of Least Squares
Still using Ordinary Least Squares –we’ll examine alternatives later
* Recall that OLS minimizes the squared errors in predictions  
$ SSE = \sum(y-\hat y)^2 $  

Solving for each parameter estimate ($\beta_i$) is hard to compute manually  
* For $k$ predictor variables, we have to solve a system of $k-1$ equations  

We cannot do this effectively without linear algebra, so we’ll rely on Python to estimate our parameters

## F-test
Hypotheses:  
$H_0$: None of the independent variables explain any variability in $y$  
$H_a$: At least one of the independent variables explain some variability in $y$  

## Other Assessments of Fit
When comparing models, one can use 𝑅𝑅𝑎𝑎2as a comparison, but there are others:
* Log Likelihood $\ln(L)$: A measure of information lost. Should not be used for multiple regression for the same reason as $R^2$. Larger is better.
* Akaike Information Criterion (AIC = $2k - \ln(L)$): Modifies log likelihood to penalize for extra parameters. Smaller is better.
* Bayesian Information Criterion (BIC = $k\ln(n) - 2 \ln(L)$): Like AIC, but stronger penalty for extra parameters. Smaller is better.

## Assessments of Fit
Typicallythey will all agree on the best model.
* $R_a^2$: Least punishment for extra variables
    * If they disagree, this will result in largest model of the three
* AIC: Punishes extra variables more than $R_a^2$ but less than BIC
    * If all data is normal, this is equivalent to $R_a^2$
    * This is a moderate approach, trading off between completeness and parsimony
* BIC: Punishes extra variables more than AIC and $R_a^2$
    * This will result in the most parsimonious model of the three

## Inference about \beta_i
An additional consideration: If you are conducting simultaneous inferences, you must adjust your alpha level (Bonferroni)  
This would affect both hypothesis tests and confidence intervals  
If you are talking about each parameter independently, this is not required  



# 34. Higher Order Models
In this lesson, we'll consider adding predictor variables to our linear regression that are functions of existing variables, such as $x^2$, $\ln x$, $e^x$, etc.


We may want to model relationships that are more complex than simple linear relationships, such as
* Quadratic relationships:
* Interactions: 
* Logarithmic relationships: 
* Exponential relationships: 


## Interaction Terms
$ y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_1x_2 $

We’ve talked previously about interaction effects with categorical variables
* The same interpretation applies to quantitative variables

The level of $x_1$ changes the slope of the effect of $x_2$
* The slope for $x_1$ is now $ \beta_1 + \beta_3 x_2 $
* The slope for $x_2$ is now $ \beta_2 + \beta_3 x_1 $



# 35. Qualitative Variables
In this lesson, we'll consider including categorical variables in regression, which requires the use of dummy/indicator variables.

## Categorical (Qualitative) Variables
In order to include categorical independent variables, we must code them numerically by using dummy (indicator) variablesvalued 0 or 1

We’ll use one fewer dummy variable than the number of levels

## Recap and Review
* Whenever the relationship between an $x$ and $y$ does not appear linear, we can add higher order terms
* When one variable has an effect onthe relationship between another variable and $y$, we can add interaction terms
* Whenever interactions or higher-order teams are included, the first-order terms must also be included.
* Using the C() wrapper in Patsy will create dummy variables for you



# 36. Model Building
Chapter 9.2  
This lesson covers the broad topic of model selection, which is truly more art than science, and introduces tools to help you select a model for a given dataset: stepwise regression, ridge regression, and lasso regression.

## Model Building
Model building can be an iterative process of trying different models and comparing them
* For simple scenarios with few variables, scatterplots can provide a lot of info
* For more complicated scenarios, we have a few methods to iteratively select variables for inclusion in the model  

We’ll talk about:
* Stepwise regression
* Ridge regression
* Lasso regression

It is best practice to split your data into three parts:
* Training set: the data you’ll use to build a model
* Validation set:candidate models use this to compare accuracy
* Test set: used to assess accuracy of onlythe final model

In the final project, I’ll hold back the test set results until evaluation.


## Visual Method
## Stepwise Regression
The most rudimentary method of iterative variable selection  
First step is to hypothesize all potential predictor variables, including first order, higher order, and interaction terms  
Operates using forward selection, backwards elimination, or some combo  
* Forward Selection: At each step, look for the “best” parameter to include and add it to the model. Terms are never removed.
* Backward Elimination: Start with the full model. At each step, remove the “worst” parameter. Terms are never added.
* Mixed: Some mix of the two.

## Ridge Regression (L2 Regularization)
Recall that our sum of squared errors is  
$ SSE = \displaystyle\sum_{i=1}^n (y_i - \hat y)^2 $  
Ridge regression adds a shrinkage penalty to penalize large parameters. This is the loss function that it will minimize.   
$ Loss = SSE + Penanlty = SSE + \alpha \displaystyle \sum \hat \beta_j^2 $

$\alpha > 0$ here is **not significance**. It is instead a parameter you can use to tune how much additional parameters are penalized.  
If $\alpha=0$, this is equivalent to OLS.  
Increasing $\alpha$ artificially underestimates slopes $ \hat \beta_1, ..., \hat \beta_k $  
If $\alpha = \infin $, this will result in the model $ \hat y = \hat \beta_0 = \bar y $

## LASSO Regression (L1 Regularization)

LASSO (Least Absolute Shrinkage and Selection Operator) regression adds a different shrinkage penaltyto penalize large parameters. This is the loss functionthat it will minimize.  
$ Loss = SSE + Penalty = SSE + \alpha \displaystyle \sum_{j=1}^k |\beta_j| $

A high value of 𝛼𝛼will result in a sparse model. A low value will result in a full model. This is much easier to interpret for model selection.


# 37. Model Adequacy
Chapter 9.3  
Here we discuss assumptions and other considerations of model quality from the perspective of multiple regression.

## Assumptions (Last Week)
1. The mean value of $\epsilon$ is zero for all values of $x$
2. The variance of $\epsilon $ (some $\sigma^2$), is constant for all values of $x$
3. $\epsilon$ is normally distributed
4. Each $\epsilon_i$ is iid(independent and identically distributed)

### 1. The mean value of $\epsilon$ is zero
As with simple regression, this is still built into the method  
BUT –the mean should be zero for all predicted values  
We can identify problems by looking at plots of residual vs predicted value  


### 2. The variance of $\epsilon $ (some $\sigma^2$), is constant for all values of $x$
In simple regression we looked at plots of $x$ vs residuals  
In multiple regression, we’ll look at plots of residual vs. predicted value

#### Rectifying non-constant mean/variance
Unequal mean and variance can typically be fixed by transforming $y$  
* Common transformations include $\ln y$ and $y^\lambda$  
* Try a transform, refit the model, and check plots again
    * This modified model will lose ease of inference
* A useful method is the Box-Cox Transformation
* This finds the optimal value of $\lambda$ for a $y^\lambda$ transformation to achieve normality
* It also implements $\ln y$ when $\lambda=0$
* `yt, lamb, ci = stats.boxcox(y, alpha=0.05)`


### 3. $\epsilon$ is normally distributed
Python automatically conducts normality tests on the residuals (see bottom of summary table)  
It is still good practice to check visually with histograms and QQ-plots.

#### Rectifying non-normality
Slight departures from normality will generally not be cause for concern
* Regression is robust to non-normality, especially for large samples
* Outliers will often result in significant normality tests
* This is part of why visual analysis is so important  

For major departures, a transformation may again be required
* If the cause is non-normality of one of the independent variables, consider transforming one or more of them instead


### 4. Errors are independent
Just like before, we can try to identify this by examining ordered plots of the residuals
* We talked about time plots, but could also be spatial, etc.  

Rectifying independence problems will require time-series modeling, which is beyond the scope of this course

## Other Considerations
### Outliers
Standardized Residuals: $ \frac{\epsilon}{\sqrt{MSE}} $   
`influence = model.get_influence()`  
`influence.resid_studentized_internal`  

Outliers are not necessarily a bad thing depending on their location. They can have undue effect on the model, or influence

### Influence
Influenceis a measure of how much the linear model is affected by the presence of a single data point  

One way to measure influence is with Studentized residuals  
Studentized Residuals: Standardized residuals when the model is fit without that point  
`influence.resid_studentized_external`

Another method is to look at Influence Plot  
`ssmg.influence_plot(model)`

### Overfitting and Underfitting
Overfitting: Captures some of the random noise as part of the model. Typically caused by over-parameterization in regression.  
Underfitting: Captures not enough of the deterministic part of the true relationship. Typically cause by under-parameterization in regression.  

Both lead to poor predictions on new data sets.  
Again, it is best practice to use training, validation, and test sets when you have enough data. The amount of split is up to you as the modeler.  
We’ll do this in later examples.

### Multicollinearity
Multicollinearity occurs when the independent variables are correlated  
* May cause t-tests to be non-significant
* May inflate standard errors for $ \hat \beta $ estimates
* May cause parameters to be opposite-sign from expected

A good diagnostic is the Variance Inflation Factor
* VIF=5 is considered moderate
* VIF=10 is considered something to worry about  

Multicollinearity is not a concern for  
* The intercept
* Higher-order terms being collinear with main effects  

If there are issues, you can  
* Center/standardize the offending variables
* Remove one or more variables
* Don’t make inferences on $ \hat \beta $ 

### Extrapolation
* Extrapolation is more complex in the multivariate model
* It is still just as important as in the univariate model!



---
---

**Final Project Material Complete**

---
---
# Week 8 - Examples
This week is all about examples of working through regression problems of increasing complexity.

# 38. Pie Sale Example
Chapter 9.2-9.4  

This example looks at quarterly pie sales in 1998 and 1999 in 6 cities, creating a model and assessing it in a fairly practical manner without using stepwise regression, ridge, or lasso. We'll step into those techniques later, but I wanted to start with big-picture intuition before going deep.

This also introduces using LOWESS (Locally Weighted Scatterplot Smoothing) as a tool to augment your assessment of assumption 1. Feel free to use that in your homework and/or final project.

# 39. Galapagos Islands Example
Chapter 9.2-9.4  

This is another example of creating a linear regression model. This time we're using data about the number of species per island in the Galapagos Islands.

We first build a first-order model using all factors and examine the residuals, which deviate significantly from normality. We'll apply the Box-Cox transformation and a natural log transformation to normalize the residuals, then use stepwise regression with backward elimination to tweak the model. This transformed model is assessed for adequacy, applied (including inverse transformations), and plotted.


# 40. California Housing Example
Chapter 9.2-9.4  

This lesson is another (much longer) example delving into some data on California housing costs from back in 1990. This is an ugly dataset, so I use a log transform on the response variable which does the best as can be expected in normalizing the residuals. I then use Lasso regression in two ways: first, as used last week, but using the training set and finding the model for an alpha resulting in the model with minimum BIC. Next, I use the same Lasso regression and select a model by comparing the root mean square error for the training and validation datasets to select a model. That model is then assessed using RMSE for the test dataset, which was not used at all in training or model selection. 

---
# Week 9 - More Examples

# 41. Boston Housing Example
This example covers another really messy dataset, but focused on validating (or rather, failing to validate) the assumptions of OLS. It introduces some functions that tie together things you've mostly already seen in possibly helpful packages that you're welcome to use. It also ends with a bit of discussion about ethics in data science. Remember, just because you can use something to build a model, that doesn't mean that you should!!!

# 42. Pie Sales Revisited
This example revisits the pie data we used in Week 7, mostly to show what those functions I used in the above example look when the assumptions are pretty valid.

# 43. US Crime
This example focuses on some extra techniques you might run across. Lasso and Ridge are the gold standard for feature selection, but I'll show good ol' Brute Force as well as overviews of two methods that are rising in popularity: Select K Best and Recursive Feature Elimination. Spoiler: I don't recommend them or else I'd have taught them earlier.

 
# 44. Multicollinearity
I got a few questions on Homework 6 relating to Variance Inflation Factors and Multicollinearity, so I put together another worked example going into more depth on that topic. This is a re-attack on Lesson 40's California Housing example, picking up with the model we left off with in Lesson 40 and diving into the issue of multicollinearity. Hope it helps!

# 48. Alternate Methods of Regression Modeling
Following up on a question asking about using SciKit-Learn's linear regression methods, here's a look at three different ways you can build linear regression models. If you're happy with how we've been doing it and don't want to confuse yourself, feel free to skip this one!

---
# Week 10

# 45. Logistic Regression
Logistic regression extends the concept of ordinary least squares regression to predicting outcomes of a binary outcome (i.e., a Bernoulli trial). This lesson is not tested, but it is valuable to see classical methods of classification and look at accuracy before you go into machine learning next quarter. Enjoy!

# 46. Logistic Regression Exercise
This is an application for logistic regression, getting into some attempts at applying transformations to the data and building a model predicting diabetes onset. That's not the same data as Homework 6, just another diabetes dataset!

# 47. OLS Transformation Revisited
Here's a deeper dive on transformations as requested!
