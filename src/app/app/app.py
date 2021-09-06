import flask
import flask_uuid
import psycopg2
from flask import Flask, request, jsonify
from flask_uuid import FlaskUUID
from psycopg2 import pool
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
FlaskUUID(app)

# Healthcheck
@app.route('/')
def index():
    return jsonify({'messsage': 'connection successful'}), 201

try:
    pgdb_conn_pool = psycopg2.pool.ThreadedConnectionPool(1, 20, host="postgres", user="musical", password="abcdefg", database="musicdb")

    # GET all
    @app.route('/artistlist', methods=['GET'])
    def get_artist_namelist():
        conn = pgdb_conn_pool.getconn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM artists")
        resp = cur.fetchall()
        cur.close()
        pgdb_conn_pool.putconn(conn)
        return jsonify(resp)

    @app.route('/albumlist', methods=['GET'])
    def get_album_list():
        conn = pgdb_conn_pool.getconn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM albums")
        resp = cur.fetchall()
        cur.close()
        pgdb_conn_pool.putconn(conn)
        return jsonify(resp)

    # POST
    @app.route('/postartist', methods=['POST'])
    def post_artist_name():
        req_data = request.get_json()
        _artist_name = req_data['artist_name']
        query = 'INSERT INTO artists(artist_name) VALUES(%s)'
        post_data = (_artist_name)
        conn = pgdb_conn_pool.getconn()
        cur = conn.cursor()
        cur.execute(query, post_data)
        conn.commit()
        cur.close()
        query = "SELECT * FROM artists WHERE artist_name = " + "'" + _artist_name + "'"
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(query)
        resp = cur.fetchall()
        cur.close()
        pgdb_conn_pool.putconn(conn)
        return jsonify(resp)

    # POST
    @app.route('/postalbum', methods=['POST'])
    def post_album_name():
        req_data = request.get_json()
        _artist_name = req_data['artist_name']
        _album_title = req_data['album_title']
        _release_date = req_data['release_date']
        _price = req_data['price']
        query = 'INSERT INTO albums(artist_name, album_title, release_date, price) VALUES(%s, %s, %s, %s)'
        post_data = (_artist_name, _album_title, _release_date, _price)
        conn = pgdb_conn_pool.getconn()
        cur = conn.cursor()
        cur.execute(query, post_data)
        conn.commit()
        cur.close()
        query = "SELECT * FROM albums WHERE album_title = " + "'" + _album_title + "'"
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute(query)
        resp = cur.fetchall()
        cur.close()
        pgdb_conn_pool.putconn(conn)
        return jsonify(resp)

    # GET
    @app.route('/getartist/<uuid:id>', methods=['GET'])
    def get_artist_name(id):
        conn = pgdb_conn_pool.getconn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        query = "SELECT * FROM artists where uuid::text = " + "'" + str(id) + "'"
        cur.execute(query)
        resp = cur.fetchone()
        cur.close()
        pgdb_conn_pool.putconn(conn)
        return jsonify(resp)

    # GET
    @app.route('/getalbum/<uuid:id>', methods=['GET'])
    def get_album_title(id):
        conn = pgdb_conn_pool.getconn()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        query = "SELECT * FROM albums where uuid::text = " + "'" + str(id) + "'"
        cur.execute(query)
        resp = cur.fetchone()
        cur.close()
        pgdb_conn_pool.putconn(conn)
        return jsonify(resp)

    # DELETE
    @app.route('/deleteartist/<uuid:id>', methods=['DELETE'])
    def delete_artist(id):
        conn = pgdb_conn_pool.getconn()
        cur = conn.cursor()
        query = "DELETE FROM artists WHERE uuid::text = " + "'" + str(id) + "'"
        cur.execute(query)
        resp = conn.commit()
        cur.close()
        pgdb_conn_pool.putconn(conn)
        return jsonify(resp)

    # DELETE
    @app.route('/deletealbum/<uuid:id>', methods=['DELETE'])
    def delete_album(id):
        conn = pgdb_conn_pool.getconn()
        cur = conn.cursor()
        query = "DELETE FROM albums WHERE uuid::text = " + "'" + str(id) + "'"
        cur.execute(query)
        resp = conn.commit()
        cur.close()
        pgdb_conn_pool.putconn(conn)
        return jsonify(resp)

    # PUT
    @app.route('/putartist/<uuid:id>', methods=['PUT'])
    def put_artist(id):
        req_data = request.get_json()
        _artist_name = req_data['artist_name']
        query = 'UPDATE artists SET artist_name = %s WHERE uuid::text = ' + \
            "'" + str(id) + "'"
        put_data = (_artist_name)
        conn = pgdb_conn_pool.getconn()
        cur = conn.cursor()
        cur.execute(query, put_data)
        resp = conn.commit()
        cur.close()
        pgdb_conn_pool.putconn(conn)
        return jsonify(resp)

    # PUT
    @app.route('/putalbum/<uuid:id>', methods=['PUT'])
    def put_album(id):
        req_data = request.get_json()
        _artist_name = req_data['artist_name']
        _album_title = req_data['album_title']
        _release_date = req_data['release_date']
        _price = req_data['price']
        query = 'UPDATE albums SET artist_name = %s, album_title = %s, release_date = %s, price = %s WHERE uuid::text = ' + \
            "'" + str(id) + "'"
        put_data = (_artist_name, _album_title, _release_date, _price)
        conn = pgdb_conn_pool.getconn()
        cur = conn.cursor()
        cur.execute(query, put_data)
        resp = conn.commit()
        cur.close()
        pgdb_conn_pool.putconn(conn)
        return jsonify(resp)

finally:
    print("closing all")

if __name__ == '__main__':
    app.run(debug=True)
