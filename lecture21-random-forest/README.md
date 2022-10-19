# Lecture 24: Predicting with Random Forest and Boosting

## Motivation

You need to predict rental prices of apartments using various features. You don’t know that the various features may interact with each other in determining price, so you would like to use a regression tree. But you want to build a model that gives the best possible prediction, better than a single tree. What methods are available that keep the advantage of regression trees but give a better prediction? How should you choose from among those methods?

How can you grow a random forest, the most widely used tree-based method, to carry out the prediction of apartment rental prices? What details do you have to decide on, how should you decide on them, and how can you evaluate the results?

A regression tree can capture complicated interactions and nonlinearities for predicting a quantitative y variable, but it is prone to overfit the original data, even after appropriate pruning. It turns out, however, that combining multiple regression trees grown on the same data can yield a much better prediction. Such methods are called ensemble methods. There are many ensemble methods based on regression trees, and some are known to produce very good predictions. But these methods are rather complex, and some of them are not straightforward to use.

## This lecture

This lecture introduces two ensemble methods based on regression trees: random forest and boosting. We start by introducing the main idea of ensemble methods: combining results from many imperfect models can lead to a much better prediction than a single model that we try to build to perfection. The random forest is perhaps the most frequently used method to predict a quantitative y variable, both because of its excellent predictive performance and because it is relatively simple to use. Even more than with a single tree, it is hard to understand the underlying patterns of association between y and x that drive the predictions of ensemble methods. We discuss some diagnostic tools that can help with that: variable importance plots, partial dependence plots, and examining the quality of predictions in subgroups. Finally, we show another method: boosting, an alternative approach to making predictions based on an ensemble of regression trees via `xgboost`.

Note that some of the used methods take a considerable amount of time to run on a simple PC, thus pre-run model results are also uploaded to the repository, to speed up the seminar.

Case study:
  - [Chapter 16, A: Predicting apartment prices with random forest](https://gabors-data-analysis.com/casestudies/#ch16a-predicting-apartment-prices-with-random-forest)

## Learning outcomes

Lecturer/students should be aware that there is a separate file: [`airbnb_prepare.R`](https://github.com/gabors-data-analysis/da-coding-rstats/blob/main/lecture24-random-forest/codes/airbnb_prepare.R) for this seminar, overviewing only the data cleaning and feature engineering process. This is extremely important and powerful to understand how to prepare the data for these methods, as without it data analysts do garbage-in garbage-out analysis... Usually, due to time constraints, this part is not covered in the seminar but asked students to cover it before the seminar.

After successfully completing [`02_random_forest_airbnb.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture21-random-forest/02_random_forest_airbnb.ipynb), students should be able:

  - Estimate random forest models via `sklearn`
    - unsderstand `max_features` and `min_samples_split` parameters
    - GridSearchCV to search for hyperparameters
  - Understanding random forest's output
    - variable importance plots: all, top 10 and grouped variables (typically factors)
    - partial dependence plot
    - sub-sample analysis for understanding prediction performance across groups
    - SHAP values
  - Run a 'Horse-Race' prediction competition with:
    - Linear regression (OLS)
    - ElasticNet
    - Regression Tree with CART
    - Random Forest
    - XGBoost model

## Dataset used

- [airbnb](https://gabors-data-analysis.com/datasets/#airbnb)

## Lecture Time

Ideal overall time: **100 mins**.


## Further material

  - This lecture is a modified version of [ch16-airbnb-random-forest.ipynb](https://github.com/gabors-data-analysis/da_case_studies/blob/master/ch16-airbnb-random-forest/Ch16-airbnb-random-forest.ipynb) from [Gabor's case study repository](https://github.com/gabors-data-analysis/da_case_studies).

