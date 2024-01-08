"""module for generating mmh3 and md5 hashes for favicon search"""

#!/usr/bin/env python3

import hashlib
import codecs
import mmh3


def compute_mmh3_hash(file_name):
    try:
        with open(file_name, 'rb') as file:
            data = file.read()
            # Encode the data to base64
            encoded_data = codecs.encode(data, "base64")
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
