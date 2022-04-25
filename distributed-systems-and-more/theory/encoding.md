# Encoding

# Text

### UTF-8
size: 1-4 bytes per character

2,097,152 code points (2^21), more than enough to cover the current 1,112,064 [Unicode](https://www.twilio.com/docs/glossary/what-is-unicode) code points.

Unicode can be understood as a character set and UTF-8 is the encoding of this set

UTF-8 is a “variable-width” encoding standard. This means that it encodes each code point with a different number of bytes, between one and four. As a space-saving measure, commonly used code points are represented with fewer bytes than infrequently appearing code points.

The first UTF-8 byte signals how many bytes will follow it. Then the code point bits are “distributed” over the following bytes.

UTF-8 has been the most common encoding for the World Wide Web since 2008. As of March 2022, UTF-8 accounts for on average 97.7% of all web pages.

**Backwards Compatibility with ASCII**
UTF-8 uses one byte to represent code points from 0-127. These first 128 Unicode code points correspond one-to-one with [ASCII](https://en.wikipedia.org/wiki/ASCII) character mappings, so ASCII characters are also valid UTF-8 characters.

### ASCII
size: 1 byte

ASCII was the most common character encoding on the [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web "World Wide Web") until December 2007, when [UTF-8](https://en.wikipedia.org/wiki/UTF-8 "UTF-8") encoding surpassed it; UTF-8 is [backward compatible](https://en.wikipedia.org/wiki/Backward_compatible "Backward compatible") with ASCII.

## References
- 1 UTF-8, (17-03-2022) - https://www.twilio.com/docs/glossary/what-utf-8 
- 2 ASCII, (17-03-2022) - https://en.wikipedia.org/wiki/ASCII
- 3 Unicode, (17-03-2022) https://www.twilio.com/docs/glossary/what-is-unicode
