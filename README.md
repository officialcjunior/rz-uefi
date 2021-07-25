[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)
[![CI](https://github.com/officialcjunior/rz-uefi/actions/workflows/ci.yml/badge.svg)](https://github.com/officialcjunior/rz-uefi/actions/)

# rz-uefi

rz-uefi is a python package that provides tools for analyzing UEFI firmware modules using Rizin. It 
features an analyzer and a scanner which you can use with a script as well as with Python code.

This project is a fork of [uefi_r2](https://github.com/binarly-io/uefi_r2) and thanks to 
[binarly.io](https://www.binarly.io) for this amazing tool.

# Installation

rz-uefi is a Python package and can be installed using:

```bash
python setup.py install
```

# Usage

The tool can be used in two ways: with the script or from the Python shell. 

### With the script

Run `$ ./rzuefi_analyzer.py --help` for the basic help. You can use this to scan
or to analyze the file.

```bash
./rzuefi-analyzer.py analyze-image {image_path} -o out.json
./rzuefi-analyzer.py scan --rule {rule_path} {image_path}
```

### From code

After installing it properly, the tool can be used from Python code.

Here's some of the APIs you can use:

```python
from rzuefi.uefi_analyzer import UefiAnalyzer
from rzuefi.uefi_scanner import UefiRule, UefiScanner

summary = UefiAnalyzer.get_summary(image_path)

uefi_analyzer = UefiAnalyzer(image_path)
uefi_rule = UefiRule(rule)
scanner = UefiScanner(uefi_analyzer, uefi_rule)
result = scanner.result
```
