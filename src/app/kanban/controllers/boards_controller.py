from app.constants import *
from . import *
from flask import request

@kanban.route('/boards', methods=['POST'])

def post_board():
	title = request.args.get('title')
	board = boards_dao.create_board(title)
	query = boards_dao.board_by_id(board.id)
	return jsonify({'success': True, 'data': {
										'board': {
										'id': query.id,
										'title': title,
										'board_elements': [],
										'created_at': query.created_at,
										'updated_at': query.updated_at
										}
									}
					})


@kanban.route('/boards', methods=['GET'])

def pull_boards():
	query = boards_dao.get_boards()
	jsonList = []
	for each in query:
		todo_count = boards_dao.get_todo_count(each.id)
		inprogress_count = boards_dao.get_inprogress_count(each.id)
		done_count = boards_dao.get_done_count(each.id)
		jsonList.append({'id': each.id,
						'title': each.title,
						'created_at': each.created_at,
						'updated_at': each.updated_at,
						'todo_count': todo_count,
						'inprogress_count': inprogress_count,
						'done_count': done_count
		})
	return jsonify({'success': True, 'data': {'boards': jsonList}})


@kanban.route('/boards/<id>', methods=['GET'])

def pull_one_board(id):
	board = boards_dao.board_by_id(id)
	todo_list = boards_dao.get_todo_list(board.id)
	inprogress_list = boards_dao.get_inprogress_list(board.id)
	done_list = boards_dao.get_done_list(board.id)
	return jsonify({'success': True, 'data': {'board': {'id': board.id,
															'title': board.title,
															'created_at': board.created_at,
															'updated_at': board.updated_at,
															'todo': todo_list,
															'inprogress': inprogress_list,
															'done': done_list
															}
												}
						})


@kanban.route('/boards', methods=['DELETE'])

def delete_board():
	boardId = request.args.get('id')
	success = boards_dao.delete_board(boardId)
	return jsonify({'success': success})


@kanban.route('/board_elements', methods=['POST'])

def post_board_element():
	boardId = request.args.get('board_id')
	description = request.args.get('description')
	category = request.args.get('category')
	boardElement = boards_dao.create_element(boardId, description, category)
	return jsonify({'success': True, 'data': {'board_element': {'id': boardElement.id,
																'board_id': boardElement.board_id,
																'category': boardElement.category,
																'created_at': boardElement.created_at,
																'updated_at': boardElement.updated_at,
																'description': boardElement.description,
																'tags': boardElement.tags
																}
											}

					})


@kanban.route('/board_elements/advance', methods=['POST'])

def advance_board_element():
	element_id = request.args.get('id')
	success = boards_dao.advance_element(element_id)
	return jsonify({'success': success})


@kanban.route('/board_elements', methods=['DELETE'])

def delete_board_element():
	elementId = request.args.get('board_element_id')
	success = boards_dao.delete_element(elementId)
	return jsonify({'success': success})






















