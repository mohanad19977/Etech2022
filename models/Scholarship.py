from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re

class scholarship(models.Model):
   _name = 'x_scholarship'
   _description = 'x_scholarship'
   _rec_name="x_name"
   

   x_name = fields.Char('Name')
   x_scholarship_line_ids_0d975 = fields.One2many('x_scholarship_line_29636', 'x_scholarship_id', string='X Scholarship Line Ids 0D975')
   x_scholarship_line_ids_df6fb = fields.One2many('x_scholarship_line_1a8b1', 'x_scholarship_id', string='Participating Judges')
   x_studio_accumulative_duration = fields.Float('X Studio Accumulative Duration')
   x_studio_approval_letter = fields.Char('Approval Letter')
   x_studio_approval_letter_no= fields.Char('Approval Letter No')
   x_studio_attachment = fields.Binary('Attachment')
   x_studio_binary_field_9v8iU_filename= fields.Char('Filename for x_studio_binary_field_9v8iU')
   x_studio_binary_field_9v8iU = fields.Binary('New الملف')
   x_studio_country = fields.Many2one('x_birth_country', string='country')
   x_studio_date_field_1Eqvy = fields.Date('Letter Date')
   x_studio_date_field_UjIuN = fields.Date('New التاريخ')
   x_studio_duration_years= fields.Integer('Duration Years')
   x_studio_end_date = fields.Date('End Date')
   x_studio_many2one_field_15I43 = fields.Many2one('res.country', string='الدولة')
   x_studio_many2one_field_2djPD = fields.Many2one('x_funding_party', string='Funding Source')
   x_studio_many2one_field_bpnkP = fields.Many2one('x_funding_party', string='funding Party')
   x_studio_many2one_field_nQumW = fields.Many2one('x_specialty', string='Specialty')
   x_studio_many2one_field_SRn9u = fields.Many2one('x_institue', string='Institute')
   x_studio_start_date = fields.Date('Start Date')
   x_studio_sequence = fields.Integer('Sequence')
   x_studio_scholrship_date = fields.Date(' Scholrship Date')
   x_studio_scholarship_code = fields.Char(' Scholarship Code')
   x_studio_many2one_field_q6fvv = fields.Many2one( 'x_participationtype', string='Participation Type')
   x_studio_many2one_field_qACdR = fields.Many2one('x_specialty', string='Specialty')
   x_studio_many2one_field_kqyV7 = fields.Many2one('res.country', string='Country')
   date_end = fields.Date(compute='_compute_dateend', string='End Date')
    
   @api.depends('x_studio_start_date','x_studio_duration_years')
   def _compute_dateend(self):
        try:
          for record in self:  
            if record.x_studio_start_date and record.x_studio_duration_years:
             record.date_end= record.x_studio_start_date  + relativedelta(years=+ int(record.x_studio_duration_years))
            else: 
             record.date_end= date.today()
        except ValueError:
            record.date_end= date.today()


class X_Scholarship_Line_1a8b1(models.Model):
    _name = 'x_scholarship_line_1a8b1'
    _description = 'Scholarship Lines'
    _rec_name="x_name"
   

    x_name = fields.Char('Name')
    x_scholarship_id = fields.Many2one('x_scholarship', string='X Scholarship')
    x_studio_sequence = fields.Integer('Sequence')

   

class X_Scholarship_Line_29636(models.Model):
    _name = 'x_scholarship_line_29636'
    _description = 'Scholarship Lines'
    _rec_name="x_name"
   

    x_name = fields.Char('Name')
    x_scholarship_id = fields.Many2one('x_scholarship', string='X Scholarship')
    x_studio_authorization = fields.Boolean('Authorization')
    x_studio_job_position = fields.Char('Job Position',readonly=True)
    x_studio_last_report_date = fields.Date('Last Report Date')
    x_studio_many2one_field_1Cl23 = fields.Many2one('x_thieses', string='Thesis')
    x_studio_many2one_field_1Pi7x = fields.Many2one('x_institue', string='Institute')
    x_studio_many2one_field_9E6gH = fields.Many2one('x_judge_status', string='judge status')
    x_studio_resumption_date = fields.Date('Resumption Date')
    x_studio_sequence = fields.Integer('Sequence')
    x_studio_work_location = fields.Char('work location')
    x_studio_many2one_field_z9f19 = fields.Many2one('hr.employee', string='Judge' ,domain="[('x_studio_employee_status','=','على رأس عمله')]")


class participationtype(models.Model):
    _name = 'x_participationtype'
    _description = 'participationtype'
    _rec_name="x_name"
    

    x_name = fields.Char('Name')



class specialty(models.Model):
    _name = 'x_specialty'
    _description = 'specialty'
    _rec_name="x_name"
    

    x_name = fields.Char('Name')

class x_thiesesmodel(models.Model):
    _name = 'x_thieses'
    _description = 'thieses'
    _rec_name="x_name"
    

    x_name = fields.Char('Name')


class x_instituemodel(models.Model):
    _name = 'x_institue'
    _description = 'institue'
    _rec_name="x_name"
    

    x_name = fields.Char('Name')

class x_judgemodel(models.Model):
    _name = 'x_judge_status'
    _description = 'judge status'
    _rec_name="x_name"
    

    x_name = fields.Char('Name')    










