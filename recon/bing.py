#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Infoga: Email Information Gathering
#
# @url: https://github.com/m4ll0k/
# @author: Momo Outaadi (M4ll0k)

from lib.output import *
from lib.request import *
from lib.parser import *

class Bing(Request):
	def __init__(self,target):
		Request.__init__(self)
		self.target = target

	def search(self):
		test('Searching "%s" in Bing...'%(self.target))
		url = "http://bing.com/search?q=%40{}".format(self.target)
		try:
			resp = self.send(
				method = "GET",
				url = url,
				headers = {
							'Cookie':'SRCHHPGUSR=ADLT=DEMOTE&NRSLT=100'
							}
				)
			return self.getmail(resp.content,self.target)
		except Exception,Error:
			pass

	def getmail(self,content,target):
		return parser(content,target).email()