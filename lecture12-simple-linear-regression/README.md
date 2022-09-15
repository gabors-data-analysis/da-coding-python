# Lecture 12: Analysis of life expectancy and GDP

## Motivation

Life expectancy at birth shows how long residents of a country live; it is a summary measure of their health. Residents of richer countries tend to live longer, but you want to know the strength of that pattern. You also want to identify countries where people live especially long for the income level of their country, to start thinking about what may cause their exceptional health. You download cross-country data from the World Bank database on life expectancy and GDP per capita, and you want to uncover the pattern of association between them. How would you do that in a way that accommodates potentially nonlinear patterns and, at the same time, produces results that you can interpret?

Linear regression gives a meaningful approximation to the patterns of association, but real-life data can be messy, and the patterns may be nonlinear. What those mean for regression analysis and what we can do about them is important to understand. There are several tools that we can apply to make linear regression approximate nonlinear patterns of association, but whether we want to do so depends on the goal of the analysis. The fact that real-life data tends to be messy, with errors and extreme values, poses other challenges for regression analysis.

## This lecture

This lecture provides materials to analyze the association between life expectancy and GDP measures for various countries in 2019 (or later), inspired by the dataset [worldbank-lifeexpectancy](https://gabors-data-analysis.com/datasets/#worldbank-lifeexpectancy). During this exercise, students get familiar with creating simple linear regression-based models with different transformations, such as level-level, log-level, level-log, and log-log models, or using polynomials and piecewise linear splines transformation of the explanatory variable.

This lecture is a practice (or similar to live coding) lecture, as it does not teaches much new material, but provides students to deepen their understanding with simple regressions and the reasoning behind them.

This lecture is based on [Chapter 08, B: How is life expectancy related to the average income of a country?](https://gabors-data-analysis.com/casestudies/#ch08b-how-is-life-expectancy-related-to-the-average-income-of-a-country)

## Learning outcomes
After successfully completing codes in *raw_codes* student should have:

[`life_exp_get_data.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture12-simple-linear-regression/life_exp_get_data.ipynb)
  - Solid ground for importing and exporting data from World Bank's website via API.

[`life_exp_analysis.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture12-simple-linear-regression/life_exp_analysis.ipynb)
  - Create scatter plots for competing models.
  - Transform variables from level to log in a ggplot and scale the axis for proper interpretation.
  - Run and plot multiple single-variable regressions with:
    - log transformation,
    - higher-order polynomial,
    - piecewise linear spline
    - or using weighted OLS.
  - Be able to estimate heteroscedastic robust SEs and compare specific model results with `stargazer` in one output.
  - Create a graph, which automatically annotates observations with the *n* largest and smallest errors.


## Datasets used

- [worldbank-lifeexpectancy](https://gabors-data-analysis.com/datasets/#worldbank-lifeexpectancy), but for more recent year.

## Lecture Time

Ideal overall time: approx 60 minutes.

Solving [`00_life_exp_get_data.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture12-simple-linear-regression/00_life_exp_get_data.ipynb)) takes around *5-10 minutes* as it builds on [lecture03-data-IO](https://github.com/gabors-data-analysis/da-coding-python/tree/main/lecture03-data-IO). In principle it should be a quick reminder and practice.

Solving [`02_life_exp_analysis.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture12-simple-linear-regression/02_life_exp_analysis.ipynb) covers the main material, and takes *40-60 minutes* depending on the student's background. This lecture is mainly theory-based (practice via case study) and includes easy, but many new commands in a repetitive way. 

## Homework

*Type*: quick practice, approx 20 mins

Use the [hotels-vienna dataset](https://gabors-data-analysis.com/datasets/#hotels-vienna), similarly as we used in [`hotels_intro_to_regression.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture10-intro-to-regression/intro_to_regression.ipynb). Create and compare different models, based on transformations of `y=price` or `x=distance` variables:
  
  - level-level
  - log-level
  - level-log
  - log-log
  - polinomials of distance with square and cube terms
  - piecewise-linear-spline model, with a cutoff at 2 miles 

 Estimate these models with `statsmodels`, using robust SEs, and compare with `stargazer`. Decide which model would you use and why! Argue!

## Further material

  - More materials on the case study can be found in Gabor's *da_case_studies* repository: [ch08-life-expectancy-income](https://github.com/gabors-data-analysis/da_case_studies/tree/master/ch08-life-expectancy-income)
  - Arthur Turrell's Coding for Economics classes: [Regression](https://aeturrell.github.io/coding-for-economists/econmt-regression.html)