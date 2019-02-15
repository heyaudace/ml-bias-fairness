import numpy as np 
import pandas as pd
from sklearn import preprocessing, neighbors
class Preprocessor(object):
    def __init__(self, dataframe, categorical_features, continuous_features, others=[]):
        """
        Params:
            - 
            - 
            - 
        Returns:
            - 
        """
        self.df = dataframe
        self.categ = categorical_features
        self.contn = continuous_features
        pass
    @property
    def processed(self):
        """
        Categories are transformed to one-hot encoding
        Continuos values are normalized
        A corresponding pandas df is returned
        """
        pass
    @staticmethod
    def encode_categories(original_df: pd.DataFrame, categorical_columns, le:preprocessing.LabelEncoder, in_place=True):
        """
        Encode categories with numbers
        Params:
            -original_df: data source
            -categories: List of categorical columns
            -le: label encoder
            -in_place: whether or not the transformation should be applied in place
        Return:
            DataFrame with columns replaced by categorically encoded labels. Same as original_df if in_place, otherwise
            it is a new dataframe
        """
        new_df = original_df if in_place else original_df.copy()
        for categorical_column in categorical_columns:
            new_df[categorical_column] = le.fit_transform(new_df[categorical_column])
        return new_df

    @staticmethod
    def to_one_hot(df: pd.DataFrame, categorical_columns, enc:preprocessing.OneHotEncoder=None):
        """
        Get a numpy array containing hone-hot encodings for the categories
        Returns a numpy array of size (1, n), where index i is a (1, m) matrix containing one-hot encodings
        """
        enc = preprocessing.OneHotEncoder() if enc is None else enc
        new_columns = np.zeros((1, len(set(categorical_columns))))
        for index, column in enumerate(categorical_columns):
            one_hots = enc.fit_transform(df[column].values.reshape(-1, 1)).toarray()
            new_columns[index] = one_hots
        return new_columns

    @staticmethod
    def normalize_columns(original_df, continuos_columns, in_place=True):
        """
        Apply lambda X:  (X-X.mean())/X.std() for every column
        Params:
            - 
            - 
        Returns:
            - 
        """
        return None
    @property
    def original(self):
        return self.df
    