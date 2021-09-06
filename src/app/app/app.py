from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Artist(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  artist_name = db.Column(db.String(32))

  def __init__(self, id, artist_name):
    self.id = id
    self.artist_name = artist_name


class ArtistSchema(ma.Schema):
  class Meta:
    fields = ('id', 'artist_name')

artist_schema = ArtistSchema()
artists_schema = ArtistSchema(many = True)


class ArtistManager(Resource):
  @staticmethod
  def get():
    try: id = request.args['id']
    except Exception as _: id = None

    if not id:
      artists = Artist.query.all()
      return jsonify(artists_schema.dump(artists))
    artist = Artist.query.get(id)
    return jsonify(artist_schema.dump(artist))

  @staticmethod
  def post():
    artist_name = request.json['artist_name']

    artist = Artist(id, artist_name)
    db.session.add(artist)
    db.session.commit()
    return jsonify({
      'Message': f'Artist {artist_name} has been added'
    })


  @staticmethod
  def put():
    try: id = request.args['id']
    except Exception as _: id = None

    if not id:
      return jsonify({'Message': 'Must provide an Artist ID'})

    artist = Artist.query.get(id)
    artist_name = request.json['artist_name']
    
    artist.artist_name = artist_name
    
    db.session.commit()
    return jsonify({
        'Message': f'Artist {artist_name} updated'
    })

  @staticmethod
  def delete():
    try: id = request.args['id']
    except Exception as _: id = None

    if not id:
      return jsonify({'Message': 'Must provide an Artist ID'})

    artist = Artist.query.get(id)
    db.session.delete(artist)
    db.session.commit()

    return jsonify({'Message': f'Artist {str(artist)} was deleted'})

api.add_resource(ArtistManager, '/api/v2/artists')

if __name__ == '__main__':
  app.run(debug = True)