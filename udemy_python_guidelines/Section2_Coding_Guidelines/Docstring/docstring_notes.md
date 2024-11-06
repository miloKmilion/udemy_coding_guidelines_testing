# Docstring 

So a docstring is a documentation string for a function, a method, a class or for a python file itself.

And doc strings are always defined if we want to, for example, have a docstring for a class below its definition.

## Why do we need docstrings?

If for example the code running is small, and will be only used by you then docstrings are not needed. However, if working in a large team, or in a library that will be used open source then docstrings are a must.

## Styles

### 1. Google Style

It always starts with a brief description of a class. One or two sentences should be enough, if more lines are needed is because the funciton is too complex and then the function needs to be reorganized.

The arguments (Args) will be passed to the function. Followed by the raises and returns.

When is a function will also describe the function definition and the returns.

### 2. Numpy Style

Will also start with a description of a class of functions. Followed by, at least 2 lines per parameter. One line with the parameter description and the second indicating the type. 

Smimilarly, for the return type is listed. 

### 3. Rest style

It is the less readable of all, since has too many colons. Also has 2 lines per paramenter.

Docstrings should be only needed if is really needed. Otherwise type annotations will be enough and easier to mantain.

```bash
    "autoDocstring.generateDocstringOnEnter": true,
    "autoDocstring.quoteStyle": "'''",
    "autoDocstring.docstringFormat": "google",
```

By adding this to the settings.json will automatically help you to generate documentation.

## pydocstyle

It is a tool to evaluate the docstring and return the lines where it doesnt follow the conventions.
