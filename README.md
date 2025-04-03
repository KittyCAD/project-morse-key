# Morse key project

A single-part 3D printed Morse key design that uses a flexure mechanism. The
project includes:

- KCL CAD files for the Morse key and supporting test rig parts.
- Python scripts for supporting analysis work.
- Arduino firmware for Morse key interpretation and USB keyboard emulation.
- Documentation of the design process, including analysis and testing.

## Project Structure

```
.
├── analysis/       # Python analysis scripts
├── arduino/        # PlatformIO project for firmware
├── cad/            # KCL CAD files
├── docs/           # Assembly instructions
└── reporting/      # LaTeX documentation
```

## Prerequisites

- [TeX Live 2025](https://www.tug.org/texlive/).
- [PlatformIO](https://platformio.org/).
- [uv](https://github.com/astral-sh/uv).
- Arduino Leonardo or compatible board with USB HID support.
- 3D printer for manufacturing parts.

## Reporting

LaTeX is used for report generation. Each report has its own directory within
the `reporting` directory, and can be built either with the VSCode LaTeX
Workshop extension or with the command line. Note that
[TeX Live 2025](https://www.tug.org/texlive/) is required.

To build a report with the command line, navigate to the target report directory
and simply run `make`. Raw `.tex` files can also be formatted with
`make format`.

Note that common functionality for building is defined in `reporting/common.mk`.

## Python scripts

The python scripts are designed to be self-contained and can be run with `uv`.
All scripts are located in the `analysis` directory, and can be run with `uv` as
follows:

```bash
uv run analysis/filename.py
```

## Arduino project

The Arduino project can only support keyboard emulation on certain Arduino
devices, such as the Leonardo series. The boards must support USB HID emulation.

The project is intended to be built with PlatformIO.
