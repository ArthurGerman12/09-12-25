from flask import Blueprint, request, jsonify
from database import get_connection

news_bp = Blueprint("news", __name__, url_prefix="/news")


# CREATE
@news_bp.post("/")
def create_news():
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO news (title, content) VALUES (?, ?)", (title, content))
    conn.commit()

    return jsonify({"id": cur.lastrowid, "title": title, "content": content}), 201


# READ ALL
@news_bp.get("/")
def get_all_news():
    conn = get_connection()
    cur = conn.cursor()
    rows = cur.execute("SELECT * FROM news").fetchall()
    return jsonify([dict(row) for row in rows])


# READ ONE
@news_bp.get("/<int:id>")
def get_single_news(id):
    conn = get_connection()
    cur = conn.cursor()
    row = cur.execute("SELECT * FROM news WHERE id = ?", (id,)).fetchone()
    if not row:
        return jsonify({"error": "Not found"}), 404
    return jsonify(dict(row))


# UPDATE
@news_bp.put("/<int:id>")
def update_news(id):
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE news SET title = ?, content = ? WHERE id = ?", (title, content, id))
    conn.commit()

    return jsonify({"message": "Updated"})


# DELETE
@news_bp.delete("/<int:id>")
def delete_news(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM news WHERE id = ?", (id,))
    conn.commit()
    return jsonify({"message": "Deleted"})
