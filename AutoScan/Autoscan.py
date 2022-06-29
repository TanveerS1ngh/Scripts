import os

os.system(if EUID == 0:
   echo "This script must be run as root" 
else:  
   exit 1)



os.system('mkdir user')
