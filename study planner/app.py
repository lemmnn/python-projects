from flask import Flask,request, jsonify, render_template

app=Flask(__name__)
tasks = []

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json

    task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "completed": False
    }

    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks =[ t for t in tasks if t["id"] != task_id]
    return jsonify({"message": "task deleted"})

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def mark_done(task_id):
    for task in tasks:
        if task["id"]==task_id:
            task["completed"]=True
            return jsonify(task)
    return jsonify({"error": "task not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)