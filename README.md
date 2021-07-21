[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)

# rzuefi

Tools for analyzing UEFI firmware using Rizin

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
summary = UefiAnalyzer.get_summary(image_path, debug=True)
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
