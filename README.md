[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

# rzuefi

rzuefi is a python package that provides tools for analyzing UEFI firmware modules using Rizin. It 
features an analyzer and a scanner which you can use with a script as well as with Python code.

This project is a fork of [uefi_r2](https://github.com/binarly-io/uefi_r2) and thanks to 
[binarly.io](binarly.io) for this amazing tool.

# Dependencies

## Rizin

```
rizin 0.3.0-git @ linux-x86-64
```

# Installation

```bash
python setup.py install
```

# Example

### With script

```
./rzuefi-analyzer.py analyze-image {image_path} -o out.json
./rzuefi-analyzer.py scan --rule {rule_path} {image_path}
```

### From code

```python
from rzuefi.uefi_analyzer import UefiAnalyzer

...
summary = UefiAnalyzer.get_summary(image_path)
```

```python
from rzuefi.uefi_analyzer import UefiAnalyzer
from rzuefi.uefi_scanner import UefiRule, UefiScanner

...
uefi_analyzer = UefiAnalyzer(image_path)
uefi_rule = UefiRule(rule)
scanner = UefiScanner(uefi_analyzer, uefi_rule)
result = scanner.result
```
