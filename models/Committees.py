from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re

class x_committe_type(models.Model):
    _name = 'x_committe_type'
    _description = 'x_committe_type'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_participation_type(models.Model):
    _name = 'x_participation_type'
    _description = 'x_participation_type'
    _rec_name="x_name"

    x_name = fields.Char('Name')
    canntdublicate = fields.Boolean('can not duplicate?')

class x_funding_party(models.Model):
    _name = 'x_funding_party'
    _description = 'x_funding_party'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_committees(models.Model):
    _name = 'x_committees'
    _description = 'X Committees'
    _rec_name="x_name"

    x_studio_many2one_field_UrDkk = fields.Many2one('x_committe_type', string='Committe Type',required=True)
    x_studio_commencement_date = fields.Date('تاريخ تشكيل اللجنة أو الهيئة',required=True)
    x_studio_letter_ref_no = fields.Char('رقم قرار تشكيل اللجنة / الهيئة',required=True)
    x_studio_many2one_field_2WNM1 = fields.Many2one('x_participation_type', string='Participation Type',required=True)
    x_studio_many2one_field_dckgD = fields.Many2one('x_funding_party', string='funding Party',required=True)
    x_studio_committee_name = fields.Char('Committee Name',required=True)
    x_studio_end_date = fields.Date('تاريخ انتهاء أعمال اللجنة أو الهيئة',required=True)
    x_studio_letter_date = fields.Date('تاريخ قرار تشكيل اللجنة / الهيئة',required=True)
    x_studio_financial_income = fields.Boolean('هل يوجد مردود مالي ؟')
    x_committees_line_ids_9f1e1 = fields.One2many('x_committees_line_1678d', 'x_committees_id', string='Judges List')
    x_active = fields.Boolean('Active',default=True)
    x_name = fields.Char('Name')
    x_studio_sequence = fields.Integer('Sequence')
    
    
    x_studio_location = fields.Selection([
        ('داخل الأردن', 'داخل الأردن'),
        ('خارج الأردن', 'خارج الأردن')
    ], string='Location')


    @api.constrains('x_studio_end_date','x_studio_commencement_date')
    def _constrainsdate(self):
           for record in self: 
            if record.x_studio_end_date and record.x_studio_commencement_date:    
             if record.x_studio_end_date < record.x_studio_commencement_date:
                  raise ValidationError("End Date Must Grater Than Start Date")
    @api.onchange('x_committees_line_ids_9f1e1')
    @api.constrains('x_committees_line_ids_9f1e1')
    def _compute_x_committees_line_ids_9f1e1(self):
        for record in self:
                for line1 in record.x_committees_line_ids_9f1e1:
                   for line2 in record.x_committees_line_ids_9f1e1.filtered(lambda x:x.id!=line1.id):
                    if line1.x_studio_many2one_field_Homib.canntdublicate == True:
                        if line1.x_studio_many2one_field_Homib.id == line2.x_studio_many2one_field_Homib.id:
                           raise ValidationError("You Cant Dublicate Type For Judges List") 
                    if line1.x_studio_judge.id == line2.x_studio_judge.id:                      
                           raise ValidationError("You Cant Dublicate Judges")       

    
    # @api.onchange('x_committees_line_ids_9f1e1')
    # def _onchange_x_committees_line_ids_9f1e1(self):
    #     for record in self:
    #         record.x_studio_letter_ref_no=



class x_committees_line_1678dtcustom(models.Model):
    _name = 'x_committees_line_1678d'
    _rec_name="x_name"


    x_committees_id = fields.Integer('x_committees_id')
    x_studio_judge =fields.Many2one('hr.employee', string='Judge' ,domain="[('x_studio_employee_status','=','على رأس عمله')]")
    #x_studio_judge =fields.Many2one('hr.employee', string='Judge')

    x_studio_many2one_field_Homib = fields.Many2one('x_participation_type', string='Participation Type')
    x_studio_many2one_field_2e5p2 = fields.Many2one('hr.work.location', string='Work Location',related='x_studio_judge.work_location_id')
    x_studio_many2one_field_hO5XQ = fields.Many2one('hr.job', string='Job Position',related='x_studio_judge.job_id')
    
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description')
    