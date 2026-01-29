# 01 – Guide to the Python Environment

This repository uses a **modern Python environment setup** based on the `pyproject.toml` file.

The goal is to make the setup:
- reproducible,
- simple to initialize,
- independent from system-wide Python installations.

---

## What is `pyproject.toml` and why it matters

The `pyproject.toml` file is the **standard configuration file** for modern Python projects.

It is used to:
- declare project metadata,
- specify Python dependencies,
- define how the development environment should be created and managed.

Instead of manually creating a virtual environment and installing packages one by one, the environment can be **automatically created** from this file.

In this project, the virtual environment will be created under the name:

```text
.venv
```
---
## Using uv to manage the environment
To create and manage the environment, this project relies on `uv`, a fast Python package manager developed by Astral.  
Official documentation:  
https://docs.astral.sh/uv/getting-started/installation/  
`uv` reads the `pyproject.toml` file and takes care of:  
- creating the virtual environment,
- resolving dependencies,
- installing everything in a consistent way.

---
## Installing uv (macOS)
If you are using macOS, you can install `uv` directly from the terminal.
Open the terminal of your preferred IDE and run:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Press Enter and wait for the installation to complete.

---
## Checking and updating uv
After installation, you can verify that uv is correctly installed by checking its version:
```
uv --version
```
If you want to update uv to the latest available version, run:
```
uv self update
```

---
## Creating the virtual environment
Once uv is installed, creating the environment is straightforward.
From the root of the repository, run:
```
uv sync
```
This command will:
1. Read the `pyproject.toml` file
2. Create the `.venv` directory
3. Install all required dependencies  

After a few minutes, the environment will be ready and the `.venv` folder will appear in the project directory.

---

## Activating the environment in your IDE (Clarification)

After running `uv sync`, the `.venv` directory is created, but the final step is to **tell your IDE to actually use it** as the Python interpreter.

The exact procedure depends on the IDE, but the concept is always the same:
> the environment already exists, the IDE just needs to point to it.

---

### 🐍 PyCharm Example

**Case 1 – `.venv` already exists (recommended)**

1. Open the project in PyCharm
2. Go to  
   **Settings → Python Interpreter**
3. PyCharm will usually detect `.venv` automatically  
4. If it does not:
   - Click **Add Interpreter**
   - Select **Existing**
   - Choose `.venv/bin/python`
5. Confirm the selection

Done. PyCharm will now use the `.venv` environment without creating additional ones

---

## Final notes
- The `.venv` directory should not be committed to the repository.
- Make sure your IDE is configured to use the Python interpreter located inside `.venv`.
- This setup ensures that anyone cloning the repository can recreate the same environment with a single command.