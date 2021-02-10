#Create a bar plot of the time each officer spends on desk_work.
#Label that bar plot "Desk Work".

# Plot the number of hours spent on desk work
plt.bar(hours.officer,hours.desk_work, label="Desk Work")

# Display the plot
plt.show()


#Create a bar plot for field_work whose bottom is the height of desk_work.
#Label the field_work bars as "Field Work" and add a legend.
# Plot the number of hours spent on desk work
plt.bar(hours.officer, hours.desk_work, label='Desk Work')

# Plot the hours spent on field work on top of desk work
plt.bar(hours.officer, hours.field_work, bottom = hours.desk_work, label='Field Work')

# Add a legend
plt.legend()

# Display the plot
plt.show()
