# Week 06 – Advanced Matplotlib & Data Visualization

## 1. Object-Oriented Matplotlib

In Matplotlib, I can work with figures and axes using the object-oriented approach.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set_title('My Chart')
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.show()

Important concepts
Figure → the entire window or canvas
Axes → the area where the data is plotted
ax.plot() → creates a plot
ax.set_title() → sets the title
ax.set_xlabel() → sets the x-axis label
ax.set_ylabel() → sets the y-axis label

The object-oriented approach is useful when working with multiple plots and more complex figures.

2. Figure and Axes

A Figure can contain one or more Axes.

For example:

fig, ax = plt.subplots()

creates:

one Figure
one Axes

When creating multiple Axes:

fig, ax = plt.subplots(2, 1)

This creates two Axes arranged in two rows and one column.

The Axes can then be accessed using:

ax[0]
ax[1]
3. Subplots

Subplots allow multiple charts to be displayed inside one Figure.

fig, ax = plt.subplots(2, 1, figsize=(8, 8))

The first argument represents the number of rows.

The second argument represents the number of columns.

For example:

plt.subplots(2, 1)

means:

2 rows
1 column

Another example:

plt.subplots(2, 2)

creates four Axes:

[0] [1]
[2] [3]

Subplots are useful when different aspects of the same dataset need to be compared.

4. Bar Charts

Bar charts are useful for comparing categories.

ax.bar(
    df['name'],
    df['length']
)

Example:

ax.bar(df['name'], df['length'])

ax.set_title('Bridge Length Comparison')
ax.set_xlabel('Bridge Name')
ax.set_ylabel('Length (m)')

A bar chart can also display the values using annotations.

for i, value in enumerate(df['length']):
    ax.annotate(
        f'{value}',
        xy=(df['name'][i], value + 5)
    )
5. Scatter Plots

Scatter plots are useful for examining the relationship between two numerical variables.

ax.scatter(
    df['length'],
    df['max_vib']
)

In this example:

X-axis → Bridge Length
Y-axis → Maximum Vibration

A scatter plot can help identify patterns or relationships between variables.

For example, if the points generally move upward from left to right, there may be a positive relationship.

However, a scatter plot alone does not prove causation.

6. Multiple Datasets on One Axes

Multiple datasets can be plotted on the same Axes.

ax.plot(time, sensor_1, marker='o', label='Sensor 1')
ax.plot(time, sensor_2, marker='s', label='Sensor 2')
ax.plot(time, sensor_3, marker='*', label='Sensor 3')

A legend helps identify each dataset.

ax.legend()

Different markers can make the datasets easier to distinguish.

Examples:

marker='o'
marker='s'
marker='*'
7. Figure Customization

Matplotlib provides many methods for improving the appearance and readability of charts.

Title
ax.set_title('Bridge Length Comparison')
Axis labels
ax.set_xlabel('Bridge Name')
ax.set_ylabel('Length (m)')
Grid
ax.grid()
Legend
ax.legend()
Figure size
fig, ax = plt.subplots(figsize=(8, 6))
Layout
plt.tight_layout()

plt.tight_layout() helps prevent titles and labels from overlapping.

8. Axis Ticks

Ticks are the values or labels displayed along an axis.

For example:

ax.set_xticks(bridge_names)

Ticks can also be rotated to make long labels easier to read.

ax.tick_params(
    axis='x',
    rotation=45
)

This is especially useful when category names are long.

9. Annotations

Annotations allow important points or values to be highlighted on a chart.

ax.annotate(
    'Longest Bridge',
    xy=('Bridge 4', 200),
    xytext=('Bridge 3', 180),
    arrowprops=dict(arrowstyle='->')
)
Important parameters
xy → location of the point being identified
xytext → location of the annotation text
arrowprops → controls the arrow

For example:

arrowprops=dict(arrowstyle='->')

creates an arrow pointing toward the selected point.

10. text() vs annotate()

Matplotlib provides both text() and annotate().

text()

Used mainly for placing text at a specific location.

ax.text(
    x,
    y,
    'Important value'
)
annotate()

Used when we want to connect text to a specific point, often with an arrow.

ax.annotate(
    'Important point',
    xy=(x, y),
    xytext=(x2, y2),
    arrowprops=dict(arrowstyle='->')
)

Therefore:

text() → simple text
annotate() → text connected to a specific point
11. Finding Maximum Values in Pandas

Pandas provides useful methods for finding maximum values.

df['length'].max()

returns the maximum value in the length column.

For example:

df['length'].max()

returns:

200
12. Finding the Row of the Maximum Value

idxmax() returns the index of the row containing the maximum value.

df['length'].idxmax()

For example, if Bridge 4 has the maximum length, this may return:

