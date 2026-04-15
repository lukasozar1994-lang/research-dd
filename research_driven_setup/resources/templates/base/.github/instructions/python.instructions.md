<!-- user-language: en -->

# Instructions for GitHub Copilot Agent

## Environment

You are working in an **Ubuntu 24.04 LTS** environment. All system-level operations should follow Ubuntu best practices.

## Python Project Handling

### Virtual Environment (venv) Requirements

**CRITICAL:** For ANY Python project in this workspace:

1. **Always check for existing venv first**
   - Look for `venv/`, `.venv/`, or `env/` directories in the project root
   - Check if `pyvenv.cfg` exists in the project directory

2. **Create venv if missing**
   - If no virtual environment exists, create one using:
     ```bash
     python3 -m venv venv
     ```
   - Or for specific Python version:
     ```bash
     python3.12 -m venv venv
     ```

3. **Activate venv before ALL Python operations**
   - Always activate the virtual environment before running Python commands:
     ```bash
     source venv/bin/activate
     ```
   - This applies to:
     - Installing packages with `pip`
     - Running Python scripts
     - Executing `pip install -r requirements.txt`
     - Running development servers

4. **Install all Python packages to venv**
   - NEVER install Python packages globally
   - ALWAYS install to the virtual environment
   - Use `pip install <package>` after activating venv
   - For requirements: `pip install -r requirements.txt`

5. **Verify installation**
   - After installing packages, verify with:
     ```bash
     pip list
     python -c "import <package_name>"
     ```

