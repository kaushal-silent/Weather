import numpy as np
import matplotlib.pyplot as plt
def quadratic_model(x, a, b, c):
    return a * x**2 + b * x + c
a, b, c = 0.6, -6, 20
x = np.linspace(0, 10, 100)
y = quadratic_model(x, a, b, c)
plt.figure()
plt.scatter(x, y, label='Weather Data')
plt.title('Agile Model: Initial Weather Data')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.show()
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
x = np.linspace(0, 10, 100)
y = quadratic_model(x, a, b, c)
plt.figure()
plt.scatter(x, y, label='Weather Data')
plt.title('Agile Model: Weather Data with User Input')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.show()
with open('weather.txt', 'r') as file:
    lines = file.readlines()
    a, b, c = map(float, lines[0].split())
x = np.linspace(0, 10, 100)
y = quadratic_model(x, a, b, c)
plt.figure()
plt.scatter(x, y, label='Weather Data')
plt.title('Agile Model: Weather Data with File Input')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.show()
def generate_weather_data(start, end, num_points, a, b, c, noise_factor=10):
    x = np.linspace(start, end, num_points)
    y = quadratic_model(x, a, b, c) + np.random.normal(0, noise_factor, num_points)
    return x, y
a, b, c = 0.5, -5, 20
start_time = 0
end_time = 10
num_points = 100
x_data, y_data = generate_weather_data(start_time, end_time, num_points, a, b, c)
plt.figure()
plt.scatter(x_data, y_data, label='Weather Data')
plt.title('Agile Model: Weather Data with Noise')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.legend()
plt.show()
