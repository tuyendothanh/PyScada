# -*- coding: utf-8 -*-
from scada.models import Log
from scada.models import MessageIds


class message():
	def __init__(self):	
		
	def add(self,id,message,message_short):
		""" 
		add a new massage/error notice to the log	
		"""
		
class manageMessageIds():
	def __init__(self):	
		"""
		class init
		"""
	def add_id(self,class_name,level,description):
		""" 
		add a new message/error id to the known messages/errors
		"""