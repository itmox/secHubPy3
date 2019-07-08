import uuid;
from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker;
from helper.db.createDB import  Link, Base;

# Der link zum starten des Scans wird erstellt und in die Datenbank geschrieben
def genLink(content):
    engine = create_engine('sqlite:///securityHubDB.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    #to be replaced with a safe UUID
    linkId = str(uuid.uuid4())
    new_link = Link(link=linkId, content=content)
    session.add(new_link)
    session.commit()
    return linkId;