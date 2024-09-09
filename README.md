---

# Movie Storage System

## Overview

A movie storage system supporting JSON and CSV formats. Features include adding, deleting, updating, listing movies, and generating an HTML website.

## Features

- Store and manage movies (JSON/CSV)
- Add, delete, update, and list movies
- Search, calculate statistics, and generate HTML

## Usage

1. **Select Storage Format** in `main.py`:

   ```python
   from storage_json import StorageJson
   from storage_csv import StorageCsv
   from movie_app import MovieApp

   def main():
       choice = int(input("Choose storage method:\n1. JSON\n2. CSV\nEnter choice (1 or 2): "))
       storage = StorageJson('movies.json') if choice == 1 else StorageCsv('movies.csv')
       movie_app = MovieApp(storage)
       movie_app.run()

   if __name__ == "__main__":
       main()
   ```

2. **Run the Application**:

   ```bash
   python main.py
   ```

## Testing

- For JSON: `python test_storage_json.py`
- For CSV: `python test_storage_csv.py`

---
