## BGSD  
BGSD, or Big-Goofy Software Distro is an open-source python OS emulation framework. It has drivers for a custom file system I came up with called goofyFS, or gFS for short.  
BGSD is intended to help people get into python, by making cli apps somewhat more simple. BGSD is currently under active development, so bugs and annoying-to-use functions do exist. Keep that in mind  
and thanks for checking it out.  

## Drivers
error_screen: pops up with a windows-style error screen in the terminal. In order to use it, you have to set drivers.err_msg and drivers.err_code.  
load_goofyfs: loads the goofyfs.json file and returns a python dictionary with its contents.  
write_goofyfs: writes a gFS-formatted python dictionary to the goofyfs.json file. Arguments: gfs: dict  
find_file: locates a file in the current gFS partition and returns it. Arguments: path: str, gfs: dict, partition: str  
make_file: makes a file in the current gFS partition. Arguments: filename: str, file_desc: str, directory: str, exe: str, gfs: dict, partition: str  
list_files: returns all files in current gFS partition. Arguments: gfs: dict, partition: str  
mount_drive: mounts a gFS-formatted json file located in the mnt directory. Arguments: filename: str, gfs: dict  
shutdown: shuts down the OS.  
clear: clears the screen.  
draw_line_h: draws a horizontal line. Arguments: length: int. Returns the line (you have to output it yourself)  
draw_line_v: draws a vertical line. Arguments: length: int. Returns the line (you have to output it yourself)
