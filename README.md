# pplogger
PP's Logger Module

PyPI package: [pplogger](https://pypi.python.org/pypi/pplogger)

If you spot any problems or have any improvement ideas then feel free to open
an issue and I will be glad to look into it for you.

## Installation
A recommended way of installing the module is pip install.

### pip install
The tool is available in PyPI and can be installed using pip:
```
$ pip install --upgrade pip setuptools wheel
$ pip install pplogger
```

## Usage
```
from pplogger import get_logger

log = get_logger()
log.debug('Debug message')
```
