# SyncMate

SyncMate is a Python-based utility designed to manage and optimize startup programs on Windows, thereby improving boot times and overall system responsiveness. By streamlining the startup process, SyncMate helps ensure that only essential applications are loaded during system boot-up.

## Features

- **List Startup Programs**: Displays all programs currently set to run at startup.
- **Disable Startup Programs**: Allows users to disable specific programs from launching at startup.
- **Add Startup Programs**: Enables adding new programs to the startup list.
- **Optimize Startup**: Automatically disables non-essential programs to enhance boot performance.

## Requirements

- Python 3.x
- Windows operating system

## Installation

Clone the repository to your local machine using:

```bash
git clone https://github.com/yourusername/syncmate.git
```

## Usage

Navigate to the directory where the file is located and run the script using Python:

```bash
python syncmate.py
```

- **List Startup Programs**: The script will display a list of programs currently set to run at startup.
- **Optimize Startup**: The `optimize_startup` method will disable non-essential programs, keeping only critical applications like Windows Defender.

## Contributing

Contributions are welcome! Please fork the repository and open a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

Use this tool at your own risk. Disabling certain startup programs could affect the performance or functionality of your system. Ensure you understand the role of each program before disabling it.