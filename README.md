# In-App Key Logger (Consent-Based)

This is a **safe, educational keylogger** built in Python using Tkinter.  
It **only records keys typed inside its own application window** and requires explicit user consent before starting.  
It is intended for learning about event handling and file I/O — **not** for any malicious or covert use.

---

## 🚨 Ethical & Legal Disclaimer
This program is provided for educational purposes **only**.  
Running any kind of keylogger without the **explicit, informed consent** of the person being monitored is illegal in many jurisdictions.

By using this code, you agree that:
- You own the device you run it on **or** you have written permission from the owner and all users.
- You will not modify it to capture keystrokes outside the application window.
- You will delete logs when they are no longer needed.
- You will comply with all local laws and organizational policies.

The author(s) take no responsibility for misuse.

---

## 🎯 Features
- **Consent prompt** before any logging.
- Logs only keys typed **inside the app's text area**.
- Start/stop logging anytime.
- Choose a custom log file location.
- Open log file in your system's default editor.
- Logs include UTC timestamp + key pressed.

---

## 📂 File Structure
```

in\_app\_keylogger.py   # Main Python script
app\_keystrokes\_log.txt # Default log file (created after first run)
README.md              # Project documentation

````

---

## 🛠 Requirements
- Python **3.8+** (Tkinter included in standard builds)
- Works on Windows, macOS, and Linux

---

## ▶ How to Run
1. Download or clone the repository.
2. Open a terminal/command prompt in the project folder.
3. Run:
   ```bash
   python in_app_keylogger.py
````

4. When prompted, click **Yes** to give consent.
5. Type in the text area — your keystrokes will be logged to the default file (`app_keystrokes_log.txt`) or a file you choose.

---

## 📜 Example Log Entry

```
2025-08-09T09:15:12.345678Z   H
2025-08-09T09:15:13.123456Z   e
2025-08-09T09:15:14.654321Z   l
2025-08-09T09:15:14.987654Z   l
2025-08-09T09:15:15.111111Z   o
2025-08-09T09:15:15.555555Z   Return
```

---

## 📌 How It Works

1. **Startup** – The program shows a consent dialog.
2. **Logging enabled** – If the user agrees, logging starts.
3. **Event binding** – The `<Key>` event is bound to the text area.
4. **On each key** – The key is recorded with a timestamp in the log file.
5. **Controls** – Buttons allow start/stop logging, choosing a log file, and opening it.

---

## ✅ Recommended Safe Uses

* Personal typing practice tracker.
* Educational demonstration for event handling in Python.
* Debugging input in your own GUI app.

```
