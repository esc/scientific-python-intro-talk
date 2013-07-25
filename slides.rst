Introduction
============

About Python
------------

* General purpose programming language
* Alive since 1991
* One of the 4 programming languages uese at google

.. image:: images/python-logo.pdf
    :scale: 50%

Python is Slow
--------------

* Python is an interpreted language
* It is comparatively slow...

Example in C
------------

.. code-block:: c

    #include <stdlib.h>

    main(){
        int i, n;
        int* array;
        n = 10000000;
        array = malloc(n * sizeof(int));
        for (i = 0 ; i < n ; i++){
            array[i] = i * i;
        }
    }

So how fast is it?
-------------------

.. code-block:: console

    $ time ./example
    ./example  0.12s user 0.03s system 96% cpu 0.162 total

The Equivalent in Python
------------------------

.. code-block:: pycon

    >>> %time L = [i*i for i in xrange(10000000)]
    CPU times: user 4.15 s, sys: 0.18 s, total: 4.33 s
    Wall time: 4.43 s

Enter Numpy
-----------

* Fast multidimensional array container implemented as a Python C extension
* *Array-oriented computing*
* The core-component of scientific computing with Python

.. image:: images/numpylogo.pdf
    :scale: 25%

So how fast is it?
------------------

.. code-block:: pycon

    >>> %time a = np.arange(10000000) ; a *=a*
    CPU times: user 0.06 s, sys: 0.08 s, total: 0.13 s
    Wall time: 0.13 s

* Without Numpy, scientific computing would not be possible in Python

The advantages of Numpy
-----------------------

* Approaches C speed for many operations
* Less code than the C equivalent
* No compilation
* No memory management
* No segmentation faults (usually)

The Interpreter
---------------

* Standard interpreter is somewhat dumb

  * No history
  * No tab completion
  * No colors

Enter IPython
-------------

* Enhanced interactive interpreter

  * History
  * Tab completion
  * Colors

.. image:: images/ipynb_icon.pdf
    :scale: 25%

But IPython is so much more
---------------------------

* Aliases and magic commands
* Advanced configuration options
* Browser based notebook
* Parallel execution engine

* And who knows what else..

Other important Libraries
-------------------------

* Matplotlib
* Scipy
* Pandas
* PyTables
* Scikits-learn
* Scikits-image
* ...

Together all of these packages make up what is known as the *scientific python
ecosystem*

Why do people like Python
-------------------------

* Easy to learn
* Easy to write
* Easy to read

* Large standard library
* Literally 1000 of additional packages

What do scientists need?
------------------------

* Rapid prototyping
* Fast numerics
* Code that can be shared

You want to do science, publish papers, and not futz about with code!

Downsides
---------

* Many packages make it hard to find the right one
* Career change: scientists becoming programmers

A Non-Trivial Algorithm
-----------------------

.. code-block:: python

    def quicksort_val(array):
        if len(array) <= 1:
            return array
        lower, upper, center = [], [], []
        part = choice(array)
        for i in array:
            if i < part:
                lower.append(i)
            elif i > part:
                upper.append(i)
            else:
                center.append(i)
        return quicksort_val(lower) + \
               center + \
               quicksort_val(upper)

Naive "Testing"
---------------

* How to test this?
* Initial approach:

  * Launch IPython
  * Test with some random input:

Naive "Testing"
---------------

.. code-block:: python

  >>> sorting.quicksort_val([3, 2, 1])
  [1, 2, 3]
  >>> sorting.quicksort_val([100, 1000, 10])
  [10, 100, 1000]
  >>> sorting.quicksort_val(['a', 'c', 'b'])
  ['a', 'b', 'c']

Unit Testing
------------

* What happens if you change something, e.g. fix a bug?
* Wouldn't it be great if you could re-run your "tests" automatically?

Unit Testing
------------

.. code-block:: python

    def test_sanity():
        nt.assert_equal(quicksort_val([3, 2, 1]),
                        [1, 2, 3])
        nt.assert_equal(quicksort_val([100, 1000, 10]),
                        [10, 100, 1000])
        nt.assert_equal(quicksort_val(['a', 'c', 'b']),
                        ['a', 'b', 'c'])


What to test?
-------------

.. code-block:: python

  def test_extended():
      # Test single element
      nt.assert_equal(quicksort_val([1]),
                      [1])
      # Test empty list
      nt.assert_equal(quicksort_val([]),
                      [])
      # Test duplicates
      nt.assert_equal(quicksort_val([1, 2, 2, 1]),
                      [1, 1, 2, 2])
      # Test mixing types
      nt.assert_equal(quicksort_val(['abc', 1, 1.0]),
                      [1, 1.0, 'abc'])


Running Them
------------

.. code-block:: console

  $ nosetests code/sorting.py
  ..
  ----------------------------------------------------------------------
  Ran 2 tests in 0.002s

  OK
  $ nosetests -v code/sorting.py 
  sorting.test_sanity ... ok
  sorting.test_extended ... ok

  ----------------------------------------------------------------------
  Ran 2 tests in 0.002s

  OK

Making slides with ``rst2beamer``
---------------------------------

* list item
* list item

  * nested list item

.. code-block:: console

    $ echo "example code block" 

Next slide
----------

* Links:
* `github <http://github.com>`_

Images
------

.. image:: images/octocat.pdf

