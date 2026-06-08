# This file is used for development and local testing
import time_series_visualizer
import unittest

# Run visualization functions to manually verify figure generations
print("Rendering Trend Line Structure...")
time_series_visualizer.draw_line_plot()

print("Rendering Pivot Bar Groups...")
time_series_visualizer.draw_bar_plot()

print("Rendering Comparative Box Subplots...")
time_series_visualizer.draw_box_plot()

# Run automated tests
print("\nExecuting Unit Verification Tests:")
unittest.main(module='test_module', exit=False)