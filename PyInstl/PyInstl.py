#PyInstl.py
import time
import sys
import os
import LoadAnim
import argparse
import subprocess
from pyfiglet import Figlet
from clint.textui import puts, colored, indent


def install(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except Exception as err:
        puts(colored.red('ERROR: ') + colored.yellow(err))


def make_args():
    my_parser = argparse.ArgumentParser(description='Package Installer')
    my_parser.add_argument('Package',
                       metavar='pkg_name',
                       type=str,
                       help='The Package Name')
    
    args = my_parser.parse_args()

def get_user_input():
    if len(sys.argv) > 2:
        print('You have specified too many arguments')
        sys.exit()

    if len(sys.argv) < 2:
        return ""

    return sys.argv[1]

def main(pkg_name):
    f = Figlet(font='slant')
    print(f.renderText('PyInstl'))
    make_args()
    with indent(4, quote='>>>'):
        puts(colored.blue('Installing package: ') + str(pkg_name))
    LoadAnim.load_animation()
    install(pkg_name)
    

if __name__ == "__main__":
    main(get_user_input())