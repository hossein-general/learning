==Expression== vs ==Statement==: [Expressions](http://docs.python.org/reference/expressions.html) only contain [identifiers](http://docs.python.org/release/2.5.2/ref/identifiers.html), [literals](http://docs.python.org/release/2.5.2/ref/literals.html) and [operators](http://docs.python.org/release/2.5.2/ref/operators.html), where operators include arithmetic and boolean operators, the function [call operator](https://docs.python.org/3/reference/expressions.html?highlight=subscriptions#calls) `()` the [subscription operator](https://docs.python.org/3/reference/expressions.html?highlight=subscriptions#grammar-token-subscription) `[]` and similar, and can be reduced to some kind of "value"
(An `expression` evaluates to a value. A `statement` does something)

```python
>>> x + 2         # an expression
>>> x = 1         # a statement 
>>> y = x + 1     # a statement
>>> print y       # a statement (in 2.x)
2
```
