from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re

class x_facilitator(models.Model):
    _name = 'x_facilitator'
    _description = 'x_facilitator'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_course_subject(models.Model):
    _name = 'x_course_subject'
    _description = 'x_course_subject'
    _rec_name="x_name"

    x_name = fields.Char('Name')
    x_subject_code = fields.Char('Subject Code')

class x_course_location(models.Model):
    _name = 'x_course_location'
    _description = 'x_course_location'
    _rec_name="x_name"

    x_name = fields.Char('Name')
    x_active = fields.Boolean('Active',default=True)
    x_studio_region = fields.Char('Region')
    x_studio_sequence = fields.Integer('Sequence')
    x_studio_many2one_field_mhP5c = fields.Many2one('res.country', string='Country')

class x_execution_party(models.Model):
    _name = 'x_execution_party'
    _description = 'x_execution_party'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_instructor(models.Model):
    _name = 'x_instructor'
    _description = 'x_instructor'
    _rec_name="x_name"

    x_name = fields.Char('Name')


class x_training_avenue(models.Model):
    _name = 'x_training_avenue'
    _description = 'x_training_avenue'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_syllabus_coordinator(models.Model):
    _name = 'x_syllabus_coordinator'
    _description = 'x_syllabus_coordinator'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_funding_party(models.Model):
    _name = 'x_funding_party'
    _description = 'x_funding_party'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_trainingunit_line_20a0f(models.Model):
    _name = 'x_trainingunit_line_20a0f'
    _description = 'x_trainingunit_line_20a0f'

    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_datetime_field_yepLT = fields.Datetime('New Date & Time')
    x_studio_day = fields.Selection([
        ('Sat', 'Sat'),
        ('Sun', 'Sun'),
        ('Mon', 'Mon'),
        ('Tue', 'Tue'),
        ('Wed', 'Wed'),
        ('Thu', 'Thu'),
    ], string='Day')
    
    x_studio_sequence = fields.Integer('Sequence')
    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')

class x_trainingunit_line_6fae4(models.Model):
    _name = 'x_trainingunit_line_6fae4'
    _description = 'x_trainingunit_line_6fae4'

    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)

    x_studio_day = fields.Selection([
        ('Sat', 'Sat'),
        ('Sun', 'Sun'),
        ('Mon', 'Mon'),
        ('Tue', 'Tue'),
        ('Wed', 'Wed'),
        ('Thu', 'Thu'),
    ], string='Day')

    x_studio_from_hour = fields.Selection([
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
    ], string='From Hour')

    x_studio_from_min = fields.Selection([
        ('00', '00'),
        ('15', '15'),
        ('30', '30'),
        ('45', '45'),
    ], string='From Min')

    x_studio_sequence = fields.Integer('Sequence')

    x_studio_to_hour = fields.Selection([
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
    ], string='To Hour')

    x_studio_to_min = fields.Selection([
        ('00', '00'),
        ('15', '15'),
        ('30', '30'),
        ('45', '45'),
    ], string='To Min')

    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')

class x_trainingunit_line_e8e88(models.Model):
    _name = 'x_trainingunit_line_e8e88'
    _description = 'x_trainingunit_line_e8e88'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')

class x_prerequesite_type(models.Model):
    _name = 'x_prerequesite_type'
    _description = 'x_prerequesite_type'
    _rec_name="x_name"
    x_name = fields.Char('Name')

class x_prerequisite_details(models.Model):
    _name = 'x_prerequisite_details'
    _description = 'x_prerequisite_details'
    _rec_name="x_name"
    x_name = fields.Char('Name')

    

    

class x_trainingunit_line_b2000(models.Model):
    _name = 'x_trainingunit_line_b2000'
    _description = 'x_trainingunit_line_b2000'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_max = fields.Integer('Max')
    x_studio_min = fields.Integer('Min')

    x_studio_sequence = fields.Integer('Sequence')
    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')
    x_studio_many2one_field_qUY9l = fields.Many2one('x_prerequesite_type', string='Prerequesite type')
    x_studio_many2one_field_ZPooD = fields.Many2one('x_prerequisite_details', string='Prerequisite Details')
    

class x_trainingunit_line_bff8a(models.Model):
    _name = 'x_trainingunit_line_bff8a'
    _description = 'x_trainingunit_line_bff8a'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')

class x_trainingunit_line_177ae(models.Model):
    _name = 'x_trainingunit_line_177ae'
    _description = 'x_trainingunit_line_177ae'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')
    
class x_trainingunit_line_c713c(models.Model):
    _name = 'x_trainingunit_line_c713c'
    _description = 'x_trainingunit_line_c713c'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')
    
class x_trainingunit_line_a275d(models.Model):
    _name = 'x_trainingunit_line_a275d'
    _description = 'x_trainingunit_line_a275d'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')

class x_trainingunit_line_c7f73(models.Model):
    _name = 'x_trainingunit_line_c7f73'
    _description = 'x_trainingunit_line_c7f73'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')
    x_studio_judge = fields.Many2one('hr.employee', string='Judge')
    x_studio_position = fields.Char('Position',readonly=True,related='x_studio_judge.job_id.display_name')
    x_studio_work_location = fields.Char('Work location',readonly=True,related='x_studio_judge.work_location_id.display_name')


class x_trainingunit_line_efd36(models.Model):
    _name = 'x_trainingunit_line_efd36'
    _description = 'x_trainingunit_line_efd36'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')

class x_trainingunit_line_e020b(models.Model):
    _name = 'x_trainingunit_line_e020b'
    _description = 'x_trainingunit_line_e020b'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')

