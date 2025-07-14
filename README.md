# stegcloak


# 🕵️‍♂️ StegCloak.py — Image Steganography Tool in Python

**StegCloak.py** is a command-line based image steganography tool that allows you to **hide (encode)** and **extract (decode)** secret messages inside `.png` and `.bmp` image files using **Least Significant Bit (LSB)** technique.

> 🔐 Use this tool to securely embed sensitive information inside images for red teaming, ethical hacking, and secure communication.

---

## 📦 Features

- 🧬 **LSB Steganography** in 24-bit images
- 🔒 Optional **AES encryption** using password
- 🔓 Decode hidden data from stego images
- 💻 Built in **pure Python 3**
- ⚙️ Works offline & compatible with **Kali Linux**
- 🛠️ Clean CLI with `argparse`

---

## 🛠️ Installation

```bash
git clone https://github.com/SekharNaiyudu/stegcloak.git
cd stegcloak
pip install -r requirements.txt

If any error try This:-
python3 -m venv venv
apt install python3.11-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


-----------------------------------------------------------------------------------------------------------------------
To Encode:-
python3 stegcloak.py -m encode -i input.png -o output.png -s "Secret Message" -p "password123"

To Decode:-
python3 stegcloak.py -m decode -i output.png -p "password123"

-----------------------------------------------------------------------------------------------------------------------
Example:-
python3 stegcloak.py -m encode -i image.png -o stego.png -s "CTF{hidden_payload}" -p kali123
python3 stegcloak.py -m decode -i stego.png -p kali123

