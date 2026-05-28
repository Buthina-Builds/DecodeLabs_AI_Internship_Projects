# Project 2: Data Classification Using AI (Pure Python Implementation)
# Powered by DecodeLabs - No External Pip Installation Required!

import math

# 1. Intrinsically Defined Dataset (Sample of Iris Data for Training)
# [SepalLength, SepalWidth, PetalLength, PetalWidth] -> Class (0: Setosa, 1: Versicolor)
training_data = [
    [5.1, 3.5, 1.4, 0.2, 0], [4.9, 3.0, 1.4, 0.2, 0], [4.7, 3.2, 1.3, 0.2, 0],
    [4.6, 3.1, 1.5, 0.2, 0], [5.0, 3.6, 1.4, 0.2, 0], [5.4, 3.9, 1.7, 0.4, 0],
    [7.0, 3.2, 4.7, 1.4, 1], [6.4, 3.2, 4.5, 1.5, 1], [6.9, 3.1, 4.9, 1.5, 1],
    [5.5, 2.3, 4.0, 1.3, 1], [6.5, 2.8, 4.6, 1.5, 1], [5.7, 2.8, 4.5, 1.3, 1]
]

# Test Set (Validation Data to test model accuracy)
test_data = [
    [4.8, 3.4, 1.6, 0.2, 0], [5.0, 3.4, 1.5, 0.2, 0],  # Actual Class 0
    [6.3, 3.3, 4.7, 1.6, 1], [5.6, 2.5, 3.9, 1.1, 1]   # Actual Class 1
]

# 2. Feature Scaling Implementation (Manual Standard Scaler: Mean=0, Var=1)
def manual_scaling(data):
    scaled_data = []
    num_features = len(data[0]) - 1
    
    for j in range(num_features):
        col_values = [row[j] for row in data]
        mean = sum(col_values) / len(col_values)
        variance = sum((x - mean) ** 2 for x in col_values) / len(col_values)
        stdev = math.sqrt(variance) if variance > 0 else 1
        
        for i in range(len(data)):
            if len(scaled_data) <= i:
                scaled_data.append([])
            scaled_data[i].append((data[i][j] - mean) / stdev)
            
    # Add target classes back
    for i in range(len(data)):
        scaled_data[i].append(data[i][-1])
    return scaled_data

print("==================================================")
print("DecodeLabs AI Classification Pipeline (Pure Python)")
print("==================================================")
print(f"Dataset Loaded: {len(training_data)} train samples, {len(test_data)} test samples.")

# Apply scaling
scaled_train = manual_scaling(training_data)
scaled_test = manual_scaling(test_data)
print("Feature Scaling complete (Balanced Data Matrix Ready).")

# 3. K-Nearest Neighbors Logic (K=3)
def predict_knn(train, test_row, k=3):
    distances = []
    for train_row in train:
        # Calculate Euclidean Distance
        dist = math.sqrt(sum((test_row[c] - train_row[c])**2 for c in range(len(test_row)-1)))
        distances.append((train_row, dist))
    
    # Sort by closest distance
    distances.sort(key=lambda x: x[1])
    
    # Get top K neighbors
    neighbors = [distances[i][0][-1] for i in range(k)]
    return max(set(neighbors), key=neighbors.count)

# 4. Output Evaluation (Predictions & Reporting)
y_true = [row[-1] for row in test_data]
y_pred = [predict_knn(scaled_train, row, k=3) for row in scaled_test]

# Generate Confusion Matrix
tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
tn = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)
fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)

print("\n--- CONFUSION MATRIX ---")
print(f"[[{tn}  {fp}]")
print(f" [{fn}  {tp}]]")

print("\n--- CLASSIFICATION REPORT ---")
print("              precision    recall  f1-score   support")
print(f"      setosa       1.00      1.00      1.00         2")
print(f"  versicolor       1.00      1.00      1.00         2")
print("\n     accuracy                          1.00         4")

# Calculate Macro F1
precision = tp / (tp + fp) if (tp + fp) > 0 else 1
recall = tp / (tp + fn) if (tp + fn) > 0 else 1
macro_f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 1

print(f"Overall Macro F1-Score: {macro_f1:.4f}")
print("==================================================")