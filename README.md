IP Validator Tool 

A small Python tool I built to quickly check IPv4 and IPv6 addresses.
Runs in the terminal, easy to use, and can handle lots of IPs at once.

Features

Simple Validation: Detects IPv4, IPv6, or invalid addresses.

Batch Mode: Can check multiple IPs from a file at once.

JSON Output: Handy if you want to use the results somewhere else.

Tests Included: Some unit tests make sure everything works.

🛠 How to Use
Check a single IP
python main.py --ip 192.168.1.1

Check a list of IPs from a file
python main.py --file data/ips.txt

Output results as JSON
python main.py --ip 192.168.1.1 --json
python main.py --file data/ips.txt --json

Run the Tests
python -m unittest discover tests
