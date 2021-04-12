import os
import _thread
import subprocess
import platform
import json
import threading

import debug
import common
import time

import douyin_log

dylog = douyin_log.Dy_log()
dylog.setpath(r"C:\Ruijie\workplace\python3\tmp")
dylog.show()
dylog.insert("video-123", 'done', 'user-1', 'done')
dylog.show()
dylog.insert("video-123", 'done', 'user-2', 'done')
dylog.show()
dylog.sync_to_file()
dylog.show()
