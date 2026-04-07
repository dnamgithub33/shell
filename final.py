from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

key = b'r68c74VWu3Qk3wwHUpyhaI4j1XUNXeby'
iv = bytes.fromhex('f3fdba281a888081b4f7edce94762b45')

# Cấu hình tên file đầu vào và đầu ra
input_filename = 'decoded_result.dat'
output_filename = 'final_payload_stage2.js'

try:
    # Đọc chuỗi Hex từ file text
    if not os.path.exists(input_filename):
        raise FileNotFoundError(f"File '{input_filename}' not found.")
        
    with open(input_filename, 'r', encoding='utf-8') as f:
        # .strip() giúp loại bỏ khoảng trắng và dấu xuống dòng thừa ở đầu/cuối file
        ciphertext_hex = f.read().strip()
        
    # Chuyển đổi Hex sang mảng byte
    ciphertext = bytes.fromhex(ciphertext_hex)

    # Tiến hành giải mã
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(ciphertext)
    
    decrypted_data = unpad(decrypted_padded, AES.block_size)
    decrypted_text = decrypted_data.decode('utf-8')

    # Lưu kết quả ra file
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(decrypted_text)
        
    print(f"[+] Decryption successful! Extracted {len(decrypted_text)} characters.")
    print(f"[+] Result saved to: {output_filename}")

except FileNotFoundError as e:
    print(f"[-] {e}")
except ValueError as e:
    print(f"[-] Data format/Decryption error. Check your Hex string, Key, or IV. Details: {e}")
except Exception as e:
    print(f"[-] An unexpected error occurred: {e}")