import time
import os

while True:
    os.system("python get_stock_data.py > companies.txt")
    time.sleep(2592000)
