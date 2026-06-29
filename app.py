from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = 'courses.json'

def read_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def write_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=2)

@app.route('/api/courses', methods=['GET'])
def get_courses():
    courses = read_data()
    return jsonify(courses), 200

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    courses = read_data()
    course = next((c for c in courses if c['id'] == course_id), None)
    if course:
        return jsonify(course), 200
    return jsonify({'error': 'Course not found'}), 404

@app.route('/api/courses', methods=['POST'])
def create_course():
    data = request.get_json()
    if not data or not data.get('title') or not data.get('instructor'):
        return jsonify({'error': 'Missing required fields'}), 400

    courses = read_data()
    new_id = max((c['id'] for c in courses), default=0) + 1
    new_course = {
        'id': new_id,
        'title': data['title'],
        'description': data.get('description', ''),
        'instructor': data['instructor'],
        'duration': data.get('duration', '')
    }
    courses.append(new_course)
    write_data(courses)
    return jsonify(new_course), 201

@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    data = request.get_json()
    courses = read_data()
    course_index = next((index for (index, c) in enumerate(courses) if c['id'] == course_id), None)

    if course_index is None:
        return jsonify({'error': 'Course not found'}), 404

    course = courses[course_index]
    course['title'] = data.get('title', course['title'])
    course['description'] = data.get('description', course['description'])
    course['instructor'] = data.get('instructor', course['instructor'])
    course['duration'] = data.get('duration', course['duration'])
    
    courses[course_index] = course
    write_data(courses)
    return jsonify(course), 200

@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    courses = read_data()
    course_index = next((index for (index, c) in enumerate(courses) if c['id'] == course_id), None)

    if course_index is None:
        return jsonify({'error': 'Course not found'}), 404

    deleted_course = courses.pop(course_index)
    write_data(courses)
    return jsonify(deleted_course), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
