**iostream header**: `#include <iostream>`

###### COUT
`std::cout`: (character out) *variable*, used with insertion operator
**insertion operator**: `<<`

###### endl
`std::endl`: (end line) 
1. outputs a new line
2. flushes the buffer (slow)

> `endl` is inefficient (it creates a new line and flushes the buffer)

###### buffered input/output
==**Buffered output**==: output is typically not sent to the console immediately. Instead, the requested output “gets in line”, and is stored in a region of memory set aside to collect such requests (called a **buffer**). Periodically, the buffer is **flushed**, meaning all of the data collected in the buffer is transferred to its destination (in this case, the console).
==**Unbuffered output**==: each individual output request is sent directly to the output device


###### \n
`\n`: new line without flushing buffer

> `\n` is treated as a single linefeed (LF) character (ASCII = 10)
> its conventionally single quoted

###### cin
`std::cin`: *variable*, used with *extraction operator*
two stage process:
1. inputted characters are added to the end of an input buffer (inside `std::cin`) (the submit enter is also stored as `\n`)
2. the extraction operator (`>>`) removes characters from end of the front of the input buffer, converts them into value, [copy-assigns](Initialization%20and%20Assignment.md) to associated variable
>  it is also possible to input more than one value on a single line (values should be separated by white space (spaces, tabs, or new lines))

**extraction operator**: `>>`
> how extraction operator works:
> 1. removing leading whitespaces
> 2. if buffer is empty, it waits for user (leading white spaces are discarded again)
> 3. extracts characters  until it encounters:
> 	- new line 
> 	- a non valid character for the variable
>
> resault:
>- if any character extracted (extraction successful), it converts into a value, [copy-assigns](Initialization%20and%20Assignment.md) to the variable
>- if no character was able to extract (extraction failed), the object beeing extracted to  is copy-assigned the value 0, and any future extraction will immediately fail (until `std::cin` is clear)

***FIFO***: (first in, first out) Adding data to the end of a buffer and removing it from the front

