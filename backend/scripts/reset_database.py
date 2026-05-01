"""
Database Reset Script for MetaDoc

This script will:
1. Close all database connections
2. Delete the existing database file
3. Create a fresh database with all tables

Usage:
    python reset_database.py
"""

import os
import sys

# Add parent directory to path so we can import app
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, BACKEND_DIR)

# Get the database path (in backend directory, not scripts directory)
DB_PATH = os.path.join(BACKEND_DIR, 'metadoc.db')

print("=" * 60)
print("MetaDoc Database Reset")
print("=" * 60)
print(f"\nDatabase path: {DB_PATH}")

# Check if database exists
if os.path.exists(DB_PATH):
    print(f"Database file found: {os.path.getsize(DB_PATH)} bytes")
    
    # Try to delete the database
    try:
        os.remove(DB_PATH)
        print("[+] Database file deleted successfully")
    except PermissionError:
        print("\n[!] ERROR: Database file is locked by another process")
        print("\nPlease:")
        print("1. Stop the backend server (Ctrl+C in the terminal)")
        print("2. Wait a few seconds")
        print("3. Run this script again")
        sys.exit(1)
    except Exception as e:
        print(f"\n[X] Error deleting database: {e}")
        sys.exit(1)
else:
    print("No existing database found")

# Create fresh database
print("\nCreating fresh database...")

try:
    from app import create_app, db
    
    app = create_app()
    
    with app.app_context():
        # Drop all tables first to ensure a clean state
        print("Dropping all existing tables...")
        db.drop_all()
        print("[+] All tables dropped successfully")
        
        # Create all tables
        print("Creating fresh tables...")
        db.create_all()
        print("[+] Database tables created successfully")
        
        # Clear storage directories
        import shutil
        storage_dirs = [
            app.config.get('UPLOAD_FOLDER'),
            app.config.get('TEMP_STORAGE_PATH'),
            app.config.get('REPORTS_STORAGE_PATH')
        ]
        
        print("\nCleaning storage directories...")
        for directory in storage_dirs:
            if directory and os.path.exists(directory):
                # Don't delete the directory itself, just the contents
                for filename in os.listdir(directory):
                    file_path = os.path.join(directory, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                        print(f"  - Deleted: {file_path}")
                    except Exception as e:
                        print(f"  - Failed to delete {file_path}. Reason: {e}")
        print("[+] Storage directories cleaned successfully")
        
        # Verify tables
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        
        print(f"\nCreated {len(tables)} tables:")
        for table in tables:
            print(f"  - {table}")
    
    print("\n" + "=" * 60)
    print("Database reset and storage cleanup complete!")
    print("=" * 60)
    print("\nYou can now start the backend server:")
    print("  python run.py")
    
except Exception as e:
    print(f"\n[X] Error resetting database: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
