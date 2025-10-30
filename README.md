# Energy Consumption Prediction Project

## 📋 Project Overview
A comprehensive machine learning project for predicting energy consumption patterns using various regression models and hyperparameter optimization techniques.

## 🎯 Business Problem
Predicting energy consumption is crucial for utility companies, energy traders, and sustainability initiatives. This project aims to build accurate models to forecast energy usage based on various features like temperature, humidity, occupancy, and time-based factors.

## 📊 Dataset Features
- **Temporal Features**: month, hour, day of week
- **Environmental Factors**: temperature, humidity, season
- **Building Characteristics**: square footage, occupancy
- **Operational Data**: HVAC usage, lighting usage, renewable energy
- **Special Events**: holiday indicators

## 🛠️ Technical Implementation

### Data Preprocessing
- **Data Cleaning**: Handling missing values and outliers
- **Feature Engineering**: Created interaction terms (temperature_humidity)
- **Encoding**: One-hot encoding for categorical variables
- **Scaling**: Standardization of numerical features

### Models Implemented
1. **Linear Regression** - Baseline model
2. **Decision Tree Regression** - Non-linear relationships
3. **Random Forest Regression** - Ensemble method
4. **Regularized Models** - Ridge and Lasso regression

### Hyperparameter Optimization
- **GridSearchCV** for systematic parameter tuning
- **Cross-validation** with 5 folds
- **Metrics**: RMSE and R² score

## 📈 Results
