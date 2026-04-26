import sys
import os
sys.path.append(os.getcwd())

from app import create_app
from app.core.extensions import db
from app.models.rubric import Rubric

app = create_app()
with app.app_context():
    try:
        # Create all tables including the new rubrics table
        db.create_all()
        print("Database tables created successfully, including rubrics.")
    except Exception as e:
        print(f"Error creating tables: {e}")
