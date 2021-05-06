# Escape Sequences in Python

Character escaping is one of the most common and trivial nuance of any programming language. Python is no exception to this. However, Python does have some of its own unique character escaping sequences which sometimes makes working with Python a very notorious job.<br>"*Unicode is the one to be blamed!*"

But what the heck is **Character escaping**?<br>Character escaping is a part of programming syntax which interprets those special characters differently when used with an escape character. In many programming languages, an escape character also forms some escape sequences which are referred to as control characters. For example, line break has an escape sequence of `\n`. 

## List of escape characters

Like many other languages, Python also uses `\` (backslash) as an escape character. In the below table, the characters suffixing the backslash together form an escape sequence.

| Escape Sequence  | Description                                                                                                                             | Practical example                                                                    |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| \\\\               | Escapes backslash                                                                                                                       | When working with Windows file paths                                                 |
| \\'               | Escapes single quote                                                                                                                    | When working with text which is quoted in single quotes and has the same quote in it |
| \\"               | Escapes double quotes                                                                                                                   | Similar to single quotes but replaced with double quotes                             |
| \a               | Rings an alert sound                                                                                                                    | N/A                                                                                  |
| \b               | Works as backspace, deleting the previous character                                                                                     | N/A                                                                                  |
| \f               | ASCII form feed (kinda obsolete) means advance downward to the next "page". Basically it means to take control at starting of next page | N/A                                                                                  |
| \n               | ASCII line feed (new line) means to advance downward to the next "line". Basically it means to take control at starting of next line    | While printing a multi-line statement                                                |
| \N{UNICODE NAME} | Renders an Unicode character from the Unicode DB           | While printing an unicode characters from a file.                                    |
| \r               | ASCII carriage return means to advance from the beginning of the same line                                                              | This is usually used for rendering an animation sequence                             |
| \t               | ASCII horizontal tab                                                                                                                    | This can be used for adding indents while rendering text                             |
| \v               | ASCII vertical tab (same as form feed)                                                                                                  | N/A                                                                                  |
| \uXXXX           | Character with 16-bit hex value XXXX. Exactly four hexadecimal digits are required                                                      | N/A                                                                                  |
| \UXXXXXXXX       | Character with 32-bit hex value XXXXXXXX. Exactly eight hexadecimal digits are required                                                 | N/A                                                                                  |
| \oXXX            | Renders character based on its octal value                                                                                              | N/A                                                                                  |
| \xXX             | Renders character based on its hex value                                                                                                | N/A                                                                                  |

Click **[here](https://www.unicode.org/emoji/charts-12.0/emoji-list.html#1f600)** to check the Unicode Database.
