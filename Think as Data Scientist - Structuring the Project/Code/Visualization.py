"""
Visualization class for t-shirt project.
"""
import matplotlib.pyplot as plt
from numpy import array
from pandas import DataFrame


class Visualizer:
    """
    Class for visualizing data in t-shirt project.
    """

    def __init__(self) -> None:
        self._my_colors = ["#2E2300", "#DB9501", "#375E97", "#3F681C", "#C05805"]

    def plot_t_shirt_data(self, data: DataFrame, x_axis_attribute: str, y_axis_attribute: str, \
                          equal_axis: bool = False) -> None:
        """
        Plots t-shirt data

        :param data: DataFrame. The data frame for plotting.
        :param x_axis_attribute: str. The name of attribute from data frame to plot on x axis.
        :param y_axis_attribute: str. The name of attribute from data frame to plot on y axis.
        :param equal_axis: bool. Indicator whether to plot axis equal.
        """
        # take out x and y variables
        x = data[x_axis_attribute]
        y = data[y_axis_attribute]

        # plot basics
        fig = plt.figure()
        axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])

        # scatter plot
        axes.scatter(
            x=x,
            y=y,
            c=self._my_colors[1],
            s=300,
            alpha=0.5,
            edgecolors=self._my_colors[0]
        )

        # axis labeling
        axes.set_xlabel(x.name)
        axes.set_ylabel(y.name)
        axes.set_title("Initial Data Visualization")

        # setting axes
        if equal_axis:
            plt.axis("equal")

    @staticmethod
    def plot_clusters(x: array, y: array, labels: array) -> None:
        """
        Plots the result of 2D clustering.
        :param x: array. X-axis data.
        :param y: array. Y-axis data.
        :param labels: array. Cluster labels for observations.
        """
        # figures are used in repeated manner, so the new one has to be defined after
        fig_clust = plt.figure()
        plt.scatter(x, y, c=labels, cmap='rainbow')

    @staticmethod
    def plot_clusters_and_centroid(x: array, y: array, labels: array, x_centroids: array, y_centroids: array, \
                                   title: str = "Title") -> None:
        """
        Plots the result of 2D clustering together with centroids.
        :param x: array. X-axis data.
        :param y: array. Y-axis data.
        :param labels: array. Cluster labels for observations.
        :param x_centroids: array. Array of x-axis coordinates of centroids.
        :param y_centroids: array. Array of y-axis coordinates of centroids.
        """
        # figures are used in repeated manner, so the new one has to be defined after
        fig_clust = plt.figure()
        plt.scatter(x, y, c=labels, cmap='rainbow')
        plt.scatter(x_centroids, y_centroids, marker="+", s=200, color="black")
        plt.title(title)

    def plot_metric(self, x: array, y: array) -> None:
        """
        Plots the clustering metric.
        :param x: array. ks from k means clustering
        :param y: array. Metric values for respective k.
        """
        # figures are used in repeated manner, so the new one has to be defined after
        fig = plt.figure()
        plt.plot(x, y, c=self._my_colors[4])
