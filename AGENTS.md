# AGENTS.md - Guide for AI Coding Agents

## Project Overview

This is a minimal Python utility project created with PyCharm's default template. Currently contains a single entry point (`main.py`) with basic function examples. The project is version-controlled with Git but has no external dependencies or complex architecture yet.

**Key File:**
- `main.py` - Single module containing the `print_hi()` function and main entry point

## Development Environment

### Running Code
- **Execute main script:** `python main.py` or use PyCharm's green run button (⌃R on macOS)
- **Python Version:** Check PyCharm project settings or system Python: `python --version`
- **PyCharm Debugger:** Use breakpoints (⌘F8 to toggle) in line 8 of `main.py`

### No Build/Test Framework Currently
- No test suite, CI/CD pipeline, or package configuration exists
- Project is a standalone script, not a package

## Code Patterns & Conventions

### Function Structure
- Simple utility functions with descriptive names (e.g., `print_hi(name)`)
- Main logic guarded by `if __name__ == '__main__':` idiom (see line 14)
- String formatting uses f-strings (line 8: `f'Hi, {name}'`)

### Current Architecture
- Flat structure with all code in one file
- No dependencies, no external imports
- Entry point: `print_hi('PyCharm')` called from main block

## Adding New Features

### Expanding the Project
If adding utilities:
1. Define functions in `main.py` or create new modules as needed
2. Keep `if __name__ == '__main__':` block as the entry point
3. Consider creating a `requirements.txt` if external packages are added: `pip freeze > requirements.txt`

### Minimal Workflow
- Edit code → Run (⌃R) → Debug with breakpoints as needed
- Commit to Git when stable

## Important Notes

- **No existing test infrastructure** - Add testing framework (pytest, unittest) when needed
- **No docstrings present** - Match the minimalist style or add them when documenting public APIs
- **PyCharm specific:** Project configured in `.idea/` directory; respect PyCharm project structure

