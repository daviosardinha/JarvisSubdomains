#!/usr/bin/env python3
import sys, argparse, requests, json

BASE_URL = "https://crt.sh/?q={}&output=json"
subdomains = set()
wildcardsubdomains = set()

def parser_error(errmsg):
    print("Usage: python3 " + sys.argv[0] + " [Options] use -h for help")
    print("Error: " + errmsg)
    sys.exit()

def parse_args():    
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython3 ' + sys.argv[0] + " -d google.com")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-d', '--domain', help='Specify Target Domain to get subdomains from crt.sh', required=False)
    # A new argument was added "-f --file"
    parser.add_argument('-f', '--file', help='Specify Target list of domains to get subdomains from crt.sh', required=False)
    parser.add_argument('-r', '--recursive', help='Do recursive search for subdomains', action='store_true', required=False)
    parser.add_argument('-w', '--wildcard', help='Include wildcard in output', action='store_true', required=False)
    return parser.parse_args()

def crtsh(domain):
    try:
        response = requests.get(BASE_URL.format(domain), timeout=25)
        if response.ok:
            content = response.content.decode('UTF-8')
            jsondata = json.loads(content)
            for i in range(len(jsondata)):
                name_value = jsondata[i]['name_value']
                if name_value.find('\n'):
                    subname_value = name_value.split('\n')
                    for subname_value in subname_value:
                        if subname_value.find('*'):
                            if subname_value not in subdomains:
                                subdomains.add(subname_value)
                        else:
                            if subname_value not in wildcardsubdomains:
                                wildcardsubdomains.add(subname_value)
    except:
        pass

if __name__ == "__main__":
    args = parse_args()
    #The next line was added in order to read a list of domains given by the user.
    if args.file:
        for domain in open(args.file, 'r').readlines():
            crtsh(domain.strip())
    elif args.domain:
        crtsh(args.domain)
    if args.domain or args.file:
        for subdomain in subdomains:
            print(subdomain)

    if args.recursive:
        for wildcardsubdomain in wildcardsubdomains.copy():
            wildcardsubdomain = wildcardsubdomain.replace('*.', '%25.')
            crtsh(wildcardsubdomain)

    if args.wildcard:
        for wildcardsubdomain in wildcardsubdomains:
            print(wildcardsubdomain)
