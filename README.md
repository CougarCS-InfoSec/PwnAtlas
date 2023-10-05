# PwnAtlas
PwnAtlas is CougarCS InfoSec's multi-API wrapper module for CVE and ExploitDB lookup. It currently features the ability to lookup CVE's by both a keyword search and by it's assigned ID. It returns a dictionary of the most important values, which can be used for many purposes, including:
- Discord Bots
- Websites
- Python Scripts
- etc.

## Installation
Implementing PwnAtlas into your project is simple.

### Via Source
Clone the github repository:
```bash
git clone https://github.com/diante0x7/PwnAtlas.git
```
Then, install the ```pwnatlas``` module using pip locally by running:
```bash
cd PwnAtlas
pip install .
```

### From Release
Grab the most recent .whl file from the Releases tab and install it like this:
> For the most recent release: PwnAtlas-0.1b2
```bash
pip install PwnAtlas-0.1b2-py3-none-any.whl
```

### From PyPi
Fetch the newest release of [PwnAtlas](https://pypi.org/project/PwnAtlas)
```bash
pip install pwnatlas
```

## Implementation
You then use the module by doing this:
```python
from pwnatlas import get as cve_get

dictionary = cve_get.by_id('CVE-2019-1040')
```

## Support
Support CougarCS and it's InfoSec team by using, forking, and crediting this project as much as you can!

[Website](https://cougarcs.com)
