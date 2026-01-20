from __future__ import annotations

from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk

import sv_ttk


@dataclass(frozen=True)
class ThemeState:
    """Keeps track of the current theme state"""

    mode: str  # "light" | "dark"


# simple global state
_theme_state = ThemeState(mode="dark")


def apply_theme(root: tk.Tk, mode: str = "dark") -> None:
    """
    Sets Sun Valley theme

    args:
        root: tk.TK instance
        mode: "dark" or "light
    """
    mode = mode.lower().strip()
    if mode not in ["dark", "light"]:
        raise ValueError(f"Invalid theme mode: {mode} - must be 'dark' or 'light'")

    # Set up sv_ttk theme
    sv_ttk.set_theme(mode)

    # Save state
    global _theme_state
    _theme_state = ThemeState(mode=mode)

    # Additional style setting
    _apply_custom_ttk_styles(root)


def toggle_theme(root: tk.Tk) -> str:
    """
    Switches Light/Dark theme
    Returns new mode (light or dark)
    """
    new_mode = "dark" if _theme_state.mode == "light" else "light"
    apply_theme(root, new_mode)
    return new_mode


def get_theme_mode() -> str:
    """Returns current theme mode (dark or light)"""
    return _theme_state.mode


def _apply_custom_ttk_styles(root: tk.Tk) -> None:
    """
    Applies custom TTK styles ie. fonts paddings - Use as needed to configure UX
    """
    style = ttk.Style(root)

    # Example padding

    style.configure("TButton", padding=(10, 6))
    style.configure("TEntry", padding=(6, 4))
    style.configure("TCombobox", padding=(6, 4))
    style.configure("TLabel", padding=(8, 4))
