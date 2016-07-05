# Sandbox-Pelican

This project is under development, do not use it in production environment.
Only for testing purposes.

**Supported language: Java, Python, C/C++**
**More languages are coming soon...**

### Version
0.0.1

### Requirements
Python 2.7.10

### Installation
It is recommended to run this in [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

If you use virtualenv run the following:
```sh
$ virtualenv venv
$ . venv/bin/activate
```

Install Sandbox-Pelican using pip:
```sh
$ pip install --editable .
```

### Usage
Run Java code in sandbox:
```sh
$ sandbox java /path/to/file.java
```

Run C/C++ code in sandbox:
```sh
$ sandbox gcc /path/to/file.c
```

Run Python code in sandbox:
```sh
$ sandbox python /path/to/file.py
```

Help page:
```sh
$ sandbox --help
```

License
----

MIT


**Free Software, Hell Yeah!**
