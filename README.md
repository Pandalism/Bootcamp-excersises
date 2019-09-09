# Prediction of Daily Energy Consumption in London

The data provided is a time series from smart-meters in London from end of 2011 to 2014. It contains the daily consumption (kWh) averaged over several households in London. 

The last timestamp for which consumpton is available is January 31st 2014. 

You need to build a forecasting model that can predict the consumption for February 2014 (exluding 28th, so from the 1st to the 27th).


## Get the data

You can download the dataset from [here](https://kate-datasets.s3-eu-west-1.amazonaws.com/london_smartmeter_basic/data.zip).

The data is given as a zipped csv to save space. *NO NEED TO UNZIP IT*, Pandas is able to work directly with zipped csv.

In a notebook, run:

```
import pandas as pd

df = pd.read_csv("data.zip")
```

to load the dataset.


## Get Started

You will need to implement three functions:

* `preprocess`

This takes a dataframe and should return two dataframes: `ts` (your training data) as well as `ts_eval`.

`ts_eval` is the evaluation time series, it contains the list of days you will need to predict consumption for so KATE can evaluate the performance of your model. 

In the dataframe provided, there is a column `evaluation_set` that tells you whether this row is for evaluation or not.

To get all the rows that need to be used for evaluation only, you can use:

```
df.loc[df.evaluation_set]
```

* `train`

This takes the `ts` you have processed previously and trains your model. It should return your trained model.


* `predict`

This takes the model you have trained as well as a test time serie (on KATE this will be the `ts_eval` that you processed above, but you can test this function locally with your own time serie). 

This should return y_pred, predictions on the test set.


The recommended way of working on this project is to:
1) Download the data
2) Open it in a notebook and start prototyping
3) Break down your code into functions preprocess/train/predict and test it locally
4) When you're happy with your functions, copy/paste them in the WebIDE (in the file `model.py`)

*NOTE*: Since with this project your model will be trained directly on KATE, it is limited to models that can be trained under 1min. You will receive a `TimeoutError` if your model takes too long.

You can test that your functions work in a notebook with the following example:

```
import pandas as pd

df = pd.read_csv("data.zip")
ts, ts_eval = preprocess(df)
model = train(ts)
y_pred = predict(model, ts_eval)
print(y_pred)
```

## Baseline Model

Here is an example of a submission using an AR model.


```
import pandas as pd
from statsmodels.api import tsa


def preprocess(df):

    # Set day as index
    df.set_index(pd.to_datetime(df.day), inplace=True)
    df.drop("day", axis=1, inplace=True)

    # Save msk to split data later
    msk_eval = df.evaluation_set
    df.drop("evaluation_set", axis=1, inplace=True)

    # Split training/test data
    ts = df[~msk_eval]
    ts_eval = df[msk_eval]

    return ts, ts_eval


def train(ts):
    # Train an AR model
    model = tsa.AR(ts).fit()

    return model


def predict(model, ts_test):
    # Find starting and end date
    start = ts_test.index[0]
    end = ts_test.index[-1]

    # Generate predictions
    preds = model.predict(start=start, end=end)

    return preds
```

Good luck!