import argparse
import sys
import json
import os
from src.ip_validator import get_ip_type

def process_file(filepath: str, output_format: str):
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

    results = []
    
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    print(f"Processing {len(lines)} addresses from {filepath}...\n")

    for ip in lines:
        result = get_ip_type(ip)
        entry = {"ip": ip, "type": result, "valid": result != "Invalid"}
        results.append(entry)
        
        if output_format == 'text':
            icon = "✅" if result != "Invalid" else "❌"
            print(f"{icon} {ip.ljust(40)} -> {result}")

    if output_format == 'json':
        print(json.dumps(results, indent=4))
        
    with open('results.json', 'w') as f:
        json.dump(results, f, indent=4)
        print(f"\nResults saved to 'results.json'")

def main():
    parser = argparse.ArgumentParser(description="Professional IP Validator Tool")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--ip', type=str, help="Validate a single IP address")
    group.add_argument('--file', type=str, help="Validate a list of IPs from a text file")
    parser.add_argument('--json', action='store_true', help="Output results as JSON")

    args = parser.parse_args()

    if args.ip:
        result = get_ip_type(args.ip)
        if args.json:
            print(json.dumps({"ip": args.ip, "type": result, "valid": result != "Invalid"}, indent=4))
        else:
            print(f"IP: {args.ip} is {result}")
            
    elif args.file:
        fmt = 'json' if args.json else 'text'
        process_file(args.file, fmt)

if __name__ == "__main__":
    main()