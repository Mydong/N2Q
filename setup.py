# -*- coding: utf-8 -*-  
__author__ = 'icegene' 
from distutils.core import setup  
import py2exe 
includes = ["encodings", "encodings.*"]  
setup(  
description = "help to transfer playlists from Netease Cloud Music to QQ Music",  
name = "N2Q",  
options = {'py2exe' : { 
                     "bundle_files": 1,
                     "dll_excludes": ["MSVCP90.dll","w9xpopen.exe"]
                     }
                  },
zipfile = None,  
windows = [{"script": "N2Q.py",  
            "icon_resources": [(1, "n2q.ico")]
           }]  
)