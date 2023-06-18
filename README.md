# advent-of-code-2016
Decent solutions overall. Some very nice -- others could be improved (in terms of both elegance and performance).

If you don't see a part2, there either wasn't one, or the answer was deduced or part1 was used with modified input.

You'll also notice that I often don't actually memoize my dfs functions, I just use a closure dict of args to prevent recursing into a search space that's already been traversed elsewhere in the recursion tree. Heuristics to reduce the search space are added when it makes sense to do so based on the input.

IMO the \_\_name\_\_ construct isn't necessary because this code is not intended to be imported as a module, but it's been added in case there's some use case I haven't thought of.
