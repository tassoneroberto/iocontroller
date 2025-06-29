#!/usr/bin/env python3

import logging
import time
from ctypes import windll

import pygetwindow
import win32api
import win32con

logging.getLogger(__name__)
logging.root.setLevel(logging.INFO)


def select_window(
    window_name: str, adjust_dpi: bool = True
) -> pygetwindow.Win32Window:
    logging.info(
        f"Searching for running application window with title [{window_name}]..."
    )

    windows = pygetwindow.getWindowsWithTitle(window_name)

    if len(windows) == 0:
        raise Exception(f"Application [{window_name}] not found.")

    for window in windows:
        if window.title == window_name:
            application_window = window
            break

    logging.info(f"Application [{window_name}] successfully detected!")
    logging.info(
        f"Window size: [{application_window.width}x{application_window.height}]"
    )

    application_window.activate()

    while not application_window.isActive:
        logging.info(f"Setting it as the foreground (active) window...")
        time.sleep(1)

    logging.info(f"The selected window is now active.")

    if adjust_dpi:
        logging.info(f"Enabled system-DPI awareness.")
        adjust_window_dpi()

    return application_window


def get_relative_window_center(
    width: int, height: int, include_top_bar: bool = True
) -> tuple[int, int]:
    return (
        width // 2,
        height // 2 + (20 if include_top_bar else 0),
    )


def get_absolute_window_center(
    left: int, top: int, width: int, height: int, include_top_bar: bool = True
) -> tuple[int, int]:
    return (
        left + width // 2,
        top + height // 2 + (20 if include_top_bar else 0),
    )


def adjust_window_dpi() -> None:
    # https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setprocessdpiaware
    windll.user32.SetProcessDPIAware()


def send_message_to_window(hwnd: int, message: str) -> None:
    for c in message:
        if c == "\n":
            win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)  # type: ignore
            win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)  # type: ignore
        else:
            win32api.SendMessage(hwnd, win32con.WM_CHAR, ord(c), 0)  # type: ignore
