"""module for parsing user input and visualizing results output"""

#!/usr/bin/env python3

import argparse
from .generate_hashes import generate_md5_hash, compute_mmh3_hash


class Color:
    RED = '\033[91m'
    WHITE = '\033[97m'
    GREEN = '\033[92m'
    ORANGE = '\033[33m'
    END = '\x1b[0m'


def favicon_locator():
    parser = argparse.ArgumentParser(
        description='Generate favicon hash for search.')
    parser.add_argument('-f', '--file', help='The name of the favicon file.')
    args = parser.parse_args()
    if args.file is None:
        parser.print_help()
        exit(1)
    else:
        file_name = args.file
        md5_hash = generate_md5_hash(file_name)
        mmh3_hash = compute_mmh3_hash(file_name)
        print(Color.GREEN + "\n[+] Results:" + Color.END)
        print(f"[+] The mmh3 hash of the file is: {mmh3_hash}")
        print(f"[+] The MD5 hash of the file is: {md5_hash}")
        print(Color.RED +
              f"[+] The shodan.io search syntax is: http.favicon.hash:{mmh3_hash}" + Color.END)
        print(Color.WHITE +
              f'[+] The zoomeye.org search syntax is: iconhash:"{mmh3_hash}' + '"' + Color.END)
        print(Color.ORANGE +
              f"[+] The search.censys.io search syntax is: {md5_hash}" + Color.END)
