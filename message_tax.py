# -*- coding: utf-8 -*-

from openerp import models, fields, api

class account_tax(models.Model):
	_name = 'account.tax'
	_inherit = 'account.tax'

	message_tax = fields.Text(string="Tax Message")