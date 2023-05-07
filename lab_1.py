import numpy as np

periods = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
rate = np.array([3.89, 4.48, 5.0, 5.50, 5.81, 5.71, 5.93, 5.84, 6.15, 5.97, 6.22])
log_rate = np.log(rate)
X = np.vstack([np.ones(len(periods)), periods]).T
b = np.linalg.inv(X.T @ X) @ X.T @ log_rate
log_rate_pred = b[0] + b[1]*12
rate_pred = np.exp(log_rate_pred)

print("Прогнозоване значення на 12 період:", round(rate_pred, 2))