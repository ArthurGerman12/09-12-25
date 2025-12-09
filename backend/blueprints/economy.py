from flask import Blueprint, request, jsonify
from database import get_connection

economy_bp = Blueprint("economy", __name__, url_prefix="/economy")


# CREATE
@economy_bp.post("/")
def create_economy():
    data = request.get_json()
    market = data.get("market")
    status = data.get("status")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO economy (market, status) VALUES (?, ?)", (market, status))
    conn.commit()

    return jsonify({"id": cur.lastrowid, "market": market, "status": status}), 201


# READ ALL
@economy_bp.get("/")
def get_all_economy():
    conn = get_connection()
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM economy").fetchall()
    return jsonify([dict(row) for row in rows])


# READ ONE
@economy_bp.get("/<int:id>")
def get_single_economy(id):
    conn = get_connection()
    cur = conn.cursor()
    row = cur.execute("SELECT * FROM economy WHERE id = ?", (id,)).fetchone()
    if not row:
        return jsonify({"error": "Not found"}), 404
    return jsonify(dict(row))


# UPDATE
@economy_bp.put("/<int:id>")
def update_economy(id):
    data = request.get_json()
    market = data.get("market")
    status = data.get("status")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE economy SET market = ?, status = ? WHERE id = ?", (market, status, id))
    conn.commit()

    return jsonify({"message": "Updated"})


# DELETE
@economy_bp.delete("/<int:id>")
def delete_economy(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM economy WHERE id = ?", (id,))
    conn.commit()
    return jsonify({"message": "Deleted"})
