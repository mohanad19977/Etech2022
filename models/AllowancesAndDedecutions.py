
from urllib import request
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta
import re

class salaryattachment(models.Model):
    _inherit = 'hr.salary.attachment'
    _description = 'hr.department'
    _rec_name="x_name"
   
    x_name = fields.Char('Name')
    x_studio_unit_code = fields.Char('Unit Code')
    x_studio_many2one_field_RbZgM = fields.Many2one('hr.work.location', string='مكان العمل')
    # x_studio_many2one_field_DQFxa = fields.Many2one('x_unit_type', string='unit_type')
    x_location = fields.Char('Location')
    attachmenyList_id = fields.Many2one('salary.attachmentlist', string='attachmenyList',tracking=True)

 
    @api.onchange('attachmenyList_id')
    @api.depends('attachmenyList_id')
    def _onchange_attachment(self):
        for record in self:
         if record.attachmenyList_id:
               record.date_start=record.attachmenyList_id.StartDate
               record.x_studio_end_date=record.attachmenyList_id.EndDate
               record.employee_id=record.attachmenyList_id.Employee_id
               
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