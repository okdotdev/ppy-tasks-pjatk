import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.impute import SimpleImputer


def main():
    data = pd.read_csv('pogoda.csv')
    print(data)

    print("Rozmiar danych przed operacją:", data.shape)

    data.dropna(subset=['MinTemp', 'MaxTemp', 'RainTomorrow'], inplace=True)
    print("Rozmiar danych po operacji:", data.shape)

    print("Pierwsze 30 wierszy wyczyszczonych danych:")
    print(data.head(30))

    label_columns = ['RainToday', 'RainTomorrow', 'WindGustDir', 'WindDir9am', 'WindDir3pm', 'Location']
    label_encoder = LabelEncoder()

    for col in label_columns:
        if data[col].dtype == 'object':
            data[col] = label_encoder.fit_transform(data[col])
            print(f"Wartości tekstowe w kolumnie '{col}' zostały przekształcone na wartości numeryczne.")

    print("Pierwsze 30 wierszy danych po kodowaniu:")
    print(data.head(30))

    # Imputacja brakujących wartości średnią wartością każdej kolumny
    imputer = SimpleImputer(strategy='mean')
    data_imputed = pd.DataFrame(imputer.fit_transform(data.drop(columns=['Date'])), columns=data.columns.drop('Date'))
    data_imputed['Date'] = data['Date']

    X = data_imputed.drop(columns=['RainTomorrow', 'Date'])
    y = data_imputed['RainTomorrow']

    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
    X_validate, X_test, y_validate, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)
    print("Dane podzielone na zbiory treningowy, walidacyjny i testowy.")

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_validate_scaled = scaler.transform(X_validate)
    X_test_scaled = scaler.transform(X_test)
    print("Skalowanie danych zakończone.")

    print("Rozmiar zbioru treningowego:", X_train_scaled.shape)
    print("Rozmiar zbioru walidacyjnego:", X_validate_scaled.shape)
    print("Rozmiar zbioru testowego:", X_test_scaled.shape)

    # Trenowanie klasyfikatora KNN
    knn = KNeighborsClassifier(n_neighbors=5)  # Można dostosować liczbę sąsiadów
    knn.fit(X_train_scaled, y_train)
    print("Klasyfikator KNN wytrenowany.")

    # Dokonywanie predykcji na zbiorze testowym
    y_pred = knn.predict(X_test_scaled)

    # Ewaluacja modelu
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Dokładność na zbiorze testowym: {accuracy:.2f}")

    # Szczegółowy raport klasyfikacji
    print("Raport klasyfikacji:")
    print(classification_report(y_test, y_pred))

    # Macierz pomyłek
    print("Macierz pomyłek:")
    print(confusion_matrix(y_test, y_pred))


if __name__ == '__main__':
    main()
