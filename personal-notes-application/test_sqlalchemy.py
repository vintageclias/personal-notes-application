from sqlalchemy import create_engine, text  

# Create a simple SQLite database connection  
engine = create_engine('sqlite:///:memory:')  

# Test connection  
with engine.connect() as connection:  
    # Use `text()` to create an executable SQL statement  
    result = connection.execute(text("SELECT 1"))  
    print(result.fetchone())  