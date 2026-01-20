from __future__ import annotations

import sys
import tkinter as tk

import sv_ttk

from csv_viewer.ui.autoscale import enable_windows_dpi_awareness, apply_tk_scaling
from csv_viewer.ui.main_window import MainWindow
from csv_viewer.ui.theme import apply_theme


def main() -> None:
    # 1) DPI awareness (Windows) + scaling (Tk)
    enable_windows_dpi_awareness()

    root = tk.Tk()
    apply_tk_scaling(root)

    # 2) Theme (Sun Valley)

    apply_theme(root,"dark")

    # 3) Main Window
    root.title("Raport Generator v.0.0.1")
    root.minsize(600, 400)

    MainWindow(root)

    # 4) Event loop
    root.mainloop()



# A little protection for explorer.exe
if __name__ == "__main__":
    sys.exit(main())

