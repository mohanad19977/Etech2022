from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re


class LeaveCustom(models.Model):
    _inherit="hr.leave.type"

    x_studio_assigneddays = fields.Integer('الحد الاقصى (يوم)')
    

class LeaveCustom(models.Model):
    _inherit="hr.leave"

    x_studio_narration = fields.Text('مرجع منح الإجازة')
    x_studio_approval_letter_no = fields.Text('رقم قرار منح الإجازة',required=True)
    x_studio_approval_date = fields.Date('تاريخ صدور القرار')    
    x_studio_attachment_1 = fields.Binary('Attachment')
    x_studio_attachment_1_filename = fields.Char('Filename for x_studio_binary_field_pwFOp')
    x_studio_during_judges = fields.Boolean('ضمن العطلة القضائية ')
    x_studio_narration = fields.Char('Narration')
    x_studio_many2one_field_cnTPY = fields.Many2one('hr.employee', string='Employee')
    
    


    

