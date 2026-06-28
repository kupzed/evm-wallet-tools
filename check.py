#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from eth_account import Account
from mnemonic import Mnemonic

# RPC ETH MAINNET (Bisa diatur melalui environment variable RPC_URL)
RPC_URL = os.getenv("RPC_URL", "https://cloudflare-eth.com")

try:
    from web3 import Web3
except Exception:
    Web3 = None

def init_web3():
    if Web3 is None:
        return None
    try:
        w3 = Web3(Web3.HTTPProvider(RPC_URL, request_kwargs={"timeout": 10}))
        return w3
    except Exception:
        return None

def get_balance_w3(w3, address):
    try:
        bal = w3.eth.get_balance(address)
        return int(bal)
    except Exception:
        return None

def format_eth_balance(wei_val):
    try:
        if wei_val is None:
            return "0.0"
        if Web3:
            eth = Web3.fromWei(wei_val, "ether")
            s = f"{eth:.18f}"
            s = s.rstrip('0').rstrip('.') if '.' in s else s
            return s
        else:
            eth = int(wei_val) / 1e18
            s = f"{eth:.18f}"
            s = s.rstrip('0').rstrip('.') if '.' in s else s
            return s
    except Exception:
        return "0.0"

def parse_line_to_account(line):
    line = line.strip()
    if not line or line.startswith("#"):
        return None, None
    
    # Cek apakah private key (hex string 64 char atau 66 char dengan 0x)
    clean_line = line[2:] if line.startswith("0x") or line.startswith("0X") else line
    if len(clean_line) == 64 and all(c in "0123456789abcdefABCDEF" for c in clean_line):
        try:
            acc = Account.from_key("0x" + clean_line)
            return acc, "Private Key"
        except Exception:
            pass
            
    # Cek apakah seed phrase (biasanya 12 atau 24 kata terpisah spasi)
    words = line.split()
    if len(words) in [12, 15, 18, 21, 24]:
        try:
            Account.enable_unaudited_hdwallet_features()
            acc = Account.from_mnemonic(line)
            return acc, "Seed Phrase"
        except Exception:
            pass

    return None, None

def main():
    print("=== Check Balance Custom Wallet (PK / Seed Phrase) ===")
    filename = input("Masukkan nama file daftar PK/Phrase (default: check.txt): ").strip()
    
    if not filename:
        filename = "check.txt"
        
    if not os.path.exists(filename):
        print(f"File '{filename}' tidak ditemukan di folder ini!")
        print("Silakan buat file tersebut dan isikan Private Key atau Seed Phrase Anda.")
        return
        
    with open(filename, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f.readlines() if l.strip() and not l.strip().startswith("#")]
        
    if not lines:
        print(f"File '{filename}' kosong atau hanya berisi komentar!")
        return
        
    print(f"Membaca {len(lines)} baris dari {filename}...\n")
    
    w3 = init_web3()
    if w3 is None:
        print("Peringatan: Tidak dapat terhubung ke RPC. Saldo mungkin tampil 0.0\n")
        
    out_filename = "result_my_balances.txt"
    funded_count = 0
    
    with open(out_filename, "a", encoding="utf-8") as f_out:
        for idx, line in enumerate(lines, 1):
            acc, input_type = parse_line_to_account(line)
            if acc is None:
                print(f"[{idx}/{len(lines)}] GAGAL PARSE: Format tidak dikenali -> {line[:15]}...")
                continue
                
            address = acc.address
            wei_bal = get_balance_w3(w3, address) if w3 else None
            bal_str = format_eth_balance(wei_bal)
            
            status = f"[{idx}/{len(lines)}] [{input_type}] {address} | Balance: {bal_str} ETH"
            
            if wei_bal and wei_bal > 0:
                funded_count += 1
                status += " <-- ADA SALDO! (Disimpan)"
                f_out.write(f"{address},{bal_str} ETH,{input_type},{line}\n")
                f_out.flush()
                
            print(status)
            
    print(f"\n==========================================")
    print(f"Selesai! {funded_count} wallet dengan saldo disimpan di '{out_filename}'.")

if __name__ == "__main__":
    main()
