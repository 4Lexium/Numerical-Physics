import matplotlib.ticker as ticker

num_of_points = 10000
num_of_bins = 20
data = np.random.randn(num_of_points) # generate random numbers from a gaussian distribution
fig, ax = plt.subplots()
ax.hist(data, bins=num_of_bins, edgecolor='black')
ax.set_title("Histogram")
ax.set_xlabel("X axis")
ax.set_ylabel("Percentage")
plt.show()

num_of_points = 10000
num_of_bins = 20 
data = np.random.randn(num_of_points) # generate random numbers from a gaussian distribution
fig, ax = plt.subplots()
ax.hist(data, bins=num_of_bins, edgecolor='black')
ax.set_title("Histogram")
ax.set_xlabel("X axis")
ax.set_ylabel("Percentage")
ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=len(data)))
plt.show()