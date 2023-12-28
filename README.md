# FaviconLocator
Computes the hashes of a favicon file and provides the search syntax for Shodan, Censys and Zoomeye

NOTE: You will likely need to run "pip install mmh3" on your system first. This will install the MurmurHash3 (mmh3) library capable of generating the mmh3 hash used by Shodan.io and Zoomeye.org.

Useage:  

C:\tools\favicon>python favicon_locator.py  
Please enter the name of the favicon file (including the extension): kfc.ico  
[+] Results:  
[+] The mmh3 hash of the file is: 1691174979  
[+] The MD5 hash of the file is: 0d22ff6f71d60e14f62c34ad33dcdec1  
[+] The shodan.io search syntax is: http.favicon.hash:1691174979  
[+] The zoomeye.org search syntax is: iconhash:":1691174979"  
[+] The search.censys.io search syntax is: 0d22ff6f71d60e14f62c34ad33dcdec1  


You can read a writeup on the tool here: https://www.digitalforensicstips.com/2023/12/introducing-faviconlocator-eazy-button.html
