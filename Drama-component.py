import argparse

parser = argparse.ArgumentParser(description="Pipeline Parameter")

args = parser.parse_args()


if __name__ == "__main__":

    # =============================================================
    # Component: Importing Libairies
    # Parents: []
    import collections  # used to put data into sections
    import locale
    import math
    import sqlite3
    import statistics  # calculate math problmes
    from collections import defaultdict  # to check duplicates

    import altair as alt  # used to create interactive graphs
    import matplotlib.pyplot as plt  # used to make graphs
    import numpy as np
    import pandas as pd  # used to make for dataframes
    import plotly.graph_objects as go  # for creating tables and graphs
    from IPython.display import \
        display_html  # to disply dataframes side by side
    from IPython.display import HTML, display

    sqlite3.version
    from collections import Counter, OrderedDict

    import dataframe_image as dfi  # allows the datafrme to be an image
    import scipy.stats as stats
    from scipy import stats  # to calulate trimmed mean
    from scipy.stats import kurtosis  # to check skewness of distribution
    from scipy.stats import norm  # to plot stdev plot with mean
    from scipy.stats import skew  # to check skewness
