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
    
    x_judgepromotion_id = fields.Many2one('x_judgepromotion', string='Judgepromotion')
    x_name = fields.Char('x_name')
    x_studio_many2one_field_gXLon = fields.Many2one('hr.employee', string='Judge',required=True)
    x_studio_old_job_position= fields.Char('Old Job Position' )   
    x_studio_old_grade= fields.Many2one('x_job_grade', string='الدرجة القديمة') 
    x_studio_related_field_LHjqP = fields.Char('موقع العمل الحالي')
    x_studio_years_in_old_grade = fields.Float('الدرجة الحالية')
    x_studio_years_in_grade = fields.Float('سنة في الدرجة')
    x_studio_new_job_position = fields.Many2one('hr.job', string='الوظيفة الجديدة')
    x_studio_new_job_grade = fields.Many2one('x_job_grade', string='الدرجة الجديدة')
    x_studio_sequence = fields.Integer('Sequence')
    
    @api.onchange('x_studio_many2one_field_gXLon')
    def _onchange_(self):
        for record in self:
          if record.x_studio_many2one_field_gXLon:
            record.x_studio_old_grade= record.x_studio_many2one_field_gXLon.x_studio_many2one_field_4aoaB.id
            record.x_studio_years_in_grade= int(date.today().year - record.x_studio_many2one_field_gXLon.changedate.year) 
            record.x_studio_new_job_position= record.x_studio_many2one_field_gXLon.job_id.id
            record.x_studio_old_job_position= record.x_studio_many2one_field_gXLon.job_id.display_name
            grade= self.env["x_job_grade"].search([("x_studio_level", "=", str(int(record.x_studio_many2one_field_gXLon.x_studio_many2one_field_4aoaB.x_studio_level)+1))])
            if grade:
               record.x_studio_new_job_grade= grade[0].id

class JudgePromotion(models.Model):
    _name = 'x_judgepromotion'
    _description = 'x_judgepromotion'
    _rec_name="x_name"

    x_name = fields.Char('x_name')
    x_studio_letter_date = fields.Date('Letter Date')
    x_studio_promotions_letter_no = fields.Char('Promotions Letter No.',required=True)
    x_studio_effective_date = fields.Date('effective Date',required=True)
    x_studio_reference = fields.Char('Reference') 
    x_judgepromotion_line_ids_c0b72 = fields.One2many('x_judgepromotion_line_ac79d', 'x_judgepromotion_id', string='Judges List')
    x_active = fields.Boolean('Active',default=True)
    x_studio_sequence = fields.Integer('Sequence')
    state = fields.Boolean('state')
    Attachment = fields.Binary('Attachment')

    x_studio_selection_field_GUisB = fields.Selection([
        ('initiated','جديد'),
        ('inprocess','تحت التنفيذ'),
        ( 'approved','تم'),
        ('Rejected','مرفوض'),
    ], string='Status')

    

    
    def GetPromotionJudge(self): 
         for record in self:
            users=self.env["hr.employee"].search(["&",("changedate", "<", date.today()- relativedelta(day=+1800)),('x_studio_employee_status','=','على رأس عمله')])     
            if users:    
                order_lines = []
                #  try:
                for judge in users:
                  if judge.x_studio_many2one_field_4aoaB:  
                    grade= self.env["x_job_grade"].search([("x_studio_level", "=", str(int(judge.x_studio_many2one_field_4aoaB.x_studio_level)+1))])
                    if grade:
                        order_lines.append((0, 0, {
                            'x_studio_many2one_field_gXLon': judge.id,
                            'x_studio_old_grade': judge.x_studio_many2one_field_4aoaB.id,
                            'x_studio_years_in_grade': (date.today().year - judge.changedate.year) ,
                            'x_studio_new_job_position': judge.job_id.id,
                            'x_studio_old_job_position': judge.job_id.display_name,
                            'x_studio_new_job_grade': grade[0].id
                        }))
                        
                        # judge.write({'x_studio_many2one_field_4aoaB':grade[0]})

                record.x_judgepromotion_line_ids_c0b72=order_lines


   


    def Confirm(self):
        for record in self:
            record.state=True
            record.x_studio_selection_field_GUisB='approved'
            # for emp in record.x_judgepromotion_line_ids_c0b72:
            #  user=self.env["hr.employee"].search([("id", "=", emp.x_studio_many2one_field_gXLon.id)])     
            #  if user:    
            #     #  try:
            #      user.write({
            #         'x_studio_many2one_field_4aoaB':emp.x_studio_new_job_grade,
            #         'job_id':emp.x_studio_new_job_position,
            #         'changedate':date.today()
            #         })


    def Confirmcron(self):
        promations=self.env["x_judgepromotion"].search([("state", "=", True)])
        for record in promations:
           if record.x_studio_effective_date: 
            if record.state==True and record.x_studio_effective_date <=date.today():
             for emp in record.x_judgepromotion_line_ids_c0b72:
              user=self.env["hr.employee"].search([("id", "=", emp.x_studio_many2one_field_gXLon.id)])     
              if user:    
                #  try:
                 record.write({
                    'state':True,
                     'x_studio_selection_field_GUisB':'approved',
                    }) 
                 user.write({
                    'x_studio_many2one_field_4aoaB':emp.x_studio_new_job_grade,
                    'job_id':emp.x_studio_new_job_position,
                    'changedate':date.today()
                    }) 