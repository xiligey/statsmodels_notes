from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(list(range(100)), order=(1, 0, 0)).fit()
print(model.summary())

model.forecast(10)