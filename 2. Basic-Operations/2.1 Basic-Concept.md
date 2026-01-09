# Basic Operations

In programming, an operation is an action performed on data to produce a result.
Data by itself does nothing—**operations are what make programs useful**.

For example:

- Adding two numbers

- Comparing values

- Updating a variable

- Checking a condition

All of these are operations.

Think of **data** as raw information and **operations** as the tools that work on it.

``` python
a = 10
b = 5
result = a + b  # 15
```

**Operations Enable Program Logic:**

Logic in a program is created by combining operations.

``` python
score = 75

passed = score >= 40
```

The comparison operation (`>=`) converts raw data into a meaningful outcome (`True` or `False`), which can then control program behaviour.

> [!NOTE]
> Operations are actions that work on data to create results, making programs dynamic, logical, and capable of solving real problems.

## Types of Operations

There are five types of operations in Python:

- **Arithmetic Operations:** Arithmetic operations are used to perform mathematical calculations such as **addition**, **subtraction**, **multiplication**, and **division**.

- **Assignment Operations:** Assignment operations are used to **store values in variables** and **update existing values**.

- **Comparison Operations:** Comparison operations are used to **compare two values**.

- **Logical Operations:** Logical operations are used to **combine** or **modify Boolean values**.

- **Bitwise Operations:** Bitwise operations work on the **binary representation (bits)** of numbers instead of their actual values.

## Using Parentheses for Clarity

Parentheses allow you to control the order of evaluation, regardless of precedence.

``` pyhton
result = (10 + 2) * 3
```
- `10 + 2` is evaluated first

- Result becomes `36`

**Using Parentheses:**
- Makes code easier to read
- Prevents logical mistakes
- Is considered a best practice

### Using Associativity

**Associativity** decides the direction of evaluation when operators have the **same precedence**.

``` python
value = 20 - 5 - 3
```

Python evaluates from **left to right**:

``` python
(20 - 5) - 3 = 12
```

Understanding associativity helps avoid confusion in longer expressions.

> [!NOTE]
> Operator precedence and associativity determine how expressions are evaluated; using parentheses improves clarity and prevents bugs.

## Type Conversion in Operations

While performing operations, Python sometimes needs to **convert one data type into another** to complete the expression.

This process is called **type conversion**.

**Implicit Type Conversion:**

Python **automatically converts data types** when it is **safe to do so**.

``` python
add = 7 + 2.5
print(add)  # 9.5
```
- `7` (integer) is converted to `7.0` (float)

- This prevents loss of precision

**Explicit Type Conversion:**

Sometimes, you must **convert types manually** using **built-in functions**:

- `int()`
- `float()`
- `str()`

``` python
num = "10"
result = int(num) + 5
print(result)   # 15
```

Explicit conversion gives you **full control** over how data is handled.

> [!NOTE]
> Type conversion allows Python to safely and correctly perform operations between different data types, either automatically or through explicit control.
