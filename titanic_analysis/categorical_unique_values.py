import pandas as pd

mock_df = pd.DataFrame({
    'Sex': ['male', 'female', 'female', 'male'],
    'Embarked': ['S', 'C', 'S', 'Q']
})

categorical_features = ['Sex', 'Embarked']

def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    unique_values = {feature: df[feature].unique().tolist() for feature in categorical_features}
    return unique_values

unique_values = display_unique_values(mock_df, categorical_features)

print(unique_values)
