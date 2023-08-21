import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data Points')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    future_years = range(df['Year'].iloc[0], 2050)
    future_line = slope * future_years + intercept
    plt.plot(future_years, future_line, color='r', label='Line of Best Fit (1880-2050)')

    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    slope_new, intercept_new, r_value_new, p_value_new, std_err_new = linregress(new_df['Year'],
                                                                                 new_df['CSIRO Adjusted Sea Level'])
    future_years_2 = range(2000, 2050)
    future_line_2 = slope_new * future_years_2 + intercept_new
    plt.plot(future_years_2, future_line_2, color='b', label='Line of Best Fit (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()


plt.show(draw_plot())