from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re

class x_secondment_type(models.Model):
    _name = 'x_secondment_type'
    _description = 'x_secondment_type'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_secondment_line_e0591(models.Model):
    _name = 'x_secondment_line_e0591'
    _description = 'x_secondment_line_e0591'
    _rec_name="x_name"

    x_studio_date_field_AQt5i = fields.Date('New End Date')
    x_studio_many2one_field_eS1HP = fields.Many2one('x_misison_extension_re', string='سبب التمديد')
    x_studio_text_field_VEiLi = fields.Text('Extension Letter No.')
    x_studio_date_field_CIQTI = fields.Date('Extension Letter No.')
    x_name = fields.Char('الوصف')
    x_secondment_id = fields.Many2one('x_secondment', string='X Secondment')
    x_studio_sequence = fields.Integer('Sequance')


class x_secondment_line_6ef9b(models.Model):
    _name = 'x_secondment_line_6ef9b'
    _description = 'x_secondment_line_6ef9b'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_secondment_id = fields.Many2one('x_secondment', string='X Secondment')
    x_studio_sequence = fields.Integer('المسلسل')
    

    

class x_secondmentcustom(models.Model):
    _name = 'x_secondment'
    
	
    x_studio_judge =fields.Many2one('hr.employee', string='Judge' ,domain="[('x_studio_employee_status','=','على رأس عمله')]",readonly="[('id','>','0')]")
    x_studio_judge_grade_1 = fields.Char('الدرجة',related='x_studio_judge.x_studio_many2one_field_4aoaB.x_name',readonly=True)
    x_studio_new_work_location = fields.Many2one('hr.work.location', string='New Work Location')
    x_studio_related_field_QcS5L = fields.Char('work in related',related='x_studio_judge.job_id.display_name',readonly=True)
    x_studio_status = fields.Char('Status')
    x_studio_start_date = fields.Date('start Date',required=True)
    duration = fields.Integer(compute='_compute_dateend', string='Duration As Daye')
    Fullduration = fields.Char(compute='_compute_duration', string='المدة بالشهور')
    x_studio_last_job_position = fields.Char(compute="_compute_last_job_position", string='Last Job Position',readonly=True,default='')
    x_studio_job_position = fields.Char('Job Position' ,related='x_studio_judge.job_id.display_name',readonly=True)
    x_studio_last_work_location= fields.Char('Last Work Location',readonly=True)
    x_studio_current_work_location_1 = fields.Char('Current work location',related='x_studio_judge.work_location_id.display_name',readonly=True)
    x_studio_last_judge_grade = fields.Char('Last Judge Grade',readonly=True)
    x_studio_related_field_5V6e1 = fields.Char('Judge Grade',related='x_studio_judge.x_studio_many2one_field_4aoaB.x_name',readonly=True)
    x_studio_many2one_field_BKD8J = fields.Many2one('x_secondment_type', string='Secondement Type')
    x_studio_new_job_position = fields.Many2one('hr.job', string='الوظيفة المنتدب اليها',required=True)
    x_studio_end_date = fields.Date('End Date',required=True)
    x_studio_notes = fields.Char('ملاحظات')
    x_studio_duration = fields.Date('Duration',readonly=True)
    x_change = fields.Char('Change')
    x_name = fields.Char('Name')
    x_studio_judge_grade_2 = fields.Char('Judge Grade',readonly=True)
    x_studio_related_field_LCaCq = fields.Char('Judge Grade',related='x_studio_judge.x_studio_many2one_field_4aoaB.x_studio_grade')

    x_secondment_line_ids_31063 = fields.One2many('x_secondment_line_6ef9b', 'x_secondment_id', string='تمديدات الانتداب')

    x_studio_selection_field_elckG = fields.Selection([
        ('initiated','تم تقديم الطلب'),
        ('inprocess','بانتظار الموافقة'),
        ('approved','تمت الموافقة'),
        ('Rejected','مرفوض'),
    ], string='Pipeline status bar')



    x_secondment_line_ids_f9153 = fields.One2many('x_secondment_line_e0591', 'x_secondment_id', string='أسطر جديدة')



    x_active = fields.Boolean('Active',default=True)
    x_studio_sequence = fields.Integer('Sequance')
    x_studio_current_job_position = fields.Many2one('hr.job', string='Current Job Position')
    x_studio_current_work_location = fields.Many2one('hr.work.location', string='current Work Location')
    x_studio_related_field_FOEk5 = fields.Char('Job Position',readonly=True,related='x_studio_current_job_position.employee_ids.job_id.display_name')

    @api.depends('x_studio_judge')
    def _compute_last_job_position(self):
        for record in self:  
            if record.x_studio_judge:
                if not record.x_change:
                    if record.x_studio_judge.job_id:
                       record.x_studio_last_job_position=record.x_studio_judge.job_id.display_name
                    if record.x_studio_judge.x_studio_many2one_field_4aoaB:
                       record.x_studio_last_judge_grade=record.x_studio_judge.x_studio_many2one_field_4aoaB.x_name
                    if record.x_studio_judge.work_location_id :
                       record.x_studio_last_work_location=record.x_studio_judge.work_location_id.display_name
                    record.x_change="done"
                else:
                   record.x_studio_last_job_position=record.x_studio_last_job_position
            else:
                   record.x_studio_last_job_position=''       
 
    @api.depends('x_studio_end_date','x_studio_start_date')
    def _compute_dateend(self):
        try:
           for record in self:   
            if record.x_studio_end_date and record.x_studio_start_date:
               record.duration = (record.x_studio_end_date - record.x_studio_start_date).days
            else: 
             record.duration= 0
        except ValueError:
             record.duration= 0
    
    @api.constrains('x_studio_end_date','x_studio_start_date')
    def _constrainsdate(self):
           for record in self: 
            if record.x_studio_end_date and record.x_studio_start_date:    
             if record.x_studio_end_date < record.x_studio_start_date:
                  raise ValidationError("End Date Must Grater Than Start Date")


    @api.depends('duration','x_studio_judge')
    def _compute_duration(self):
        # try:
            for record in self: 
               dates=int(sum(self.env["x_secondment"].search([("x_studio_judge.id", "=", self.x_studio_judge.id)]).mapped('duration')))/365
               year=int(dates)
               days=dates-int(dates)
               record.Fullduration=" " + str(year) + " Year and "+ str(int(days*365)) +" Days"    


         
        # except ValueError:
        #      record.Fullduration= "0"
