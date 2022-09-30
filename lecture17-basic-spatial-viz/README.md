# Lecture 20: Spatial data visualization

## Motivation

Visualizing data spatially can allow us to make insights as to what is going on beyond our bubble. Aside from being great visuals that immediately engage audiences, map data visualizations provide a critical context for the metrics. Combining geospatial information with data creates a greater scope of understanding. Some benefits of using maps in your data visualization include:

1. A greater ability to more easily understand the distribution of your variable across the city, state, country, or world.
2. The ability to compare the activity across several locations at a glance
3. More intuitive decision making for company leaders
4. Contextualizing your data in the real world


There is lots of room for creativity when making map dashboards because there are numerous ways to convey information with this kind of visualization. In R, we map geographical regions colored, shaded, or graded according to some variable. They are visually striking, especially when the spatial units of the map are familiar entities.

| Life expectancy map    | Hotel prices in cities  |
|-------------------------|-------------------------|
| ![alt text 1](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture17-basic-spatial-viz/output/lifeexp.png) | ![alt text 2](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture17-basic-spatial-viz/output/heu_prices.png) |


## This lecture

This lecture introduces spatial data visualization using maps. During the lecture, students learn how to use the `maps` package which offers built-in maps with the [worldbank-lifeexpectancy](https://gabors-data-analysis.com/datasets/#worldbank-lifeexpectancy) data. Plotting the raw life expectancy at birth on a world map is already a powerful tool, but students will learn how to show deviance from the expected value given by the regression model. In the second part, students import raw `shp` files with auxiliary files, which contain the map of London boroughs and Vienna districts. With the [hotels-europe](https://gabors-data-analysis.com/datasets/#hotels-europe) dataset the average price for each unit on the map is shown.

Case studies used during the lecture:
  - [Chapter 08, B: How is life expectancy related to the average income of a country?](https://gabors-data-analysis.com/casestudies/#ch08b-how-is-life-expectancy-related-to-the-average-income-of-a-country)
  - [Chapter 03, B: Comparing hotel prices in Europe: Vienna vs London](https://gabors-data-analysis.com/casestudies/#ch03b-comparing-hotel-prices-in-europe-vienna-vs-london)

## Learning outcomes
After successfully completing [`01_spatial_datavisualisation.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture17-basic-spatial-viz/01_spatial_datavisualisation.ipynb) students should be able:

  - Understand how `geom_polygon` works
  - Shaping the outlook of the map with `coord_equal` or `coord_map`
  - Creating a `theme_map` theme
  - Use different coloring with `scale_fill_gradient`
  - How to match different data tables to be able to plot a map
  - Use custom values as a filler on the map based on life-expectancy case study

After successfully completing [`02_spatial_datavisualisation.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture17-basic-spatial-viz/02_spatial_datavisualisation.ipynb) students should be able:

    - Use `geopandas` package to import 'shp' files and other needed auxiliary files as 'shx' and 'dbf'
    - `geom_path` to color the edges of the map
    - Map manipulations to show only inner-London boroughs
    - Add (borough or district) names to a map with `geom_text`
    - Control for limits of legend colors with `scale_fill_gradientn()`
    - Use nice color maps with unique palettes
    - Task for Vienna: replicate the same as for London

## Lecture Time

Ideal overall time: **40-60 mins**.

Going through [`01_spatial_datavisualisation.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture17-basic-spatial-viz/01_spatial_datavisualisation.ipynb) and [`02_spatial_datavisualisation.ipynb`](https://github.com/gabors-data-analysis/da-coding-python/blob/main/lecture17-basic-spatial-viz/02_spatial_datavisualisation.ipynb) takes around 20-40 minutes. Solving the tasks takes the remaining 20-40 minutes as there are two long tasks.


## Homework

*Type*: quick practice, approx 10 mins

Get countries' GDP growth rates with the `WDI` package. Plot the values in a world map.


## Further material

 - Arthur Turrell's Coding for Economics classes: [Geo-Spatial Visualisation](https://aeturrell.github.io/coding-for-economists/geo-vis.html).
  - Create beautiful maps with [Plotly](https://plotly.com/python/maps/).
  - Maps with [Matplotlib](https://towardsdatascience.com/mapping-with-matplotlib-pandas-geopandas-and-basemap-in-python-d11b57ab5dac).
  