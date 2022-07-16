#!/usr/bin/python3
# -*- coding: utf-8 -*-

import queue
import sys
from pathlib import Path
import argparse
from sms77api.Sms77api import Sms77api
import os
from dotenv import load_dotenv
from queue import Queue
from threading import Thread
import logging
from time import time


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SmsWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
    
    def run(self):
        while True:
            number, message = self.queue.get()
            try:
                send_message(number, message)
            finally:
                self.queue.task_done()

load_dotenv()
SMS77IO_API_KEY = os.getenv('SMS77IO_API_KEY')
client = Sms77api(SMS77IO_API_KEY)

def load_file(numbers):
    folder_db = "input"
    path = Path(f'{folder_db}/{numbers}')
    return [number for line in open(path, 'r') for number in line.split()]

def log(type, message):
    folder_db = "output"
    path = Path(f'{folder_db}/{type}.txt')
    f = open(path, "a+")
    f.write(f'{message}')
    f.close()

def show_balance():
    return client.balance()

def count_numbers(numbers):
    folder_db = "input"
    path = Path(f'{folder_db}/{numbers}')
    return [number for line in open(path, 'r') for number in line.split()]

def send_message(number, message):

    message = load_file(message)

    res = client.sms(number, message[0], {'json': True})
    if(int(res['success']) == 100):
        print(f'\033[92m Message Sent succesfully to {number} \033[00m')
        log("success", "{}\n".format(number))
    else:
        print("\033[91m Message not sent to {} - {} \033[00m".format(number, res['messages'][0]['error_text']))
        log("error", "{}\n".format(number))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Send SMS with sms77.io')
    parser.add_argument("-n", "--numbers", help="file that contains phone numbers")
    parser.add_argument("-m", "--message", help="file that contains the message")
    parser.add_argument("-b", "--balance", action="store_true", help="See the available balance")
    parser.add_argument("-c", "--count", help="Count numbers available to send")
    parser.add_argument("-t", "--threads", default=5, type=int, help="Threads to boost the speed, Default = 5")
    args = parser.parse_args()

    if args.numbers and args.message:
        ts = time()
        queue = Queue()
        for x in range(args.threads):
            worker = SmsWorker(queue)
            worker.daemon = True
            worker.start()
        
        numbers = load_file(args.numbers)

        for number in numbers:
            # logger.info('Queueing {} {}'.format(number, args.message))
            queue.put((number, args.message))
        queue.join()
        # logging.info('Took %s', time() - ts)

    elif args.balance:
        print("Your available balance is {} euro\n".format(show_balance()))
    elif args.count:
        print("{} Phone numbers available\n".format(len(count_numbers(args.count))))
    else:
        parser.print_help()
        sys.exit(0)
