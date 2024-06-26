from tkinter import filedialog

from scripts.globals import tile_paths


def get_images() -> None:
    filetypes = [("Select Tiles", "*.jpg;*.jpeg;*.png;")]
    selected_files = filedialog.askopenfilenames(filetypes=filetypes)
    tile_paths + list(selected_files)
