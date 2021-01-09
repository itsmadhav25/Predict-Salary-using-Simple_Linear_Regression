# Predict-Salary-using-Simple_Linear_Regression

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure

This project has four major parts :

1. model.py - This contains code for our ML model to predict salaries based on trainign data in 'dataset.csv' file.

2. application.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the predicted value based on our model and returns it.

3. request.py - This uses requests module to call APIs already defined in application.py and dispalys the returned value.

4. templates - This folder contains the HTML template to allow user to enter employee detail and displays the predicted employee salary.

