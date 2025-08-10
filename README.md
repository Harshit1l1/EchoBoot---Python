# EchoBoot — Trusted, Auditable Multiboot USB

Scaffold v0.2 • Python 3.11+ • **AGPL-3.0-or-later**

Goal: a clean, minimalist Python stack with a native GUI that provisions secure, multi-ISO boot media using rEFInd + Syslinux with integrity verification, provenance logs, and zero black boxes.

## Quick start (CLI)

```bash
pipx run --spec . echoboot --help
echoboot scan
echoboot plan /dev/sdX --esp-mb 512 --label ECHOBOOT
echoboot esp-init /mnt/esp --title "EchoBoot"
```

**Warning:** Partitioning commands are printed for review only; they are not executed. Proceed carefully.

## Contributing
See `CONTRIBUTING.md`.

## License
AGPL-3.0-or-later
