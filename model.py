from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


def build_model():
    """This function builds a new model and returns it.

    The model should be implemented as a sklearn Pipeline object.

    Your pipeline needs to have two steps:
    - preprocessor: a Transformer object that can transform a dataset
    - model: a predictive model object that can be trained and generate predictions

    :return: a new instance of your model
    """
    preprocessor = ColumnTransformer([("processing", TfidfVectorizer(), "text")])
    return Pipeline([("preprocessor", preprocessor), ("model", MultinomialNB())])