import mmh3
import hashlib
import codecs

def compute_mmh3_hash(file_name):
    try:
        with open(file_name, 'rb') as file:
            data = file.read()
            # Encode the data to base64
            encoded_data = codecs.encode(data,"base64")
            hash_value = mmh3.hash(encoded_data)
            return hash_value
    except FileNotFoundError:
        return "File not found. Please check the file path."
    except Exception as e:
        return f"An error occurred: {e}"
        
def generate_md5_hash(file_name):
    try:
        with open(file_name, 'rb') as file:
            data = file.read()
            md5_hash = hashlib.md5(data).hexdigest()
            return md5_hash
    except FileNotFoundError:
        return "File not found. Please check the file path."
    except Exception as e:
        return f"An error occurred: {e}"

# Ask for the name of the favicon file
file_name = input("Please enter the name of the favicon file (including the extension): ")

md5_hash = generate_md5_hash(file_name)
mmh3_hash = compute_mmh3_hash(file_name)

print("[+] Results:")
print(f"[+] The mmh3 hash of the file is: {mmh3_hash}")
print(f"[+] The MD5 hash of the file is: {md5_hash}")
print(f"[+] The shodan.io search syntax is: http.favicon.hash:{mmh3_hash}")
print(f'[+] The zoomeye.org search syntax is: iconhash:"{mmh3_hash}' +'"')
print(f"[+] The search.censys.io search syntax is: {md5_hash}")
