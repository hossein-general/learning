# Initialization and Assignment
copy-assignment: copies the value on the right-hand side of the = operator to the variable on the left-hand side of the operator
initialization: process of specifying an initial value for an object
initializer: the syntax used to initialize an objec
indeterminate value: a value that is not predictable, sometimes called a “garbage value”
narrowing conversions: using a value that the variable can not safely hold

initialization forms:
1. Default:
	- **==default-initialization==** (no initializer) (int a;): most cases leaves variable with indeterminate value
2. Traditional initilization forms:
	- ***==copy-initialization==*** (int b = 5;): copies the value on the right-hand side of the equals into the variable being created on the left-hand side / when implicitly copied
		copy-initialization initialization was inherited from the C language
	* ***==direct-initialization==*** (int c ( 6 );): allow for more efficient initialization of complex objects 
3. Modern initialzation forms (preferred):
	- ***==list-initialization==*** (int d { 7 }; int d = {7};):
		> disallows narrowing conversions
		>  also provides a way to initialize objects with a list of values
			
		-  ***direct***: `int width { 5 };`
			> direct-list-initialization of initial value 5 into variable width (preferred)
			
		- **_copy_**: `int height = { 6 };`
			> copy-list-initialization of initial value 6 into variable height (rarely used)
			
	- ***==value-intialization==*** (`int e {};`): special form of list-initialization (using an empty set of braces)
		> implicitly initialize the variable to zero (or whatever value is closest to zero for a given type)
			
	- ***==zero-initialization==***: value-initialization in cases where zeroing occurs

other:
Aggregate initialization (see 13.8 -- Struct aggregate initialization).
Reference initialization (see 12.3 -- Lvalue references).
Static-initialization, constant-initialization, and dynamic-initialization (see 7.8 -- Why (non-const) global variables are evil).

>int x {};      // value initialization
std::cin >> x; // we're immediately replacing that value so an explicit 0 would be meaningless

instantiation: means a variable has been created (allocated) and initialized (includes default initialization)
instance: An instantiated object (Most often applied to class type objects)

`[[maybe_unused]]`: allows us to tell the compiler that we’re okay with a variable being unused





