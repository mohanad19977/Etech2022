from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re






class departmenttechnical(models.Model):
    _inherit = 'hr.department'
                   

    x_location = fields.Char('Location')               
    x_studio_unit_code = fields.Char('Unit Code')
    x_studio_many2one_field_DQFxa = fields.Many2one('x_unit_type', string='Unit Type')
    x_studio_many2one_field_RbZgM = fields.Many2one('hr.work.location', string='مكان العمل')


class  x_unittypemodel(models.Model):
    _name = 'x_unit_type'
    _description = 'x_unit_type'
    _rec_name="x_name"
    

    x_name = fields.Char('Name')