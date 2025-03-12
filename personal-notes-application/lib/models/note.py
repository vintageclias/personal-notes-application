from sqlalchemy import Column, Integer, String, ForeignKey  
from sqlalchemy.orm import relationship  
from sqlalchemy.ext.declarative import declarative_base  

Base = declarative_base()  

class Note(Base):  
    __tablename__ = 'notes'  

    id = Column(Integer, primary_key=True)  
    title = Column(String, nullable=False)  
    content = Column(String, nullable=False)  
    user_id = Column(Integer, ForeignKey('users.id'))  

    user = relationship("User", back_populates="notes")  

    @classmethod  
    def create(cls, session, title, content, user_id):  
        note = cls(title=title, content=content, user_id=user_id)  
        session.add(note)  
        session.commit()  
        return note  

    @classmethod  
    def delete(cls, session, note_id):  
        note = session.query(cls).get(note_id)  
        if note:  
            session.delete(note)  
            session.commit()  
            return True  
        return False  

    @classmethod  
    def get_all(cls, session):  
        return session.query(cls).all()  

    @classmethod  
    def find_by_id(cls, session, note_id):  
        return session.query(cls).get(note_id)  