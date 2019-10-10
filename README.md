# LeetCode

Решения задач с https://leetcode.com/

# Usage

Creat python virtual enviroment with python 3.6+ version   
Install requirements from requirements.txt

```bash
python3.6 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```
### First way

```bash

python learn_argparse.py --num1 10 --num2 2000

```
### Second way
```python

from learn_argparse import sum_all_nums


sum_all_nums(10, 2000)

"""
20000
"""

```

# TESTS

```bash
python -m doctest -v learn_argparse.py
```

