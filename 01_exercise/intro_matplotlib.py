"""A set of exercises with matplotlib"""


def draw_co2_plot():
    """
    Here is some chemistry data

      Time (decade): 0, 1, 2, 3, 4, 5, 6
      CO2 concentration (ppm): 250, 265, 272, 260, 300, 320, 389

    Create a line graph of CO2 versus time, the line should be a blue dashed
    line.

    The title of the plot should be 'Chemistry data'
    The label of the x axis should be 'Time (decade)'
    The label of the y axis should be 'CO2 concentration (ppm)'

    Your function does not need to return the plot -
    the final line of the function should be (assuming you have imported pyplot as plt):
    plt.show()
    """

    import matplotlib.pyplot as plt

    # create data
    time = [0, 1, 2, 3, 4, 5, 6]
    co2 = [250, 265, 272, 260, 300, 320, 389]

    plt.plot(time, co2, 'b--')
    plt.title("Chemistry Data")
    plt.xlabel('Time (decade)')
    plt.ylabel('CO2 concentration (ppm)')

    return True


def draw_equations_plot():
    """
    Plot the following lines on the same plot

      y=cos(x) coloured in red with dashed lines
      y=x^2 coloured in blue with linewidth 3
      y=exp(-x^2) coloured in black

    Add a legend, title for the x-axis and a title to the curve, the x-axis
    should range from -4 to 4 (with 50 points) and the y axis should range
    from 0 to 2. The figure should have a size of 8x6 inches.

    NOTE: Make sure you create the figure at the beginning as doing it at the
    end will reset any plotting you have done, and again finish with plt.show()
    """
    import matplotlib.pyplot as plt
    import numpy as np

    # Constants
    xsteps = 50
    xstart = -4
    xend = 4

    # compute
    xseries = np.linspace(xstart, xend, xsteps)
    ycos = np.cos(xseries)
    ysq = xseries ** 2
    yexp = np.e ** (-1 * ysq)

    # graph
    plt.figure(figsize=(8, 6))
    plt.plot(xseries, ycos, 'r--', label="y = cos(x)")
    plt.plot(xseries, ysq, 'b', linewidth=3, label="y = x ** 2")
    plt.plot(xseries, yexp, 'k', label="y = exp(-1 * x ** 2)")
    plt.legend()
    plt.show()

    return True
