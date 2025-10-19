import re
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# ekstrak fitur dasar password
def extract_features(password):
    return [
        len(password),                                      # panjang password
        len(set(password)),                                 # variasi karakter unik
        int(bool(re.search(r'[A-Z]', password))),           # ada huruf besar?
        int(bool(re.search(r'[a-z]', password))),           # ada huruf kecil?
        int(bool(re.search(r'[0-9]', password))),           # ada angka?
        int(bool(re.search(r'[^A-Za-z0-9]', password)))     # ada simbol?
    ]

# membaca dataset
try:
    df = pd.read_csv('data.csv', on_bad_lines='skip') 
except Exception as e:
    print(f"Error membaca data.csv: {e}")
    # handling jika data tidak terbaca
    df = pd.DataFrame({
        'password': ['password', '123456', 'P@ssword1', 'Qwerty2024!', 'abcdEF12#', 'admin123', 'Super$trong2025', 'thisispassword123'],
        'strength': [0, 0, 1, 2, 2, 1, 2, 1]
    })

# mengahpus baris dengan password yang kosong (jika ada)
df.dropna(subset=['password'], inplace=True)

X = [extract_features(p) for p in df['password']]
y = df['strength'].values

# train model
model = LogisticRegression(max_iter=1000).fit(X, y)

# prediksi strength password
def predict_strength(password):
    if not isinstance(password, str):
        return "Invalid"
    
    level = model.predict([extract_features(password)])[0]
    if level == 0:
        return "Weak"
    elif level == 1:
        return "Medium"
    else:
        return "Strong"
