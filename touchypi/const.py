import os

RUNNING_ON_PI = (os.uname().sysname == "Linux") and (os.uname().machine == "armv6l")
