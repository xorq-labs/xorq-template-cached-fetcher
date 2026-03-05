For every Xorq release do the following:

```bash
uv lock --upgrade-package xorq
uv export --no-emit-project --format requirements.txt > requirements.txt
```