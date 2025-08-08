---
layout: post
title:  "CPP Notes"
date:   2025-05-2025
---

# Initialization
It is recommended to initialize value upon creation with a values. We can choose to add specific value, or default zero initialization. Multiple values can be initialized at the same time 

```c
// default initialization without value
int width
int x, y;
```

## Copy-Initialization
Initialization inherited from C language. It copies the value to the variable. Not commonly used because it is less efficient form of initialization. It is best practice to initialize a single variable on a line.

```c
int width = 5; // copy-initialization
```

## Direct-initialization
Introduced for more efficient initialization of complex objects. It was superseded by direct-list-initialization.

```c
int d { 7 };   // direct-list-initialization (initial value in braces)
```

## Direct List Initialization
Modern way to initialize objects in C++. One of main benefits of this initialization is due to _narrowing conversions_. 

If you try to list-initialize a variable using a value that the variable can not safely hold, compiler will raise an error. Narrowing convention only applies to the list initialization, any subsequent assignment is allowed.

```c
int width { 5 };    // direct-list-initialization of initial value 5 into variable width (preferred)

int height = { 6 }; // copy-list-initialization of initial value 6 into variable height (rarely used)

int w1 { 4.5 }; // compile error: list-init does not allow narrowin conversion - fraction can't be saved in int

w1 = 4.5;  // assignemnt is allowed

int width {}; // value-initialization / zero-initialization to value 0

int x ( 5 ), y (6)
```

# IOSTREAM

iostream is used by importing it as a library

```c
#include <iostream>
```

## std::count
Character output prints characters to console as standard output. Characters are not directly written to standard output, but they are buffered and flushed periodically.

### Newline
There are 2 common ways to move cursor to next line. 

- `std::endl` - adds a new line character and flushes the buffer. Useful when we want to explicitly flush the buffer.
- `"\n"` - adds a new line character without flushing the buffer. More efficient than `std::endl`. It is preferred to use `"` and helps avoid inadvertent multicharacter literals.

## std::cin
std::cin (which stands for “character input”) reads input from keyboard. Typically used to input data from console to variable

```c
    std::cout << "Hello " << "World" << std::endl; // print Hello world! to console
    std::cout << "Enter your age:"
    
    int x {};
    std::cin >> x;
```

# Functions

Simple example of using functions.

```c
#include <iostream>

int getUserInput() {
    std::cout << "Enter an integer: ";
    int input;
    std::cin >> input;

    return input;
}


int main() {
    std::cout << "Wellcome to first program" << "\n";

    const int x { getUserInput()};
    const int y { getUserInput() };

    std::cout << x << " * " << y << " = " << x * y << "\n";

    return EXIT_SUCCESS;
}
```

## Value Parameters
Value parameters are passed to a function by value. They are copied into the matching parameter.

```c
#include <iostream>

void printValues(int x, int y)
{
    std::cout << x << '\n';
    std::cout << y << '\n';
}
```

# Preprocessor
Preprocessor accepts code files and produces a translation unit. Translation unit is prepared code that is the input to the compiler. Some tasks done by the preprocessor are:

- Strips out comments
- Ensures each file ends with a new line
- Processes _#include_

## Preprocessor directive
Also called a directive, it is an instruction that start `#` and ends with a new line character (`/n`) instead of semicolon `;`. These directives tell the preprocessor to perform certain text manipulation tasks.

## `#include`
The `#include` directive is replaced by the preprocessor with the content of included file.

## `#define`
`#define` creates a macro that defines how input text is converted into replacement text.

```c
#include <iostream>

#define COLOR "green"

int main()
{
    std::cout << "My name is: " << MY_NAME << '\n';

    return 0;
}
```

# Header Files
Typically header files are used to propagate one or more several declaration into a code file. They should follow name of the cpp implementation. Following ODR (One Definition Rule), no implementation should be defined in the header file.

```c
// mathutil.h
int multiply(int x, int y);

// mathutil.cpp
#include "mathutil.h"

int multiply(int x, int y) {
    return x * y;
}

//main.cpp
#include <iostream>
#include "mathutil.h"

int main() {
    int x { 2 }
    int y { 4 }
    std::cout << x << " * " << y << " = " << multiply(x, y) << "\n";

    return 0;
}
```

Header files can contain another header files.

```c
// file: foo.h 
#include <string_view> // required to use std::string_view

std::string_view getApplicationName(); // std::string_view used here
```

## Header File Best Practices
- Header guards should be always included
- No variables are defined
- Has the same name as its associated c++ file
- Contains only declaration of function contained in its associated cpp file
- Includes all header files for functionality it needs
- Includes only what it requires
- No .cpp files should be included
- Includes documentation on what something does and how to use the header. Describe how the code works in source files.

# Constants
Constant is a named variable that can not be changed. There is no specific naming convention. 

## Best Practice
- Variable should be constant wherever possible
- Values for parameters should not be constants

```c
const int size { 10 }
```

# Literals
Meaning of literal values can not be redefined. For example, value `3` can never be different.

Literal values have their type. It is typically deduced from the value. Sometimes we need to change the default type assigned to the literal. This can be done with Suffixes.

```c
    std::cout << 5u << '\n'; // 5u is type unsigned int
```

## C Strings
C Strings are string literals placed between two *double* (`"`)quotes. We use single quotes (`'`) for char literals. Strings are not fundamental type in C++. They are inhereted from C language and are called C strings.

- Each string terminates with a special character, *null terminator* `\0`.
- Strings are constant types created at the beginning 

# Control Flow

## `if`
```c
if (condition) {
   true_statement;
}
else {
    false_statement;
}
```

Single line statements can avoid parenthesis.

```c
if (age >= minDrinkingAge) purchaseBeer();
else std::cout << "No drinky for you\n".
```

## `switch`
Switch expression must evaluate to integral type.

```c
void printDigitName(int x)
{
    switch (x)
    {
    case 1:
        std::cout << "One";
        break;
    case 2:
        std::cout << "Two";
        break;
    case 3:
        std::cout << "Three";
        break;
    default:
        std::cout << "Unknown";
        break;
    }
}
```

## `while`

While uses loop variable to identify terminating condition. It always should be a signed as unsigned integers can lead to unpredictable results.

```c
    int count{ 1 };
    while (count <= 10)
    {
        std::cout << count << ' ';
        ++count;
    }

    std::cout << "done!\n";
```

Sometime we use infinite loops intentionally.

```c
while (true)
{
  // this loop will execute forever
}
```

## `do while`
```c
 do
    statement; // can be a single statement or a compound statement
while (condition);
```

## `for`
Statement `for` is prefered to while when there is obvious loop variable.

```c
for (init-statement; condition; end-expression)
   statement;
```

It is possible to emit any or all for statements.

```c
int i{ 0 };
for ( ; i < 10; ) // no init-statement or end-expression
{
    std::cout << i << ' ';
    ++i;
}
```
