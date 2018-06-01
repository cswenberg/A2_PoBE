from app.constants import *
from . import *


### BOARD METHODS ###

def board_by_id(board_id):
  """
  Get board by ID
  """
  return Board.query.filter_by(id=board_id).first()

def create_board(sometitle):
	board = Board(title=sometitle)
	db.session.add(board)

	try:
		db.session.commit()
		return board
	except Exception as e:
		db.session.rollback()
		print(e)
		return False

def delete_board(someid):
	board = board_by_id(someid)
	db.session.delete(board)

	try:
		db.session.commit()
		return True
	except Exception as e:
		db.session.rollback()
		print(e)
		return False

def get_boards():
	return Board.query.all()


### ELEMENT METHODS ###

def element_by_id(element_id):
	return BoardElement.query.filter_by(id=element_id).first()

def create_element(bID, descrip, categ):
	boardElement = BoardElement(board_id = bID, description = descrip, category = categ)
	db.session.add(boardElement)

	try:
		db.session.commit()
		return boardElement
	except Exception as e:
		db.session.rollback()
		print(e)
		return False

def delete_element(someid):
	element = element_by_id(someid)
	db.session.delete(element)

	try:
		db.session.commit()
		return True
	except Exception as e:
		db.session.rollback()
		print(e)
		return False

def advance_element(someid):
	element = element_by_id(someid)
	category = element.category
	if category == 'todo':
		element.category = 'inprogress'
	elif category == 'inprogress':
		element.category = 'done'

	try:
		db.session.commit()
		return True
	except Exception as e:
		db.session.rollback()
		print(e)
		return False


def clean_element_list(query):
	returnList = []
	for boardElement in query:
		returnList.append({'id': boardElement.id,
						'board_id': boardElement.board_id,
						'category': boardElement.category,
						'created_at': boardElement.created_at,
						'updated_at': boardElement.updated_at,
						'description': boardElement.description,
						'tags': []
						})
	return returnList

def get_todo_list(boardId):
	query = BoardElement.query.filter_by(category='todo',board_id=boardId)
	return clean_element_list(query)


def get_inprogress_list(boardId):
	query = BoardElement.query.filter_by(category='inprogress',board_id=boardId)
	return clean_element_list(query)


def get_done_list(boardId):
	query = BoardElement.query.filter_by(category='done',board_id=boardId)
	return clean_element_list(query)
	

def get_todo_count(boardId):
	count = BoardElement.query.filter_by(category='todo',board_id=boardId).count()
	return count

def get_inprogress_count(boardId):
	count = BoardElement.query.filter_by(category='inprogress',board_id=boardId).count()
	return count

def get_done_count(boardId):
	count = BoardElement.query.filter_by(category='done',board_id=boardId).count()
	return count















