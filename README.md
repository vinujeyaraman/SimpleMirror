# Reverse Words in a String

A simple Python program that reverses every individual word in one or multiple lines of input while preserving the original word order. This project is an excellent beginner-friendly exercise for learning Python string manipulation, loops, list comprehensions, and user input handling.

---

## Features

- Reverse every word in a sentence
- Supports multiple lines of input
- Preserves the original word order
- Maintains spaces between words
- Uses Python list comprehensions for clean and efficient code
- Beginner-friendly and easy to understand

---

## Requirements

- Python 3.x

No external libraries are required.

---

## How It Works

The program:

1. Accepts the number of input lines.
2. Reads each line from the user.
3. Splits each line into individual words.
4. Reverses each word.
5. Prints the modified sentence while keeping the original word order.

---

## Example

### Input

```
Enter the number of lines of input: 2

Hello World
Python Programming
```

### Output

```
olleH dlroW
nohtyP gnimmargorP
```

---

## Example 2

### Input

```
ChatGPT is awesome
```

### Output

```
TPGtahC si emosewa
```

---

## Project Structure

```
.
├── reverse_words.py
├── README.md
└── LICENSE
```

---

## Code Overview

The program uses:

- `split()` to separate each sentence into words.
- List comprehensions to reverse each word efficiently.
- Slicing (`[::-1]`) to reverse strings.
- `" ".join()` to reconstruct the sentence with spaces.

Example:

```python
words = line.split()
reversed_words = [word[::-1] for word in words]
print(" ".join(reversed_words))
```

---

## Concepts Demonstrated

- Python strings
- String slicing
- Lists
- List comprehensions
- Loops
- User input
- String methods (`split()` and `join()`)

---

## Future Improvements

- Reverse the order of words instead of letters.
- Preserve multiple consecutive spaces.
- Read input from a text file.
- Save the output to a file.
- Build a graphical user interface (GUI).

---

## License

This project is licensed under the MIT License.

---

## Author

Created as a beginner-friendly Python project to practice string manipulation, list comprehensions, and fundamental programming concepts.
