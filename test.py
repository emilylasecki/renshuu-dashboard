import matplotlib.pyplot as plt
 
# Create a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2)
 
# Now axs is a 2D array of Axes objects
axs[0, 0].plot([1, 2, 3], [4, 5, 6])
axs[0, 1].scatter([1, 2, 3], [4, 5, 6])
axs[1, 0].bar([1, 2, 3], [4, 5, 6])
axs[1, 1].hist([1, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 5])
 
plt.show()