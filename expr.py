import xorq as xo
from xorq_template_cached_fetcher import (
    do_hackernews_fetcher_udxf,
)


expr = (
    xo.memtable(
        data=({"maxitem": 43182839, "n": 1000},),
        name="t",
    )
    .pipe(do_hackernews_fetcher_udxf)
)
