#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import fileinput
import re
from pathlib import Path
import argparse
from sms77api.Sms77api import Sms77api


# def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
# def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
# def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
# def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
# def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
# def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
# def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
# def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

def save_to_file(message, output_type):
    folder_db = "output"
    path = Path(f'{folder_db}/{output_type}.txt')
    f = open(path, "a+")
    f.write(f'{message}\n')
    f.close()


def send_message(numbers, message):
    for lines in fileinput.input([numbers]):
        try:
            email = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", lines).group()
        except AttributeError:
            print("\033[91m ERROR - {} \033[00m".format(lines.strip()))
            errors = errors + 1
            # break

        # print("\033[93m Line: {} , Email {} \033[00m".format(lines.strip(), email))
        domain = email.split("@")[1].split(".")[0]
        filename = email.split("@")[1].lower()


    print("No. of lines printed: {:,.2f}".format(count))
    print("No. of excluded domains found: {:,.2f}".format(found))
    print("No. of domains found: {:,.2f}".format(not_found))
    print("No. of errors found: {:,.2f}".format(errors))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send SMS with sms77.io')
    parser.add_argument("-n", "--numbers", help="file that contains phone numbers")
    parser.add_argument("-m", "--message", help="file that contains the message")
    args = parser.parse_args()

    if args.numbers and args.message:
        send_message(args.numbers, args.message)
    else:
        parser.print_help()
        sys.exit(0)
