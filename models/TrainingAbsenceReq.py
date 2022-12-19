from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re

class TrainingAbsenceReq(models.Model):
    _name = 'x_training_absence_req'
    _description = 'x_training_absence_req'
    _rec_name="x_name"
  
    x_active = fields.Boolean('Active',default=True)
    x_color = fields.Integer('Color')
    x_name = fields.Char('Name')
    x_studio_details = fields.Text('Details')
    x_studio_kanban_state = fields.Selection([
        ('normal', 'In Progress'),
         ('done', 'Ready'),
          ('blocked', 'Blocked')
    ], string='Kanban State')
    x_studio_priority = fields.Boolean('High Priority')
    x_studio_request_type = fields.Selection([
        ('الاعتذار عن حضور كامل', 'الاعتذار عن حضور كامل'),
          ('الاعتذار عن حضور جلسة', 'الاعتذار عن حضور جلسة')
    ], string='Request Type')
    x_studio_sequence = fields.Integer('Sequence')
    x_studio_many2one_field_n6Gvs = fields.Many2one('hr.employee', string='Judge')
    x_studio_many2one_field_PbW0c = fields.Many2one('x_trainingunit', string='TrainingUnit')
    x_studio_stage_id = fields.Many2one('x_training_absence_req_stage', string='Stage',required=True)
    x_studio_user_id = fields.Many2one('res.users', string='Responsible')

class TrainingAbsenceReqstage(models.Model):
    _name = 'x_training_absence_req_stage'
    _description = 'x_training_absence_req_stage'
    _rec_name="x_name"

    x_name = fields.Char('Stage Name',required=True)
    x_studio_sequence = fields.Integer('Sequence')


     