3

We can then use this index to find the bridge name:

df['name'][df['length'].idxmax()]

This returns:

Bridge 4

The same technique can be used for maximum vibration:

df['name'][df['max_vib'].idxmax()]
13. Basic Data Relationship Analysis

A scatter plot can be used as a first step to examine the relationship between two numerical variables.

For example:

ax.scatter(
    df['length'],
    df['max_vib']
)

If the points generally increase from left to right, the variables may have a positive relationship.

If they generally decrease from left to right, they may have a negative relationship.

If the points are widely scattered without a clear pattern, the relationship may be weak.

Important

A visual relationship does not necessarily mean that one variable causes the other.

Correlation and causation are different concepts.

14. Saving Figures

Matplotlib figures can be saved as image files.

plt.savefig('bridge_length.png')

For higher image quality:

plt.savefig(
    'bridge_length.png',
    dpi=300
)

It is usually better to save the figure before displaying it:

plt.savefig('bridge_length.png', dpi=300)
plt.show()
15. Reusable Plot Functions

Instead of repeating the same plotting code, I can create a reusable function.

def plot_sensor(time, sensor_data, sensor_name):

    fig, ax = plt.subplots()

    ax.plot(
        time,
        sensor_data,
        marker='o',
        label=sensor_name
    )

    ax.set_title(sensor_name)
    ax.set_xlabel('Time')
    ax.set_ylabel('Vibration')

    ax.legend()
    ax.grid()

    plt.tight_layout()
    plt.show()

Then I can use the same function for different sensors:

plot_sensor(time, sensor_1, 'Sensor 1')
plot_sensor(time, sensor_2, 'Sensor 2')
plot_sensor(time, sensor_3, 'Sensor 3')

This makes the code more reusable and reduces repetition.

16. Complete Project Example

In the Week 06 project, I used Pandas and Matplotlib together.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'name': bridge_names,
    'length': bridge_lengths,
    'year': construction_years,
    'material': materials,
    'max_vib': maximum_vibrations
})

I then created multiple visualizations using subplots.

fig, ax = plt.subplots(
    3,
    1,
    figsize=(8, 8)
)
Bridge Length
ax[0].bar(
    df['name'],
    df['length']
)
Maximum Vibration
ax[1].bar(
    df['name'],
    df['max_vib']
)
Bridge Length vs Maximum Vibration
ax[2].scatter(
    df['length'],
    df['max_vib']
)

Finally:

plt.tight_layout()
plt.show()
17. Project Analysis

Using Pandas:

df['length'].max()

I found the maximum bridge length.

Using:

df['length'].idxmax()

I found the index of the longest bridge.

Then:

df['name'][df['length'].idxmax()]

gave the name of the longest bridge.

The same method was used to find the bridge with the highest maximum vibration.

For this small dataset:

Longest Bridge: Bridge 4
Length: 200 m

Bridge with Highest Vibration: Bridge 4
Maximum Vibration: 5.2

The scatter plot suggests that longer bridges tend to have higher maximum vibration values in this dataset.

However, this conclusion is based on only five observations and does not prove a causal relationship.

18. Important Matplotlib Methods
Method	Purpose
plt.subplots()	Create a Figure and Axes
ax.plot()	Create a line plot
ax.bar()	Create a bar chart
ax.scatter()	Create a scatter plot
ax.set_title()	Set chart title
ax.set_xlabel()	Set x-axis label
ax.set_ylabel()	Set y-axis label
ax.legend()	Display legend
ax.grid()	Display grid
ax.set_xticks()	Set x-axis ticks
ax.set_yticks()	Set y-axis ticks
ax.tick_params()	Customize tick appearance
ax.annotate()	Add annotation
ax.text()	Add text
plt.tight_layout()	Improve layout
plt.savefig()	Save figure
plt.show()	Display figure
19. Important Pandas Methods Used in the Project
Method	Purpose
pd.DataFrame()	Create a DataFrame
df['column']	Select a column
.max()	Find the maximum value
.idxmax()	Find the index of the maximum value
20. Key Lessons

This week I learned that effective data visualization is not only about creating charts.

A good visualization should:

clearly communicate information
use an appropriate chart type
have meaningful titles and axis labels
make important values easy to identify
avoid unnecessary visual complexity
help the viewer understand patterns in the data

I also learned that different chart types serve different purposes:

Bar chart → comparing categories
Line chart → showing changes or trends
Scatter plot → examining relationships between numerical variables
Subplots → comparing multiple visualizations in one Figure
Week 06 Outcome

By the end of Week 06, I can create customized Matplotlib figures, work with multiple Axes, create subplots, add annotations, visualize relationships between variables, and perform simple data analysis using Pandas.

