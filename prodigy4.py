# in_app_keylogger.py
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime
import os
import subprocess
import sys

DEFAULT_LOGFILE = "app_keystrokes_log.txt"

class AppKeyLogger:
    def __init__(self, root):
        self.root = root
        root.title("In-App Key Logger (Consent required)")

        # Ask for explicit consent before doing anything
        consent = messagebox.askyesno(
            "Consent required",
            "This app will record keys typed INSIDE this window and save them to a file.\n\n"
            "Do you consent to this and are you the owner of this machine / have permission?"
        )
        if not consent:
            messagebox.showinfo("No consent", "Consent not given. Exiting.")
            root.destroy()
            return

        self.logfile = DEFAULT_LOGFILE
        self.logging_enabled = True  # default on; show controls to toggle

        # Top frame: show current log file and let user choose another
        top_frame = tk.Frame(root)
        top_frame.pack(fill='x', pady=6)
        tk.Label(top_frame, text="Log file:").pack(side='left')
        self.log_label = tk.Label(top_frame, text=self.logfile)
        self.log_label.pack(side='left', padx=6)
        tk.Button(top_frame, text="Choose file...", command=self.choose_file).pack(side='right')

        # Main typing area
        self.text = tk.Text(root, width=80, height=20)
        self.text.pack(padx=10, pady=6)
        self.text.insert("end", "Type here. Keystrokes will be logged to the file above.\n")

        # Buttons: start/stop logging, open log
        btn_frame = tk.Frame(root)
        btn_frame.pack(fill='x', pady=6)
        tk.Button(btn_frame, text="Start logging", command=lambda: self.set_logging(True)).pack(side='left', padx=4)
        tk.Button(btn_frame, text="Stop logging", command=lambda: self.set_logging(False)).pack(side='left', padx=4)
        tk.Button(btn_frame, text="Open log", command=self.open_log).pack(side='right', padx=4)

        # Bind key events only for this text widget (so we capture only in-app typing)
        self.text.bind("<Key>", self.on_key)

    def choose_file(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                                            initialfile=self.logfile)
        if path:
            self.logfile = path
            self.log_label.config(text=self.logfile)

    def set_logging(self, val: bool):
        self.logging_enabled = val
        status = "ON" if val else "OFF"
        messagebox.showinfo("Logging", f"Logging turned {status} (only inside this window).")

    def on_key(self, event):
        """Handle key events. We log a simple line: timestamp <TAB> key_name_or_char"""
        if not self.logging_enabled:
            return

        # Prefer printable character; fall back to keysym for control keys
        key_repr = event.char if event.char and event.char != '\x00' else event.keysym
        timestamp = datetime.utcnow().isoformat() + "Z"
        entry = f"{timestamp}\t{key_repr}\n"

        try:
            # append each event (keeps implementation simple and robust)
            with open(self.logfile, "a", encoding="utf-8") as f:
                f.write(entry)
        except Exception as e:
            # Do not spam GUI with errors; print so developer can see
            print("Failed to write log:", e)

    def open_log(self):
        """Open the log file in the system default editor (best-effort)."""
        if not os.path.exists(self.logfile):
            messagebox.showinfo("No log", "Log file does not exist yet.")
            return
        try:
            if sys.platform.startswith("win"):
                os.startfile(self.logfile)
            elif sys.platform == "darwin":
                subprocess.run(["open", self.logfile])
            else:
                subprocess.run(["xdg-open", self.logfile])
        except Exception as e:
            messagebox.showerror("Error", f"Could not open log file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppKeyLogger(root)
    root.mainloop()