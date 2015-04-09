from app import db
from models import BlogPost

# Create the database and the db tables
db.create_all()

# insert into the database
db.session.add(BlogPost("Good", "I'm good."))
db.session.add(BlogPost("Well", "I'm Well."))
db.session.add(BlogPost("Fine", "I'm Fine."))
db.session.add(BlogPost("postgres", "we setup a local postgres"))

# Commit the changes
db.session.commit()
