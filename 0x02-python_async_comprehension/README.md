
# Python Async Comprehension

This project focuses on asynchronous programming in Python, specifically using async comprehensions.

## Table of Contents

1. [Learning Objectives](#learning-objectives)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Project Structure](#project-structure)
5. [Files](#files)
    - [0-async_generator.py](#0-async_generatorpy)
    - [1-async_comprehension.py](#1-async_comprehensionpy)
    - [2-measure_runtime.py](#2-measure_runtimepy)
6. [Usage](#usage)
7. [Author](#author)
8. [License](#license)

## Learning Objectives

- Understand the basics of asynchronous programming.
- Learn how to use async comprehensions.
- Explore the `asyncio` module and its utilities.

## Requirements

- Python 3.7 or higher
- `asyncio` module

## Installation

To clone the repository and access the directory, run:

```bash
git clone https://github.com/Henry4593/alx-backend-python.git
cd alx-backend-python/0x02-python_async_comprehension
```

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Project Structure

```plaintext
.
├── 0x02-python_async_comprehension
│   ├── 0-async_generator.py
│   ├── 1-async_comprehension.py
│   ├── 2-measure_runtime.py
│   └── README.md
```

## Files

### 0-async_generator.py

Defines a coroutine called `async_generator` that yields a random number between 0 and 10 asynchronously.

### 1-async_comprehension.py

Defines a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator`.

### 2-measure_runtime.py

Defines a coroutine called `measure_runtime` that measures the total runtime of executing `async_comprehension` four times in parallel using `asyncio.gather`.

## Usage

To run the scripts, use the following commands:

```bash
python3 0-async_generator.py
python3 1-async_comprehension.py
python3 2-measure_runtime.py
```

## Author

Joseph Otieno

## License

This project is licensed under the MIT License.