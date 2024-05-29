from scapy.all import * 
from pathlib import Path 
import csv

ip = conf.ifaces  # default interface
# cat="CAt"
# # filename = input("Would you like to name the file? ")
# p = Path("temp/host")
# p.mkdir(parents=True, exist_ok=True)
# fn = input("Please name the file: ")
# filepath = p / fn
# with filepath.open("w", encoding ="utf-8") as f:
#     f.write(str(ip))

print(ip)
