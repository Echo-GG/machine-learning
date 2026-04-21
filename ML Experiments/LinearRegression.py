# Linear Regression implementation using Gradient Descent
import numpy as np

class LinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.lr = learning_rate
        self.n_iters = n_iterations
        self.weights = None
        self.bias = None
        self.loss_history = []

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y).ravel()  # ensure y is a 1D vector to avoid shape and broadcasting issues

        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0.0
        self.loss_history = []

        for _ in range(self.n_iters):
            y_pred = X.dot(self.weights) + self.bias
            loss = (1 / (2 * n_samples)) * np.sum((y_pred - y) ** 2)
            self.loss_history.append(loss)

            dw = (1 / n_samples) * X.T.dot(y_pred - y)
            db = (1 / n_samples) * np.sum(y_pred - y)

            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        X = np.array(X)
        if X.ndim == 1:
            X = X.reshape(-1, 1)
        return X.dot(self.weights) + self.bias


# Samples:
if __name__ == "__main__":
    np.random.seed(42)
    X = 2 * np.random.rand(100, 1)
    y = (4 + 3 * X + np.random.randn(100, 1)).ravel()  # generate 1D variable y

    model = LinearRegression(learning_rate=0.1, n_iterations=100)
    model.fit(X, y)

    print(f"Weights: {model.weights}, Bias: {model.bias}")
    print(f"Final loss: {model.loss_history[-1]}")
