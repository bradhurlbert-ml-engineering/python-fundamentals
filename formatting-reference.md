# **Python f-string Formatting Cheat Sheet**

---

## **NUMBERS**

### **Decimal Places:**
```python
value = 3.14159

print(f"{value:.2f}")    # 3.14 (2 decimals)
print(f"{value:.3f}")    # 3.142 (3 decimals)
print(f"{value:.0f}")    # 3 (no decimals, rounds)
```

### **Thousands Separator:**
```python
number = 1234567

print(f"{number:,}")       # 1,234,567
print(f"{number:,.2f}")    # 1,234,567.00 (with decimals)
```

### **Percentage:**
```python
rate = 0.157

print(f"{rate:.1%}")     # 15.7%
print(f"{rate:.2%}")     # 15.70%
print(f"{rate:.0%}")     # 16%
```

### **Scientific Notation:**
```python
big = 1234567890

print(f"{big:e}")        # 1.234568e+09
print(f"{big:.2e}")      # 1.23e+09
```

### **Padding with Zeros:**
```python
number = 7

print(f"{number:02d}")   # 07 (2 digits)
print(f"{number:03d}")   # 007 (3 digits)
print(f"{number:05d}")   # 00007 (5 digits)
```

---

## **ALIGNMENT & WIDTH**

### **Left, Right, Center:**
```python
text = "Brad"

print(f"{text:<10}")     # "Brad      " (left align, 10 chars)
print(f"{text:>10}")     # "      Brad" (right align)
print(f"{text:^10}")     # "   Brad   " (center)
```

### **With Fill Character:**
```python
text = "Brad"

print(f"{text:*<10}")    # "Brad******" (fill with *)
print(f"{text:=>10}")    # "======Brad"
print(f"{text:-^10}")    # "---Brad---"
```

### **Numbers with Alignment:**
```python
number = 42

print(f"{number:>5}")    # "   42" (right align, 5 chars)
print(f"{number:<5}")    # "42   " (left align)
print(f"{number:^5}")    # " 42  " (center)
```

---

## **SIGN DISPLAY**

```python
pos = 42
neg = -42

print(f"{pos:+}")        # +42 (always show sign)
print(f"{neg:+}")        # -42

print(f"{pos: }")        # " 42" (space for positive)
print(f"{neg: }")        # "-42"
```

---

## **BINARY, OCTAL, HEX**

```python
number = 255

print(f"{number:b}")     # 11111111 (binary)
print(f"{number:o}")     # 377 (octal)
print(f"{number:x}")     # ff (hex lowercase)
print(f"{number:X}")     # FF (hex uppercase)
print(f"{number:#x}")    # 0xff (with prefix)
```

---

## **COMBINED FORMATTING**

### **Currency:**
```python
price = 1234.567

print(f"${price:,.2f}")           # $1,234.57
print(f"${price:>10,.2f}")        # " $1,234.57" (right align)
print(f"${price:<10,.2f}")        # "$1,234.57 "
```

### **Tables:**
```python
# Name alignment with width
name = "Brad"
age = 35
salary = 150000

print(f"{name:<10} {age:>3} ${salary:>10,}")
# Output: "Brad         35   $150,000"
```

---

## **DATES & TIMES**

```python
from datetime import datetime

now = datetime.now()

print(f"{now:%Y-%m-%d}")           # 2026-02-11
print(f"{now:%Y/%m/%d}")           # 2026/02/11
print(f"{now:%m/%d/%Y}")           # 02/11/2026
print(f"{now:%B %d, %Y}")          # February 11, 2026
print(f"{now:%A}")                 # Tuesday
print(f"{now:%H:%M:%S}")           # 20:45:30 (24-hour)
print(f"{now:%I:%M %p}")           # 08:45 PM (12-hour)
print(f"{now:%Y-%m-%d %H:%M}")     # 2026-02-11 20:45
```

---

## **QUICK REFERENCE TABLE**

| Format | Example | Output |
|--------|---------|--------|
| `:.2f` | `f"{3.14159:.2f}"` | `3.14` |
| `:,` | `f"{1234567:,}"` | `1,234,567` |
| `:.1%` | `f"{0.157:.1%}"` | `15.7%` |
| `:03d` | `f"{7:03d}"` | `007` |
| `:<10` | `f"{'Brad':<10}"` | `Brad      ` |
| `:>10` | `f"{'Brad':>10}"` | `      Brad` |
| `:^10` | `f"{'Brad':^10}"` | `   Brad   ` |
| `:+` | `f"{42:+}"` | `+42` |
| `:b` | `f"{255:b}"` | `11111111` |
| `:x` | `f"{255:x}"` | `ff` |

---

## **COMMON REAL-WORLD PATTERNS**

### **Money:**
```python
amount = 1234.56
print(f"${amount:,.2f}")          # $1,234.56
```

### **Progress:**
```python
completed = 45
total = 180
percent = completed / total
print(f"{percent:.1%} complete")  # 25.0% complete
```

### **File Sizes:**
```python
bytes = 1234567
mb = bytes / 1024 / 1024
print(f"{mb:.2f} MB")             # 1.18 MB
```

### **Table Formatting:**
```python
print(f"{'Name':<15} {'Age':>5} {'Salary':>12}")
print(f"{'Brad':<15} {35:>5} ${150000:>11,}")
print(f"{'Alice':<15} {28:>5} ${95000:>11,}")

# Output:
# Name              Age       Salary
# Brad               35     $150,000
# Alice              28      $95,000
```

### **Scientific Data:**
```python
value = 0.0001234
print(f"{value:.2e}")             # 1.23e-04
```

### **Coordinates:**
```python
lat = 32.2217
lon = -110.9265
print(f"({lat:.4f}, {lon:.4f})")  # (32.2217, -110.9265)
```

---

## **QUICK SYNTAX BREAKDOWN**

```python
f"{variable:fill align width .precision type}"
         ↓    ↓     ↓     ↓         ↓
         *    <    10    .2         f

# Examples:
f"{value:.2f}"       # 2 decimal places
f"{value:10.2f}"     # width 10, 2 decimals
f"{value:>10.2f}"    # right align, width 10, 2 decimals
f"{value:*>10.2f}"   # fill with *, right align, width 10, 2 decimals
```

---

## **SAVE THIS REFERENCE:**

**Copy this into a file:** `python-fundamentals/formatting-reference.md`

You'll refer to it constantly when you need specific formatting.

---

## **MOST USED (90% of the time):**

```python
# These are what you'll actually use most:

f"{variable}"           # Basic (use this most)
f"{variable:.2f}"       # 2 decimals
f"{variable:,}"         # Thousands separator
f"{variable:.1%}"       # Percentage
f"{variable:<10}"       # Left align with width