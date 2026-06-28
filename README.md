# 🧰 EVM Wallet Tools (`evm-wallet-tools`)

Perangkat Python serbaguna untuk membuat (*generate*) wallet Ethereum secara massal serta memeriksa saldo ETH Mainnet secara otomatis, atau memeriksa saldo dari daftar **Private Key** / **Seed Phrase** milik Anda sendiri secara aman dan lokal.

---

## 📂 Struktur Proyek

```text
evm-wallet-tools/
├── run.py              # Main entry point (Menu Interaktif Utama)
├── generate.py         # Skrip pembuatan wallet acak (12/24 kata) & cek saldo
├── check.py            # Skrip pemeriksaan saldo custom PK / Seed Phrase
├── check.txt           # File sampel tempat menaruh daftar PK / Seed Phrase
├── requirements.txt    # Daftar dependensi Python
└── .gitignore          # Konfigurasi proteksi file sensitif agar tidak ter-push
```

---

## 📌 Fitur Utama

1. **Menu Utama Interaktif (`run.py`)**
   - Menjalankan seluruh alat dari satu pintu utama tanpa perlu mengeksekusi skrip terpisah secara manual.

2. **Random Wallet Generator (`generate.py`)**
   - Pilihan panjang Mnemonic Phrase: **12 kata** (standard) atau **24 kata** (extra secure).
   - Membuat wallet EVM unik secara otomatis.
   - Pengecekan saldo real-time via Web3 RPC.
   - Menyimpan daftar wallet ke `phrase.txt`, `privatekey.txt`, `address.txt`, dan memisahkan wallet bersaldo ke `balance.txt`.

3. **Custom Wallet Checker (`check.py`)**
   - Memeriksa saldo dari daftar Private Key atau Seed Phrase milik Anda sendiri.
   - Secara default membaca file `check.txt`.
   - Deteksi otomatis format input (Private Key hex 64 karakter atau Seed Phrase 12/24 kata).
   - Memisahkan hasil wallet yang berisi saldo ke `result_my_balances.txt`.

4. **Keamanan & Privasi Maksimal**
   - **100% Lokal:** Proses pembuatan dan kalkulasi kunci dilakukan sepenuhnya di dalam RAM komputer Anda.
   - **Privacy First:** Hanya alamat publik (`0x...`) yang dikirimkan ke jaringan RPC untuk cek saldo. Kunci privat Anda **tidak pernah** meninggalkan komputer.

---

## 🛠️ Prasyarat & Instalasi

Pastikan komputer Anda sudah terpasang **Python 3.8+** dan `pip`.

1. **Clone repository ini:**
   ```bash
   git clone <URL_REPOSITORY_ANDA>
   cd evm-wallet-tools
   ```

2. **Install dependensi yang dibutuhkan:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Cara Penggunaan

### 1. Menjalankan via Menu Utama (Direkomendasikan)

Eksekusi file entry point utama:

```bash
python3 run.py
```

Anda akan disajikan menu interaktif:
```text
==========================================
           EVM WALLET TOOLS               
==========================================
1. Generate Wallet (Buat Wallet Baru)
2. Check Wallet    (Cek Saldo Wallet)
3. Exit            (Keluar)
==========================================
Pilih menu (1/2/3): 
```

---

### 2. Penjelasan Mode Operasi

#### 🔹 Pilihan 1: Generate Wallet (`generate.py`)
- Masukkan jumlah wallet yang ingin dibuat (misal: `10`).
- Pilih panjang kata Mnemonic:
  - **1** untuk 12 Kata (128-bit)
  - **2** untuk 24 Kata (256-bit)
- Hasil wallet akan disimpan secara otomatis ke file `phrase.txt`, `privatekey.txt`, dan `address.txt`. Wallet yang memiliki saldo ETH > 0 akan disimpan ke `balance.txt`.

#### 🔹 Pilihan 2: Check Wallet (`check.py`)
- Buka file `check.txt` dan masukkan daftar Private Key atau Seed Phrase Anda (1 baris per wallet).
- Jalankan menu pilihan 2. Skrip akan membaca `check.txt` secara default (atau Anda bisa menentukan nama file lain).
- Wallet yang memiliki saldo ETH > 0 akan otomatis disimpan di `result_my_balances.txt`.

---

## ⚙️ Kustomisasi RPC Provider

Secara default, skrip menggunakan RPC publik Ethereum Mainnet. Jika Anda memiliki RPC Node pribadi (misalnya dari Infura, Alchemy, atau QuickNode) untuk koneksi lebih cepat dan stabil, atur melalui *environment variable*:

```bash
export RPC_URL="https://mainnet.infura.io/v3/YOUR_API_KEY"
python3 run.py
```

---

## 🔒 Catatan Keamanan (Security Disclaimer)

- **Proteksi Git:** Jangan pernah menghapus `*.txt` dari file `.gitignore`. Kunci privat Anda tidak akan pernah ter-push ke GitHub selama file `.gitignore` tetap aktif.
- **Penyimpanan Kunci:** Simpan Private Key dan Seed Phrase Anda di tempat yang aman dan privat.
