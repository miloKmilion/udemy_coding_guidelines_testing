# PEP8

Python Enhanced Proposal.

This are just a set of rules that will be enforced to have the proper code behavior. For example if the imports are located at the end of the file.

## Imports

One common approach is to separate code into several blocks. This will also help to identify git changes, since is easier to see by modified line.

```python
# Correct
import sys
import os
```

```python
# Incorrect
import sys, os
```

One common rule to imports is:

1. Standard Libaries -> Standard Library
2. Related third party libraries -> Third party libraries
3. Local applications/lirary specific. -> First (Party) local

## Indentation

It is recommended to use 4 space per indentation level. By pressing the tab key, the indentation is set automatically to 4 spaces.

## Comments

The first standar rule is to avoid comments. More comments indicates the code is not readable and needs to be updated.

However, comments are needed if a formula or an expression needs to be described.

## Naming conventions

"Code needs to be read like a book and understood like a book as well"

- Functions and Variables: Lowercase with underscore --> Snake case.
- Constant values: UPPERCASE or UPPERCASE with underscore.
- Class variables: Camel case no underscore. Or Capitalized words.