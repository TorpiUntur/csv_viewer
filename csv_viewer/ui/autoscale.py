from __future__ import annotations

import sys
import tkinter as tk


def enable_windows_dpi_awareness() -> None:
    """Sets up the windows dpi awareness."""
    if sys.platform != "win32":
        return

    try:
        import ctypes

        # DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2
        ctypes.windll.user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))  # type: ignore[attr-defined]
    except (AttributeError, OSError):
        # Fallback for older systems
        try:
            import ctypes

            ctypes.windll.shcore.SetProcessDpiAwareness(2)  # type: ignore[attr-defined]
        except (AttributeError, OSError):
            pass


def apply_tk_scaling(root: tk.Tk) -> float:
    """
    Sets up the tkinter scaling based on real DPI
    Returns scaling value (for diagnostics)
    """
    pixels_per_inch = float(root.winfo_fpixels("1i"))
    scale = pixels_per_inch / 72.0
    root.tk.call("tk", "scaling", scale)
    return scale
