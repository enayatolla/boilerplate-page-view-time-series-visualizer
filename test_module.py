import unittest
import time_series_visualizer
import matplotlib as mpl

class DataCleaningTestCase(unittest.TestCase):
    def test_data_cleaning(self):
        # Targets standard index lengths following statistical outlier purging
        actual = time_series_visualizer.df.shape[0]
        expected = 1238
        self.assertEqual(actual, expected, "Data cleaning sequence failed to yield the targeted row shape.")

class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_line_plot()
        self.ax = self.fig.axes[0]

    def test_line_plot_title(self):
        self.assertEqual(self.ax.get_title(), "Daily freeCodeCamp Forum Page Views 5/2016-12/2019", "Line chart title structure mismatch.")

    def test_line_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Date", "X label must explicitly read 'Date'")
        self.assertEqual(self.ax.get_ylabel(), "Page Views", "Y label must explicitly read 'Page Views'")

class BarPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_bar_plot()
        self.ax = self.fig.axes[0]

    def test_bar_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Years", "X label must read 'Years'")
        self.assertEqual(self.ax.get_ylabel(), "Average Page Views", "Y label must read 'Average Page Views'")

class BoxPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_box_plot()
        self.ax1 = self.fig.axes[0]
        self.ax2 = self.fig.axes[1]

    def test_box_plot_titles(self):
        self.assertEqual(self.ax1.get_title(), "Year-wise Box Plot (Trend)")
        self.assertEqual(self.ax2.get_title(), "Month-wise Box Plot (Seasonality)")

if __name__ == "__main__":
    unittest.main()