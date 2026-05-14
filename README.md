For every Xorq release do the following:

```bash
uv lock --upgrade-package xorq
uv export --locked --no-dev --no-emit-project --no-header --no-annotate > requirements.txt
```

The export flags must match what `xorq uv build` compares against, otherwise the
in-tree `requirements.txt` fails the packager's byte-exact check (see
[xorq-labs/xorq#1941](https://github.com/xorq-labs/xorq/issues/1941)).