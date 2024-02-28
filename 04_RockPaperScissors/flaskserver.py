from flask import request, Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class count_score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    score = db.Column(db.Integer, nullable=False)

class count_symboles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    schere_count = db.Column(db.Integer, nullable=False)
    stein_count = db.Column(db.Integer, nullable=False)
    papier_count = db.Column(db.Integer, nullable=False)
    echse_count = db.Column(db.Integer, nullable=False)
    spock_count = db.Column(db.Integer, nullable=False)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/set_score", methods=['POST'])
def set_score():
    if request.method == 'POST':
        data = request.json
        user_name = data.get('user_name')
        new_score = data.get('score')

        # Fetch the existing record or create a new one if not exists
        user_score = count_score.query.filter_by(user_name=user_name).first()
        if user_score:
            user_score.score = new_score
        else:
            user_score = count_score(user_name=user_name, score=new_score)
            db.session.add(user_score)

        # Commit changes to the database
        db.session.commit()
        return "Score updated successfully!"


@app.route("/get_score", methods=['GET'])
def get_score():
    if request.method == 'GET':
        user_name = request.args.get('user_name')
        user_score = count_score.query.filter_by(user_name=user_name).first()
        if user_score:
            return f"User: {user_score.user_name}, Score: {user_score.score}"
        else:
            return "User not found!"

# create an increase score method
@app.route("/update_score", methods=['POST'])
def update_score():
    if request.method == 'POST':
        data = request.json
        user_name = data.get('user_name')


        # Fetch the existing record or create a new one if not exists
        user_score = count_score.query.filter_by(user_name=user_name).first()
        if user_score:
            user_score.score = user_score.score + 33
        else:
            user_score = count_score(user_name=user_name, score=33)
            db.session.add(user_score)
            user_symboles = count_symboles(user_name=user_name, schere_count=0, stein_count=0, papier_count=0, echse_count=0, spock_count=0)
            db.session.add(user_symboles)

        # Commit changes to the database
        db.session.commit()
        return "Score updated successfully!"


#delete score method
@app.route("/delete_score", methods=['POST'])
def delete_score():
    if request.method == 'POST':
        data = request.json
        user_name = data.get('user_name')
        user_score = count_score.query.filter_by(user_name=user_name).first()
        if user_score:
            db.session.delete(user_score)
            db.session.commit()
            return "Score deleted successfully!"
        else:
            return "User not found!"

# set symboles count
@app.route("/set_symboles", methods=['POST'])
def set_symboles():
    if request.method == 'POST':
        data = request.json
        user_name = data.get('user_name')
        schere_count = data.get('schere_count')
        stein_count = data.get('stein_count')
        papier_count = data.get('papier_count')
        echse_count = data.get('echse_count')
        spock_count = data.get('spock_count')

        # Fetch the existing record or create a new one if not exists
        user_symboles = count_symboles.query.filter_by(user_name=user_name).first()
        if user_symboles:
            user_symboles.schere_count = schere_count
            user_symboles.stein_count = stein_count
            user_symboles.papier_count = papier_count
            user_symboles.echse_count = echse_count
            user_symboles.spock_count = spock_count
        else:
            user_symboles = count_symboles(user_name=user_name, schere_count=schere_count, stein_count=stein_count, papier_count=papier_count, echse_count=echse_count, spock_count=spock_count)
            db.session.add(user_symboles)

        # Commit changes to the database
        db.session.commit()
        return "Symboles count updated successfully!"

#get symboles count
@app.route("/get_symboles", methods=['GET'])
def get_symboles():
    if request.method == 'GET':
        user_name = request.args.get('user_name')
        user_symboles = count_symboles.query.filter_by(user_name=user_name).first()
        if user_symboles:
            return f"User: {user_symboles.user_name}, Schere: {user_symboles.schere_count}, Stein: {user_symboles.stein_count}, Papier: {user_symboles.papier_count}, Echse: {user_symboles.echse_count}, Spock: {user_symboles.spock_count}"
        else:
            return "User not found!"

# update symboles count here i want to provide  the name of the field that should be inremented by one
@app.route("/update_symboles", methods=['POST'])
def update_symboles():
    if request.method == 'POST':
        data = request.json
        user_name = data.get('user_name')
        field_name = data.get('field_name')
        user_symboles = count_symboles.query.filter_by(user_name=user_name).first()
        if user_symboles:
            if field_name == "schere_count":
                user_symboles.schere_count += 1
            elif field_name == "stein_count":
                user_symboles.stein_count += 1
            elif field_name == "papier_count":
                user_symboles.papier_count += 1
            elif field_name == "echse_count":
                user_symboles.echse_count += 1
            elif field_name == "spock_count":
                user_symboles.spock_count += 1
            db.session.commit()
            return "Symboles count updated successfully!"
        else:
            return "User not found!"

@app.route("/delete_symboles", methods=['POST'])
def delete_symboles():
    if request.method == 'POST':
        data = request.json
        user_name = data.get('user_name')
        user_symboles = count_symboles.query.filter_by(user_name=user_name).first()
        if user_symboles:
            db.session.delete(user_symboles)
            db.session.commit()
            return "Symboles count deleted successfully!"
        else:
            return "User not found!"





if __name__ == "__main__":
    app.run()
