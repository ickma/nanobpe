# NanoBPE

NanoBPE is an imitation of [micrograd](https://github.com/karpathy/micrograd), designed to explore Byte Pair Encoding (BPE) and its potential applications beyond natural language processing, particularly in fields like recommendation systems and supply chain optimization.

## Features

- Implements a basic Byte Pair Encoding (BPE) algorithm.
- Simple and lightweight, inspired by micrograd’s minimalistic approach.
- Flexible tokenization for experimenting with different types of data.

## Installation

NanoBPE is still under development and hasn't been packaged for PyPI yet. To use it, you'll need to clone the repository and append the project directory to your Python path.

```bash
git clone https://github.com/ickma/nanobpe.git
```

## Usage
Since NanoBPE isn’t available as a package, you need to import it manually in your Python environment (e.g., Jupyter Notebook or any Python script):

```python
import sys
sys.path.append('path/to/nanobpe')
from nanobpe.base import BaseTokenizer
```
Once imported, you can initialize the BaseTokenizer and start experimenting with Byte Pair Encoding in your own applications.


## Example
```# Example code to initialize and use BaseTokenizer
tokenizer = BaseTokenizer()
tokenizer.train("your text here")
tokens = tokenizer.encode("your text here")
print(tokens)
```

# Future work
Future Work

I aim to explore the potential of using a BPE-like algorithm in areas beyond NLP, such as:

+ Recommendation Systems: Investigating how BPE can be adapted to improve content or product recommendations.
+ Supply Chain Optimization: Experimenting with subword tokenization in supply chain models, potentially improving demand forecasting or inventory management.

I will continue to develop this repository sporadically, and contributions or suggestions are welcome!