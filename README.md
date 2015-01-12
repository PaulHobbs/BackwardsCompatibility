A simple library to check the backwards compatibility of changes to python libraries.

A change to a library is said to be backwards compatible if its API changes
only by adding symbols to the global scope, adding fields to classes, or adding
arguments to functions.

Any other change can potentially break a client of the library.
