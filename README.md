# Human-like Typing Emulator

A Python application that emulates human typing behavior by pasting clipboard content with realistic timing patterns. Perfect for scenarios where you need to type text naturally without obvious copy-paste detection.

## Features

- **Human-like typing patterns**: Variable delays between keystrokes, occasional pauses, and word boundary detection
- **Hotkey activation**: Press Command+H to start typing clipboard content
- **100% accuracy**: Types exactly what's in your clipboard with no errors
- **Fully configurable**: Adjust typing speed and patterns via `.env` file
- **Silent operation**: Runs quietly in the background with no console output
- **Persistent listener**: Start once and use repeatedly until you close the program

## Installation

1. **Install Python dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Configure settings** (optional):
   - Copy `.env.example` to `.env` if you want custom settings
   - The default `.env` file already has sensible defaults
   - Edit `.env` to adjust typing speed and patterns

## Usage

1. **Start the application**:
   ```bash
   python3 emulation.py
   ```

2. **Copy text to clipboard**:
   - Copy any text you want to type (Command+C)

3. **Position your cursor**:
   - Click in the text field where you want the text to appear

4. **Trigger typing**:
   - Press **Command+H** to start typing

5. **Stop the application**:
   - Press **Ctrl+C** in the terminal to quit
   - The process automatically ends when you shut down your computer

## Configuration

Edit the `.env` file to customize typing behavior:

### Typing Speed

Adjust these values to control overall typing speed (all values in seconds):

```env
MIN_KEYSTROKE_DELAY=0.05    # Minimum delay between characters
MAX_KEYSTROKE_DELAY=0.15    # Maximum delay between characters
```

**Speed Presets**:
- **Fast**: MIN=0.03, MAX=0.08
- **Medium** (default): MIN=0.05, MAX=0.15
- **Slow**: MIN=0.1, MAX=0.25

### Human-like Patterns

```env
PAUSE_CHANCE=0.1            # Probability of taking a longer pause (0.0-1.0)
PAUSE_MIN=0.3               # Minimum pause duration
PAUSE_MAX=0.8               # Maximum pause duration
WORD_BOUNDARY_DELAY=0.1     # Extra delay after spaces/punctuation
```

### Applying Changes

After editing `.env`, restart the application for changes to take effect:
1. Press **Ctrl+C** to stop
2. Run `python3 emulation.py` again

## How It Works

The emulator creates realistic typing patterns by:

1. **Variable keystroke timing**: Each character has a random delay between MIN and MAX
2. **Word boundary detection**: Adds extra delay after spaces and punctuation
3. **Random pauses**: Occasionally inserts longer pauses to simulate reading/thinking
4. **No errors**: Types with 100% accuracy (no typo simulation)

## Requirements

- Python 3.6 or higher
- macOS (Command key support)
- Dependencies listed in `requirements.txt`

## Troubleshooting

**Hotkey not working?**
- Make sure the application is running (you should see the terminal window)
- Check that your system allows Python to control keyboard input
- On macOS, you may need to grant accessibility permissions in System Preferences > Security & Privacy > Privacy > Accessibility

**Typing too fast/slow?**
- Edit the `.env` file and adjust MIN_KEYSTROKE_DELAY and MAX_KEYSTROKE_DELAY
- Restart the application after making changes

**Nothing happens when pressing Command+H?**
- Ensure you have text in your clipboard
- The application runs silently - there's no confirmation message
- Try copying text and pressing Command+H again

## License

Free to use and modify as needed.
