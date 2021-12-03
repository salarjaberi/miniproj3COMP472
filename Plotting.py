import numpy as np
import matplotlib.pyplot as plt
barWidth = 0.15
fig = plt.subplots(figsize=(20, 14))
#fig.subplots_adjust(bottom=0.3)

# set height of bar
#correct label
Correct = [70, 70, 73, 33, 35]
#wrong label
Wrong = [9, 8, 6, 36, 34]
#Accuracy label
Accuracy = [88.61, 89.74, 92.41, 47.83, 50.72]
GoldStrandard=[86.17]

# Set position of bar on X axis
br1 = np.arange(len(Correct))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3]


# Make the plot
plt.bar(br1, Correct, color='g', width=barWidth,
        edgecolor='grey', label='Correct')
plt.bar(br2, Wrong, color='r', width=barWidth,
        edgecolor='grey', label='Wrong')
plt.bar(br3, Accuracy, color='b', width=barWidth,
        edgecolor='grey', label='Accuracy')
plt.bar(br4, GoldStrandard, color='y', width=barWidth,
        edgecolor='grey', label='GoldStrandard')


# Adding Xticks
plt.xlabel('Models', fontweight='bold', fontsize=15)
plt.ylabel('Models Data', fontweight='bold', fontsize=15)
plt.xticks([r + barWidth for r in range(len(Correct))],
           ['Model1', 'Model2', 'Model3', 'Model4', 'Model5'])
plt.legend()
plt.show()
