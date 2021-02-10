#Create a histogram of gravel.radius.
# Create a histogram of gravel.radius
plt.hist(gravel.radius)

# Display histogram
plt.show()


#Modify the histogram such that the histogram is divided into 40 bins and the range is from 2 to 8.
# Create a histogram
# Range is 2 to 8, with 40 bins
plt.hist(gravel.radius, range =(2,8), bins=40)

# Display histogram
plt.show()


#Normalize your histogram so that the sum of the bins adds to 1.
# Create a histogram
# Normalize to 1
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density=True)

# Display histogram
plt.show()


#Label the x-axis (Gravel Radius (mm)), the y-axis (Frequency), and the title(Sample from Shoeprint).
# Create a histogram
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density=True)

# Label plot
plt.xlabel('Gravel Radius (mm)')
plt.ylabel('Frequency')
plt.title('Sample from Shoeprint')

# Display histogram
plt.show()
