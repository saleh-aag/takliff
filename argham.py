import time
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Load the MNIST dataset
X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False)
X = X / 255.0  # Normalize pixel values between 0 and 1

# Split data into training and test sets
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]

# List of hyperparameters to evaluate
hidden_layers = [(64,), (128,), (256,)]  # Hidden layer sizes
activations = ['logistic', 'tanh', 'relu']  # Activation functions
learning_rates = [0.001, 0.01, 0.1]  # Learning rates

print("Starting hyperparameter evaluation...")
results = []

for layer in hidden_layers:
    for act in activations:
        for lr in learning_rates:
            # Build the model with current hyperparameters
            model = MLPClassifier(
                hidden_layer_sizes=layer,
                activation=act,
                learning_rate_init=lr,
                max_iter=50,
                random_state=42
            )
            
            # Train the model and measure time
            start_time = time.time()
            model.fit(X_train, y_train)
            train_time = time.time() - start_time
            
            # Evaluate the model
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            
            # Save results
            results.append({
                'Hidden Layers': layer,
                'Activation Function': act,
                'Learning Rate': lr,
                'Accuracy': accuracy,
                'Training Time (seconds)': train_time
            })
            
            print(f"Configuration: layers={layer}, activation={act}, learning rate={lr} | Accuracy: {accuracy:.4f} | Time: {train_time:.2f} seconds")

# Display final evaluation results
print("\nFinal Evaluation Results:")
print("-------------------------------------------------------------")
print("Hidden Layers | Activation | Learning Rate | Accuracy  | Training Time")
print("-------------------------------------------------------------")
for res in results:
    print(f"{str(res['Hidden Layers']):<13} | {res['Activation Function']:<12} | {res['Learning Rate']:<13} | {res['Accuracy']:.4f} | {res['Training Time (seconds)']:.2f} seconds")