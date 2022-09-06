from crypt import methods
import os
from re import search
from unicodedata import category
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category



QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get('page', 1 , type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE

    end = start +   QUESTIONS_PER_PAGE
    questions = [Question.format() for Question in selection]

    current_question = questions[start:end]
    return current_question

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')

    return response

  # @app.route('/')
  # def smiley():
  #   return jsonify({'message':'HELLO, WORLD!'})

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def categories():
    categories = Category.query.all()
    formatted_categories= {Category.id:Category.type for Category in categories}
    
    return jsonify({
      'success': True,
      'categories':formatted_categories
    })


  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions')
  def questions():
   
    selection = Question.query.order_by(Question.id).all()
    current_question = paginate_questions(request, selection)

    

    categories = Category.query.order_by(Category.id).all()
    formatted_categories= {Category.id:Category.type for Category in categories}
    for category in categories:
      current_category = category.type
 
   
   

    return jsonify({
      'success': True,
      'questions': current_question,
      'total_questions': len(Question.query.all()),
      'categories': formatted_categories,
      'currentCategory': current_category
      })
      
    
   
    

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()

      if question is None:
        abort(404)
      
      question.delete()
      selection = Question.query.order_by(Question.id).all()
      formatted_questions = [Question.format() for Question in selection]

      return jsonify({
        'success': True,
        'deleted': question_id,
        'questions': formatted_questions,
        'total_questions': len(Question.query.all())
        })
    except:
      abort(422)


  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def create_question():
    body = request.get_json()

    new_question = body.get('question', None)
    new_answer = body.get('answer', None)
    new_category = body.get('category', None)
    new_difficulty = body.get('difficulty', None)

    try:
      question = Question(question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
      question.insert()

      selection = Question.query.order_by(Question.id).all()
      current_question = paginate_questions(request, selection)

      return jsonify({
        'success': True,
        'created': question.id,
        'questions': current_question,
        'total_questions': len(Question.query.all())
     })
     
    except:
      abort(422)

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions/search', methods=['POST'])
  def search_question():
    body = request.get_json()

    searchTerm = body.get('searchTerm', None)

    try:
      selection = Question.query.order_by(Question.id).filter(Question.question.ilike('%{}%'.format(searchTerm)))
      current_question = paginate_questions(request, selection)



      # selection = Question.query.order_by(Question.id).all()
      
    # Artist.query.filter(Artist.name.ilike('%' + request.form.get('search_term', '') + '%')).all()

      return jsonify({
        'success': True,
        'questions': current_question,
        'total_questions': len(selection.all()) 
        
      })
    except:
      abort(422)
  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def get_category(category_id):

    categories = Category.query.filter(category_id == Category.id).all()
    data = []
    questions = Question.query.filter(Question.category == category_id).all()
    # current_question = [question.question for question in questions]
    data1 = []
    

    try:
      for category in categories:
        data.append({
          "id":category.id,
          "category":category.type
        })
      for question in questions:
        data1.append({
          'id':question.id,
          'question':question.question,
          'answer':question.answer,
          'difficulty':question.difficulty,
          'category':question.category
        })
      return jsonify({
          'success': True,
          'categories': data,
          'categories_num': len(data),
          'questions': data1,
          })
    except:
        return jsonify({
          'Error': "category not found"
        })


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  @app.route('/quizzes', methods=['POST'])
  def get_quizzes():

    try:
      body = request.get_json()

      previous_questions = body.get('previous_questions', None)
      category = body.get('quiz_category', None)

  

      if int(category['id']) == 0:
         new_quiz = Question.query.filter(Question.id.notin_(previous_questions)).all()


      else:
        new_quiz = Question.query.filter(Question.id.notin_(previous_questions), Question.category == str(category['id'])).all()

        

      if not new_quiz:
        new_quiz = None
        abort(404)

      else:
        new_quiz = random.choice(new_quiz)
        
        question = new_quiz.format()


      return jsonify({
        'success': True,
        'question': question,
        'current_category': category['type']
      })
    except:
      abort(422)

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
       "success": False, 
       "error": 404,
       "message": "Not found"
   }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': "unprocessable"
    }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message': "bad request"
    }), 400
  

  
  return app

    