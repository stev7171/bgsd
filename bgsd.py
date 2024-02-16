import json, os

dbg = "[BGSD]"

print(f"{dbg} Booting BGSD...")
print(f"{dbg} Changing to kernel directory...")
os.chdir('_kern')
print(f"{dbg} Locating file system (Currently located in _kern/goofyfs.json)...")
if "goofyfs.json" in os.listdir():
    print(f"{dbg} Reading GoofyFS...")
    f = open("goofyfs.json", "r")
    goofyfs = json.loads(f.read())

    PARTITION = "GFS.A"
    BOOTSEC = ".BOOT"
    print(f"{dbg} Locating partition (GFS.A)...")
    if "PARTITION-" + PARTITION in goofyfs:
        BOOTPATH = goofyfs["PARTITION-" + PARTITION][BOOTSEC]["LDR"].replace('_boot/', '')

        print(f"{dbg} Booting into OS bootloader...")
        if goofyfs["PARTITION-" + PARTITION][BOOTSEC]["EXE"] == "TRUE":
                os.chdir('../_boot')
                os.system(f'{BOOTPATH}')
                f.close()
        else:
                print(f"{dbg} Failed!")
                input("\nPress enter to exit...")
                os.system("color 07")
                os.system("cls")
    else:
                print(f"{dbg} Failed!")
                input("\nPress enter to exit...")
                os.system("color 07")
                os.system("cls")
else:
    print(f"{dbg} Failed!")
    input("\nPress enter to exit...")
    os.system("color 07")
    os.system("cls")