class x_trainingunit_line_73a61(models.Model):
    _name = 'x_trainingunit_line_73a61'
    _description = 'x_trainingunit_line_73a61'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')    

class x_trainingunit_line_6efa9(models.Model):
    _name = 'x_trainingunit_line_6efa9'
    _description = 'x_trainingunit_line_6efa9'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')    

    
class x_trainingunit_line_727c3(models.Model):
    _name = 'x_trainingunit_line_727c3'
    _description = 'x_trainingunit_line_727c3'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')    

class x_trainingunit_line_213b8(models.Model):
    _name = 'x_trainingunit_line_213b8'
    _description = 'x_trainingunit_line_213b8'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_trainingunit_id = fields.Many2one('x_trainingunit', string='X Trainingunit')       
    

class x_trainingunit(models.Model):
    _name = 'x_trainingunit'
    _description = 'x_trainingunit'
    _rec_name="x_name"


    x_active = fields.Boolean('Active',default=True)
    x_name = fields.Char('Name')
    x_studio_allow_expenses = fields.Boolean('Allow Expenses?')
    x_studio_attendance_type = fields.Selection([
        ('وجاهي', 'وجاهي'),
        ('عبر الانترنت', 'عبر الانترنت'),
    ], string='Attendance Type')

    x_studio_char_field_vrhnI = fields.Char('New Text')
    x_studio_commitment_ = fields.Boolean('Commitment ?')
    x_studio_cource_code = fields.Char('Cource Code')
    x_studio_end_date = fields.Date('End Date')    
    x_studio_financial_effect_ = fields.Boolean('Financial Effect ?')
    x_studio_many2one_field_CENRk = fields.Many2one('x_facilitator', string='Facilitator')
    x_studio_many2one_field_HZhMd = fields.Many2one('x_course_subject', string='Course subject')
    x_studio_many2one_field_jCZUC = fields.Many2one('x_course_location', string='Course Location')
    x_studio_many2one_field_oE4gS = fields.Many2one('x_execution_party', string='Execution Party')
    x_studio_many2one_field_w8UM9 = fields.Many2one('x_instructor', string='Instructor')
    x_studio_many2one_field_wh3Nr   = fields.Many2one('x_training_avenue', string='training avenue')
    x_studio_many2one_field_WKgRp = fields.Many2one('x_syllabus_coordinator', string='syllabus Coordinator')
    x_studio_many2one_field_WMiv9 = fields.Many2one('x_funding_party', string='funding Party')
    x_studio_many2one_field_zF8r1 = fields.Many2one('res.country', string='Country')
    x_studio_max_trainees = fields.Integer('Max Trainees')
    x_studio_min_trainees = fields.Integer('Min. Trainees')
    x_studio_one_from_every_position = fields.Boolean('One from every Position')
    x_studio_selection_field_7Am97 = fields.Selection([
        ('status1', 'Not started'),
        ('status2', 'In progress'),
        ('status3', 'Cancelled'),
    ], string='Pipeline status bar')

    x_studio_sequence = fields.Integer('Sequence')
    x_studio_serial_no = fields.Integer('Serial No.')
    x_studio_start_date = fields.Date('Start Date')
    x_studio_text_field_MBcAQ = fields.Text('New Multiline Text')

    x_trainingunit_line_ids_1d388 = fields.One2many('x_trainingunit_line_20a0f', 'x_trainingunit_id', string='New Lines')
    x_trainingunit_line_ids_1dfad = fields.One2many('x_trainingunit_line_6fae4', 'x_trainingunit_id', string='New Lines')
    x_trainingunit_line_ids_2480c = fields.One2many('x_trainingunit_line_e8e88', 'x_trainingunit_id', string='New Lines')
    x_trainingunit_line_ids_2d387 = fields.One2many('x_trainingunit_line_b2000', 'x_trainingunit_id', string='New Lines')
    x_trainingunit_line_ids_4237f = fields.One2many('x_trainingunit_line_bff8a', 'x_trainingunit_id', string='New Lines')
    x_trainingunit_line_ids_5acfd = fields.One2many('x_trainingunit_line_177ae', 'x_trainingunit_id', string='New Lines')
    x_trainingunit_line_ids_80df3 = fields.One2many('x_trainingunit_line_c713c', 'x_trainingunit_id', string='New Lines')
    x_trainingunit_line_ids_81b47 = fields.One2many('x_trainingunit_line_a275d', 'x_trainingunit_id', string='New Lines')
    x_trainingunit_line_ids_a1c3f = fields.One2many('x_trainingunit_line_c7f73', 'x_trainingunit_id', string='New Lines')
    x_trainingunit_line_ids_d1e8e = fields.One2many('x_trainingunit_line_efd36', 'x_trainingunit_id', string='New Lines')
    x_trainingunit_line_ids_df2fe = fields.One2many('x_trainingunit_line_e020b', 'x_trainingunit_id', string='New Lines')
    x_trainingunit_line_ids_e21c9 = fields.One2many('x_trainingunit_line_73a61', 'x_trainingunit_id', string='Judges')
    x_trainingunit_line_ids_e5c1b = fields.One2many('x_trainingunit_line_6efa9', 'x_trainingunit_id', string='New Lines')
    x_trainingunit_line_ids_e60a5 = fields.One2many('x_trainingunit_line_727c3', 'x_trainingunit_id', string='New Lines')
    x_trainingunit_line_ids_f8285 = fields.One2many('x_trainingunit_line_213b8', 'x_trainingunit_id', string='New Lines')












