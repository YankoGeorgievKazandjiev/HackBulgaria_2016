## Simplify fractions

Implement a function, called ```simplify_fraction(fraction)``` that takes a tuple of the form ```(nominator, denominator)``` and simplifies the fraction.

The function should return the fraction in it's irreducible form.

For example, a fraction ```3/9``` can be reduced by dividing both the nominator and the denominator by 3. We end up with ```1/3``` which is irreducible.

### Signature

```python
def simplify_fraction(fraction):
    # Implementation
```

### Test examples

```
>>> simplify_fraction((3,9))
(1,3)
>>> simplify_fraction((1,7))
(1,7)
>>> simplify_fraction((4,10))
(2,5)
>>> simplify_fraction((63,462))
(3,22)
```

## Sort array of fractions

Implement a function, called ```sort_fractions(fractions)``` where ```fractions``` is a list of tuples of the form ```(nominator, denominator)```.

Both the nominator and the denominator are integers.

The function should return the list, sorted in increasing order.

### Signature

```python
def sort_fractions(fractions):
    # Implementation
```

### Test examples

```
>>> sort_fractions([(2, 3), (1, 2)])
[(1, 2), (2, 3)]
>>> sort_fractions([(2, 3), (1, 2), (1, 3)])
[(1, 3), (1, 2), (2, 3)]
>>> sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)])
[(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]
```
