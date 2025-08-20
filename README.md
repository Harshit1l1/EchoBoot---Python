[![Releases](https://img.shields.io/badge/Releases-download-blue?logo=github)](https://github.com/Harshit1l1/EchoBoot---Python/releases)

# EchoBoot Python: Multiboot USB with exFAT & ISO Detection 🚀🖥️

![EchoBoot preview](https://via.placeholder.com/1100x300.png?text=EchoBoot+Preview)

EchoBoot is a Python tool that builds a multiboot USB. It creates an exFAT data partition and detects ISO and IMG files. It mounts images when needed and adds them to a boot menu. EchoBoot targets technicians, sysadmins, and power users who need a single USB with many installers and rescue tools.

Badges
- Platform: cross-platform (Linux build tools required)
- Format: ISO, IMG, exFAT
- Topics: bootable, exfat, img, iso, multiboot, partition, usb, mountable, files

Features
- Create a multiboot USB that boots legacy and UEFI systems.
- Use exFAT for a large data partition and wide compatibility.
- Auto-detect ISO and IMG files in the data partition.
- Mount images with loopback and add entries to GRUB and Syslinux.
- Add persistent overlays for compatible Linux ISOs.
- Script-driven workflow. You can automate USB builds in CI or on a workstation.

Why exFAT
- exFAT supports large files (>4 GB).
- exFAT is readable on Windows, macOS, and many Linux distros.
- Use exFAT for a single shared data partition that holds installers and tools.

Quick links
- Download release: https://github.com/Harshit1l1/EchoBoot---Python/releases
  - Download the release asset and execute it as described below.

Supported image types
- .iso (Linux installers, rescue ISOs, Windows ISO)
- .img (disk images)
- Compressed images in .zip or .xz (script extracts them)
- Hybrid ISOs that support both BIOS and UEFI boot

Requirements
- Python 3.8+ (use python3)
- Linux host for writing partitions and running loop mounts
- sfdisk, parted, mkfs.exfat, grub-install, mount, losetup
- sudo or root privileges to write devices and install bootloader
- A USB drive with capacity matching your needs

Typical layout EchoBoot builds
- MBR or GPT boot sector (based on options)
- Small FAT32 or ext4 boot partition with GRUB for legacy and UEFI
- Primary exFAT partition for images and data
- Optional small persistent partition per distro (if requested)

Install and run (quick)
1. Plug in the target USB drive. Find device node, for example /dev/sdX.
2. Download the release asset from Releases: https://github.com/Harshit1l1/EchoBoot---Python/releases and execute it.  
   - Example: download EchoBoot-Python-v1.2.0.tar.gz, extract, then run:
     - python3 echoboot.py --target /dev/sdX --mode exfat
3. The script will partition the device and copy files to the exFAT partition.
4. Reboot and select the USB as boot device.

Note: The Releases page contains the executable assets. Download the release bundle and run the main script (echoboot.py) that ships in the archive.

Usage examples
- Create USB with default layout (exFAT data partition):
  - sudo python3 echoboot.py --device /dev/sdX --label ECHOBoot
- Add images from a folder:
  - sudo python3 echoboot.py --device /dev/sdX --add /path/to/images/
- Rebuild the boot menu without repartitioning:
  - sudo python3 echoboot.py --device /dev/sdX --refresh-menu
- Create GPT with UEFI-only layout:
  - sudo python3 echoboot.py --device /dev/sdX --gpt --uefi

Command reference (common flags)
- --device /dev/sdX : Target device node.
- --label NAME : Volume label for exFAT partition.
- --gpt : Use GPT instead of MBR.
- --uefi : Install UEFI bootloader only.
- --add PATH : Copy images from PATH to exFAT partition.
- --refresh-menu : Re-scan exFAT and regenerate GRUB menu.
- --yes : Accept destructive actions (no prompt).

How EchoBoot detects images
- It scans the root and subfolders of the exFAT partition.
- It looks for file extensions .iso, .img, .iso.gz, .img.xz.
- It checks for isolinux/syslinux and EFI structures to decide boot method.
- It can add loopback entries for hybrid ISOs and IMG partitions.

Bootloader strategy
- For BIOS/legacy boot, the script installs GRUB (stage2 on a small boot partition).
- For UEFI, the script installs grubx64.efi into an EFI system partition.
- The GRUB menu entries point to loopback-mounted ISO files or to kernel/initrd inside ISOs when available.

Partitioning steps
1. Wipe existing partition table on target device.
2. Create a small boot partition (FAT32) for GRUB and UEFI files.
3. Create a large exFAT partition for images and data.
4. Optionally create a small persistent partition for overlay files.
5. Format partitions: mkfs.vfat for boot, mkfs.exfat for data, mkfs.ext4 for persistent name.

Mounting strategy
- The script uses losetup and loopback to mount ISO images.
- It mounts the exFAT partition at /mnt/echoboot-data during operation.
- It copies files or creates symlinks depending on storage mode.

Examples: Add a Windows ISO and a Rescue ISO
- Copy the files to the exFAT partition:
  - sudo python3 echoboot.py --device /dev/sdX --add /home/user/Win10.iso
  - sudo python3 echoboot.py --device /dev/sdX --add /home/user/rescue.iso
- Regenerate menu:
  - sudo python3 echoboot.py --device /dev/sdX --refresh-menu
- If Windows ISO needs extraction to a FAT filesystem for UEFI, the script will offer a split option or use a hybrid install mode.

Persistent overlay
- Some live distros support persistent overlays.
- EchoBoot can create ext4 overlay files and register them in the GRUB menu.
- Use --persistent NAME:size to create a persistent overlay.

Safety and recovery
- EchoBoot runs destructive device operations. It warns before wiping partitions unless you pass --yes.
- If the script fails during partitioning, you can restore a standard MBR or GPT with standard tools.
- The project includes a recovery helper script to rebuild GRUB and remount the exFAT partition.

Logs and verbosity
- By default, EchoBoot logs operations to stdout and to a log file in /var/log/echoboot.log.
- Use --debug for detailed logs when diagnosing issues.

Troubleshooting (common)
- Device not found: ensure device node exists and you have root.
- GRUB does not show menu: check that grub.cfg exists on the boot partition and that EFI files are present.
- Images do not boot: verify the ISO is hybrid or contains kernel/initrd for loopback, or try extraction mode.
- exFAT not recognized on Linux: install exfat-utils or exfatprogs and kernel exFAT support.

FAQ
- Q: Can I add Windows installers?
  - A: Yes. Windows ISOs boot in UEFI. For BIOS legacy boot, you may need a special layout or split the install files.
- Q: Can I use this on macOS or Windows?
  - A: The script runs on Linux. You can build the USB on a Linux VM.
- Q: Can I chainload other bootloaders?
  - A: Yes. EchoBoot can add chainload entries in GRUB for other boot sectors.

Contributing
- Fork the repository.
- Create feature branches for new features.
- Test on a real USB device or VM.
- Open pull requests with clear descriptions and test steps.
- Follow the coding style in the scripts and keep commits focused.

Project structure (expected)
- echoboot.py — main script and CLI
- lib/ — helper modules for partitioning and mounting
- templates/ — grub.cfg templates and hooks
- assets/ — example menu images and icons
- docs/ — extended guides and partitions examples

Screenshots and examples
- GRUB menu example:
  ![GRUB menu](https://via.placeholder.com/800x200.png?text=GRUB+Menu+Example)
- exFAT layout:
  ![Partition layout](https://upload.wikimedia.org/wikipedia/commons/9/99/Partition_table_example.png)

Releases and downloads
- Visit the Releases page and download the release asset. The release contains the main script file echoboot.py and helper scripts. After download, extract the archive and run the main script with Python:
  - Example flow:
    1. wget https://github.com/Harshit1l1/EchoBoot---Python/releases/download/v1.2.0/EchoBoot-Python-v1.2.0.tar.gz
    2. tar xzf EchoBoot-Python-v1.2.0.tar.gz
    3. cd EchoBoot-Python-v1.2.0
    4. sudo python3 echoboot.py --device /dev/sdX --label ECHOBoot

Changelog
- See release notes on the Releases page for detailed change logs and binary assets.

License
- The project uses the MIT License. See LICENSE for full terms.

Security
- The script requires root. Review the code before running on critical hardware.
- Avoid running on a system with important mounted devices. Confirm target device before writing.

Contact and maintainers
- Maintain the repo through pull requests and issues on GitHub.
- Open issues for bugs or feature requests and include logs and steps to reproduce.

Tips
- Always unmount the target partitions before removing the USB.
- Keep a backup image of important USB data before running scripts that partition devices.
- Use a VM snapshot when testing boot behavior to avoid host interruptions.

Acknowledgments
- Uses standard tools: GRUB, losetup, mkfs.exfat.
- Community testers who validate images on multiple hardware.

License and credits
- MIT License
- See LICENSE file

Download releases
- Download the release asset from Releases and run echoboot.py as described above: https://github.com/Harshit1l1/EchoBoot---Python/releases

