# Lecture 16: Introduction to time-series regression

## Motivation

Heating and cooling are potentially important uses of electricity. To investigate how weather conditions affect electricity consumption, you have collected data on temperature and residential electricity consumption in a hot region. How should you estimate the association between temperature and electricity consumption? How should you define the variables of interest, and how should you prepare the data, which has daily observations on temperature and monthly observations on electricity consumption? Should you worry about the fact that both electricity consumption and temperature vary a lot across months within years, and if yes, what should you do about it?

Time series data is often used to analyze business, economic, and policy questions. Time series data presents additional opportunities as well as additional challenges for regression analysis. Unlike cross-sectional data, it enables examining how y changes when x changes, and it also allows us to examine what happens to y right away or with a delay. However, variables in time series data come with some special features that affect how we should estimate regressions, and how we can interpret their coefficients.

## This lecture

This lecture introduces time-series regression via the [arizona-electricity](https://gabors-data-analysis.com/datasets/#arizona-electricity) dataset. During this lecture, students manipulate time-series data along time dimensions, create multiple time-series related graphs and get familiar with (partial) autocorrelation. Differenced variables, lags of the outcome, and lags of the explanatory variables, (deterministic) seasonality are used during regression models. Estimating these models are via `statsmodels`'s `get_robustcov_results` with Newey-West standard errors. Model comparisons and estimating cumulative effects with valid SEs are shown.

This lecture is based on [Chapter 12, B: Electricity consumption and temperature](https://gabors-data-analysis.com/casestudies/#ch12b-electricity-consumption-and-temperature)

## Learning outcomes
After successfully completing [`intro_time_series.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture16-timeseries-regression/intro_time_series.ipynb), students should be able:

  - Merge different time-series data
  - Create time-series related descriptives and graphs
    - handle date as the axis with different formatting
    - create autocorrelation and partial autocorrelation graphs and interpret
  - Run time-series regression
    - Estimate Newey-West standard errors and understand the role of lags
    - Control for seasonality via dummies
    - Add lagged variables to the model (and possibly leads as well)
    - How and why to use the same time interval when comparing competing time-series models
    - Estimate the standard error(s) for the cumulative effect

## Datasets used

- [arizona-electricity](https://gabors-data-analysis.com/datasets/#arizona-electricity)

## Lecture Time

Ideal overall time: **60-80 mins**.

Going through [`intro_time_series.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture16-timeseries-regression/intro_time_series.ipynb) takes around *50-70 minutes* as there are some discussions and interpretations of the time series (e.g. stationarity, a transformation of variables, etc). Solving the tasks takes the remaining *5-10 minutes*.


## Homework

*Type*: quick practice, approx 20 mins

You will use the [case-shiller-la](https://gabors-data-analysis.com/datasets/#case-shiller-la) dataset to build a model for unemployment based on the Shiller price index. Load the data and consider only `pn` (Shiller price index) and `un` (unemployment) as the variables of interest. Both are seasonally adjusted. Decide which transformation to use to make the variables stationary. Create models, where you predict unemployment based on the Shiller price index. At least you should have one model where you use only the contemporaneous effects and one when you use lagged variables for both variables as explanatory variables.


## Further material

  - More materials on the case study can be found in Gabor's *da_case_studies* repository: [ch12-electricity-temperature](https://github.com/gabors-data-analysis/da_case_studies/tree/master/ch12-electricity-temperature)

