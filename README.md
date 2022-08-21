# Coding for Data Analysis with Python   
by [Peter Duronelly](https://github.com/peterduronelly) and [Ádám Víg](https://github.com/adamvig96) 

This coding course is the Python alternative to Ágoston Reguly's corresponding [R-course](https://github.com/gabors-data-analysis/da-coding-rstats) to supplement to ***Data Analysis for Business, Economics, and Policy** 
by Gábor Békés (CEU) and Gábor Kézdi (U. Michigan),  Cambridge University Press, 2021*

*Textbook* information: see the textbook's website [gabors-data-analysis.com](https://gabors-data-analysis.com/) or visit [Cambridge University Press](https://www.cambridge.org/highereducation/books/data-analysis-for-business-economics-and-policy/D67A1B0B56176D6D6A92E27F3F82AA20)    
To get a copy: [Inspection copy for instructors](https://www.cambridge.org/highereducation/books/data-analysis-for-business-economics-and-policy/D67A1B0B56176D6D6A92E27F3F82AA20/examination-copy/personal-details) or [Order online](https://gabors-data-analysis.com/order)   


## Acknowledgments

We'd like to say thanks for [Ágoston Reguly](https://github.com/regulyagoston) who created the template for the initial coding supplement in R to the Data Analysis handbook. We followed his steps in writing the Python-version of the teaching material. 


## Status

This is version 0.1, as of August 21, 2022.

Comments are really welcome in email or as a GitHub issue. 


## Overview

The course is an introducton to the Python programming language, its software environment, and also to data exploration, data transformation, visualization, and more advanced data analysis. 

The material primarily consists of `Jupyter notebooks`, and is sometimes supplemented with additional data. In most cases, however, we used the [textbook's datasets](https://gabors-data-analysis.com/datasets/) to bring the course as close to the original textbook as possible.  

Lectures 0 to 6 are general introductions to Python and its concepts. These notebooks focus on coding principles, Python's main building blocks, and introduce the data analyst's most important data structure: Pandas dataframes.

Lecture 7 gives insight how to use Python for data exploration. Lectures 8 and 9 expands the toolkit for advanced data analytics techniques.

Lectures 10 to 16 cover everything you need to know about linear regression in Python on an introductionary level. We start with simple linear regression on cross-sectional data, then we explore binary models, and multiple linear regression. Finally we discuss the basic time-series regression model and its intricacies. 


## Philosopy and how to use

We tried to put together a benchmark course to supplement the Data Analysis texbook and to help anyone, students and intructors alike, follow the book's material. 


## Note

Most data science courses use the Anaconda environment for Python. We, however, use `pip` and `pipenv`, and run Jupyter notebooks from the course's environment. Anaconda is a great tool for data analysis and data science, but once someone goes beyond ad-hoc adata analysis and needs to develop and deploy advanced data solutions in a production environment in Python, `pip` is going to be the way to go. 