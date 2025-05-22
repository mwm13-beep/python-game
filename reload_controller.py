import time
from pathlib import Path
from queue import Queue
from threading import Thread
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import json
from pathlib import Path
import os
import signal
import queue

# === Configuration ===
SOURCE_DIR = Path("./source")
SITE_PACKAGES_DIR = Path("./venv/lib/python3.9/site-packages")  # Adjust if needed
GAME_CMD = "python -m source.main"

# === Message Queue ===
event_queue = Queue()

# === Process Lifecycle ===
running_proc = None

# === Watchdog Event Handler ===
class TriggerHandler(FileSystemEventHandler):
    def __init__(self, tag):
        self.tag = tag  # "source" or "packages"

    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"[WATCHER] {self.tag} file changed: {event.src_path}")
        event_queue.put(self.tag)

# === Game Start and restart logic ===
def start_restart_game():
    global running_proc

    if running_proc and running_proc.poll() is None:
        print("[RELOAD] Terminating previous game...")
        try:
            os.killpg(os.getpgid(running_proc.pid), signal.SIGTERM)
            running_proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            print("[RELOAD] Timeout. Killing...")
            os.killpg(os.getpgid(running_proc.pid), signal.SIGKILL)
            running_proc.wait()

    running_proc = subprocess.Popen(
        GAME_CMD,
        shell=True,
        preexec_fn=os.setsid
    )
    print(f"[RELOAD] Started game (PID: {running_proc.pid})")

# === Threaded Watcher Setup ===
def start_watcher(path: Path, tag: str):
    observer = Observer()
    handler = TriggerHandler(tag)
    observer.schedule(handler, str(path), recursive=True)
    observer.start()
    return observer

# === Message Loop ===
def dispatcher_loop(watch_config):
    debounce_state = {}
    while True:
        try:
            tag = event_queue.get(timeout=1)  # Waits 1 second for new events
            now = time.time()
            last = debounce_state.get(tag, 0)
            debounce_time = watch_config.get(tag, {}).get("debounce", 1)

            if now - last >= debounce_time:
                debounce_state[tag] = now
                print(f"[RELOAD] Handling {tag} change (debounce = {debounce_time}s)...")
                start_restart_game()
            else:
                print(f"[DEBOUNCE] Skipping {tag} — triggered too soon")
        except queue.Empty:
            continue  # Timeout occurred, go back to waiting

# === Main function handles set up ===
observers = []

def main():
    # Load the config
    with open("watch_config.json", "r") as f:
        watch_config = json.load(f)

    # 🔧 Start the initial game process
    print("[INIT] Starting initial game process...")
    start_restart_game()

    # Start all observers
    print("[INIT] Starting observers...")
    for tag, opts in watch_config.items():
        path_str = opts.get("path")
        if not path_str:
            print(f"[WARN] No path for tag: {tag}")
            continue
        observer = start_watcher(Path(path_str), tag)
        observers.append(observer)

    # Start dispatcher
    print("[INIT] Starting dispatcher loop...")
    dispatch_thread = Thread(target=dispatcher_loop(watch_config), daemon=True)
    dispatch_thread.start()

    # Lifecycle management
    print("[DEBUG] Main thread entering lifecycle loop")
    while True:
        time.sleep(1)

# === Shutdown logic ===
def shutdown():
        print("\n[EXIT] Stopping...", flush=True)
        for observer in observers:
            observer.stop()
        for observer in observers:
            observer.join()
        if running_proc:
            try:
                print("[RELOAD] Terminating previous game...")
                os.killpg(os.getpgid(running_proc.pid), signal.SIGTERM)
                running_proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                print("[RELOAD] Timeout. Killing...")
                os.killpg(os.getpgid(running_proc.pid), signal.SIGKILL)
                running_proc.wait()

# === Handles Keyboard Interrupts ===
try:
    main()
except KeyboardInterrupt:
    shutdown()
    print("\n[EXIT] Global shutdown complete.")
