import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the linear function to fit the data
def linear_func(x, a, b):
    return a * x + b

# Load the data
y_data = np.array([
    20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200,
    210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370,
    380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540,
    550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710,
    720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880,
    890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000
])

x_data = np.array([
    1, 30, 63, 93, 124, 157, 187, 220, 249, 283, 312, 344, 376, 408, 437, 468, 501, 532,
    563, 594, 627, 657, 690, 720, 751, 783, 816, 847, 878, 909, 941, 972, 1003, 1034,
    1066, 1097, 1128, 1159, 1191, 1222, 1254, 1285, 1316, 1348, 1379, 1410, 1442, 1474,
    1505, 1536, 1569, 1600, 1632, 1663, 1694, 1725, 1757, 1788, 1820, 1852, 1883, 1914,
    1946, 1978, 2009, 2041, 2072, 2103, 2134, 2166, 2198, 2229, 2261, 2292, 2324, 2356,
    2388, 2419, 2450, 2481, 2513, 2545, 2576, 2607, 2639, 2671, 2702, 2733, 2765, 2797,
    2827, 2859, 2890, 2922, 2953, 2985, 3016, 3048, 3079
])

# Fit the curve to the data
popt, pcov = curve_fit(linear_func, x_data, y_data)

# Plot the data and the fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, linear_func(x_data, *popt), 'r-', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Curve Fitting Example with Linear Function')
plt.show()

# Print the optimized parameters
print("Optimized Parameters (a, b):", popt)

