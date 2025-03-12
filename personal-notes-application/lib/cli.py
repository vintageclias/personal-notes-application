import click  
from sqlalchemy import create_engine  
from sqlalchemy.orm import sessionmaker  
from lib.models import User, Note  

# Set up the database connection  
engine = create_engine('sqlite:///personal_notes.db')  
Session = sessionmaker(bind=engine)  
session = Session()  

@click.group()  
def cli():  
    """Personal Notes CLI"""  
    pass  

@cli.command()  
@click.argument('name')  
def add_user(name):  
    """Add a new user."""  
    user = User.create(session, name)  
    click.echo(f"User '{user.name}' added with ID: {user.id}.")  

@cli.command()  
@click.argument('title')  
@click.argument('content')  
@click.argument('user_id')  
def add_note(title, content, user_id):  
    """Add a new note for a user."""  
    try:  
        note = Note.create(session, title, content, user_id)  
        click.echo(f"Note '{note.title}' added for user ID: {user_id}.")  
    except Exception as e:  
        click.echo(f"Failed to add note: {e}")  

@cli.command()  
def list_users():  
    """List all users."""  
    users = User.get_all(session)  
    if users:  
        click.echo("Users:")  
        for user in users:  
            click.echo(f"ID: {user.id}, Name: {user.name}")  
    else:  
        click.echo("No users found.")  

@cli.command()  
def list_notes():  
    """List all notes."""  
    notes = Note.get_all(session)  
    if notes:  
        click.echo("Notes:")  
        for note in notes:  
            click.echo(f"ID: {note.id}, Title: {note.title}, User ID: {note.user_id}")  
    else:  
        click.echo("No notes found.")  

@cli.command()  
@click.argument('user_id')  
def delete_user(user_id):  
    """Delete a user by ID."""  
    if User.delete(session, user_id):  
        click.echo(f"User ID {user_id} deleted.")  
    else:  
        click.echo("User not found or could not be deleted.")  

@cli.command()  
@click.argument('note_id')  
def delete_note(note_id):  
    """Delete a note by ID."""  
    if Note.delete(session, note_id):  
        click.echo(f"Note ID {note_id} deleted.")  
    else:  
        click.echo("Note not found or could not be deleted.")  

@cli.command()  
@click.argument('user_id')  
def view_user_notes(user_id):  
    """View all notes of a specified user."""  
    notes = session.query(Note).filter(Note.user_id == user_id).all()  
    if notes:  
        click.echo(f"Notes for User ID {user_id}:")  
        for note in notes:  
            click.echo(f"ID: {note.id}, Title: {note.title}, Content: {note.content}")  
    else:  
        click.echo(f"No notes found for User ID {user_id}.")  

if __name__ == "__main__":  
    cli()  