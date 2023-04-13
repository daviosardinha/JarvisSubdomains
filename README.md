This Was a tool built intially by https://github.com/YashGoti/crtsh, credits to this guy.
I decided to continue to update what he started few years ago.

Thank You YashGoti




# JarvisSubdomains.py
A Python utility to fetch subdomains by making requests on https://crt.sh

### Requirements
```
argparse
requests
json
```

### Installation
```
git clone https://github.com/daviosardinha/JarvisSubdomains.git
cd JarvisSubdomains.py
python3 JarvisSubdomains.py -h
```
* if you want to use crtsh from anywhere try below installation guide
```
git clone https://github.com/daviosardinha/JarvisSubdomains.git
cd JarvisSubdomains.py
mv JarvisSubdomains.py JarvisSubdomains
chmod +x JarvisSubdomains
cp JarvisSubdomains /usr/bin/
```

### Options
|Flags||Description|
|-|-|-|
|-h|--help|show this help message and exit|
|-d DOMAIN|--domain DOMAIN|Specify Target Domain to get subdomains from crt.sh|
|-f|--file| Specify Target list to get subdomains from crt.sh|
|-r|--recursive|Do recursive search for subdomains|
|-w|--wildcard|Include wildcard in output|

### Usage
```
python3 JarvisSubdomains.py -d example.com
python3 JarvisSubdomains.py -f file.txt
python3 JarvisSubdomains.py -d example.com -w
python3 JarvisSubdomains.py -d example.com -r
python3 JarvisSubdomains.py -d example.com -r -w
```
