# Stream Editor - `sed`

Sed is a classic UNIX tool that can apply changes on a strem. That is typically a stream passed of a text file.

## Replace pattern

The basic use is to replace a word for another word:

`sed 's/<old>/<new>/' <file>`

If we don't know exactly the pattern we want to change, we can also use regex pattern matching e.g. `[a-z]*`. In this case `&` can be used to represent the text matching the pattern. This enables us for example surround the pattern with the paranthesis.

`sed -r 's/[a-z]*/&/' <file>`

Above command uses extended regular expression by setting the flag `-r`. The command surrounds the first word of the line with paranthesis.

## Usage

By default sed prints out its output. This can be changed.

`sed -i 's/hello/world/' file.txt` - changes the input file

## Examples

| comand  | description   |
| - | - |
| `sed '30,35d' input.txt > output.txt` | deletes lines between line 30 and 35 |
| `sed -n '/<to_match>/,$p' files.txt | wc -l` | print count of lines after match |

## References

[1] GNU sed; <https://www.gnu.org/software/sed/manual/sed.html>
[2] Sed; <https://www.grymoire.com/Unix/Sed.html>