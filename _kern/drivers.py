import os, json

COLORS = {
    "RESET": "\033[0m",
    "FG": {
        "BLACK": "\033[30m",
        "RED": "\033[31m",
        "GREEN": "\033[32m",
        "YELLOW": "\033[33m",
        "BLUE": "\033[34m",
        "MAGENTA": "\033[35m",
        "CYAN": "\033[36m",
        "WHITE": "\033[37m"
    },
    "BG": {
        "BLACK": "\033[40m",
        "RED": "\033[41m",
        "GREEN": "\033[42m",
        "YELLOW": "\033[43m",
        "BLUE": "\033[44m",
        "MAGENTA": "\033[45m",
        "CYAN": "\033[46m",
        "WHITE": "\033[47m"
    }
}

# ERROR HANDLING #######################################################################################################
err_msg = ""
err_code = ""

def error_screen():

    DEF_ERR_MSG = f"""
Oops! 
            
        {err_msg}
        Please revert back to DEFAULT SETTINGS.
            
        Error code:
            ERR_{err_code}: MODIFIED FS
"""

    os.system("color 47")
    os.system("cls")
    print(DEF_ERR_MSG)
    input("Press enter to shut down...")
    shutdown()

# GOOFY-FS DRIVERS ###################################################################################################
PARTITION = "GFS.A"
ROOTDIR = "A:/"

def load_goofyfs():
    with open("goofyfs.json", "r") as g:
        goofyfs = json.loads(g.read())
    
    return goofyfs

GFS: dict = load_goofyfs()

def write_goofyfs(gfs: dict[str]):
    with open("goofyfs.json", "w") as g:
        g.write(json.dumps(gfs))

def find_file(path: str, gfs: dict = load_goofyfs(), partition: str = "GFS.A"):
    path = path.replace("A:/", "")
    c_path = gfs["PARTITION-" + partition][ROOTDIR]
    return c_path[path]

def make_file(filename: str, file_desc: str, directory: str, exe: str="FALSE", gfs: dict = load_goofyfs(), partition: str = "GFS.A"):
    filename = filename.replace("A:/", "")
    c_path = gfs["PARTITION-" + partition][ROOTDIR]
    c_path[directory + "/" + filename] = {"FLC": file_desc, "EXE": exe, "_FL": "TRUE", "DIR": directory}

    write_goofyfs(gfs)

def list_files(gfs: dict = load_goofyfs(), partition: str = "GFS.A"):
    ret = []
    for file in gfs["PARTITION-" + partition][ROOTDIR]:
        ret.append([file, gfs["PARTITION-" + partition][ROOTDIR][file]])
    return ret

def mount_drive(filename: str, gfs: dict = load_goofyfs()):
    os.chdir('../mnt')
    if filename in os.listdir():
        with open(filename, "r") as f:
            gfs_drv = json.loads(f.read())

        gfs.update(gfs_drv)
        GFS.update(gfs_drv)
        return gfs
    else:
        return {"ERR": "File mount error"}

# VIDEO DRIVERS ###################################################################################################
    
def shutdown():
    os.system("color 07")
    os.system("cls")
    quit()

def clear():
    os.system("cls")

def draw_line_h(length):
    ret = ''
    for _ in range(length):
        ret += '#'
    return ret

def draw_line_v(length):
    ret = ''
    for _ in range(length):
        ret += '#\n'
    return ret

def set_color(fg="GREEN", bg="BLACK"):
    print(COLORS["BG"][bg.upper()], COLORS["FG"][fg.upper()], end="\r")