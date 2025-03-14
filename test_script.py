from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker  
from lib.models import User, Note  # Adjust this import according to your folder structure  

# Set up the database connection  
engine = create_engine('sqlite:///personal_notes.db')  
Session = sessionmaker(bind=engine)  
session = Session()  

# --- Test User Methods ---  
try:  
    # Create a User  
    print("Creating user...")  
    user = User.create(session, "John Doe")  
    print(f"User created: ID={user.id}, Name={user.name}")  

    # List all users  
    print("\nListing all users...")  
    users = User.get_all(session)  
    for u in users:  
        print(f"User(ID={u.id}, Name={u.name})")  

    # Delete a User  
    print(f"\nDeleting user ID={user.id}...")  
    success = User.delete(session, user.id)  
    print("User deleted." if success else "User not found.")  

except Exception as e:  
    print(f"Error: {e}")  

# --- Test Note Methods ---  
try:  
    # Create a Note  
    print("\nCreating note...")  
    note = Note.create(session, "Sample Note", "This is the content of the note.", user.id)  
    print(f"Note created: ID={note.id}, Title={note.title}, User ID={note.user_id}")  

    # List all notes  
    print("\nListing all notes...")  
    notes = Note.get_all(session)  
    for n in notes:  
        print(f"Note(ID={n.id}, Title={n.title}, User ID={n.user_id})")  

    # Delete a Note  
    print(f"\nDeleting note ID={note.id}...")  
    success = Note.delete(session, note.id)  
    print("Note deleted." if success else "Note not found.")  

except Exception as e:  
    print(f"Error: {e}")  

# Close the session  
session.close()  
