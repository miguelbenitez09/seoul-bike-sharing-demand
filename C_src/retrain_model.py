"""
Script para reentrenar el modelo de predicción de demanda de bicicletas
"""
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

def retrain_model(data_path, model_output_path):
    """
    Reentrena el modelo con nuevos datos
    
    Args:
        data_path: Ruta al archivo de datos procesados
        model_output_path: Ruta donde guardar el modelo entrenado
    """
    # Cargar datos
    data = pd.read_csv(data_path)
    
    # Separar features y target
    X = data.drop('Rented_Bike_Count', axis=1)
    y = data['Rented_Bike_Count']
    
    # División de datos
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Escalar datos
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Entrenar modelo
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    # Guardar modelo y scaler
    with open(f'{model_output_path}/best_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    
    with open(f'{model_output_path}/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    
    print(f"Modelo reentrenado y guardado en {model_output_path}")
    print(f"R² Score en test: {model.score(X_test_scaled, y_test):.4f}")

if __name__ == "__main__":
    retrain_model(
        data_path="../A_data/02_processed/processed_bike_data.csv",
        model_output_path="../D_models"
    )
