from app import create_app, db
from app.models import User, Question

app = create_app()


#  creates a shell context that adds the database instance and models to the shell session:
#  add the function, and you can work with database entities without having to import them
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Question': Question}