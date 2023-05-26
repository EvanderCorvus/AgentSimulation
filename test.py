import matplotlib.pyplot as plt

# Create some data for the plot
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 8, 27, 64, 125]

# Plot the data
plt.plot(x, y1, label='Line 1')
plt.plot(x, y2, label='Line 2')

# Customize the appearance of each legend
legend1 = plt.legend(loc='upper left')
legend2 = plt.legend(loc='upper right')

# Create a new legend that combines the two legends
plt.gca().add_artist(legend1)

# Customize the labels for each legend
legend1.get_texts()[0].set_text('Legend 1')
legend2.get_texts()[0].set_text('Legend 2')

# Show the plot
plt.show()
