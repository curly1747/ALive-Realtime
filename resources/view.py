from flask_config import app
from flask import render_template, jsonify, request
from resources.cronjob import UpdateStreamList
from resources.ultils import Actor
from returns.pipeline import is_successful

stream_list = UpdateStreamList(interval=45)
stream_list.start()


@app.route('/')
def hello_world():  # put application's code here
    return render_template("home.html", stream_list=stream_list.current)


@app.route('/current_stream')
def current_stream():
    return jsonify(stream_list.current)


@app.route('/ban')
def ban_user():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"message": "missing user_id"}), 400

    reason = request.args.get("reason")
    if not reason:
        return jsonify({"message": "missing reason"}), 400

    result = Actor.ban_user(user_id=user_id, reason=reason)
    if not is_successful(result):
        return jsonify({"message": result.unwrap()}), 400
    result = result.unwrap()
    return jsonify(result)


@app.route('/delete_stream')
def delete_stream():
    room_id = request.args.get("room_id")
    if not room_id:
        return jsonify({"message": "missing room_id"}), 400

    result = Actor.delete_stream(room_id=room_id)
    if not is_successful(result):
        return jsonify({"message": result.unwrap()}), 400
    result = result.unwrap()
    return jsonify(result)
