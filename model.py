from keras import layers
from keras import Input
from keras.models import Sequential
from keras.utils import np_utils
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import numpy as np

class Preprocessor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        # convert to 0,1
        X = X / 255
        
        # insert extra dimensions
        X = np.expand_dims(X, -1)
        
        if y is None:
            return X

        y = np_utils.to_categorical(y, 4)
        return X, y


def keras_builder():
    model = Sequential([
        layers.ZeroPadding2D((1,1), input_shape=[28,28,1]),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dense(200, activation="relu"),
        layers.Dropout(0.5),
        layers.Dense(4, activation="softmax")
    ])
    model.compile(
        optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
    )
    return model


def build_model():
    """This function builds a new model and returns it.

    The model should be implemented as a sklearn Pipeline object.

    Your pipeline needs to have two steps:
    - preprocessor: a Transformer object that can transform a dataset
    - model: a predictive model object that can be trained and generate predictions

    :return: a new instance of your model
    """
    preprocessor = Preprocessor()

    model = KerasClassifier(build_fn=keras_builder, batch_size=16, epochs=10)

    return Pipeline([("preprocessor", preprocessor), ("model", model)])
