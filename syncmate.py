import os
import subprocess
import winreg

class SyncMate:
    def __init__(self):
        self.startup_registry_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        self.registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        self.startup_programs = self.get_startup_programs()

    def get_startup_programs(self):
        programs = {}
        try:
            with winreg.OpenKey(self.registry, self.startup_registry_path) as key:
                for i in range(0, winreg.QueryInfoKey(key)[1]):
                    name, path, _ = winreg.EnumValue(key, i)
                    programs[name] = path
        except WindowsError:
            pass
        return programs

    def list_startup_programs(self):
        print("Startup Programs:")
        for name, path in self.startup_programs.items():
            print(f"{name}: {path}")

    def disable_startup_program(self, program_name):
        try:
            with winreg.OpenKey(self.registry, self.startup_registry_path, 0, winreg.KEY_SET_VALUE) as key:
                winreg.DeleteValue(key, program_name)
            print(f"Disabled {program_name} from startup.")
        except FileNotFoundError:
            print(f"{program_name} not found in startup programs.")
        except WindowsError as e:
            print(f"Error disabling {program_name}: {e}")

    def add_startup_program(self, program_name, program_path):
        try:
            with winreg.OpenKey(self.registry, self.startup_registry_path, 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, program_name, 0, winreg.REG_SZ, program_path)
            print(f"Added {program_name} to startup.")
        except WindowsError as e:
            print(f"Error adding {program_name} to startup: {e}")

    def optimize_startup(self):
        print("Optimizing startup programs...")
        # Example logic for optimization: disable all except essential
        essential_programs = ['SecurityHealth', 'Windows Defender']
        for name in list(self.startup_programs.keys()):
            if name not in essential_programs:
                self.disable_startup_program(name)
        print("Optimization complete.")

def main():
    syncmate = SyncMate()
    syncmate.list_startup_programs()
    syncmate.optimize_startup()
    syncmate.list_startup_programs()

if __name__ == "__main__":
    main()