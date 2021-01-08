import flask as fl # Web services
import numpy as np # For working with Arrays
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline

# Create new web app
app = fl.Flask(__name__)

# Add root route
#@app.route('/powerPredictor')
#def powerPredictor():
#    return {data.head()}

# Load in file locally, skip 1 row due to heading, labelled [speed][power].
speed, power = np.loadtxt("data.csv", delimiter=",", skiprows=1, unpack=True)

# Test Output
print(speed, power)

# Plot speed, power
plt.plot(speed, power)

# Plot labels
plt.xlabel('Wind Speed')
plt.ylabel('Power Generated')

# Display plot
plt.show()

# Linear Regression
from sklearn.linear_model import LinearRegression

#reg = LinearRegression().fit(speed, power)
#reg.score(speed, power)