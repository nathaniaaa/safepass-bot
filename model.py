import re
import numpy as np
from sklearn.linear_model import LogisticRegression

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

# contoh untuk training model
X = [extract_features(p) for p in [
    'password', '123456', 'P@ssword1', 'Qwerty2024!', 'abcdEF12#', 'admin123', 'Super$trong2025', 'thisispassword123'
]]
y = [0, 0, 1, 2, 2, 1, 2, 1]  # note: 0=lemah, 1=sedang, 2=kuat

# train model
model = LogisticRegression().fit(X, y)

# prediksi strength password
def predict_strength(password):
    level = model.predict([extract_features(password)])[0]
    if level == 0:
        return "Weak"
    elif level == 1:
        return "Medium"
    else:
        return "Strong"
