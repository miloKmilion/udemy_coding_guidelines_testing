# isort

Tool to sort imports. Since by PEP8 are guidelines to import tools and libraries.

The goal is to create a readable way to organize imports for other users and development. There are seeral styles for imports and depends of the user and company regulations.

There are 5 blocks defined by default in isort defined by:

1. Special imports such as **future**
2. Standard libraries.
3. Third party libraries such as pandas or numpy.

One of the isort caveats is that sometimes we need to specify the third party libraries. So we will need to specify the third party libraries manualy and avoid confusions.

The option: force_single_line = True or False will automatically change the behavior of having one import per line.
By having the single line, will make easier to find changes in the code since the changes will be reflected individually.
