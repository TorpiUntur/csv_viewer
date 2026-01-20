from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from csv_viewer.ui.theme import toggle_theme, get_theme_mode


class MainWindow(ttk.Frame):
    def __init__(self, master: tk.Tk) -> None:
        super().__init__(master)
        self.master = master

        self.pack(fill="both", expand=True)

        # Layout: topbar + content + status
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self._build_topbar()
        self._build_content()
        self._build_statusbar()

    def _build_topbar(self) -> None:
        topbar = ttk.Frame(self)
        topbar.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 0))
        topbar.columnconfigure(2, weight=1)

        ttk.Label(topbar, text="CSV Viewer (placeholder UI)").grid(row=0, column=0, sticky="w")

        self.theme_btn_text = tk.StringVar(value=self._theme_button_label())
        ttk.Button(
            topbar,
            textvariable=self.theme_btn_text,
            command=self._on_toggle_theme,
        ).grid(row=0, column=1, padx=(10, 0), sticky="e")

        # Placeholder space to the right (future: open/save buttons)
        ttk.Label(topbar, text="").grid(row=0, column=2, sticky="ew")

    def _build_content(self) -> None:
        content = ttk.Frame(self)
        content.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        content.rowconfigure(0, weight=1)
        content.columnconfigure(0, weight=3)
        content.columnconfigure(1, weight=2)

        left = ttk.Frame(content)
        right = ttk.Frame(content)

        left.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        right.grid(row=0, column=1, sticky="nsew")

        ttk.Label(left, text="Left panel: CSV table preview (ETAP 2)").pack(anchor="w")
        ttk.Label(right, text="Right panel: plot controls + plot (ETAP 3+)").pack(anchor="w")

    def _build_statusbar(self) -> None:
        self.status_var = tk.StringVar(value="Ready")
        status = ttk.Label(self, textvariable=self.status_var, style="Status.TLabel", anchor="w")
        status.grid(row=2, column=0, sticky="ew", padx=10, pady=(0, 10))

    def _on_toggle_theme(self) -> None:
        new_mode = toggle_theme(self.master)
        self.theme_btn_text.set(self._theme_button_label())
        self.status_var.set(f"Theme switched to: {new_mode}")

    def _theme_button_label(self) -> str:
        # Pokazuj akcję, nie stan (bardziej intuicyjne)
        return "Switch to Dark" if get_theme_mode() == "light" else "Switch to Light"
