# Kotlin

## Kotlin Overview
  
- typed language
- compiled to bytecode and run on the JVM
- immutable first, mutable variables must be explicitly declared
- scalability - coroutines support and structured concurrency
- migration from Java - very smooth transition
- ecosystem and seamless interopability with Java libraries
  - gives access to masive ecosystem

## Basics

### Program entrypoint

```Kotlin
fun main() {
    println("Hello world!")
}
```

and with parameters:

```Kotlin
fun main(args: Array<String>) {
    println(args.contentToString())
}
```

### Functions

```Kotlin
fun sum(a: Int, b: Int): Int {
    return a + b
}
```

### Variables

```Kotlin
val a: Int = 1  // immediate assignment
val b = 2   // `Int` type is inferred
val c: Int  // Type required when no initializer is provided
c = 3       // deferred assignment
```

### Class

```Kotlin
class Shape

class Rectangle(var height: Double, var length: Double) {
    var perimeter = (height + length) * 2
}
```

### String Templates

```Kotlin
var a = 1
// simple name in template:
val s1 = "a is $a" 

a = 2
// arbitrary expression in template:
val s2 = "${s1.replace("is", "was")}, but now is $a"
```

### Loops

```Kotlin
fun maxOf(a: Int, b: Int): Int {
    if (a > b) {
        return a
    } else {
        return b
    }
}
```

Inlined Conditional:

```Kotlin
fun maxOf(a: Int, b: Int) = if (a > b) a else b
```

```Kotlin
val items = listOf("apple", "banana", "kiwifruit")
for (item in items) {
    println(item)
}
```

### When expression - Pattern Matching

```Kotlin
fun describe(obj: Any): String =
    when (obj) {
        1          -> "One"
        "Hello"    -> "Greeting"
        is Long    -> "Long"
        !is String -> "Not a string"
        else       -> "Unknown"
    }
```

### Ranges

```Kotlin
val x = 10
val y = 9
if (x in 1..y+1) {
    println("fits in range")
}   
```

### Type Check and casting

```Kotlin
fun getStringLength(obj: Any): Int? {
    if (obj !is String) return null

    // `obj` is automatically cast to `String` in this branch
    return obj.length
}
```

### Data Class

```Kotlin
data class Customer(val name: String, val email: String)
```

Dataclass provides following functionality:

- getters (and setters in case of vars) for all properties
- equals()
- hashCode()
- toString()
- copy()

### Filter

``` Kotlin
val positives = list.filter { x -> x > 0 }
// or replace `x` variable with `it`
val positives = list.filter { it > 0 }
```

### Presence in Collection

```Kotlin
if ("john@example.com" in emailsList) { ... }

if ("jane@example.com" !in emailsList) { ... }
```

### Read only Map

```Kotlin
val map = mapOf("a" to 1, "b" to 2, "c" to 3)

// access the key

println(map["key"])
map["key"] = value

// traverse
for ((k, v) in map) {
    println("$k -> $v")
}
```

### Range iteration

```Kotlin
for (i in 1..100) { ... }  // closed range: includes 100
for (i in 1 until 100) { ... } // half-open range: does not include 100
for (x in 2..10 step 2) { ... }
for (x in 10 downTo 1) { ... }
(1..10).forEach { ... }
```

### Null

```Kotlin
val files = File("Test").listFiles()

// shorthand
println(files?.size) // size is printed if files is not null

// If-not-null-else shorthand
// To calculate the fallback value in a code block, use `run`
val filesSize = files?.size ?: run {
    return someSize
}
println(filesSize)

// execute statement if null 
val email = values["email"] ?: throw IllegalStateException("Email is missing!")

// execute if not null
val emails = ... // might be empty
val mainEmail = emails.firstOrNull() ?: ""
```
