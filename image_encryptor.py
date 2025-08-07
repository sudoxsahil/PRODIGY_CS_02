import cv2
import numpy as np
import random
import os

def encrypt_image(image_path, key, seed, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print("[-] Error: Image not found!")
        return

    rows, cols, _ = img.shape
    random.seed(seed)

    # XOR encryption
    encrypted = np.copy(img)
    encrypted = encrypted ^ key

    # Pixel shuffling using a random permutation
    flat = encrypted.reshape(-1, 3)
    indices = list(range(len(flat)))
    random.shuffle(indices)
    shuffled = flat[indices]

    shuffled_img = shuffled.reshape(rows, cols, 3)
    cv2.imwrite(output_path, shuffled_img)
    print(f"[+] Encrypted image saved as {os.path.abspath(output_path)}")

def decrypt_image(image_path, key, seed, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print("[-] Error: Image not found!")
        return

    rows, cols, _ = img.shape
    random.seed(seed)

    # Generate the same shuffle
    flat = img.reshape(-1, 3)
    indices = list(range(len(flat)))
    random.shuffle(indices)

    # Reverse the shuffle
    reverse_indices = [0] * len(indices)
    for i, idx in enumerate(indices):
        reverse_indices[idx] = i
    unshuffled = flat[reverse_indices]

    # XOR decryption
    decrypted = np.array(unshuffled).reshape(rows, cols, 3)
    decrypted = decrypted ^ key

    cv2.imwrite(output_path, decrypted)
    print(f"[+] Decrypted image saved as {os.path.abspath(output_path)}")

if __name__ == "__main__":
    print("=== Image Encryption & Decryption Tool ===")
    choice = input("Enter 'e' to encrypt OR 'd' to decrypt: ").lower()

    input_path = input("Input image path: ")
    output_path = input("Output image path (e.g. enc.png or dec.png): ")
    key = int(input("Enter numeric key (1–255): "))
    seed = int(input("Enter swapping seed (e.g. 50): "))

    if choice == 'e':
        encrypt_image(input_path, key, seed, output_path)
    elif choice == 'd':
        decrypt_image(input_path, key, seed, output_path)
    else:
        print("[-] Invalid choice!")
