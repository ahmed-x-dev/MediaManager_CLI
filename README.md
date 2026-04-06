# 📚 Terminal Media Library

A powerful terminal-based Python library for managing your personal media collection including shows, games, and manga. Organize, track, and manage all your entertainment in one place with a simple command-line interface.

## 🎯 Overview

Terminal Media Library is a lightweight, terminal-native application designed for media enthusiasts. Manage your entire entertainment collection—TV shows, video games, and manga—directly from your terminal. Store data persistently using JSON, and enjoy a clean, intuitive interface for all your library management needs.

## ✨ Features

- 📺 **Multi-Media Support** - Manage shows, games, and manga in one unified library
- ➕ **Add Items** - Easily add new media with metadata (title, genre, status, rating, etc.)
- ✏️ **Edit Items** - Update details of existing media entries
- ❌ **Remove Items** - Delete items you no longer want to track
- 💾 **Persistent Storage** - All data saved in JSON format for easy backup and portability
- 🔍 **Search & Filter** - Find media by title, genre, or status
- 📊 **View Library** - Display your entire collection in a formatted list
- ⚡ **Fast & Lightweight** - No heavy dependencies, pure Python solution

## 📋 Requirements

- Python 3.8+
- See `requirements.txt` for dependencies

## 🚀 Quick Start

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ahmed-x-dev/List_app.git
   cd List_app
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Launch the application:
```bash
python list_app.py
```

**With custom configuration:**
```bash
python list_app.py --config config.json
```

**Get help:**
```bash
python list_app.py --help
```

## 📁 Project Structure

```
List_app/
├── README.md                 # This file
├── requirements.txt          # Project dependencies
├── list_app.py              # Main application script
├── config.json              # Configuration file
├── database/                # Data storage
│   └── library.json         # Media library database
└── modules/                 # Core library modules
    ├── media.py             # Media class definitions
    ├── database.py          # Database operations
    └── utils.py             # Utility functions
```

## ⚙️ Configuration

Edit `config.json` to customize the application:

```json
{
  "database_path": "./database/library.json",
  "theme": "dark",
  "items_per_page": 20,
  "default_media_type": "show",
  "auto_backup": true,
  "backup_dir": "./backups/"
}
```

### Configuration Options

| Option | Type | Description |
|--------|------|-------------|
| `database_path` | string | Location of JSON database file |
| `theme` | string | UI theme (dark, light) |
| `items_per_page` | integer | Items displayed per page in list view |
| `default_media_type` | string | Default media type (show, game, manga) |
| `auto_backup` | boolean | Automatically backup database |
| `backup_dir` | string | Directory for backup files |

## 📊 Data Structure

Your media library is stored in JSON format:

```json
{
  "library": [
    {
      "id": 1,
      "type": "show",
      "title": "Breaking Bad",
      "genre": "Drama/Crime",
      "status": "Completed",
      "rating": 9.5,
      "episodes_watched": 62,
      "date_added": "2026-01-15"
    },
    {
      "id": 2,
      "type": "game",
      "title": "Elden Ring",
      "genre": "Action RPG",
      "status": "In Progress",
      "rating": 9.0,
      "hours_played": 45,
      "date_added": "2026-02-20"
    },
    {
      "id": 3,
      "type": "manga",
      "title": "Attack on Titan",
      "genre": "Action/Fantasy",
      "status": "Reading",
      "rating": 8.5,
      "chapters_read": 139,
      "date_added": "2026-03-01"
    }
  ]
}
```

## 🛠️ Technologies Used

- **Python 3.8+** - Core language
- **JSON** - Lightweight data storage
- **Argparse** - Command-line interface

## 📝 Example Usage

### Interactive Menu

```
╔════════════════════════════════════════╗
║    Terminal Media Library v1.0         ║
╚════════════════════════════════════════╝

1. View Library
2. Add New Item
3. Search Item
4. Edit Item
5. Delete Item
6. Export Library
7. Import Library
8. Exit

Choose an option: _
```

### Python API

```python
from list_app import MediaLibrary

# Initialize library
library = MediaLibrary(config_file='config.json')

# Add a show
library.add_item(
    item_type='show',
    title='Stranger Things',
    genre='Sci-Fi/Drama',
    status='Completed',
    rating=8.7
)

# Search items
results = library.search('Stranger Things')

# Edit item
library.edit_item(item_id=1, rating=9.0, episodes_watched=42)

# View all items
all_items = library.get_all_items()

# Export library
library.export_to_csv('library_export.csv')
```

## 🎮 Supported Media Types

| Type | Fields |
|------|--------|
| **Show** | Title, Genre, Status, Rating, Episodes Watched, Seasons |
| **Game** | Title, Genre, Status, Rating, Hours Played, Platform |
| **Manga** | Title, Genre, Status, Rating, Chapters Read, Volumes |

## 🐛 Troubleshooting

**Database file not found:**
- Ensure the `database_path` in config.json is correct
- Run initialization command to create a new database

**Encoding errors:**
- Check that your terminal supports UTF-8
- Update locale settings if needed

**Permission errors:**
- Ensure read/write permissions on the database directory
- Check file ownership and permissions

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes thoroughly
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## ⚡ Tips & Best Practices

- **Regular Backups** - Enable auto-backup feature or manually export your library
- **Consistent Naming** - Use consistent titles and genres for better searchability
- **Update Regularly** - Keep your library current with your viewing/playing progress
- **Export Regularly** - Export your library as a CSV backup separate from JSON
- **Use Meaningful Status** - Use clear status labels (Completed, In Progress, Planned, Dropped)
- **Rate Fairly** - Use consistent rating criteria for all media

## 📚 Supported Status Values

- ✅ **Completed** - Finished watching/reading/playing
- ⏳ **In Progress** - Currently watching/reading/playing
- 📋 **Planned** - Want to watch/read/play
- ❌ **Dropped** - Stopped watching/reading/playing
- ⏸️ **On Hold** - Temporarily paused

## 📞 Support & Questions

For issues or questions:
- Check existing issues on GitHub
- Create a new issue with detailed description
- Include error messages and steps to reproduce
- Attach your `library.json` if relevant (redact sensitive data)

## 🚀 Future Features

- 🌐 Web interface
- 📱 Mobile app
- ☁️ Cloud sync
- 🔐 User accounts
- 📈 Statistics and insights
- 🏷️ Advanced tagging system

---

**Enjoy organizing your media collection! 🎬🎮📖**