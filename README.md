# Ubiquiti EdgeSwitch with Netmiko and TextFSM
*Take unstructured data (strings) and convert them to structured data with TextFSM*

## Libraries

- **Netmiko** is a multi-vendor tool that allows you to connect to your network device, in this case, an EdgeSwitch EdgeSwitch.
- **TextFSM** is a library that helps take unstructured data and converts them to structured data (i.e. taking in unstructured strings and putting them in a list of dictionary objects)

## Instructions

**NOTE**: This was tested on a Linux Machine, can't speak for Windows or Mac OS

1. Git clone NTC Templates (Network To Code) into your user's home directory

```
git clone https://github.com/networktocode/ntc-templates ~/ntc-templates
```

2. Git Clone my repo

3. Create a Python Virtual Environment and Install Required Library

```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python3 edgeswitch.py
```
