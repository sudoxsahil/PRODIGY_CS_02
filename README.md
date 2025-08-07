# PRODIGY_CS_02
# 🔐 Task 02: Image Encryption using Pixel Manipulation

This is Task-02 of my Cybersecurity Internship at **Prodigy InfoTech**.  
The project demonstrates **image encryption and decryption** using pixel-level operations in Python.

## 📌 Objective
To build a simple tool that:
- Encrypts an image by applying mathematical operations and pixel swapping.
- Decrypts the image back using the same key and seed.

## ⚙️ Features
- Encrypts any `.jpg`, `.png` image using a numeric key and swapping seed.
- Decrypts accurately if the same key and seed are used.
- Easy-to-use terminal interface.

## 🖥️ Technologies Used
- Python
- OpenCV (`cv2`)
- NumPy

## 🚀 How to Run

```bash
python3 image_encryptor.py

🖼 Sample Output
🔐 Encryption:
=== Image Encryption & Decryption Tool ===
Enter 'e' to encrypt OR 'd' to decrypt: e
Input image path: /home/kali/Desktop/photo.jpg
Output image path: enc.png
Enter numeric key (1–255): 91
Enter swapping seed (e.g. 50): 999
[+] Encrypted image saved as enc.png

🔓 Decryption:
=== Image Encryption & Decryption Tool ===
Enter 'e' to encrypt OR 'd' to decrypt: d
Input image path: enc.png
Output image path: dec.png
Enter numeric key (1–255): 91
Enter swapping seed (e.g. 50): 999
[+] Decrypted image saved as dec.png


