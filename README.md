Udacity Trivia API project 

API Development and Documentation project for Udacity students taking the ALX-T Full Stack developer Nanodegree program. Students are able to create their endpoints, error handling, create, update, delete and search through their questions and category lists. As a part of the Fullstack Nanodegree, it serves as a practice module for lessons from Course 2: API Development and Documentation. By completing this project, students learn and apply their skills structuring and implementing well formatted API endpoints that leverage knowledge of HTTP and API development best practices.

Getting Started

Pre-requisites and Local Development
Developers using this project should already have Python3, pip and node installed on their local machines.

Backend
From the backend folder run pip install requirements.txt. All required packages are included in the requirements file.

To run the application run the following commands:

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run

These commands put the application in development and directs our application to use the __init__.py file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, look for the commands in the Flask documentation.

The application is run on http://127.0.0.1:5000/ by default and is a proxy in the frontend configuration.

Frontend
From the frontend folder, run the following commands to start the client:

npm install // only once to install dependencies
npm start 

By default, the frontend will run on localhost:3000.

Tests
In order to run tests navigate to the backend folder and run the following commands:

dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql

The first time you run the tests, omit the dropdb command.

All tests are kept in that file and should be maintained as updates are made to app functionality.

API Reference

Getting Started
Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
Authentication: This version of the application does not require authentication or API keys

Error Handling
Errors are returned as JSON objects in the following format:

{
    "success": False, 
    "error": 400,
    "message": "bad request"
}

{
    "success": False, 
    "error": 404,
    "message": "not found"
}

{
    "success": False, 
    "error": 422,
    "message": "unprocessable"
}

The API will return three error types when requests fail:

400: Bad Request
404: Resource Not Found
422: Not Processable

Endpoints

GET /categories

General:
Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
Request Arguments: None
Returns: An object with a single key, categories, that contains an object of id: category_string key: value pairs.
Sample: curl http://127.0.0.1:5000/categories

{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}

GET '/questions?page=${integer}'

- Fetches a paginated set of questions, a total number of questions, all categories and current category string. 
- Request Arguments: page - integer
- Returns: An object with 10 paginated questions, total questions, object including all categories, and current category string

{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "currentCategory": "Sports", 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "success": true, 
  "total_questions": 18
}

GET '/categories/${id}/questions'

- Fetches questions for a cateogry specified by id request argument 
- Request Arguments: id - integer
- Returns: An object with questions for the specified category, total questions, and current category string 

{
  "categories": [
    {
      "category": "Science", 
      "id": 1
    }
  ], 
  "categories_num": 1, 
  "questions": [
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ], 
  "success": true
}

DELETE '/questions/${id}'
- Deletes a specified question using the id of the question
- Request Arguments: id - integer
- Returns: Does not need to return anything besides the appropriate HTTP status code. Optionally can return the id of the question. If you are able to modify the frontend, you can have it remove the question using the id instead of refetching the questions. 
(env) (base) Masss-MacBook-Pro:flaskr mass$ curl -X DELETE http://127.0.0.1:5000/questions/36

{
  "deleted": 36, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }, 
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Scarab", 
      "category": 4, 
      "difficulty": 4, 
      "id": 23, 
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ], 
  "success": true, 
  "total_questions": 18
}



POST '/questions'
- Sends a post request in order to add a new question
- Request Body: 

(env) (base) Masss-MacBook-Pro:flaskr mass$ curl -X POST -H "Content-Type: application/json" -d '{"question":"What is flask"}' http://127.0.0.1:5000/questions

{
      "answer": null, 
      "category": null, 
      "difficulty": null, 
      "id": 36, 
      "question": "What is flask"
    }
  ], 
  "success": true, 
  "created": 36
  "total_questions": 19
}

POST '/questions'
- Sends a post request in order to search for a specific question by search term 
- Request Body: 
(env) (base) Masss-MacBook-Pro:flaskr mass$ curl -X POST -H "Content-Type: application/json" -d '{"searchTerm":"Who discovered penicillin?"}' http://127.0.0.1:5000/questions/search

{
    'searchTerm': 'Who discovered penicillin?'
}
- Returns: any array of questions, a number of totalQuestions that met the search term 
{
  "questions": [
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }
  ], 
  "success": true, 
  "total_questions": 1
}

POST '/quizzes'
- Sends a post request in order to get the next question 
- Request Body: 
{'previous_questions':  an array of question id's such as [1, 4, 20, 15]
'quiz_category': a string of the current category }

- Returns: a single new question object 
{
    'question': {
        'id': 2,
        'question': 'What movie earned Tom Hanks his third straight Oscar nomination, in 1996?',
        'answer': 'Apollo 13', 
        'difficulty': 4,
        'category': 5
    }
}

Deployment N/A

Authors
Yours truely Mass Njie

Acknowledgements
The awesome team at Udacity, ALX-T and all of the students, soon to be full stack extraordinaires!