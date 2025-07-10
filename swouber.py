import re
import sys

def translate_swouber_code(code):
    """
    Translate Swouber keywords to Python keywords.
    """
    replacements = {
        r"\bfctn\b": "def",
        r"\bcls\b": "class",
        r"\bmd\b": "import",
        r"\bfmd\b": "from",
    }
    for pattern, replacement in replacements.items():
        code = re.sub(pattern, replacement, code)
    return code

def run_swouber_code_line(code_line):
    """
    Run a single line of Swouber code, with translation.
    """
    if not code_line.strip():
        # Empty input: do nothing, no error
        return
    try:
        translated = translate_swouber_code(code_line)
        compiled = compile(translated, "<swouber>", "single")
        exec(compiled, globals())
    except Exception as e:
        print(f"<{str(e).splitlines()[-1]}>")

def run_file(filename):
    """
    Load and run a Swouber file (any extension).
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()
        translated = translate_swouber_code(code)
        exec(translated, globals())
    except FileNotFoundError:
        print(f"<file '{filename}' not found>")
    except Exception as e:
        print(f"<{str(e).splitlines()[-1]}>")

def swouber_repl():
    print("""Swouber 1.0
    swouber.github.io

    Remember swouber is licensed under the MIT this means the software is fully customizable
     Created by Zohan Haque
Please note this a repl it is an interactive shell
""")
    while True:
        try:
            line = input(">>> ")
            if line.strip() == "exit":
                break
            run_swouber_code_line(line)
        except KeyboardInterrupt:
            print("\n<KeyboardInterrupt>")
            break

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_file(sys.argv[1])
    else:
        swouber_repl()

