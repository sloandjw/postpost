# PostPost Processor

A lightweight, rule-based post-processing tool for modifying NC/G-code output using configurable profiles.

## Features
- Text-based rule engine with regex support
- Insert, replace, or delete lines
- Warn if required codes are missing
- Easy YAML-based configuration

## Getting Started
1. Install dependencies:
    ```bash
    pip install pyyaml
    ```

2. Run the processor:
    ```bash
    python main.py
    ```

## File Structure
- `src/` – Core logic
- `rules/` – Sample rule profiles (YAML)
- `nc_files/` – Input/output examples

## License
MIT
