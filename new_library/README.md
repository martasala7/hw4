Diabetes Prediction Model

The library we have created contains a machine learning pipeline designed to predict the occurrence of diabetes mellitus using a dataset. The pipeline includes data loading, cleaning, model training, model evaluation and returns the probabilities predicted by the model implemented. The model chosen is a Random Forest Classifier. 

Requirements

To run this project, you will need the following libraries installed in your environment:

- Python 3.12.7
- pandas (for data manipulation)
- os (to build a platform-independent file path to ensure the CSV file is correctly     loaded from the same directory as the script) 
- scikit-learn (for machine learning models and data splitting)
  - `sklearn.model_selection.train_test_split` (for splitting the data into train and test sets)
  - `sklearn.ensemble.RandomForestClassifier` (for training a Random Forest model)
  - `sklearn.metrics.accuracy_score` (for evaluating model accuracy)
  - `sklearn.metrics.roc_auc_score` (for evaluating ROC AUC)
