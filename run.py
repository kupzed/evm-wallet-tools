#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import generate
import check

def show_menu():
    print("==========================================")
    print("           EVM WALLET TOOLS               ")
    print("==========================================")
    print("1. Generate Wallet (Buat Wallet Baru)")
    print("2. Check Wallet    (Cek Saldo Wallet)")
    print("3. Exit            (Keluar)")
    print("==========================================")

def main():
    while True:
        show_menu()
        choice = input("Pilih menu (1/2/3): ").strip()
        print()
        if choice == "1":
            generate.main()
            print()
        elif choice == "2":
            check.main()
            print()
        elif choice == "3":
            print("Terima kasih! Sampai jumpa.")
            sys.exit(0)
        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh pengguna.")
        sys.exit(0)
