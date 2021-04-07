import os
import subprocess
import platform
import json

import debug
import common
import auto_adb

config_file = r"C:\Ruijie\workplace\python3\test\config.json"
mm = common.common()
info = mm.readfile(config_file, 'all')
print(type(info), info)
