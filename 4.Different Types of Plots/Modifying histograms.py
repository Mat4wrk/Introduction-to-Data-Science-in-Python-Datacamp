#Create a histogram of the column weight from the DataFrame puppies.
# Create a histogram of the column weight
# from the DataFrame puppies
plt.hist(puppies.weight)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()


#Change the number of bins to 50.
# Change the number of bins to 50
plt.hist(puppies.weight,
        bins = 50)

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()


#Change the range to start at 5 and end at 35.
# Change the range to start at 5 and end at 35
plt.hist(puppies.weight,
        range = (5, 35))

# Add labels
plt.xlabel('Puppy Weight (lbs)')
plt.ylabel('Number of Puppies')

# Display
plt.show()
