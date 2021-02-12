# What are the advantages of NumPy over regular Python lists?

NumPy's arrays are more compact than Python lists -- a list of lists as you describe, in Python, would take at least 20 MB or so, while a NumPy 3D array with single-precision floats in the cells would fit in 4 MB. Access in reading and writing items is also faster with NumPy.

Maybe you don't care that much for just a million cells, but you definitely would for a billion cells -- neither approach would fit in a 32-bit architecture, but with 64-bit builds NumPy would get away with 4 GB or so, Python alone would need at least about 12 GB (lots of pointers which double in size) -- a much costlier piece of hardware!

The difference is mostly due to "indirectness" -- a Python list is an array of pointers to Python objects, at least 4 bytes per pointer plus 16 bytes for even the smallest Python object (4 for type pointer, 4 for reference count, 4 for value -- and the memory allocators rounds up to 16). A NumPy array is an array of uniform values -- single-precision numbers takes 4 bytes each, double-precision ones, 8 bytes. Less flexible, but you pay substantially for the flexibility of standard Python lists!

[link] (https://stackoverflow.com/questions/993984/what-are-the-advantages-of-numpy-over-regular-python-lists)
