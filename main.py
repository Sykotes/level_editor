from scripts.editor import Editor
from scripts.globals import VERSION


def main() -> None:
    print(f"LevelEditor v{VERSION}")
    editor: Editor = Editor()
    editor.run()


if __name__ == "__main__":
    main()
