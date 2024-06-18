# size_prediction.py

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def train_size_prediction_model(dataset_path):
    # Load the dataset
    data = pd.read_csv(dataset_path)

    # Encode the 'size' column
    label_encoder = LabelEncoder()
    data['size_encoded'] = label_encoder.fit_transform(data['size'])

    # Split the dataset into features (X) and target (y)
    X = data[['weight', 'age', 'height']]
    y = data['size_encoded']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Impute missing values in the features
    imputer = SimpleImputer(strategy='mean')
    X_train_imputed = imputer.fit_transform(X_train)
    X_test_imputed = imputer.transform(X_test)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train_imputed, y_train)

    return model
