==**uninitialized== variable**: A variable that has not been given a known value (has garbage value)
> “initialized” and “uninitialized” are not strict opposites

- Initialized = The object is given a known value at the point of definition.
- Assignment = The object is given a known value beyond the point of definition.
- Uninitialized = The object has not been given a known value yet.

**==Undefined== Behavior (UB)**: result of executing code whose behavior is not well-defined by the C++ language
symptoms:
- different results every time
- same incorrect results
- behaves inconsistently (sometimes produces the correct result, sometimes not)
- seems like it’s working but produces incorrect results later in the program
- crashes (immediately / later)
- works on some compilers but not others.
- works until you change some other seemingly unrelated code.

**implementation**: A specific compiler and the associated standard library it comes with

==**implementation-defined== behavior**: Behavior that is defined by the implementation 
>the compiler can choose a behavior that is efficient for a given platform, the compiler can choose a behavior that is efficient for a given platform

==**Unspecified== behavior**: behavior is left up to the implementation to define, but the implementation is not required to document the behavior