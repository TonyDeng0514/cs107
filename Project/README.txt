README.txt

This is a readme file for my project.

In my project, I created two classes, one used to describe the Z/nZ group with modulo addition.

The other is creating a polynomial class with the coefficients being elements in a defined Z/nZ group.

The first class has a group structure and the second class has a ring structure.

The motivation for this project is to use python class to represent the group structure in mathematics.

During my planning phase, I realised that it is very hard to teach python to be familiar with all different kinds of binary operations, as well as teaching them to calculate symbols.
So, I limited this to the class that only describe the Z/nZ group with modulo addition.

With this group in mind, I thought I could generate a polynomial with coefficients being the elements of this group, so the next thing I did was to create a class that generates polynomials.

Instructions on running my files: click run.

In the group file, when generating a group, one needs to input a positive integer to define the identity.
The value stored in the object would be all the elements in the group.

There are methods in the group class that access the elements, compare two groups, and change an input integer to its equivalent class.

In the polynomial file, I imported the group class.
Inputs for this polynomial class would be a power, which should be a positive integer, and coefficients, which should be a group object.

The value stored would be a list with each element being a term.

The accessor representation would print out the polynomial in a string format.
There's also mutator called addition that add two polynomials together. This methods requries that the coefficients are in the same Z/nZ group.

