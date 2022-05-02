import os
import shutil
import sys

def find_pattern(bin, sz, pattern, wildcard = 0x69):
    for i in range(0, sz):
        for m in range(0, len(pattern)): 
            if pattern[m] == 0x69:
                continue
            if wc_bin[i + m] != pattern[m]:
                break
            if m == len(pattern) - 1:
                return i
    return None


default_path = "C:/Program Files/obs-studio/obs-plugins/64bit/win-capture.dll"
wc_path = None 

argslen = len(sys.argv)
if argslen == 1:
    if not os.path.exists(default_path):
        print("Usage:", __file__, "<path to obs installation>/obs-studio/obs-plugins/64bit/win-capture.dll")
        exit(1)
    wc_path = default_path

if wc_path is None:
    if argslen != 2:
        print("Invalid number of parameters! Please provide the path to win-capture.dll")
        exit(1)
    wc_path = sys.argv[1]

if not os.path.exists(wc_path):
    print("Invalid file path for win-capture.dll : ", wc_path)
    exit(1)

print("[+] Opening file...")
wc_file = open(wc_path, "rb")
if wc_file is None:
    print("[!] Failed to open file")
    exit(1)

print("[+] Reading file...")
wc_bin = bytearray(wc_file.read())
wc_file.close()
sz = len(wc_bin)
print("[+]", sz, "bytes")

print("[+] Looking for pattern...")
offset = find_pattern(wc_bin, sz, [0x41, 0x8D, 0x51, 0x23, 0xFF, 0x15, 0x69, 0x69, 0x69, 0x69, 0xBA])
if offset is None:
    if find_pattern(wc_bin, sz, [0x41, 0x8D, 0x51, 0x24]) != None:
        print("[+] This binary has already been patched!")
        exit(0)
    print("[!] Failed to find pattern!")
    exit(1)
print("[+] File Offset:", offset)

wc_bin[offset + 3] = 0x24
print("[+] Creating backup...")
shutil.copyfile(wc_path, wc_path + '.bak')
print("[+] Applying patch...")
wc_pfile = open(wc_path, "wb")
if wc_pfile is None:
    print("[!] Failed to open file for patching")
    exit(1)

wc_pfile.write(wc_bin)
print("[+] Patch applied successfully")