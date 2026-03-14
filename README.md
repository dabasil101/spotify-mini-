# 🎵 Spotify-Mini

A sleek, "Pill-style" mini-player for Spotify on Linux. Designed to stay out of your way while keeping your music controls and progress visible at a glance.

![alt text](<Screenshot from 2026-03-15 00-51-52.png>) ![alt text](<Screenshot from 2026-03-15 00-54-31.png>) ![alt text](<Screenshot from 2026-03-15 02-38-01.png>) ![alt text](<Screenshot from 2026-03-15 02-38-39.png>)

![License](https://img.shields.io/badge/license-MIT-purple)
![Platform](https://img.shields.io/badge/platform-Linux-blue)
![Python](https://img.shields.io/badge/python-3.12-blueviolet)

## ✨ Features

- **Minimalist "Pill" UI**: A floating, rounded bar that fits perfectly into any "riced" Linux setup.
- **Real-time Progress**: Visual progress bar tracking your current track position.
- **Zero-Config**: Communicates directly with Spotify via DBus (no API keys required).
- **Draggable**: Position it anywhere on your screen.
- **Clean Interface**: Control buttons are integrated into the design, with administrative options (like Close) tucked away in a **Right-Click Context Menu**.
- **Always on Top**: Stays visible above your workspace for quick access.

## 🚀 Installation

### Prerequisites

Ensure you have the following installed on your system:
- Spotify (Desktop client)
- Python 3.12+
- `pydbus` for system communication
- `tkinter` for the GUI

```bash
pip install pydbus
