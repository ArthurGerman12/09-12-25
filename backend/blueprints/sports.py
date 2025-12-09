from flask import Blueprint, request, jsonify
from database import get_connection

sports_bp = Blueprint("sports", __name__, url_prefix="/sports")


# CREATE
@sports_bp.post("/")
def create_sport():
    data = request.get_json()
    team = data.get("team")
    score = data.get("score")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO sports (team, score) VALUES (?, ?)", (team, score))
    conn.commit()

    return jsonify({"id": cur.lastrowid, "team": team, "score": score}), 201


# READ ALL
@sports_bp.get("/")
def get_all_sports():
    conn = get_connection()
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM sports").fetchall()
    return jsonify([dict(row) for row in rows])


# READ ONE
@sports_bp.get("/<int:id>")
def get_single_sport(id):
    conn = get_connection()
    cur = conn.cursor()
    row = cur.execute("SELECT * FROM sports WHERE id = ?", (id,)).fetchone()
    if not row:
        return jsonify({"error": "Not found"}), 404
    return jsonify(dict(row))


# UPDATE
@sports_bp.put("/<int:id>")
def update_sport(id):
    data = request.get_json()
    team = data.get("team")
    score = data.get("score")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE sports SET team = ?, score = ? WHERE id = ?", (team, score, id))
    conn.commit()

    return jsonify({"message": "Updated"})


# DELETE
@sports_bp.delete("/<int:id>")
def delete_sport(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM sports WHERE id = ?", (id,))
    conn.commit()
    return jsonify({"message": "Deleted"})
