from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def split_data(df, target_column='diabetes_mellitus', test_size=0.3, random_state=42):
    """Split the dataset into train and test sets."""
    X = df.drop(columns=target_column)
    y = df[target_column]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_model(X_train, y_train):
    """Train a Random Forest model."""
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def predict(model, X_test):
    """Make predictions on the test set."""
    return model.predict(X_test)

def calculate_accuracy(y_test, y_pred):
    """Calculate the accuracy of the model."""
    return accuracy_score(y_test, y_pred)

def predict_proba(model, X):
    """Predict probabilities with the trained model."""
    return model.predict_proba(X)[:, 1]

from sklearn.metrics import roc_auc_score
def calculate_roc_auc(model, X, y):
    """Compute ROC_AUC metric using predicted probabilities."""
    y_pred_proba = predict_proba(model, X)  
    return roc_auc_score(y, y_pred_proba)