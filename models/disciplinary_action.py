from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re


class x_violationtype(models.Model):
    _name = 'x_violationtype'
    _description = 'x_violationtype'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_disciplinaryactionty(models.Model):
    _name = 'x_disciplinaryactionty'
    _description = 'x_disciplinaryactionty'
    _rec_name="x_name"

    x_name = fields.Char('Name')
    PreviesAction = fields.Many2one('x_disciplinaryactionty', string='Previous Action') 

class x_disciplinaryactionju(models.Model):
    _name = 'x_disciplinaryactionju'
    _description = 'x_disciplinaryactionju'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_disciplinaryauthoriz(models.Model):
    _name = 'x_disciplinaryauthoriz'
    _description = 'x_disciplinaryauthoriz'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_disciplinaryactionst(models.Model):
    _name = 'x_disciplinaryactionst'
    _description = 'x_disciplinaryactionst'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_disciplinarysource(models.Model):
    _name = 'x_disciplinarysource'
    _description = 'x_disciplinarysource'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_disciplinaryeffect(models.Model): #check
    _name = 'x_disciplinaryeffect'
    _rec_name='x_name'	

    x_name = fields.Char('Name')
    IsGrade  = fields.Boolean('Is Grade')

class DisciplinaryActionscustom(models.Model):
    _name = 'x_disciplinary_action'
    

    x_studio_judge = fields.Many2one('hr.employee', string='Judge',required=True)
    x_studio_many2one_field_SkrpV = fields.Many2one('x_disciplinaryactionty', string='نوع الاجراء',required=True)
    x_studio_violation_date = fields.Date('تاريخ حدوث المخالفة')
    x_studio_disciplinary_action_date = fields.Date('تاريخ إصدار العقوبة ')
    x_studio_many2one_field_cSMfO = fields.Many2one('x_violationtype', string='نوع المخالفة')
    x_studio_many2one_field_mQZS2 = fields.Many2one('x_disciplinaryauthoriz', string='DisciplinaryAuthorizedBy')
    x_studio_action_date = fields.Date('تاريخ الاجراء')
    x_studio_duration = fields.Char('مدة العقوبة ')
    date_end = fields.Date(compute='_compute_dateend', string='End Date',readonly=True)
    x_studio_many2one_field_pfGMy = fields.Many2one('x_disciplinaryactionju', string='سبب الاجراء')
    x_studio_many2one_field_kU4e0 = fields.Many2one('x_disciplinaryactionst', string='حالة الاجراء')
    x_studio_reporting_date = fields.Date('تاريخ الاخبار عن المخالفة')
    x_studio_disciplinary_letter_no = fields.Char('رقم كتاب العقوبة',required=True)
    x_studio_reporting_attachment = fields.Binary('مرفقات')
    x_studio_many2one_field_dDowS = fields.Many2one('x_disciplinarysource', string='DisciplinarySource')
    x_studio_effective_date = fields.Date('تاريخ سريان و اعتماد الاجراء')
    x_studio_disciplinary_end_date = fields.Date('تاريخ انتهاء العقوبة')
    x_studio_many2one_field_hm3Un = fields.Many2one('x_disciplinaryeffect', string='تأثير العقوبة')
    x_studio_disciplinary_attachment = fields.Binary('disciplinary Attachment')

    x_active = fields.Boolean('Active',default=True)
    x_name = fields.Char('Name')
    x_studio_sequence = fields.Integer('Sequance')

    x_studio_selection_field_ZGU2N = fields.Selection([
        ('initiated', 'تم تقديم الطلب'),
        ('Inprocess', 'بانتظار الموافقة'),
        ('approved', 'تمت الموافقة'),
        ('rejected', 'مرفوض'),
    ], string='Pipeline status bar')

    x_studio_reporting_attachment_filename = fields.Char('Filename for x_studio_binary_field_qp5He')
    x_studio_disciplinary_action_detail_1 = fields.Text('Disciplinary Action Detail')
    x_studio_disciplinary_attachment_filename = fields.Char('Filename for x_studio_binary_field_Grg0b')
    x_studio_related_field_uPdwO = fields.Char('رقم القاضي',related='x_studio_judge.x_studio_judge_code')#related='x_studio_judge.x_studio_judge_code'


    @api.depends('x_studio_action_date','x_studio_duration')
    def _compute_dateend(self):
        try:
           for record in self: 
            if record.x_studio_action_date and record.x_studio_duration:
              record.date_end= record.x_studio_action_date  + relativedelta(days =+ int(record.x_studio_duration))
            else: 
             record.date_end= date.today()
           
        except ValueError:
            record.date_end= date.today()
            # raise ValidationError("Invalid field value for duration Must be As Dayes")
    
     
    @api.onchange('x_studio_many2one_field_hm3Un')
    def _degreade(self):
        for record in self:  
           if record.x_studio_many2one_field_hm3Un and record.x_studio_many2one_field_hm3Un.IsGrade: 
                user=self.env["hr.employee"].search([("id", "=", self.x_studio_judge.id)])     
                if user:    
                #  try:
                    grade= self.env["x_job_grade"].search([("x_studio_level", "=", str(int(user[0].x_studio_many2one_field_4aoaB.x_studio_level)+1))])
                    if grade:
                        user.write({'x_studio_many2one_field_4aoaB':grade[0]})
                   
                #  except ValueError:
                #     pass

    @api.constrains('x_studio_many2one_field_SkrpV')
    def _check_name(self):
        for record in self:
           if record.x_studio_many2one_field_SkrpV: 
             if record.x_studio_many2one_field_SkrpV.PreviesAction:
                recorduser=self.env["x_disciplinary_action"].search_count(["&",("x_studio_judge.id", "=", record.x_studio_judge.id) ,("x_studio_many2one_field_SkrpV.id" ,"=" , record.x_studio_many2one_field_SkrpV.PreviesAction.id) ])     
                if recorduser == 0:     
                    raise ValidationError("This Action Type Need Previous Action")


    