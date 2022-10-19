# Lecture 25: Matplotlib vs Plotnine on the GDP and Life Expectancy data

## Motivation

People tend to live longer in richer countries. How long people live is usually measured by life expectancy; how rich a country is usually captured by its yearly income, measured by GDP. But should we use total GDP or GDP per capita? And what’s the shape of the patterns of association? Is the same percent difference in income related to the same difference in how long people live among richer countries and poorer countries? Finding the shape of the association helps benchmarking life expectancy among countries with similar levels of income and identify countries where people tend to live especially long or especially short lives for their income.

The lecture illustrates the choice between total and per capita measures (here GDP), regressions with variables in logs, and two ways to model nonlinear patterns in the framework of the linear regression: piecewise linear splines, and polynomials. It also illustrates whether and how to use weights in regression analysis, and what that choice implies for the correct interpretation of the results. The lecture also shows how to use informative visualization to present the results of regressions.


## This lecture

This lecture covers the same graphs in two separate notebooks: [`life_expectancy_gdp_plotnine.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture25-matplotlib-vs-plotnine/life_expectancy_gdp_plotnine.ipynb) and [`life_expectancy_gdp_matplotlib.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture25-matplotlib-vs-plotnine/life_expectancy_gdp_matplotlib.ipynb). Our goal was to show that exactly the same graphs can be created with `matplotlib` (and with its high-level interface, `seaborn`) and with `plotnine`.

Case study:
  - [CH08B How is life expectancy related to the average income of a country?](https://gabors-data-analysis.com/casestudies/#ch08b-how-is-life-expectancy-related-to-the-average-income-of-a-country)

## Learning outcomes
After successfully completing [`life_expectancy_gdp_plotnine.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture25-matplotlib-vs-plotnine/life_expectancy_gdp_plotnine.ipynb) and/or [`life_expectancy_gdp_matplotlib.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture25-matplotlib-vs-plotnine/life_expectancy_gdp_matplotlib.ipynb) students should be able to:

  - Estimate simple
    - level-level regression
    - log-level regression
    - quadratic regression
    - spline regression
  - Visualise regression line on a scatter plot
    - set axis ticks to percent format
    - scale axis to log
    - use weights for point sizes
  

## Lecture Time

Ideal overall time: **30-60  mins** depending on whether you go through only one, or both notebooks.


## Further material

  - This lecture is a modified version of [`ch08-life-expectancy-income.ipynb`](https://github.com/gabors-data-analysis/da_case_studies/blob/master/ch08-life-expectancy-income/ch08-life-expectancy-income.ipynb) from [Gabor's case study repository](https://github.com/gabors-data-analysis/da_case_studies).
  - Tutorial to the `seaborn` library can be found [here](https://seaborn.pydata.org/tutorial.html).