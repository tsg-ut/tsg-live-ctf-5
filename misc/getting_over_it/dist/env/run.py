#!/usr/bin/env python3.7
import sys
import os
import binascii
import re
import subprocess
import signal

with open("flag", "r") as f:
    flag = f.read().strip("\n")

def handler(x, y):
    sys.exit(-1)


signal.signal(signal.SIGALRM, handler)
signal.alarm(30)


def gen_filename():
    base = '/prog/'
    if 'BASE' in os.environ:
        base = os.environ['BASE'] + '/'
    return base + binascii.hexlify(os.urandom(50)).decode('utf-8')


def is_bad_str(code):
    code = code.lower()
    # I don't like these words :)
    for s in ['!', 'std', "#", "return", "unsafe", "sandbox", '}']:
        if s in code:
            return True
    return False


def is_bad(code):
    return is_bad_str(code)


place_holder = '/* code */'
flag_holder = '/* redacted */'
template_file = 'template.rs'
MAX_SIZE = 50

def run_with_timeout(l, timeout, devnull=False):
    try:
        if devnull:
            subprocess.check_call(l, timeout=timeout, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            subprocess.check_call(l, timeout=timeout)
    except Exception as e:
        return False
    return True

def main():
    print(f'Give me the source code(size <= {MAX_SIZE}).')
    size = 0
    code = input()
    if len(code) > MAX_SIZE:
        print('too big')
        return False

    if is_bad(code):
        print('bad code')
        return False

    with open(template_file, 'r') as f:
        template = f.read()

    basename = gen_filename()
    filename = basename + "/prog.rs"

    os.system(f'mkdir {basename}')
    with open(filename, 'w') as f:
        f.write(template.replace(place_holder, code).replace(flag_holder, flag))
    if not run_with_timeout(f'rustc -O {filename} -o {basename}/prog'.split(' '), 2, devnull=True):
        print('compile error')
        return
    if not run_with_timeout(f'{basename}/prog', 0.2):
        print('run error')
        return


main()
