# ThreadingVsMultiprocessing

## Overview
This project demonstrates the use of **threading** and **multiprocessing** in Python through two key scripts:

1. `filesorter.py` - A multi-threaded file sorter that organizes files by their extensions.
2. `factorize.py` - A multiprocessing-based number factorization tool that compares synchronous and parallel execution.

## Features
- **Multi-threaded File Sorting**: Organizes files from a specified directory into subfolders based on their extensions using threading.
- **Multiprocessing Factorization**: Computes factors of numbers using both synchronous and parallel processing.
- **Command-line Interface**: Allows users to specify input and output directories for sorting.
- **Performance Comparison**: Measures execution time for both synchronous and parallel processing.

## Installation
Ensure you have Python 3 installed. Clone the repository and navigate to the project folder:

```sh
git clone https://github.com/paulmusquaro/ThreadingVsMultiprocessing.git
cd ThreadingVsMultiprocessing
```

## Usage

### File Sorter
Sorts files in a directory by their extensions.

```sh
python filesorter.py --source <path_to_source_directory> --output <path_to_output_directory>
```

Example:
```sh
python filesorter.py --source ./downloads --output ./sorted_files
```

If no `--output` directory is specified, files will be sorted into the `dist` folder.

### Factorization
Calculates factors of a list of numbers both synchronously and in parallel using multiprocessing.

Run the script:
```sh
python factorize.py
```
The script will output the results and execution time for both methods.

## Dependencies
No external dependencies are required as the project uses only Python's standard library.

## License
This project is licensed under the MIT License.
