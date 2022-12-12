from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
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




class departmenttechnical(models.Model):
    _inherit = 'hr.department'
                   

    x_location = fields.Char('Location')               
    x_studio_unit_code = fields.Char('Unit Code')
    x_studio_many2one_field_DQFxa = fields.Many2one('comodel_name', string='Unit Type')
    x_studio_many2one_field_RbZgM = fields.Many2one('hr.work.location', string='مكان العمل')


class  x_unittypemodel(models.Model):
    _name = 'x_unit_type'
    _description = 'x_unit_type'
    _rec_name="x_name"
    

    x_name = fields.Char('Name')