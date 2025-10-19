from model import extract_features

def get_recommendation(password, strength):
    if strength == "Strong":
        return "Wih keren! Password kamu sudah sangat kuat. Pertahankan ya!"
        
    if strength == "Medium":
        return "Sudah cukup baik! Untuk membuatnya 'Strong', kamu bisa menambah variasi simbol atau memperpanjang password."

    if strength == "Weak":
        features = extract_features(password)
        recommendations = []

        if features[0] < 8:
            recommendations.append("• Perpanjang password (minimal 8 karakter)")
        if features[2] == 0: # tidak ada huruf besar
            recommendations.append("• Tambahkan setidaknya 1 huruf besar (A-Z)")
        if features[4] == 0: # tidak ada angka
            recommendations.append("• Tambahkan setidaknya 1 angka (0-9)")
        if features[5] == 0: # tidak ada simbol
            recommendations.append("• Tambahkan setidaknya 1 simbol (contoh: !@#$%)")
        
        if not recommendations:
             return "Password ini terlalu umum dan mudah ditebak. Coba ganti dengan kombinasi kata yang tidak berhubungan."
        
        return "Password kamu masih lemah. Coba tips berikut:\n" + "\n".join(recommendations)
        
    return "Tidak dapat memberikan rekomendasi."