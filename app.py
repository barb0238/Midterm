from flask import Flask, jsonify, request

students = [
    {
        'ID': 1,
        'Name': 'Cameron',
        'Grade': 5
    }
]

app = Flask(__name__)

@app.route('/')
def hello():
    return "Midterm things (Cameron Barber)"

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({'students': students})

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = None
    for s in students:
        if s["ID"] == student_id:
            student = s
            break
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    return jsonify({'student': student})

@app.route('/students', methods=['POST'])
def add_student():
    new_student = {
        'ID': len(students) + 1,
        'Name': request.json['Name'],
        'Grade': request.json['Grade']
    }
    students.append(new_student)
    return jsonify({'student': new_student}), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = None
    for s in students:
        if s["ID"] == student_id:
            student = s
            break
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    student['Name'] = request.json.get('Name', student['Name'])
    student['Grade'] = request.json.get('Grade', student['Grade'])
    return jsonify({'student': student})

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = None
    for s in students:
        if s["ID"] == student_id:
            student = s
            break
    if student is None:
        return jsonify({'error': 'Student not found'}), 404
    students.remove(student)
    return jsonify({'result': 'Student deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
