# System Utility Python Script

## Description

This Python script provides various system utility functions, including displaying a login message, toggling Dark Mode on macOS, and executing the CCleaner utility.

## Features

1. **Login Message**: The script displays a colorful login message in the terminal.

2. **Dark Mode Toggle**: It can toggle Dark Mode on macOS using AppleScript.

3. **CCleaner Execution**: The script runs the `cclean` command via the Zsh shell.

## Usage

Before running the script, ensure you have the necessary permissions to execute system commands. Here's how to use it:

1. **Run the Script**: Navigate to the script's directory in your terminal and execute it using:

    ```shell
    python script_name.py
    ```

2. **Login Message**: After execution, the script will display the login message.

3. **Dark Mode Toggle**: It toggles Dark Mode on macOS.

4. **CCleaner Execution**: The script runs the `cclean` command. Ensure you have the permissions and the command is available.

## Dependencies

- Python's `subprocess` and `os` modules for executing system commands.
- `osascript` command for macOS Dark Mode.

## Compatibility

- Primarily intended for macOS for Dark Mode toggle.
- Ensure compatibility with the `cclean` command on your system.

## Troubleshooting

- Refer to terminal error messages for issues.
- Ensure proper permissions for system commands and AppleScript.

## Disclaimer

This script is provided as-is and without warranties. Use it at your own risk and exercise caution when executing system commands.
