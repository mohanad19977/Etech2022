from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re

class XJudgepromotionLineAc79D(models.Model):
    _name = 'x_judgepromotion_line_ac79d'
    _description = 'X Judgepromotion Line Ac79D'
    _rec_name="x_name"
   

    x_studio_many2one_field_gXLon = fields.Many2many('hr.employee', string='Judge',required=True)
    x_studio_old_job_position.job_id.display_name= fields.Char('Old Job Position',readonly=True)   
    x_studio_old_grade= fields.Char('Old Grade',readonly=True) 
    x_studio_related_field_LHjqP = fields.Char('موقع العمل الحالي',readonly=True)
    x_studio_years_in_old_grade = fields.Float('الدرجة الحالية')
    x_studio_years_in_grade = fields.Float('سنة في الدرجة')
    x_studio_new_job_position = fields.Many2one('hr.job', string='الوظيفة الجديدة',required=True)
    x_studio_new_job_grade = fields.Many2one('x_job_grade', string='الدرجة الجديدة',required=True)
    


class JudgePromotion(models.Model):
    _name = 'x_judgepromotion'
    _description = 'x_judgepromotion'
    _rec_name="x_name"

    x_name = fields.Char('x_name')
    x_studio_letter_date = fields.Date('Letter Date')
    x_studio_promotions_letter_no = fields.Char('Promotions Letter No.')
    x_studio_effective_date = fields.Date('effective Date')
    x_studio_reference = fields.Char('Reference') 
    x_judgepromotion_line_ids_c0b72 = fields.One2many('x_judgepromotion_line_ac79d', 'x_judgepromotion_id', string='Judges List')
    x_active = fields.Boolean('Active')
    
    