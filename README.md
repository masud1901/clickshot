# ClickShots
# ClickShots

[![Tests](https://github.com/yourusername/clickshots/actions/workflows/tests.yml/badge.svg)](https://github.com/yourusername/clickshots/actions)
[![PyPI version](https://badge.fury.io/py/clickshots.svg)](https://badge.fury.io/py/clickshots)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust automated screenshot capture system that monitors user interactions.

## Installation

```bash
pip install -e .
```

## Usage

### Command Line

```bash
# Use default directory (~/Pictures/clickshots)
clickshots

# Or specify a custom directory
clickshots -d /path/to/save/directory
clickshots --directory /path/to/save/directory
```

### Python Code

```python
from clickshots import main

# Use default directory
main()

# Or specify directory
main(save_dir="/path/to/save/directory")
```

### Controls

- **Ctrl + Shift**: Toggle mouse/touchpad screenshots
- **Alt + \\**: Toggle keyboard screenshots
- **Ctrl + C**: Exit program

