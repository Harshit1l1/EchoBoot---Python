# Contributing

- Never ship destructive disk ops without `--i-understand` + target path typed twice.
- Dry-run everything first; show exact commands.
- Prefer reproducible, pinned sources for bootloaders; verify signatures.
- Tests: fake device layer; never touch real disks in CI.
- Commits: Conventional Commits; sign commits if possible.
