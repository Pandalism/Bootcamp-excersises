# Prediction of Daily Energy Consumption in London

The data provided is a time series from smart-meters in London from end of 2011 to 2014. It contains the daily consumption (kWh) averaged over several households in London. 

The last timestamp available in the training data is March 31st 2014. You need to build a forecasting model that can predict consumption for February 2014 (exluding 28th, so from the 1st to the 27th).

The DataFrame used for testing is in the same format as the training data but only contains the column `day` (no `consumption`).