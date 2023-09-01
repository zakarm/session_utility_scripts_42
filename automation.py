import subprocess, os

def login_message():
    print('\033[34m' + '@zmrabet a7ssen oujdi' + '\033[0m')
    print('\033[31m' + ' >> 9ra w zid 9ra << ' + '\033[0m')

def enable_dark_mode():
    try:
        script = """
            tell application "System Events"
                tell appearance preferences
                    set dark mode to not dark mode
                end tell
            end tell
        """
        subprocess.call(["osascript", "-e", script])
        print("Dark Mode activated successfully.")
    except subprocess.CalledProcessError as e:
        print("Error toggling to the Dark Mode: {}".format(e))


def execute_ccleaner():
    try:
        os.system("zsh -i -c cclean")
        os.system("clear")
    except Exception as e:
        print("Error: {}".format(e))


if __name__ == "__main__":
    login_message()
    enable_dark_mode()
    execute_ccleaner()

