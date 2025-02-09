mostly refer to: spaces, tabs, newlines

Some language elements must be whitespace-separated

Quoted text takes the amount of whitespace literally
> Newlines are not allowed in quoted text

line length for formatting:
>appropriate length of line: 80 char at most


``` c++
int main()
{
    std::cout << "This is a really, really, really, really, really, really, really, "
        "really long line\n"; // one extra indentation for continuation line

    std::cout << "This is another really, really, really, really, really, really, really, "
                 "really long line\n"; // text aligned with the previous line for continuation line

    std::cout << "This one is short\n";
}
```

If a long line is split with an operator (eg. << or +), the operator should be placed at the beginning of the next line

aligning values or comments or adding spacing between blocks of code

 [clang-format](https://clang.llvm.org/docs/ClangFormat.html) is a popular automatic formatter
 
A **style guide** is a concise, opinionated document containing (sometimes arbitrary) programming conventions, formatting guidelines, and best practices
- [C++ Core Guidelines](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines), maintained by Bjarne Stroustrup and Herb Sutter.
- [Google](https://google.github.io/styleguide/cppguide.html).
- [LLVM](https://llvm.org/docs/CodingStandards.html)
- [GCC/GNU](https://gcc.gnu.org/codingconventions.html)

