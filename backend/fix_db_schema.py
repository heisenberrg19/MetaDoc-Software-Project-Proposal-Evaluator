import sys
import os

# Add the project directory to sys.path
sys.path.append(os.getcwd())

from app import create_app
from app.core.extensions import db
from sqlalchemy import text

app = create_app()

with app.app_context():
    print("Checking Rubric table schema...")
    try:
        # Check for missing columns
        db.session.execute(text("ALTER TABLE rubrics ADD COLUMN system_instructions TEXT"))
        print("Added column: system_instructions")
    except Exception as e:
        print(f"Column system_instructions might already exist or error: {e}")

    try:
        db.session.execute(text("ALTER TABLE rubrics ADD COLUMN evaluation_goal TEXT"))
        print("Added column: evaluation_goal")
    except Exception as e:
        print(f"Column evaluation_goal might already exist or error: {e}")
        
    db.session.commit()
    print("Schema update complete.")
