print('Dvpl Converter by RifsxD')
import os
f = '4_packed'
files = os.listdir(f)
for file in files:
    os.rename(f + "/" + file, f + "/" + file + ".dvpl")
    
# Coded by RifsxD
# https://discord.gg/8bkWQNR4pn