# Basic Knowledge
**porting** (related to portable applications)
**instruction set** (languages that a cpu understands)
**binary digit** (bit)
**CPU family** (instruction set architecture (ISA))
**Assembler** (assembely to machine)
**compiling and interpreting** (translate to machine language)

programming languages:    
- Machine Lnaguage
- Assembly
- high level 

important points:
- Rules
- Best Practice
- Warning

**ANSI** (American National Standard Institute)
**ANSI C** (C89 standard)
**C90**
**compilers** (ANSI C/C90 compliant)
**ISO** (in 1999 (C99))

* C++ standardized in 1998
* C++ updated in 2003 (informally: C++03)
* C++ updates (C++11, C++14, C++17, C++20, C++23)

**monospace font** (unambigous fixed-width font) (where all symbols have the same width)
**compiler first step** (checking rules)
**compiler second step**: translate c++ code into machine languag
**object names**: name.obj, name.o
linker (combine all the object files and create a file like "executable") (cross-file dependency check)
linking (the thing that linker does)
library file (collection of precompiled code)
compiler extensions (compiler-specific behaviors)
your program is ill-formed (done something that definitively violates the rules of the language)
diagnostic message
diagnostic error
diagnostic warning
increasing warning level and changing compiler extension to standard c++ (C/C++ > General tab and set Warning level to Level4 (/W4))
enable signed/unsigned conversion warnings at warning level 4 (C/C++ > Command Line tab, under Additional Options, add /w44365)
compile standard library headers at warning level 3 (instead of 4) (C/C++ > External Includes tab, set External Header Warning Level to Level3)
treat warnings as errors (C/C++ > General tab and set Treat Warnings As Errors to Yes)
select a language standard (Configuration Properties > C/C++ > Language)
