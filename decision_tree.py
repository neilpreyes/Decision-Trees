#-------------------------------------------------------------------------
# AUTHOR: Neil Patrick Reyes
# FILENAME: A_1
# SPECIFICATION: Create decision trees based on data provided via csv file
# FOR: CS 4210- Assignment #1
# TIME SPENT: 30 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)


#transform the original categorical training features into numbers and add to the 4D array X.
  string_to_int_mapping = {
        'Young': 0,
        'Presbyopic': 1,
        'Prepresbyopic': 2,
        'Myope': 0,
        'Hypermetrope': 1,
        'No': 0,
        'Yes': 1,
        'Reduced': 0,
        'Normal': 1
  }
  for row in db:
     X.append([string_to_int_mapping[row[0]], string_to_int_mapping[row[1]], string_to_int_mapping[row[2]],string_to_int_mapping[row[3]]])


#transform the original categorical training classes into numbers and add to the vector Y.
  for row in db:
     Y.append([string_to_int_mapping[row[4]]])

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()