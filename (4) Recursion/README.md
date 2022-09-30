# Recursion

Recursion is not any Data Structure or any Algorithm. But it is important as it is used in many Data structures and Algorithms.

Recursion is used in `backtracking`

Recursion function calls itself:

```python
# Simplest Recursion function
def my_func():
    my_func()
```

Now the question remains, why we use `recursion`? What is the benefit of using this?:

- If it helps to find the solution to a problem when we convert the problem into more small problem ,
  then we will use recursion.

Let's get the concept of this `recursion` with an Example:

We all know about `factorial`, right? if $n$ is an integer number then the factorial of $n$ will be writen as $n!$.
That means, multiplication of all the numbers from 1 to $n$.

$n! = n \times (n - 1) \times (n - 2) \times ... \times 3 \times 2 \times 1$

In the same way,

$(n - 1)! = (n - 1) \times (n - 2) \times ... \times 3 \times 2 \times 1$

Now we can write $n!$ as -

$n! = n \times (n - 1)!$

This concludes that, factorial of any number is the multiplication of the factorial of its previous number.

$f(n) = n \times f(n - 1);$ for all $n > 0$

This function is called `recursive` function.
