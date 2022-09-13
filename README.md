# Coding for Data Analysis with Python

Introduction to Data Analysis with Python - lecture materials by [Peter Duronelly](https://github.com/peterduronelly) and [Ádám Vig](https://github.com/adamvig96)  with [Ágoston Reguly](https://regulyagoston.github.io/) (Georgia Tech) and [Gábor Békés](https://sites.google.com/site/bekesg/) ([CEU](https://people.ceu.edu/gabor_bekes), [KRTK](https://kti.krtk.hu/en/kutatok/gabor-bekes/5896/), [CEPR](https://voxeu.org/users/gaborbekes0)) 

This course material is a supplement to **[Data Analysis for Business, Economics, and Policy](https://www.cambridge.org/highereducation/books/data-analysis-for-business-economics-and-policy/D67A1B0B56176D6D6A92E27F3F82AA20)**  by Gábor Békés (CEU) and Gábor Kézdi (U. Michigan),  Cambridge University Press, 2021.

*Textbook* information: see the textbook's website [**gabors-data-analysis.com**](https://gabors-data-analysis.com/) or visit [Cambridge University Press](https://www.cambridge.org/highereducation/books/data-analysis-for-business-economics-and-policy/D67A1B0B56176D6D6A92E27F3F82AA20)

To get a copy: [Inspection copy for instructors](https://www.cambridge.org/highereducation/books/data-analysis-for-business-economics-and-policy/D67A1B0B56176D6D6A92E27F3F82AA20/examination-copy/personal-details) or [buy from Amazon](https://www.amazon.com/Data-Analysis-Business-Economics-Policy-dp-1108716202/dp/1108716202/ref=mt_other?_encoding=UTF8&me=&qid=) or [order online around the globe](https://gabors-data-analysis.com/order)   


## Acknowledgments

We'd like to say thanks for [Ágoston Reguly](https://github.com/regulyagoston) who created the template for Coding for Data Analysis series. We followed his steps in writing the Python-version of the teaching material. 

We thank [CEU Department of Econimics and Business](https://economics.ceu.edu/) for financial support. 

## Status

This is version 0.1, as of 13 September, 2022.

Comments are really welcome -- just add a GitHub issue. 


## Overview

The course is an introducton to the Python programming language, its software environment, and also to data exploration, data transformation, visualization, and more advanced data analysis. The idea is that people will learn working with Python along with learning to carry out data analysis.

The material primarily consists of `Jupyter notebooks`, and is sometimes supplemented with additional data. In most cases, however, we used the [textbook's datasets](https://gabors-data-analysis.com/datasets/) to bring the course as close to the original textbook as possible.  

Lectures 0 to 9 mostly complements [Part I: Data Exploration (Chapter 1-6)](https://gabors-data-analysis.com/chapters/#part-i-data-exploration).Lectures 0 to 6 are general introductions to Python and its concepts. These notebooks focus on coding principles, Python's main building blocks, and introduce the data analyst's most important data structure: Pandas dataframes. Lecture 7 gives insight how to use Python for data exploration. Lectures 8 and 9 expands the toolkit for advanced data analytics techniques.

Lecture 10 to 16 complements [PART II: Regression Analysis (Chapter 7-12)](https://gabors-data-analysis.com/chapters/#part-ii-regression-analysis) and cover everything you need to know about linear regression in Python on an introductionary level. We start with simple linear regression on cross-sectional data, then we explore binary models, and multiple linear regression. Finally we discuss the basic time-series regression model and its intricacies. 


## Philosopy and how to use

We tried to put together a benchmark course to supplement the Data Analysis texbook and to help anyone, students and intructors alike, follow the book's material. Anyone is free to use the notebooks in their current or in any modified form, with proper reference to the original material. 

While we teach the basics on Python, this is not a classical coding course material. The notebooks take the reader through the data analysis workflow of the first 12 chapters of the textbook providing assitance in Python along the way. You will learn gradually what is needed to carry out analytical steps from loading data to running regressions. We will suggest additional resources to learn more coding tools and enhance your skills. 

It is possible to learn the very basics of Python using these notebooks, but simply completing the exercises won't make anyone a programmer. Using the codebase _and_ the textbook together however, does help in understanding statistical and data analytics concepts and see the theory in practice. 

The lectures are pre-written, which an educated reader can follow and understand. Nevertheless, instructors may want to modify and tailor-make the codes according to their own teaching habits and philosophy. Homeworks are not part of the codebase, giving  instructors another task in the practical coding sessions of their data analytics courses. 

The material's main focus is the manipulation and analysis of tabular data. `Pandas` dataframes provide most of the tools for these manipulation exercises, and we use the `statsmodels` package for running linear regressions. As for data vizualization, we added a basic intro to the most popular `matplotlib`pacakge, but rely heavily on a new favorite: `plotnine`, the Python-implementation of R's _ggplot_, for visualization and graphical representation. 


## Course content

| Lecture | Learning outcomes | Case study | Dataset |
| ------- | ----------------- | ---------- | ------- |
| [lecture00-intro](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture00-intro) | basic terminology; Jupyter notebooks ; how to setup the environment | - | - |
| [lecture01-coding-basics](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture01-coding-basics) | coding basics; basic variable types | - | - |
| [lecture02-basic-structures](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture02-basic-structures) | basic data structures: lists, tuples, sets, distionaries; working with modules | - | - |
| [lecture03-data-IO](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture03-data-IO) | how to read and write files; navigating the file system | - | - |
| [lecture04-pandas-basics](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture04-pandas-basics) | pandas dataframe basics; how manipulate tabular data with Pandas: conversion, filtering, replacing values, adding new variables, sorting; using pipes | [Ch03: Finding a good deal among hotels: data exploration](https://gabors-data-analysis.com/casestudies/#ch03a-finding-a-good-deal-among-hotels-data-exploration) | [hotels-vienna](https://gabors-data-analysis.com/datasets/#hotels-vienna) | 
| [lecture05-graphs-basics](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture05-graphs-basics) | matplotlib basics; deep-dive into plotline | [Ch03: Finding a good deal among hotels: data exploration](https://gabors-data-analysis.com/casestudies/#ch03a-finding-a-good-deal-among-hotels-data-exploration) | [stocks-sp500](https://gabors-data-analysis.com/datasets/#stocks-sp500); [hotels-vienna](https://gabors-data-analysis.com/datasets/#hotels-vienna) |
| [lecture06-conditionals](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture06-conditionals) | conditional statements; for loop, while loop, list comprehension | - | - |
| [lecture07-data-exploration](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture07-data-exploration) | descriptive statistics, customized plots, hypothesis testing, correlation & association | [CH01B Comparing online and offline prices](https://gabors-data-analysis.com/casestudies/#ch01b-comparing-online-and-offline-prices-data-collection) | [billion-prices](https://gabors-data-analysis.com/datasets/#billion-prices) | 
| [lecture08-functions](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture08-functions) | user-defined functions & lambda functions | - | - |
| [lecture09-exception-handling](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture09-exception-handling) | try-except | - | - |
| [lecture10-intro-to-regression](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture10-intro-to-regression) | binary means, non-parametric regression (lowess), simple linear regression (OLS), analysis of results, log and non-linear regressions | [CH07A Finding a good deal among hotels with simple regression](https://gabors-data-analysis.com/casestudies/part-II/#ch07a-finding-a-good-deal-among-hotels-with-simple-regression), [CH08A Finding a good deal among hotels with non-linear function](https://gabors-data-analysis.com/casestudies/part-II/#ch08a-finding-a-good-deal-among-hotels-with-non-linear-function) | [hotels-vienna](https://gabors-data-analysis.com/datasets/#hotels-vienna)
| [lecture11-feature-engineering](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture11-feature-engineering) | creating new variables from existing ones, creating ordered variables, factors/dummy variables, imputing, randomizing, log transformation, winsorizing | [Ch04A Management quality and firm size](https://gabors-data-analysis.com/casestudies/#ch04a-management-quality-and-firm-size-describing-patterns-of-association); [CH17A Predicting firm exit](https://gabors-data-analysis.com/casestudies/#ch17a-predicting-firm-exit-probability-and-classification) | [wms-management-survey](https://gabors-data-analysis.com/datasets/#wms-management-survey); [bisnode-firms](https://gabors-data-analysis.com/datasets/#bisnode-firms)
| [lecture12-simple-linear-regression](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture12-simple-linear-regression) | EDA, how to decide on functional form, models with logs and polynomials, piecewise linear spline, weighted OLS, residual analysis | [CH08B How is life expectancy related to the average income of a country?](https://gabors-data-analysis.com/casestudies/#ch08b-how-is-life-expectancy-related-to-the-average-income-of-a-country) | [worldbank-lifeexpectancy](https://gabors-data-analysis.com/datasets/#worldbank-lifeexpectancy) | 
| [lecture13-advanced-linear-regression](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture13-advanced-linear-regression) | multiple linear regression, how to choose from models, confidence interval, prediction interval, robustness & external validity, training and test sample | [Ch03B Comparing hotel prices in Europe: Vienna vs London](https://gabors-data-analysis.com/casestudies/#ch03b-comparing-hotel-prices-in-europe-vienna-vs-london), [CH09B How stable is the hotel price–distance to center relationship?](https://gabors-data-analysis.com/casestudies/part-II/#ch09b-how-stable-is-the-hotel-pricedistance-to-center-relationship) | [hotels-europe](https://gabors-data-analysis.com/datasets/#hotels-europe) | 
| [lecture14-binary-models](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture14-binary-models) | saturated probability models, mupltiple regression with binary outcomes, logit & probit models, comparison of non-linear models | [CH11A Does smoking pose a health risk?](https://gabors-data-analysis.com/casestudies/#ch11a-does-smoking-pose-a-health-risk) | [share-health](https://gabors-data-analysis.com/datasets/#share-health) |
| [lecture15-datetime](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture15-datetime) | handling date and time, time zone awareness, datetime in Pandas | - | - |
| [lecture16-timeseries-regression](https://github.com/gabors-data-analysis/da-coding-python/tree/develop/lecture16-timeseries-regression) | manipulation of time-series data, autocorrelation, Newey-West standard errors, lagged variables | [CH12B Electricity consumption and temperature](https://gabors-data-analysis.com/casestudies/#ch12b-electricity-consumption-and-temperature) | [arizona-electricity](https://gabors-data-analysis.com/datasets/#arizona-electricity) | 




## Technical Note: environment

Most data science courses use the Anaconda environment for Python. We, however, use `pip` and `pipenv`, and run Jupyter notebooks from the course's environment. Anaconda is a great tool for data analysis and data science, but once someone goes beyond ad-hoc adata analysis and needs to develop and deploy advanced data solutions in a production environment in Python, `pip` is going to be the way to go. 
