from level_editor.editor import Editor
from level_editor.settings import VERSION


def main() -> None:
    print(f"LevelEditor v{VERSION}")
    editor: Editor = Editor()
    editor.run()
