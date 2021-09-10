# Homework 1

## Team Members
Samuel Lindsay, lindsays15@students.ecu.edu<br>
Ian Lozano Diaz, lozanodiazi20@students.ecu.edu<br>
Thaddaeus Parchman, parchmant18@students.ecu.edu<br>

## Run Instructions

### Dependencies

Required Python modules.
``` Python
numpy
sklearn
matplotlib
```

### Running

Two files that can be run are included, a jupyter notebook file and python file. To run using jupyter, load the file and execute each cell interactively. To Run the Python file under a Unix environment use the command below where the version of python is =>3.7.

``` bash
python ./knn.py
```

### Run Parameters

While crude, the user does have the ability to modify two runtime parameters with relative ease. Under a section titled "Options", in both the notebook and Python file, there is a variable "trials", this is initially set at 5 but can be easily modified by the user. We conducted several runs with this variable set to a value of 1000. The second parameters is the name of the output plot, coltrolled by the variable "plot_name", also in the "Options" section.

## Questions

### Which K (from 1 to 20) works the best? If all Ks have similar accuracy, please write down your thoughts about “Why.”

We found that a run of only five trials per k was insufficient for stable reproduction of trends. We became curious and expanded the number of trials greatly, to 1000. Graphs of 5 trials and 1000 trials are both provided below. Multiple reproductions of the 1000 trial graph demonstrated a maximum accuracy most frequently at a value of k = 13. However, none of the tested k-values performed terribly. All ks had an accuracy of ~0.94 or higher. However, the high and low ends of the k-value ranges performed the worst. The high accuracy suggests that the data is well clustered and hence knn is a well-suited method for classification.

Worth note is that even numbers perform worse than odd numbers. I suspect this has to do with how the algorithm handles split decision edge cases; the instances when neighbors are evenly split between two (or more) groups. I could not locate it in the documentation but my suspiscion is that in such cases an assignment is made by some form of random choice thus reducing the accuracy of predictions. 



k = 5                      |  k = 1000
:-------------------------:|:-------------------------:
![](k5.png)                |  ![](k1000.png)

