from models import  Dog

# takes a declarative_base and creates a SQLite database
def create_table(base, engine):
    base.metadata.create_all(engine)

# takes a Dog instance as an argument and saves the dog to the database
def save(session, dog):
    session.add(dog)
    session.commit()

# takes a session and returns a list of Dog instances for every record in the database.
def get_all(session):
    return session.query(Dog).all()

# takes a session and name and returns a Dog instance corresponding to its database record retrieved by name
def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

# takes a session and id and returns a Dog instance corresponding to its database record retrieved by id
def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

# takes a session, a name, and a breed as arguments and returns a Dog instance matching that record
def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()

# takes a session instance, and breed as arguments and updates the instance's breed
def update_breed(session, dog, breed):
    dog.breed = breed
    session.add(dog)
    session.commit()