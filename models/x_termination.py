from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re

class x_grade(models.Model):
    _name = 'x_grade'
    _description = 'x_grade'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_termination_reason(models.Model):
    _name = 'x_termination_reason'
    _description = 'x_termination_reason'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_termination(models.Model):
    _name = 'x_termination'
    _description = 'x_termination'
    

    x_studio_judge  = fields.Many2one('hr.employee', string='اسم القاضي',required=True)
    x_studio_many2one_field_vufKW = fields.Many2one('hr.job', string='الوظيفة',readonly=True)
    x_studio_termination_letter = fields.Char('رقم الكتاب',required=True)
    x_studio_informing_date  = fields.Date('تاريخ التبليغ',required=True)
    x_studio_many2one_field_nlhaS = fields.Many2one('x_grade', string='الدرجة',readonly=True)
    x_studio_many2one_field_7HPS4 = fields.Many2one('hr.work.location', string='مركز العمل ',readonly=True)
    x_studio_letter_date = fields.Date('تاريخ الكتاب',required=True)
    x_studio_many2one_field_CDskR = fields.Many2one('x_termination_reason', string='X Studio Many2One Field Cdskr',required=True)
    x_studio_explanation = fields.Html('Explanation')
    x_active = fields.Boolean('Active',default=True)
    x_name = fields.Char('Name')
    message_follower_ids = fields.One2many('mail.followers', 'res_id', string='Followers')
    message_ids = fields.One2many('mail.message', 'res_id', string='Messages')
    activity_ids = fields.One2many('mail.activity', 'res_id', string='Activities')
    x_studio_sequence = fields.Integer('Sequence')
