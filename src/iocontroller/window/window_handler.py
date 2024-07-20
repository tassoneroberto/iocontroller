#!/usr/bin/env python3

import time
import logging

import win32gui

logging.getLogger(__name__)
logging.root.setLevel(logging.INFO)


def select_window(window_name: str) -> tuple[int, int, int, int]:
    logging.info(f"Checking for application window with title [{window_name}]...")
    hwnd = win32gui.FindWindow(None, r"{}".format(window_name))
    if hwnd == 0:
        raise Exception(f"Application [{window_name}] not detected.")

    dimensions = win32gui.GetWindowRect(hwnd)
    width = dimensions[2] - dimensions[0]
    height = dimensions[3] - dimensions[1]
    logging.info(
        f"Application [{window_name}] detected successfully. Window size: [{width}x{height}]"
    )

    win32gui.SetForegroundWindow(hwnd)

    while window_name != win32gui.GetWindowText(win32gui.GetForegroundWindow()):        
        logging.info(f"Setting it as active window...")
        time.sleep(1)

    logging.info(f"The selected window is now active.")

    return dimensions


def get_relative_window_center(dimensions: tuple[int, int, int, int]) -> list[int]:
    return [
        (dimensions[2] - dimensions[0]) // 2,
        (dimensions[3] - dimensions[1]) // 2,
    ]


def get_absolute_window_center(dimensions: tuple[int, int, int, int]) -> list[int]:
    return [
        (dimensions[2] - dimensions[0]) // 2 + dimensions[0],
        (dimensions[3] - dimensions[1]) // 2 + dimensions[1] + 20,
    ]
