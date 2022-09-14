# Lecture 04: Data Munging with pandas

## Motivation

Before analyzing the data, data analysts spend a lot of time organizing, managing, and cleaning it to prepare it for analysis. This is called data wrangling or data munging. It is often said that 80 percent of data analysis time is spent on these tasks. Data wrangling is an iterative process: we usually start by organizing and cleaning our data, then start doing the analysis, and then go back to the cleaning process as problems emerge during analysis.

Here we introduce students to a (relatively) easy way of carrying out this task and use the case study of [finding a good deal among hotels]((https://gabors-data-analysis.com/casestudies/#ch02a-finding-a-good-deal-among-hotels-data-preparation)). The initial data preparation, continues to work towards finding hotels that are underpriced relative to their location and quality. In this lecture, we illustrate how to find problems with observations and variables and how to solve those problems.

## This lecture


This lecture introduces `pandas` as the data type of variable Python. It shows multiple columns and row manipulations with one DataFrame, also introduces students how to manipulate raw data in various ways with `pandas`.

This lecture is based on [Chapter 02, A: Finding a good deal among hotels: data preparation](https://gabors-data-analysis.com/casestudies/#ch02a-finding-a-good-deal-among-hotels-data-preparation).


## Learning outcomes
After successfully completing [`pandas_basics.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture04-pandas-basics/pandas_basics.ipynb), students should be able to:

  - create pandas `Series`
  - create pandas `DataFrames` from `Series`, dictionaries, lists
  - access data in a `DataFrame` with `loc` and `iloc`
  - reset index
  - rename columns
  - access metadata of `DataFrame`s

After successfully completing [`pandas_data_munging.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture04-pandas-basics/pandas_data_munging.ipynb), students should be able to:

  - add variables
  - separate a character variable into two (or more) variables
  - convert different type of variables to specific types:
    - character to numeric
  - string manipulations in pandas Series
  - filter out different observations
    - select observations with specific values
    - tabulate different values of a variable
    - filter out missing values
    - replace specific values with others
    - handle duplicates
  - use pipes to do multiple manipulations at once
  - sort data ascending or descending according to a specific variable

## Datasets used
* [Hotels Europe](https://gabors-data-analysis.com/datasets/#hotels-europe)


## Lecture Time

Ideal overall time: **60 mins**.


## Homework

*Type*: quick practice, approx 10 mins

Use the same [hotel-europe data from OSF](https://osf.io/r6uqb/), but now 
  - Download both `hotels-europe_price.csv` and `hotels-europe_features.csv`
  - `merge` them in this order by `hotel_id`
  - filter for :
    - time: 2018/01 and weekend == 1
    - city: Vienna or London. Hint: for multiple matches, use something like: 
    ```r 
    data.loc[data["city"].isin(['City_A','City_B'])]
    ``` 
    - accommodation should be Apartment, 3-4 stars (only) with more than 10 reviews
    - price is less than 600$
 - arrange the data in ascending order by price

## Further material

  - More materials on the case study can be found in Gabor's [da_case_studies repository](https://github.com/gabors-data-analysis/da_case_studies): [ch02-hotels-data-prep](https://github.com/gabors-data-analysis/da_case_studies/blob/master/ch02-hotels-data-prep/ch02-hotels-data-prep.R)
  - Arthur Turrell's Coding for Economics classes: [Data Analysis Quickstart](https://aeturrell.github.io/coding-for-economists/data-analysis-quickstart.html), [Working with Data](https://aeturrell.github.io/coding-for-economists/data-intro.html), [Data Transformation](https://aeturrell.github.io/coding-for-economists/data-transformation.html)