# SMS77.IO API Based Sender

This is a simple sms api based sender.

## Supported providers
- **sms77.io**

## Installation

It was tested with **python3**.
Make sure you have installed **python3** before you install anrun it.

```bash
chmod +x install.sh
./install.sh
```

## Usage

```bash
usage: send.py [-h] [-n NUMBERS] [-m MESSAGE] [-b] [-c COUNT] [-t THREADS]

Send SMS with sms77.io

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBERS, --numbers NUMBERS
                        file that contains phone numbers
  -m MESSAGE, --message MESSAGE
                        file that contains the message
  -b, --balance         See the available balance
  -c COUNT, --count COUNT
                        Count numbers available to send
  -t THREADS, --threads THREADS
                        Threads to boost the speed, Default = 5

```

**Note**
> You need to add in input/ folder numbers.txt and message.txt if it does not exists already.

## TODO

- More options