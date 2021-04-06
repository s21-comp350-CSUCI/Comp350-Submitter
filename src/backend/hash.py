#!/usr/local/bin/python3

import hashlib, sys
from datetime import datetime

def hashThis(arg1, arg2, arg3):
    nowTime = datetime.now().time()
    stringToken = "{}:{}:{}:{}".format(*arg1, arg2, arg3, nowTime)
    token = hashlib.md5(stringToken.encode()).hexdigest()
    return token
    
usage = "./hash.py <student email | token list> <admin> <event> <time>"
if len(sys.argv) != 4:
    print(usage)
    exit(0)

print(hashThis(sys.argv[1], sys.argv[2], sys.argv[3]))
