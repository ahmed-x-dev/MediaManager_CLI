# 📚 Terminal Media Library
# 📚 Terminal Media Library

A lightweight terminal-based media library to organize your **games, movies, series, and manga** all in one place. Manage your entertainment collection with ease using a simple CLI interface and persistent JSON storage.

---

## ✨ Features

- 🎮 **Multi-section support** — Organize games, movies/series, and manga separately
- ➕ **Add items** — Quick and easy item entry with metadata
- ✏️ **Edit items** — Update any item details at any time
- 🗑️ **Remove items** — Delete items you no longer want
- 💾 **Persistent storage** — All data saved in JSON format
- 🖥️ **Terminal UI** — Clean, interactive command-line interface
- 🔌 **API Integration** — Connect to external APIs for data retrieval

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone or download this repository:
   ```bash
   git clone <repository-url>
   cd List_app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure API keys (optional):
   - Edit `config.py` with your API keys:
     ```python
     shows_api = "your_api_key_here"
     games_api = "your_api_key_here"
     ```

### Usage

Run the application:
```bash
python main.py
```

Follow the on-screen menu to:
1. Select a section (Games, Movies & Series, or Manga)
2. View all items in that section
3. Add, edit, or delete items as needed
4. Exit when done

---

## 📁 Project Structure

```
List_app/
├── main.py              # Main application entry point
├── config.py            # API configuration keys
├── libirary.py          # Core library operations
├── info_from_APIs.py    # API integration module
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── data/
    └── library.json     # JSON database storage
```

---

## 📝 Database

Your library data is stored in `data/library.json`. Each entry contains:
- Title
- Genre
- Status (Watching, Completed, On Hold, etc.)
- Additional metadata

---

## 🔧 Configuration

Edit `config.py` to add your API keys for enhanced functionality:
- `shows_api(OMDB)` — API key for movie/series data
- `games_api(RAWG)` — API key for game data

---

## 📖 Notes

- Data persists between sessions
- The menu is intuitive and user-friendly
- Invalid choices will prompt you to try again

---

## 💡 Future Enhancements

- Search and filter functionality
- Rating and review system
- Import/export features
- Statistics and analytics

---

## 📄 License

Open source project.
