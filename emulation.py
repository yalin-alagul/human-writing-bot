#!/usr/bin/env python3
"""
Human-like Typing Emulator
Emulates human typing by pasting clipboard content with realistic timing patterns.
Triggered by Command+H hotkey.
"""

import os
import time
import random
import pyperclip
from pynput import keyboard
from pynput.keyboard import Controller, Key
from dotenv import load_dotenv


class TypingEmulator:
    """Emulates human-like typing with configurable speed and patterns."""

    def __init__(self):
        """Initialize the typing emulator with configuration from .env file."""
        # Load environment variables
        load_dotenv()

        # Load configuration with defaults
        self.min_delay = float(os.getenv('MIN_KEYSTROKE_DELAY', '0.05'))
        self.max_delay = float(os.getenv('MAX_KEYSTROKE_DELAY', '0.15'))
        self.pause_chance = float(os.getenv('PAUSE_CHANCE', '0.1'))
        self.pause_min = float(os.getenv('PAUSE_MIN', '0.3'))
        self.pause_max = float(os.getenv('PAUSE_MAX', '0.8'))
        self.word_boundary_delay = float(os.getenv('WORD_BOUNDARY_DELAY', '0.1'))

        # Initialize keyboard controller
        self.controller = Controller()

        # Word boundary characters (spaces and common punctuation)
        self.word_boundaries = {' ', '.', ',', '!', '?', ';', ':', '\n', '\t'}

    def get_delay(self, char):
        """
        Calculate delay for a character based on human-like patterns.

        Args:
            char: The character being typed

        Returns:
            float: Delay in seconds
        """
        # Base delay with random variation
        delay = random.uniform(self.min_delay, self.max_delay)

        # Add extra delay for word boundaries
        if char in self.word_boundaries:
            delay += self.word_boundary_delay

        # Occasionally add a longer pause (simulating reading/thinking)
        if random.random() < self.pause_chance:
            delay += random.uniform(self.pause_min, self.pause_max)

        return delay

    def type_text(self, text):
        """
        Type the given text with human-like delays.

        Args:
            text: The text to type
        """
        if not text:
            return

        for char in text:
            # Type the character
            self.controller.type(char)

            # Wait with human-like delay
            delay = self.get_delay(char)
            time.sleep(delay)

    def on_hotkey(self):
        """Callback function when hotkey is pressed."""
        try:
            # Get clipboard content
            text = pyperclip.paste()

            # Type the text if clipboard is not empty
            if text:
                self.type_text(text)
        except Exception:
            # Silent error handling - no output
            pass

    def start(self):
        """Start listening for the hotkey."""
        # Define the hotkey combination (Command+H on macOS)
        hotkey = keyboard.HotKey(
            keyboard.HotKey.parse('<cmd>+h'),
            self.on_hotkey
        )

        # Create listener
        self.listener = keyboard.Listener(
            on_press=lambda key: hotkey.press(self.listener.canonical(key)),
            on_release=lambda key: hotkey.release(self.listener.canonical(key))
        )

        with self.listener:
            self.listener.join()

    def _for_canonical(self, key):
        """
        Convert key to canonical form for hotkey matching.

        Args:
            key: The key event

        Returns:
            Canonical form of the key
        """
        try:
            return self.listener.canonical(key)
        except AttributeError:
            # Fallback for canonical conversion
            if hasattr(key, 'vk'):
                return keyboard.KeyCode.from_vk(key.vk)
            return key


def main():
    """Main entry point for the application."""
    emulator = TypingEmulator()

    try:
        # Start the hotkey listener (runs indefinitely)
        emulator.start()
    except KeyboardInterrupt:
        # Silent exit on Ctrl+C
        pass


if __name__ == '__main__':
    main()
