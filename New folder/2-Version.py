# Output string contain:
    # Version Number.
    # Additional information on the build number and compiler used.

#--------------------Command line or Powershell--------------
"""
>> python --version
>> 3.9.7
>> python -V
>> 3.9.7
""" 

#--------------------Using sys Module------------------------               ---output---
import sys
print("Python Version:", sys.version)           # 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)]
print("Version Information:", sys.version_info) # (majoe=3, minor=9, micro=7, releaselevel='final', serial=0)
print("By name Major:", sys.version_info.major)         # 3
print("By index [1]:",sys.version_info[1])              # 9

#--------------------Basic Information-----------------------
"""
Version info contains: 
    - it is tuple information
    - components are:
        -> major, minor, micro, releaselevel and serial
             |      |      |          |            |
           number number number     string       number

        -> for example (2, 0, 0, 'final', 0)
        -> releaselevel can be: 'alpha', 'beta', 'candidate', 'final'
        -> we can access a particular:
            > by index: sys.version_info[0]
            > by name: sys.version_info.releaselevel
"""

#--------------------Using platform module-------------------           ---Output---
import platform
print(platform.python_version())        # 3.9.7
print(platform.python_version_tuple())  # it shows as tuple: ('3', '9', '7')