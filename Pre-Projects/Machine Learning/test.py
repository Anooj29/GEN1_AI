import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load Dataset (Replace 'your_file.csv' with actual filename)
df = pd.read_csv(r"C:\GEN1_AI\Dataset\Machine_Learning\Weather\CO2 emission by countries.csv", encoding= 'unicode_escape')

# Display first few rows
print(df.head())

# Select Features and Target Variable
features = ["Country", "Population", "GDP", "EnergyConsumption"]  # Modify based on your dataset
target = "CO2_Emissions"

# Handling Missing Values
df = df.dropna()

# One-Hot Encoding for Categorical Data (Country)
encoder = OneHotEncoder(handle_unknown="ignore")
encoded_countries = encoder.fit_transform(df[["Country"]])
country_labels = encoder.get_feature_names_out(["Country"])

# Convert to DataFrame
# df_encoded = pd.DataFrame(encoded_countries, columns=country_labels)

# Concatenate with original dataset
df = pd.concat([df.drop(columns=["Country"]), df_encoded], axis=1)

# Standardizing Numeric Features (Optional)
scaler = StandardScaler()
df[["Population", "GDP", "EnergyConsumption"]] = scaler.fit_transform(df[["Population", "GDP", "EnergyConsumption"]])

# Splitting into Train & Test Sets
X = df.drop(columns=[target])
y = df[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate the Model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"R² Score: {r2}")

# Predict on New Data (Example)
new_data = pd.DataFrame([[1000000, 50000, 1000]], columns=["Population", "GDP", "EnergyConsumption"])  # Example
new_data_encoded = encoder.transform([["United States"]])  # Encode country
new_data_encoded = pd.DataFrame(new_data_encoded, columns=country_labels)

# Concatenate new data with encoded country
new_data = pd.concat([new_data, new_data_encoded], axis=1)
new_data[["Population", "GDP", "EnergyConsumption"]] = scaler.transform(new_data[["Population", "GDP", "EnergyConsumption"]])

# Make Prediction
predicted_emission = model.predict(new_data)
print(f"Predicted CO2 Emission: {predicted_emission[0]}")
