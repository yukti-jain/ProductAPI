#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, jsonify, request


# In[2]:


app = Flask(__name__)

courses = [
           {'course_id' : 0,
            'name' : "NLP - Natural Language Processing with Python",
            'price' : 700,
            'description' : "Learn to use Machine Learning, Spacy, NLTK, SciKit-Learn, Deep Learning, and more to conduct Natural Language Processing"
           },
           {'course_id' : 1,
            'name' : "Git Complete: The definitive, step-by-step guide to Git",
            'price' : 400,
            'description' : "Go from zero to hero with Git source control step-by-step with easy to understand examples. Become the next Git expert!"
            
           }
          ]


# In[3]:


@app.route('/')
def index():
    return "Welcome to Courses API"

@app.route('/courses', methods=['GET'])
def get():
    return jsonify({'Courses':courses})

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    return jsonify({'Courses':courses[course_id]})

@app.route('/courses', methods=['POST'])
def create():
    request_data = request.get_json()
    course = {'course_id' : courses[-1]['course_id'] + 1 ,
                  'name' : request_data['name'] ,
                  'price' : request_data['price'],
                  'description' : request_data['description']
           }
    courses.append(course)
    return jsonify({'Created':course})

@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    courses[course_id]['name'] = request.json.get('name', courses[course_id]['name'])
    courses[course_id]['description'] = request.json.get('description', courses[course_id]['description'])
    courses[course_id]['price'] = request.json.get('price', courses[course_id]['price'])
    return jsonify({'course': courses[course_id]})

@app.route('/courses/<int:courseid>', methods=['DELETE'])
def delete_course(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result': True})


# In[ ]:


if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




