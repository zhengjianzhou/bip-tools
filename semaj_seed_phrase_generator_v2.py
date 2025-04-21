#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib, mnemonic, sys, base58

def int2bin     (i,     n) : return bin(i         )[2:].zfill(n)
def hex2bin     (h,     n) : return bin(int(h, 16))[2:].zfill(n)
def hex2byte    (h       ) : return bytes.fromhex(h)
def to2048      (n       ) : return ([] if n == 0 else to2048(n // 2048) + [n % 2048]) if n else []
def from2048    (s       ) : return sum(c * (2048 ** i) for i, c in enumerate(reversed(s)))
def wd2effwd    (s,   wdl) : return ([          i  for i in s if i in wdl] * 24) [:24]
def wd2idxs     (s,   wdl) : return ([wdl.index(i) for i in s if i in wdl] * 24) [:24]
def h256i       (s       ) : return int(hashlib.sha256(s.encode('utf8')).hexdigest(), 16)
def idx2eng     (idx, wdl) : return ' '.join(wdl[i] for i in idx)
def bits2idxs   (bits    ) : return [int(bits[i:i+11], 2) for i in range(0, len(bits), 11)]
def checksum    (i,     n) : return hex2bin(hashlib.sha256((i%2**n).to_bytes(n//8)).hexdigest(), n)[:n//32]
def ient2idxs    (i,     n) : return bits2idxs(int2bin(i%2**n,n)+checksum(i%2**n,n))
def int2seed    (i,     n) : return idx2eng(ient2idxs(i%2**n,n), mnemonic.Mnemonic('english').wordlist)
def int2b58     (i       ) : return base58.b58encode_int(i).decode('utf-8')
def strhash2b58 (s       ) : return int2b58(h256i(s))
def splitstr    (s,     n) : return [s[i*n:(i+1)*n]  for i in range(len(s)//n + 1)]

def genseed(words, s='', n=256, lang='chinese_simplified', use23wordsonly=False):
    mw = mnemonic.Mnemonic(lang)
    i_words = from2048(wd2idxs(words, mw.wordlist))
    i_hash  = (h256i(s) if s else 0)
    if use23wordsonly:
        i_words = i_words >> 11 << 3  # ">>11" remove last word - only use 23, "<<3" to fill the missing 3bits
        i_hash  = i_hash     << 3  #                                        "<<3" to fill the missing 3bits
    return int2seed(i_words + i_hash, n)

def main_cli():
    args = (sys.argv[1:] + ['', '', '', ''])[:4]
    words, passcode, nbit, lang = args[:4]
    nbit = int(nbit) if nbit else 256
    lang = lang if lang else 'chinese_simplified'
    words = words if lang.startswith('chinese') else words.split(' ')
    words_eff = wd2effwd(words, mnemonic.Mnemonic(lang).wordlist)
    print( "---> INPUT:", words_eff, passcode, nbit, lang)
    print( "OLD Version->", genseed(words, passcode, nbit, lang, True ) )
    print( "NEW SEED   ->", genseed(words, passcode, nbit, lang, False) )
    pass_hash_b58 = strhash2b58(passcode) if passcode else ''
    print(f"Suggested Passphrase: Passcode.SHA256.Base58: {pass_hash_b58} => {' '.join(splitstr(pass_hash_b58, 4))}")

### tkinter ui main function
def main_ui():
    import tkinter as tk
    def generate_output():
        word_input_raw = word_input_entry.get()
        passcode_str_raw = passcode_entry.get()
        seed_length = seed_length_entry.get().split(' ')[0]
        lang = lang_select_entry.get().lower()

        words = word_input_raw.strip()
        words = words if lang.startswith('chinese') else words.split(' ')
        words_eff = wd2effwd(words, mnemonic.Mnemonic(lang).wordlist)
        passcode = passcode_str_raw.strip()
        nbit = {12:128, 23:256, 24:256}[int(seed_length)]

        if int(seed_length) == 23:
            seed_phrases = genseed(words, passcode, int(nbit) if nbit else 256, lang, True)
        else:
            seed_phrases = genseed(words, passcode, int(nbit) if nbit else 256, lang, False)

        pass_hash_b58 = strhash2b58(passcode) if passcode else ''
        pass_hash_b58_sp = ' '.join(splitstr(pass_hash_b58, 6))
        indexed_seed_phrases = dict([(i+1, s) for i, s in enumerate(seed_phrases.split(' '))])
    
        output1.config(state="normal")
        output2.config(state="normal")
        output3.config(state="normal")
        output4.config(state="normal")

        output1.delete(1.0, tk.END)
        output2.delete(1.0, tk.END)
        output3.delete(1.0, tk.END)
        output4.delete(1.0, tk.END)
    
        output1.insert(tk.END, f"{''.join(words_eff)}")
        output2.insert(tk.END, f"{seed_phrases}")
        output3.insert(tk.END, f"{indexed_seed_phrases}")
        output4.insert(tk.END, f"{pass_hash_b58_sp}")

        output1.config(state="disabled")
        output2.config(state="disabled")
        output3.config(state="disabled")
        output4.config(state="disabled")
    
    root = tk.Tk()
    root.title("Semaj's SeedPhrase Generator")
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=2)
    root.grid_rowconfigure(3, weight=2)
    root.grid_columnconfigure(0, weight=1)
    
    seed_length_entry = tk.StringVar(root)
    seed_length_entry.set("24 Words")
    dropdown = tk.OptionMenu(root, seed_length_entry, "12 Words", "23 Words (24 - but last word ignored)", "24 Words")
    dropdown.config(font=("Arial", 14))
    dropdown.grid(row=0, column=0, sticky="w", padx=10, pady=5)

    lang_select_entry = tk.StringVar(root)
    lang_select_entry.set("CHINESE_SIMPLIFIED")
    dropdown_lang = tk.OptionMenu(root, lang_select_entry, 'CHINESE_SIMPLIFIED', 'CHINESE_TRADITIONAL', 'CZECH', 'JAPANESE', 'FRENCH', 'ENGLISH', 'SPANISH', 'ITALIAN', 'PORTUGUESE', 'KOREAN')
    dropdown_lang.config(font=("Arial", 14))
    dropdown_lang.grid(row=1, column=0, sticky="w", padx=10, pady=5)

    label1 = tk.Label(root, text="Please input your Source Phrases here", font=("Arial", 12), anchor='w')
    word_input_entry = tk.Entry(root, font=("Arial", 14))
    label2 = tk.Label(root, text="Please input your passcode here, it can be empty or any ascii code except space", font=("Arial", 12), anchor='w')
    passcode_entry = tk.Entry(root, font=("Arial", 14))
    
    label1.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
    word_input_entry.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
    label2.grid(row=4, column=0, sticky="ew", padx=10, pady=5)
    passcode_entry.grid(row=5, column=0, sticky="ew", padx=10, pady=5)
    
    generate_button = tk.Button(root, text="Generate Seed Phrase", font=("Arial", 16), command=generate_output)
    generate_button.grid(row=6, column=0, sticky="ew", padx=10, pady=10)
    
    output1 = tk.Text(root, height=1, wrap="word", font=("Arial", 12))
    output2 = tk.Text(root, height=3, wrap="word", font=("Arial", 12))
    output3 = tk.Text(root, height=4, wrap="word", font=("Arial", 12))
    output4 = tk.Text(root, height=1, wrap="word", font=("Arial", 12))
    
    label3 = tk.Label(root, text="Your input:", font=("Arial", 12), anchor='w')
    label4 = tk.Label(root, text="Your Seed Phrase - Please keep them secure!!!", font=("Arial", 12), anchor='w')
    label5 = tk.Label(root, text="Your Optional Pass Phrase - You may choose ANY of them!!!", font=("Arial", 12), anchor='w')

    label3.grid(row=7, column=0, sticky="ew", padx=10, pady=5)
    output1.grid(row=8, column=0, sticky="ew", padx=10, pady=5)
    label4.grid(row=9, column=0, sticky="ew", padx=10, pady=5)
    output2.grid(row=10, column=0, sticky="ew", padx=10, pady=5)
    output3.grid(row=11, column=0, sticky="ew", padx=10, pady=5)
    label5.grid(row=12, column=0, sticky="ew", padx=10, pady=5)
    output4.grid(row=13, column=0, sticky="ew", padx=10, pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv[1:]) > 1:
        main_cli()
    else:
        main_ui()

