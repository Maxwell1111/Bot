
import csv
import matplotlib.pyplot as plt

# open csv file
with open('test.csv', 'r') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    
    # get column titles from first row
    column_titles = next(data)
    subject_name = column_titles[0]
    x_axis_title = column_titles[1]
    y_axis_title = column_titles[2]
    
    # set x and y axis
    x_axis = []
    y_axis = []
    
    # get data
    for row in data:
        x_axis.append(float(row[1]))
        y_axis.append(float(row[2]))
    
    # plot data
    plt.plot(x_axis, y_axis)
    
    # set axis titles
    plt.xlabel(x_axis_title)
    plt.ylabel(y_axis_title)
    #add trendline
 
    # show plot
    plt.show()