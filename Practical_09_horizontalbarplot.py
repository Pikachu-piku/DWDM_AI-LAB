import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

# Prompt the user to enter the number of rolls to be performed
number_of_rolls = int(
    input('Please enter the number of rolls to perform - 360/36,000/36,000,000\n'))

# Perform the rolls of 2 dice and add the values obtained on each
rolls = [random.randrange(1, 7)+random.randrange(1, 7)
         for i in range(number_of_rolls)]

# Find the frequency of the all the values
values, frequencies = np.unique(rolls, return_counts=True)

# Title for the plot
title = f'Frequencies for {len(rolls):,} Rolls'

# Set the style of the grid to be a white one
sns.set_style("whitegrid")

# Using the barplot function to plot the bars , with the orient keyword set to h for horizontal bars
axes = sns.barplot(frequencies, values, palette='bright', orient="h")

# Set the title of the plot
axes.set_title(title)

# Set the X and Y labels
axes.set(xlabel='Frequency', ylabel='Die Value')

# Set the right end of the x axis to be 1.1 times the maximum frequency
axes.set_xlim(right=max(frequencies)*1.10)

# Using this variable to determine the Y co-ordinate of the text that appears at the top of the bar
y_coordinate = 0.3

# For all the bars, set the text displaying frequency and the percentage
for bar, frequency in zip(axes.patches, frequencies):

    # Setting up the X and Y co-ordinates for the text
    text_x = 1.01*frequency
    text_y = y_coordinate

    # Setting the text value to be displayed on the bar
    text = f'{frequency:,}\n{frequency/len(rolls):.3%}'
    axes.text(text_x, text_y, text, fontsize=11, ha='left', va='bottom')

    # Update the Y co-ordinate for the next bar
    y_coordinate = y_coordinate+1

# Display the plot
plt.show()
