def preprocess(df):
    """This function takes a dataframe and preprocesses it so it is
    ready for the training stage.

    The DataFrame contains the time axis and the target column.

    It also contains some rows for which the target column is unknown.
    Those are the observations you will need to predict for KATE
    to evaluate the performance of your model.

    Here you will need to return the training time serie: ts together
    with the preprocessed evaluation time serie: ts_eval.

    Make sure you return ts_eval separately! It needs to contain
    all the rows for evaluation -- they are marked with the column
    evaluation_set. You can easily select them with pandas:

         - df.loc[df.evaluation_set]


    :param df: the dataset
    :type df: pd.DataFrame
    :return: ts, ts_eval
    """
    import pandas as pd

    # reindex to day
    df.set_index(pd.to_datetime(df.day), inplace=True)
    df.drop(['day'], axis=1, inplace=True)

    # split into train and eval
    ts_eval = df.loc[df.evaluation_set]
    ts = df.loc[~df.evaluation_set]

    # drop eval column
    ts.drop(['evaluation_set'], axis=1, inplace=True)
    ts_eval.drop(['evaluation_set'], axis=1, inplace=True)

    return ts, ts_eval


def train(ts):
    """Trains a new model on ts and returns it.

    :param ts: your processed training time serie
    :type ts: pd.DataFrame
    :return: a trained model
    """
    from statsmodels.api import tsa

    model = tsa.ARMA(ts, (5,5)).fit()

    return model


def predict(model, ts_test):
    """This functions takes your trained model as well
    as a processed test time serie and returns predictions.

    On KATE, the processed testt time serie will be the ts_eval you built
    in the "preprocess" function. If you're testing your functions locally,
    you can try to generate predictions using a sample test set of your
    choice.

    This should return your predictions either as a pd.DataFrame with one column
    or a pd.Series

    :param model: your trained model
    :param ts_test: a processed test time serie (on KATE it will be ts_eval)
    :return: y_pred, your predictions
    """
    y_pred = model.predict(start=ts_test.index[0], end=ts_test.index[-1])
    return y_pred
