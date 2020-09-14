import subprocess
mods = open("mods.txt")
mods = mods.read().strip('][').split(', ')
for i in mods:
    print(i)
    subprocess.call('pip install ' + i, shell=True)