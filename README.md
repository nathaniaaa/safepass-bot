# SafePassJourney Bot 🔐

Selamat datang di SafePassJourney, bot Telegram yang dirancang untuk membantumu menganalisis kekuatan *password* secara instan.
Bot ini menggunakan model *machine learning* (Logistic Regression) yang dilatih pada dataset dengan lebih dari 600.000 *password* untuk memberikan prediksi kekuatan yang akurat dan rekomendasi yang cerdas.
Dataset = https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier-dataset 

## Catatan Penting: Status Bot
Saat ini, bot **tidak di-hosting secara publik** dan tidak berjalan 24/7. Repositori ini adalah untuk portofolio dan demonstrasi kode.
Bot dapat dijalankan di komputer lokal sendiri dengan mengikuti step di bawah ini.

## Demo (Contoh Penggunaan)
Berikut adalah contoh bagaimana bot ini bekerja saat dijalankan secara lokal:

**Perintah /start**
![Screenshot_2025-10-19-18-18-45-968_org telegram messenger](https://github.com/user-attachments/assets/9a83dd22-ca52-4016-803d-778a3f73d642)

**Mengecek Password**
![Screenshot_2025-10-19-18-22-52-712_org telegram messenger](https://github.com/user-attachments/assets/973b173e-0d3b-4718-bb6e-3a5c3ea8decf)

## Perintah yang Tersedia

* **`/start`**
    Menampilkan pesan selamat datang dan instruksi dasar tentang cara menggunakan bot.

* **`/check <password>`**
    Menganalisis *password* yang diberikan. Bot akan membalas dengan level kekuatan (*Weak*, *Medium*, atau *Strong*) beserta rekomendasi spesifik.

    **Contoh Penggunaan:**
    `/check Rahasia123!`

## Cara Menjalankan di Lokal

1.  **Clone repositori:**
    ```bash
    git clone https://github.com/nathaniaaa/safepass-bot
    ```

2.  **Install semua *library* yang dibutuhkan:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Buat file `.env`:**
    * Buat file bernama `.env` di dalam folder proyek.
    * Isi file tersebut dengan token bot telegram:
        ```
        TELEGRAM_TOKEN=123456:ABCdeFGHIJKLMn...
        ```

4.  **Jalankan bot:**
    ```bash
    python telegram_bot.py
    ```
    Bot sekarang akan berjalan di terminal.
