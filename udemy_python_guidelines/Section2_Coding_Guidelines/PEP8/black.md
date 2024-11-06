# BLACK

Not a really configurable tool. The vast majority of configurations are already set.

Every project using black it has almost the same layout. ```pycodestile```
will complain about the formatting.

``` python
black {source folder}
```

```bash
[tool.black]
target-version = ['py310]
line-length = 80
skip-string-normalization = false
skip-magic-trailing-comma = false

exclude = ''' #Folders to exclude.
(
    asv_bench/env
)
'''  
```

The line lenght can be adapted. 