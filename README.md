# python-intentionally-vuln-package
vulnerable version of demo_math_ops package.
You will find this package in PyPi repo here - https://pypi.org/project/vuln-demo-math-ops/ 


## Install the Package from local file Sources
1. Clone the repo.
```sh
$ git clone https://github.com/rahg0/python-intentionally-vuln-package.git
$ cd python-intentionally-vuln-package
```

2. Install the package locally.
```sh
$ pip install .

$ pip list

$ pip show vuln_demo_math_ops
```

## Usage within a Python Code
```py
from vuln_demo_math_ops import addition_module, subtraction_module, multiplication_module, division_module
```
OR

```py
from vuln_demo_math_ops import add, sub, mult, div
```

### Sample Python code
```py
from vuln_demo_math_ops import add, sub, mult, div

# Initialise some integer variables
value1 = 5
value2 = 3

print("Adding {0} and {1} gives {2}".format(value1, value2, add(value1, value2)))
print("Subtracting {0} from {1} results in {2}" .format(value1,value2, sub(value1,value2)))
print("Multiplying {0} by {1} equals {2}" .format(value1,value2, mult(value1,value2)))
print("Dividing {0} by {1} gives {2}" .format(value1,value2, div(value1,value2)))
```
### Execution
```sh
$ python math_sample_code.py
Adding 5 and 3 gives 8
Subtracting 5 from 3 results in 2
Multiplying 5 by 3 equals 15
Dividing 5 by 3 gives 1.6666666666666667
```


## Create Wheel & Source Distribution files
1. Clone the repo.
```sh
$ git clone https://github.com/rahg0/python-intentionally-vuln-package.git
$ cd python-intentionally-vuln-package
```

2. Install the tools setuptools, wheel, and twine needed to build & upload package.
```sh
$ pip install setuptools wheel twine
```

3. Build the distribution files.
```sh
$ python setup.py sdist bdist_wheel
```

4. Source distribution (**.tar.gz**) and Wheel file (**.whl**) will be placed under **`dist/`** directory.


## Upload the Package to PyPi (Optional)
```sh
$ twine upload dist/*
```

## Install the Package from PyPi
```sh
$ pip install vuln_demo_math_ops

$ pip list

$ pip show vuln_demo_math_ops
```

## Creating a Container Image with this Package fetched from PyPi
1. Sample Dockerfile:
```Dockerfile
FROM python:alpine
RUN pip install vuln-demo-math-ops
CMD ["sleep", "36000"]
```

2. Build the image:
```sh
$ docker image build -t py-vuls-image .
```

3. Scan the image using any vulnerability scanner tool like orca-cli:
```sh
$ orca-cli image scan py-vuls-image
  ____   ___   _____ ___      ____ ____ _____ __  __ ___   ____ ________  __
 / __ \ / _ \ / ___// _ |    / __// __// ___// / / // _ \ /  _//_  __/\ \/ /
/ /_/ // , _// /__ / __ |   _\ \ / _/ / /__ / /_/ // , _/_/ /   / /    \  /
\____//_/|_| \___//_/ |_|  /___//___/ \___/ \____//_/|_|/___/  /_/     /_/
✓ Performing image scanning for security risks
✓ Performing results analysis and policy decision (via Orca Cloud)
========================================================================
VULNERABILITIES
alpine (OS Packages)
[TOTAL: 0 | HIGH: 0 | MEDIUM: 0 | LOW: 0 | UNKNOWN: 0]

node-pkg (Node.js)
[TOTAL: 0 | HIGH: 0 | MEDIUM: 0 | LOW: 0 | UNKNOWN: 0]

python-pkg (Python)
[TOTAL: 6 | CRITICAL: 2 | HIGH: 3 | MEDIUM: 1 | LOW: 0 | UNKNOWN: 0]
╭──────────┬──────────────────┬───────────────────┬───────────────┬──────────┬───────┬───────┬────────╮
│ PACKAGE  │ VULNERABILITY ID │ INSTALLED VERSION │ FIXED VERSION │ SEVERITY │ CVSS2 │ CVSS3 │ STATUS │
├──────────┼──────────────────┼───────────────────┼───────────────┼──────────┼───────┼───────┼────────┤
│ agpt     │ CVE-2024-6091    │ 0.2.2             │               │ CRITICAL │       │ 9.8   │ FAILED │
├──────────┼──────────────────┼───────────────────┼───────────────┼──────────┼───────┼───────┼────────┤
│ gradio   │ CVE-2025-23042   │ 5.10.0            │ 5.11.0        │ CRITICAL │       │       │ FAILED │
├──────────┼──────────────────┼───────────────────┼───────────────┼──────────┼───────┼───────┼────────┤
│ Flask    │ CVE-2023-30861   │ 1.0.2             │ 2.3.2, 2.2.5  │ HIGH     │       │ 7.5   │ FAILED │
├──────────┼──────────────────┼───────────────────┼───────────────┼──────────┼───────┼───────┼────────┤
│ waitress │ CVE-2022-24761   │ 2.0.0             │ 2.1.1         │ HIGH     │ 5     │ 7.5   │ FAILED │
├──────────┼──────────────────┼───────────────────┼───────────────┼──────────┼───────┼───────┼────────┤
│ waitress │ CVE-2024-49769   │ 2.0.0             │ 3.0.1         │ HIGH     │       │ 7.5   │ FAILED │
├──────────┼──────────────────┼───────────────────┼───────────────┼──────────┼───────┼───────┼────────┤
│ waitress │ CVE-2024-49768   │ 2.0.0             │ 3.0.1         │ MEDIUM   │       │ 4.8   │ FAILED │
╰──────────┴──────────────────┴───────────────────┴───────────────┴──────────┴───────┴───────┴────────╯

```
