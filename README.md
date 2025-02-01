Here is a step-by-step breakdown of how to set up a Python project using a `pyproject.toml` file and create an editable install, based on the provided source:

1.  **Project Setup**:
    *   Create a directory for your project, for example, `snake-say-project`.
    *   Inside this project directory, create another directory for your package, for example, `snake-say`.
    *   Move your Python files (e.g., `cli.py` and `snake.py`) into the `snake-say` directory.
    *   Create a `pyproject.toml` file in the project's root directory, which is the `snake-say-project` directory.

2.  **Convert `cli.py` to `__main__.py`:**
    *   Rename the entry point file, `cli.py`, to `__main__.py`. This is a convention that allows Python to treat the directory as a module and execute this file when the directory is called.
    *   The `__main__.py` file will serve as the main entry point for the package.

3.  **Create the `pyproject.toml` File:**
    *   Add a `build-system` section to your `pyproject.toml` file. This specifies the build system you'll be using (e.g., `setuptools`). This section is required.
        ```toml
        [build-system]
        requires = ["setuptools>=61.0"]
        build-backend = "setuptools.build_meta"
        ```
    *   Add a `project` section to define metadata about your package, including name and version. For example:
        ```toml
        [project]
        name = "snake-say"
        version = "1.0.0"
        ```
    *   Note that the structure of this file is defined by PEP 621.

4.  **Create a Virtual Environment**:
    *   Navigate to your project directory in the terminal.
    *   Create a virtual environment using `python -m venv venv`.
    *   Activate the virtual environment (e.g., on Windows, `venv\Scripts\activate`; on Linux, `source venv/bin/activate`).

5.  **Install the Package in Editable Mode**:
    *   Use the command `python -m pip install -e .` to install your package in editable mode.
        *   The `-e` flag makes it so changes in your source code are immediately reflected without reinstalling.
        *   The `.` refers to the current directory, which contains the `pyproject.toml` file.

6.  **Address Import Issues**:
    *   When using `python -m snake-say`, the Python interpreter looks in its path for a module called `snake-say`.
    *   To fix import errors, modify your imports to use absolute imports. For example, change `import snake` to `from snake-say import snake`.
    *   **This will break the direct `python snake-say` command**.
    *   Installing the package makes both commands work because it adds the package to Python's path.

7.  **Create an Entry Point (Optional):**
    *   To run your script directly from the terminal using a command like `snakey`, add a `[project.scripts]` section to the `pyproject.toml` file.
    *   In your `__main__.py` file, add a function that contains the program's main code.
    *   Add a call to the `main()` function.
    *   Modify your `__main__.py` to avoid running the code on import using the `if __name__ == "__main__":` idiom.
    *   Example `pyproject.toml` entry:
        ```toml
        [project.scripts]
        snakey = "snake_say.__main__:main"
        ```
        *   `snakey` is the name of the command that will be available.
        *   `snake_say` is the package name.
        *   `__main__` is the name of the module, and `main` is the function to call.
    *   After making this change in `pyproject.toml`, you must run `python -m pip install -e .` again to update the package installation.

8.  **Run Your Package**:
    *   You can now run your package by using `snake-say` or `python -m snake-say` or the entry point name, like `snakey`, from anywhere in the terminal, as long as the virtual environment is active.

9.  **Understanding Egg-info (Optional):**
    *   After installing the package, a `snake-say.egg-info` folder is created. This contains metadata about the package.
    *   You can access this metadata by using the `importlib.metadata` module.
    *   The egg-info folder should be added to your `.gitignore` file as it is not part of the source code.
    *   The editable install makes the source code load from the location of the project. If it weren't editable, the information would live elsewhere.

By following these steps, you will have a well-structured Python project that is easy to develop and use and you can avoid issues with Python path and relative imports.

[watch the video here](https://youtu.be/v6tALyc4C10?list=TLPQMDEwMjIwMjU3cd9V4cTnuA)