# Calculator with Pytest

This is a simple Python calculator project that implements basic arithmetic operations, along with a comprehensive test suite written using `pytest`.

## 📌 Features

- Addition
- Subtraction
- Multiplication
- Division (with division-by-zero check)
- Power
- Modulo (with modulo-by-zero check)

## ✅ Technologies Used

- Python 3.10+
- Pytest for unit testing

## 📁 Project Structure

```
calculator/
├── calculator.py          # Implementation of functions
└── test_calculator.py     # Unit tests using pytest
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/calculator-tests.git
cd calculator-tests
```

### 2. Install dependencies

Make sure you have Python installed. Then install `pytest`:

```bash
pip install pytest
```

### 3. Run the tests

```bash
python -m pytest
```

Or simply:

```bash
pytest
```

(if it's available in your PATH)

## 🧪 Sample Test Case

```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```

## 📄 License

This project is open-source and free to use under the MIT License.
