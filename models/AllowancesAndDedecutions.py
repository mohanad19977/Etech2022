
from urllib import request
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta
import re


class attachmentList(models.Model):
    _name = 'salary.attachmentlist'	
    
    Employee_id = fields.Many2one('hr.employee', string='Employee',required=True)
    StartDate = fields.Date('Start Date',required=True)
    EndDate = fields.Date('End Date',required=True)
    
  
    salary_attach_ids = fields.One2many('hr.salary.attachment', 'attachmenyList_id', string='salary attachment',tracking=True)


class x_salary_attachmentlis(models.Model):
    _name = 'x_salary_attachmentlis'
    _description = 'x_salary_attachmentlis'
    _rec_name="x_name"

    x_active = fields.Boolean('Active',default=True)
    x_name = fields.Char('Name')
    x_studio_sequence = fields.Integer('Sequance')