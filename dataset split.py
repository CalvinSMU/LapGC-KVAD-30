import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Create dataset
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'S1': [47, 29, 12, 23, 31, 17, 18, 30, 17, 16, 11, 17, 26, 18, 34, 26, 38, 19, 27, 8, 24, 9, 18, 22, 22, 18, 40, 17, 19, 15],
    'S2': [20, 10, 13, 12, 30, 11, 15, 14, 15, 22, 10, 16, 16, 15, 11, 10, 16, 11, 10, 11, 10, 12, 8, 19, 16, 14, 10, 14, 13, 19],
    'S3': [50, 28, 34, 34, 50, 52, 47, 42, 37, 30, 35, 29, 36, 42, 55, 40, 40, 41, 31, 34, 44, 42, 48, 59, 77, 32, 42, 56, 24, 35],
    'S4': [19, 11, 12, 10, 10, 14, 7, 13, 8, 8, 15, 7, 12, 15, 14, 17, 11, 20, 9, 9, 11, 16, 6, 6, 16, 8, 20, 10, 7, 7],
    'S5': [17, 16, 20, 17, 28, 25, 15, 12, 11, 16, 10, 22, 15, 21, 21, 35, 10, 24, 24, 17, 18, 24, 14, 10, 28, 24, 31, 33, 41, 26],
    'S6': [42, 56, 36, 31, 48, 25, 42, 50, 38, 36, 56, 45, 38, 29, 61, 37, 35, 45, 47, 45, 53, 37, 35, 25, 47, 45, 57, 25, 31, 55],
    'S7': [22, 13, 14, 7, 8, 11, 16, 17, 12, 6, 10, 15, 7, 12, 9, 10, 7, 16, 7, 16, 9, 8, 21, 8, 12, 10, 7, 7, 27, 14],
    'S8': [20, 8, 14, 12, 15, 8, 13, 6, 17, 12, 11, 10, 12, 14, 19, 7, 16, 14, 10, 12, 8, 9, 15, 8, 21, 15, 23, 12, 9, 13]
}

df = pd.DataFrame(data)

# Simplified stratification strategy - use KMeans clustering to create 3 comprehensive strata
from sklearn.cluster import KMeans

# Cluster using all S variables
kmeans = KMeans(n_clusters=3, random_state=42)
df['stratum'] = kmeans.fit_predict(df[['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']])

# Calculate sample sizes
total_samples = len(df)
train_size = 20
val_size = 5
test_size = 5

# Initialize empty datasets
train_df = pd.DataFrame()
val_df = pd.DataFrame()
test_df = pd.DataFrame()

# Stratified sampling for each stratum
for stratum in sorted(df['stratum'].unique()):
    stratum_data = df[df['stratum'] == stratum]
    stratum_count = len(stratum_data)
    
    # Calculate theoretical counts for train, val, test sets
    train_count = max(1, round(train_size * (stratum_count / total_samples)))
    val_count = max(1, round(val_size * (stratum_count / total_samples)))
    test_count = max(1, stratum_count - train_count - val_count)
    
    # Adjust counts to ensure correct total
    while train_count + val_count + test_count > stratum_count:
        if test_count > 1:
            test_count -= 1
        elif val_count > 1:
            val_count -= 1
        else:
            train_count -= 1
    
    # Perform stratified sampling
    if stratum_count > 1:
        # First split test set
        if test_count > 0:
            temp_train_val, temp_test = train_test_split(
                stratum_data, 
                test_size=test_count, 
                random_state=42
            )
        else:
            temp_train_val = stratum_data.copy()
            temp_test = pd.DataFrame(columns=df.columns)
        
        # Then split train and validation sets
        if val_count > 0 and len(temp_train_val) > 1:
            temp_train, temp_val = train_test_split(
                temp_train_val, 
                test_size=val_count, 
                random_state=42
            )
        else:
            temp_train = temp_train_val.copy()
            temp_val = pd.DataFrame(columns=df.columns)
    else:
        # For single sample case, assign to training set
        temp_train = stratum_data.copy()
        temp_val = pd.DataFrame(columns=df.columns)
        temp_test = pd.DataFrame(columns=df.columns)
    
    # Add to corresponding datasets
    train_df = pd.concat([train_df, temp_train])
    val_df = pd.concat([val_df, temp_val])
    test_df = pd.concat([test_df, temp_test])

# Check final dataset sizes
print(f"Training set size: {len(train_df)}")
print(f"Validation set size: {len(val_df)}")
print(f"Test set size: {len(test_df)}")

# Show split results
print("\nTraining set IDs:", sorted(train_df['ID'].tolist()))
print("Validation set IDs:", sorted(val_df['ID'].tolist()))
print("Test set IDs:", sorted(test_df['ID'].tolist()))

# Distribution balance analysis
def compare_distributions(full_df, train_df, val_df, test_df):
    results = {}
    for col in ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']:
        full_mean = full_df[col].mean()
        train_mean = train_df[col].mean()
        val_mean = val_df[col].mean()
        test_mean = test_df[col].mean()
        
        results[col] = {
            'full': full_mean,
            'train': train_mean,
            'val': val_mean,
            'test': test_mean,
            'train_diff%': abs((train_mean - full_mean)/full_mean)*100,
            'val_diff%': abs((val_mean - full_mean)/full_mean)*100,
            'test_diff%': abs((test_mean - full_mean)/full_mean)*100
        }
    return results

# Perform comparison
dist_comparison = compare_distributions(df, train_df, val_df, test_df)

# Print comparison results
print("\nScene distribution balance analysis:")
print("{:<5} {:<10} {:<10} {:<10} {:<10} {:<15} {:<15} {:<15}".format(
    "Var", "Full mean", "Train mean", "Val mean", "Test mean", 
    "Train diff%", "Val diff%", "Test diff%"))

for col, stats in dist_comparison.items():
    print("{:<5} {:<10.2f} {:<10.2f} {:<10.2f} {:<10.2f} {:<15.2f} {:<15.2f} {:<15.2f}".format(
        col, 
        stats['full'], 
        stats['train'], 
        stats['val'], 
        stats['test'],
        stats['train_diff%'],
        stats['val_diff%'],
        stats['test_diff%']
    ))