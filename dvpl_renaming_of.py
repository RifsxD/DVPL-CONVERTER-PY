print('Dvpl Converter by RifsxD.')
import os
f = '2_unpacked'
files = os.listdir(f)
for file in files:
    a = f + "/" + file
    os.rename(a, a[0:-5])
    
# Code By RifsxD
# https://discord.gg/8bkWQNR4pn