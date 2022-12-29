from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re


class x_location_transfer(models.Model):

    _name = 'x_location_transfer'
    _description = 'x_location_transfer'
    _rec_name="x_name"

    x_studio_judge = fields.Many2one('hr.employee', string='اسم القاضي',required=True,domain="[('x_studio_employee_status','=','على رأس عمله')]")
    x_studio_new_work_location = fields.Many2one('hr.work.location', string='جهة النقل',required=True)
    x_studio_many2one_field_RymCx = fields.Many2one('hr.job', string='الوظيفة')   
    x_studio_many2one_field_X1jqs = fields.Many2one('x_transfer_reason', string='سبب النقل')
    transfer_apply_chanel = fields.Many2one('x_transfer_apply_chanel', string='قناة تقديم الطلب')
    x_studio_many2one_field_mNvNk = fields.Many2one('hr.work.location', string='مركز العمل قبل النقل')
    x_studio_grade_years = fields.Many2one('hr.payroll.structure', string='Grade / Years')
    x_studio_tdocno = fields.Char('TDOCNO')
    x_studio_transfer_date = fields.Date('تاريخ طلب النقل',required=True)
    x_studio_many2one_field_TdUQu = fields.Many2one('x_transfer_status', string='Transfer Status')
    Attachment = fields.Binary('Attachment')

    x_studio_selection_field_GUisB = fields.Selection([
        ('initiated','جديد'),
        ('inprocess','تحت التنفيذ'),
        ( 'approved','تم'),
        ('Rejected','مرفوض'),
    ], string='Pipeline status bar')

    x_active = fields.Boolean('Active',default=True)
    x_name = fields.Char('Name')

    message_follower_ids = fields.One2many('mail.followers', 'res_id', string='Followers')
    message_ids = fields.One2many('mail.message', 'res_id', string='Messages')
    activity_ids = fields.One2many('mail.activity', 'res_id', string='Activities')
    x_studio_sequence = fields.Integer('Sequance')
    
    @api.onchange('x_studio_selection_field_GUisB')
    def _onchange_x_studio_selection_field_5CEax(self):
         for record in self:   
            if record.x_studio_selection_field_GUisB == 'approved':
               user=self.env["hr.employee"].search([("id", "=", record.x_studio_judge.id)])     
               if user:    
                #  try:
                 user.write({
                    'work_location_id':record.x_studio_new_work_location
                    })

    def Confirmcron(self):
        locations=self.env["x_location_transfer"].search([("x_studio_selection_field_GUisB", "!=", 'approved')])
        for record in locations:
            if record.x_studio_selection_field_GUisB != 'approved' and record.x_studio_transfer_date <date.today():
             user=self.env["hr.employee"].search([("id", "=", record.x_studio_judge.id)])     
             if user:    
                #  try:
                 record.write({
                    'x_studio_selection_field_GUisB':'approved',
                    }) 
                 user.write({
                    'work_location_id':record.x_studio_new_work_location
                    })      

class x_transfer_reason(models.Model):
    _name = 'x_transfer_reason'
    _description = 'x_transfer_reason'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_transfer_status(models.Model):
    _name = 'x_transfer_status'
    _description = 'x_transfer_status'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_transfer_apply_chanel(models.Model): #by mohanad
    _name = 'x_transfer_apply_chanel'
    _description = 'x_transfer_apply_chanel'
    _rec_name="x_name"

    x_name = fields.Char('Name')

