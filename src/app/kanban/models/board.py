from . import *

class Board(Base):
	__tablename__ = 'boards'
	id 			= db.Column('id', db.Integer, primary_key=True)
	title		= db.Column('title', db.String(256), unique=True, nullable=False)
	elements = db.relationship('BoardElement', backref='board')

	def __init__(self, **kwargs):
		"""
		Constructor
		"""
		self.title = kwargs.get('title')


class BoardElement(Base):
	__tablename__ = 'elements'
	id 			= db.Column(db.Integer, primary_key=True)
	board_id 	= db.Column(db.Integer, db.ForeignKey('boards.id'))
	category 	= db.Column(db.String(256), nullable=False)
	description = db.Column(db.String(256), nullable=False)
	#tags 		= db.Column(db.Array(String(256)))

	def __init__(self, **kwargs):
		"""
		Constructor for a Board element
		"""
		self.description = kwargs.get('description', None)
		self.board_id = kwargs.get('board_id', None)
		self.category = kwargs.get('category', None)
		self.tags = []









