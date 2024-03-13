# Is it edible or poisonous?

by Jessica Baggett, Ryan Joseph, Melissa Mosby and Christian Suarez

### Background:
Our dataset, "Mushroom Classification" (Kaggle), was found on Kaggle. We decided to use this dataset because it fits the supervised machine learning and allows for predictions.  

The "Mushroom Classification" dataset is completely categorical classifications for a number of attributes for 23 species of gilled mushroom in the Agarcius and Leptioa family mushroom. The data was drawn from The Audubon Society Field Guide to North American Mushrooms in 1981.

### Question:
Is this mushroom edible or poisonous? To analyze the data, we used random forest and logistic regression. We also created a flask application with 10 mushroom attributes to predict if a mushroom is edible or poisonous. Finally, we presented our findings in an HTML file.

### Machine Learning and Analysis:
Our dataset is supervised learning. Random forest and logistic regression are both strong and robust models that can analyze categorical classifications effectively. Also, these models can analyze our data to fit our yes or no question.

We selected these two models because we wanted to explore the possibilities of what each model could predict/train given the uniqueness of the complete categorial of our dataset.

The random forest and logistic regression models were ran twice. The first analyses used all 22 mushroom attributes. The second analyses were to optimize the original models. The optimization used 10 selected attributes. 

### Random Forest Model Analysis Details:
The random forest model was created in Juypter notebook and used the following libraries: numpy, python matplotlib, python pandas, Scikit-learn, and scipy,stats. 

#### First analysis steps:
1) Import and read mushroom csv;
2) Separated the y variable, edible or poisonous, and the x variables, mushroom attributes;
3) Encoded with LabelEncoder to code "p" for poisonous as positive "1";
4) Used OneHotEncoder;
5) Split the trained data;
6) Trained the data;
7) Scaled the data;
8) Fit the random forest model;
9) Made predictions;
10) Evaluated model on the confusion matrix and accuracy score; and
11) Ran a feature importance to see which attributes were more important.

#### Optimized analysis steps:
1) Remove the bottom 12 attributes;
2) Separated the y variable, edible or poisonous and the x variables, mushroom attributes;
3) Encoded with LabelEncoder to code "p" for poisonous as positive "1";
4) Used OneHotEncoder;
5) Split the trained data;
6) Trained the data;
7) Scaled the data;
8) Fit the random forest model;
9) Made predictions;
10) Evaluated model on the confusion matrix and accuracy score; and
11) Created a pie chart showing the 10 most important attributes.

### Logistic Regression Model Analysis Details:
The logistic regression model was created in Juypter notebook and used the following libraries: numpy, python matplotlib, python pandas, Scikit-learn. 

#### First analysis steps:
1) Import and read mushroom csv;
2) Separated the y variable, edible or poisonous, and the x variables;
3) Encoded with LabelEncoder;
4) Created dummies for x variables;
5) Split the trained data;
6) Trained the data;
7) Made predictions;
8) Evaluated model on the confusion matrix and accuracy score; and
9) Created a scatter plot.

#### Optimized analysis steps:
1) Import and read mushroom csv;
2) Separated the y variable, edible or poisonous, and removed 13 x variables;
3) Encoded with LabelEncoder;
4) Created dummies for x variables;
5) Split the trained data;
6) Trained the data;
7) Made predictions; and
8) Evaluated model on the confusion matrix and accuracy score.

### Flask Application:
We created a flask application to predict if a mushroom is edible or poisonous. The application has 10 mushroom attributes that you enter and based on those selections, you find out if the mushroom is edible or poisonous. 









#### Resources:

(https://www.kaggle.com/datasets/uciml/mushroom-classification?resource=download).

Comprehensive Guide on Feature Selection. (https://www.kaggle.com/code/prashant111/comprehensive-guide-on-feature-selection).

Multilabel-indicator is not supported for confusion matrix. (https://stackoverflow.com/questions/46953967/multilabel-indicator-is-not-supported-for-confusion-matrix).

How to adjust padding with cutoff or overlapping labels. (https://stackoverflow.com/questions/6774086/how-to-adjust-padding-with-cutoff-or-overlapping-labels).

How do I get the row count of a Pandas DataFrame?. (https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe).

How to avoid overlapping of labels & autopct in a pie chart. (https://stackoverflow.com/questions/23577505/how-to-avoid-overlapping-of-labels-autopct-in-a-pie-chart).

NeuronNet Insurance Charges- COLAB RunTime.ipynb. (https://colab.research.google.com/drive/1JmQtNPw7p22TszcKibvtIFQa63ZK-IM4?usp=drive_link).

Pickle your model in Python. (https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb#:~:text=Using%20pickle%20%2C%20simply%20save%20your,and%20rb%20for%20read%20mode).

Machine Learning Model Deployment on Heroku Using Flask. (https://towardsdatascience.com/machine-learning-model-deployment-on-heroku-using-flask-467acb4a34da). 

Flask Python Buttons (https://stackoverflow.com/questions/19794695/flask-python-buttons).



