# Lecture 05: graphs basics

## Motivation

You should look at your data. Graphs and charts let you explore and learn about the structure of the information you collect. Good data visualizations also make it easier to communicate your ideas and findings to other people. Beyond that, producing effective plots from your own data is the best way to develop a good eye for reading and understanding graphs — good and bad — made by others, whether presented in research articles, business slide decks, public policy advocacy, or media reports.

To create a powerful graph, it is a good starting principle that all of our decisions should be guided by the *usage of the graph*: a summary concept to capture what we want to show and to whom. Its main elements are purpose, focus, and audience. Once usage is clear, the first set of decisions to make is about how we convey information: how to show what we want to show. For those decisions it is helpful to understand the entire graph as the
overlay of three graphical objects:

  1. Geometric object; the geometric visualization of the information we want to convey, such as a
  set of bars, a set of points, or a line; multiple geometric objects may be combined.
  2. Scaffolding: elements that support understanding the geometric object, such as axes, labels, and
  legends.
  3. Annotation: adding anything else to emphasize specific values or explain more detail.

Keeping these in mind this lecture introduces students to how to create graphs that take into account these principles.

## This lecture

This lecture introduces the tools to create and manipulate plots with `plotnine` and `matplotlib`. `plotnine` is used through the [`case studies`](https://github.com/gabors-data-analysis/da_case_studies) for the textbook, its based on `ggplot2` of the R language.

`matplotlib` is the primary charting library of Python. It is a massive library, which offers so much, that it can easily become overwhelming. Creating a basic chart is fairly simple, but sometimes just a little customization already requires a deep dive into the API. 

One of the reasons we cover matplotlib here though is that many other libraries are also built on the matplotlib API, and  plotting charts directly from Pandas dataframes is easier if we have a basic understading of matplotlib's mechanics. There are other popular charting packages, such as `seaborn` or `Plotly`, but we think that a real Pythonista should be able to work with matplotlib objects.

Case studies used/related in/to this lecture:

  - [Chapter 03, B Comparing hotel prices in Europe: Vienna vs London](https://gabors-data-analysis.com/casestudies/#ch03b-comparing-hotel-prices-in-europe-vienna-vs-london) is the base for this lecture.
  - Some tools are used in [Chapter 04, A Management quality and firm size: describing patterns of association](https://gabors-data-analysis.com/casestudies/#ch04a-management-quality-and-firm-size-describing-patterns-of-association)


## Learning outcomes
After completing [`01_plotnine_intro.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture05-graphs-basics/01_plotnine_intro.ipynb) students should be able to:

  - create `ggplot` objects with different types of figures using `geoms` 
  - manipulating axis with `scale_*_continuous` and `scale_*_discrete`, where `*` stands for `y` or `x`
    - set limits
    - set break points
  - add annotation to a plot
    - lines, dots and text
  - bar charts:
    - simple
    - stacked
    - stacked with percentages, using `scales` package
  - box plot
  - violine plot
  - use `color[x]` color values from a pre-defined list

After completing [`02_matplotlib_intro.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture05-graphs-basics/02_matplotlib_intro.ipynb) students should be able to:

- the two key object in a `matplotlib` plot
  - `Figure` 
  - `Axes`
- set
  - y-axis limits
  - legends
  - log scale
- using a second axis
- spacing between the bars and horizontal grids
- chart within a chart

## Datasets used
* [Hotel Europe](https://gabors-data-analysis.com/datasets/#hotels-europe)

## Lecture Time

Ideal overall time: **30-60mins**.

Showing [`plotnine_intro.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture05-graphs-basics/plotnine_intro.ipynb) takes around *30 minutes* while doing the tasks would take approx *10-15 minutes*. Showing [`matplotlib_intro.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture05-graphs-basics/matplotlib_intro.ipynb) takes around *15-20 minutes*.

## Further material

  - [Introduction to Matplotlib — Data Visualization in Python](https://heartbeat.comet.ml/introduction-to-matplotlib-data-visualization-in-python-d9143287ae39) in general focuses on visualization with matplotlib.
  - Arthur Turrell's Coding for Economics classes: [Intro to Data Visualisation](https://aeturrell.github.io/coding-for-economists/vis-intro.html), [Common Plots](https://aeturrell.github.io/coding-for-economists/vis-common-plots.html)
  - [Official webpage of `plotnine`](https://plotnine.readthedocs.io/en/stable/)
  - [Official webpage of `matplotlib`](https://matplotlib.org/)
