import pandas as pd
import numpy as np

def preprocess(df):
    """This function takes a dataframe and preprocesses it so it is
    ready for the training stage.

    The DataFrame contains columns used for training (features)
    as well as the target column.

    It also contains some rows for which the target column is unknown. 
    Those are the observations you will need to predict for KATE 
    to evaluate the performance of your model.

    Here you will need to return the training set: X and y together
    with the preprocessed evaluation set: X_eval.

    Make sure you return X_eval separately! It needs to contain
    all the rows for evaluation -- they are marked with the column
    evaluation_set. You can easily select them with pandas:

         - df.loc[df.evaluation_set]

    For y you can either return a pd.DataFrame with one column or pd.Series.

    :param df: the dataset
    :type df: pd.DataFrame
    :return: X, y, X_eval
    """
    import json

    # drop unneeded features
    list_to_keep = ['goal',
                    'static_usd_rate',
                    'deadline',
                    'created_at',
                    'launched_at',
                    'state',
                    'evaluation_set']

    # list of items to further investigate to achieve 
    list_to_investigate = ['category', 'currency', 'profile', 'creator']

    selected_df = df[list_to_keep]


    # Apply conversions
    # goal currency application
    selected_df['goal_usd'] = selected_df['goal'] * selected_df['static_usd_rate']
    selected_df = selected_df.drop(['goal', 'static_usd_rate'], axis = 1)

    # set dates to relative one another
    # hypothesis here is longer deadlines likelier to succeed
    # longer setup time (launch after created) more effort put into crowdfund
    selected_df['launch_to_deadline'] = selected_df['deadline'] - selected_df['launched_at']
    selected_df['created_to_launch'] =  selected_df['launched_at'] - selected_df['created_at']
    selected_df = selected_df.drop(['launched_at', 'created_at'], axis = 1)

    # df = df.drop(list_to_drop, axis = 1)

    # # apply conversions
    # # create one hot encoding function
    # def custom_one_hot_encode(df, column, categories):
    #     for category in categories:
    #         df[f'{column}_{category}'] = (df[column] == category) * 1
    #     del df[column]

    # # one hot encode for currencies
    # currencies = 


    # # parse json and convert categories to major categories
    # df['category'] = df['category'].apply(lambda row: json.loads(row)['slug'].split('/')[0])

    # Seperate X_eval and X from data
    X_eval = selected_df[selected_df['evaluation_set']]
    X = selected_df[~selected_df['evaluation_set']]

    # Pull y from X
    y = pd.DataFrame(X['state'])
    X = X.drop('state', axis = 1)
    X_eval = X_eval.drop('state', axis = 1)

    return X, y, X_eval
    


def train(X, y):
    """Trains a new model on X and y and returns it.

    :param X: your processed training data
    :type X: pd.DataFrame
    :param y: your processed label y
    :type y: pd.DataFrame with one column or pd.Series
    :return: a trained model
    """
    raise NotImplementedError


def predict(model, X_test):
    """This functions takes your trained model as well 
    as a processed test dataset and returns predictions.

    On KATE, the processed test dataset will be the X_eval you built
    in the "preprocess" function. If you're testing your functions locally,
    you can try to generate predictions using a sample test set of your
    choice.

    This should return your predictions either as a pd.DataFrame with one column
    or a pd.Series

    :param model: your trained model
    :param X_test: a processed test set (on KATE it will be X_eval)
    :return: y_pred, your predictions
    """
    raise NotImplementedError
