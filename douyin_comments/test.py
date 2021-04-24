import os
import _thread
import subprocess
import platform
import json
import threading
import re

import debug
import common
import time

import douyin_log

page_info = {
        301:{"tag":"node","attrs":{"resource-id":"com.ss.android.ugc.aweme:id/dzo"},"finds":{"bounds"}}
    }
print(page_info)
