from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re


class x_job_card_line_dd787(models.Model):
    _name = 'x_job_card_line_dd787'
    _description = 'x_job_card_line_dd787'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_a46c1(models.Model):
    _name = 'x_job_card_line_a46c1'
    _description = 'x_job_card_line_a46c1'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_308da(models.Model):
    _name = 'x_job_card_line_308da'
    _description = 'x_job_card_line_308da'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_f76d9(models.Model):
    _name = 'x_job_card_line_f76d9'
    _description = 'x_job_card_line_f76d9'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_d15d8(models.Model):
    _name = 'x_job_card_line_d15d8'
    _description = 'x_job_card_line_d15d8'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')
    
class x_job_card_line_adbfb(models.Model):
    _name = 'x_job_card_line_adbfb'
    _description = 'x_job_card_line_adbfb'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_38487(models.Model):
    _name = 'x_job_card_line_38487'
    _description = 'x_job_card_line_38487'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_d0b43(models.Model):
    _name = 'x_job_card_line_d0b43'
    _description = 'x_job_card_line_d0b43'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_48653(models.Model):
    _name = 'x_job_card_line_48653'
    _description = 'x_job_card_line_48653'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_5409b(models.Model):
    _name = 'x_job_card_line_5409b'
    _description = 'x_job_card_line_5409b'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

    
class x_job_card_line_6cc70(models.Model):
    _name = 'x_job_card_line_6cc70'
    _description = 'x_job_card_line_6cc70'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_323d1(models.Model):
    _name = 'x_job_card_line_323d1'
    _description = 'x_job_card_line_323d1'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_cc73b(models.Model):
    _name = 'x_job_card_line_cc73b'
    _description = 'x_job_card_line_cc73b'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_927d5(models.Model):
    _name = 'x_job_card_line_927d5'
    _description = 'x_job_card_line_927d5'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_95d8c(models.Model):
    _name = 'x_job_card_line_95d8c'
    _description = 'x_job_card_line_95d8c'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_f03ff(models.Model):
    _name = 'x_job_card_line_f03ff'
    _description = 'x_job_card_line_f03ff'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_a2d81(models.Model):
    _name = 'x_job_card_line_a2d81'
    _description = 'x_job_card_line_a2d81'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_69939(models.Model):
    _name = 'x_job_card_line_69939'
    _description = 'x_job_card_line_69939'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_e464d(models.Model):
    _name = 'x_job_card_line_e464d'
    _description = 'x_job_card_line_e464d'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_662eb(models.Model):
    _name = 'x_job_card_line_662eb'
    _description = 'x_job_card_line_662eb'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')
    
class x_job_card_line_724fa(models.Model):
    _name = 'x_job_card_line_724fa'
    _description = 'x_job_card_line_724fa'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_bc98f(models.Model):
    _name = 'x_job_card_line_bc98f'
    _description = 'x_job_card_line_bc98f'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

    

class x_job_card_line_14a4d(models.Model):
    _name = 'x_job_card_line_14a4d'
    _description = 'x_job_card_line_14a4d'
    _rec_name="x_name"

    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Admin Assignment Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')
    x_studio_admin_serial_no = fields.Integer('Admin Serial No')
    x_studio_administrative_task = fields.Many2one('x_administrative_tas', string='	Administrative task')

class x_administrative_tas(models.Model):
    _name = 'x_administrative_tas'
    _description = 'x_administrative_tas'

    _rec_name="x_name"
    x_name = fields.Char('Name')

class x_job_card_line_f6cc0(models.Model):
    _name = 'x_job_card_line_f6cc0'
    _description = 'x_job_card_line_f6cc0'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_3ec95(models.Model):
    _name = 'x_job_card_line_3ec95'
    _description = 'x_job_card_line_3ec95'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_e470d(models.Model):
    _name = 'x_job_card_line_e470d'
    _description = 'x_job_card_line_e470d'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_competency(models.Model):
    _name = 'x_competency'
    _description = 'x_competency'

    _rec_name="x_name"
    x_name = fields.Char('Name')

class x_competency_group(models.Model):
    _name = 'x_competency_group'
    _description = 'x_competency_group'
    
    _rec_name="x_name"
    x_name = fields.Char('Name')

    

class x_job_card_line_48288(models.Model):
    _name = 'x_job_card_line_48288'
    _description = 'x_job_card_line_48288'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')
    x_studio_competency_serial_no = fields.Integer('Competency Serial no')
    x_studio_many2one_field_3F0DG = fields.Many2one('x_competency', string='Competency')
    x_studio_many2one_field_fNd8S = fields.Many2one('x_competency_group', string='Competency Group')
    x_studio_minimum_level = fields.Selection([
        ('متخصص', 'متخصص'),
        ('متقدم', 'متقدم'),
        ('مبتدئ', 'مبتدئ'),
        ('مستخدم', 'مستخدم'),
    ], string='Minimum Level')

class x_job_card_line_e8478(models.Model):
    _name = 'x_job_card_line_e8478'
    _description = 'x_job_card_line_e8478'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_cfc27(models.Model):
    _name = 'x_job_card_line_cfc27'
    _description = 'x_job_card_line_cfc27'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_b050a(models.Model):
    _name = 'x_job_card_line_b050a'
    _description = 'x_job_card_line_b050a'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_12317(models.Model):
    _name = 'x_job_card_line_12317'
    _description = 'x_job_card_line_12317'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_09b57(models.Model):
    _name = 'x_job_card_line_09b57'
    _description = 'x_job_card_line_09b57'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_c6d4f(models.Model):
    _name = 'x_job_card_line_c6d4f'
    _description = 'x_job_card_line_c6d4f'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_practical_qualificat(models.Model):
    _name = 'x_practical_qualificat'
    _description = 'x_practical_qualificat'

    _rec_name="x_name"
    x_name = fields.Char('Name')

    

class x_job_card_line_c9d70(models.Model):
    _name = 'x_job_card_line_c9d70'
    _description = 'x_job_card_line_c9d70'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Experience Remarks',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')  

    x_studio_experience_field = fields.Selection([
        ('السلكالقضائي', 'السلك القضائي'),
        ('المحاماة', 'المحاماة'),
    ], string='Experience field')

    x_studio_importance = fields.Selection([
        ('أساسي', 'أساسي'),
        ('مرغوب به', 'مرغوب به'),
    ], string='Importance')

    x_studio_mandatory = fields.Boolean('Mandatory?')
    x_studio_max_years = fields.Integer('Max Years')
    x_studio_max_years_1 = fields.Integer('Max Years')
    x_studio_min_years_1 = fields.Integer('min Years')
    x_studio_practical_serial_no = fields.Integer('Practical Serial No')
    x_studio_many2one_field_Glsb2 = fields.Many2one('x_practical_qualificat', string='Practical Qualification')

class x_job_card_line_4103f(models.Model):
    _name = 'x_job_card_line_4103f'
    _description = 'x_job_card_line_4103f'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')


class x_job_card_line_72dd4(models.Model):
    _name = 'x_job_card_line_72dd4'
    _description = 'x_job_card_line_72dd4'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')
    

class x_job_card_line_4f4a9(models.Model):
    _name = 'x_job_card_line_4f4a9'
    _description = 'x_job_card_line_4f4a9'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_c7f1f(models.Model):
    _name = 'x_job_card_line_c7f1f'
    _description = 'x_job_card_line_c7f1f'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_9b0f8(models.Model):
    _name = 'x_job_card_line_9b0f8'
    _description = 'x_job_card_line_9b0f8'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_107e8(models.Model):
    _name = 'x_job_card_line_107e8'
    _description = 'x_job_card_line_107e8'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_5a94b(models.Model):
    _name = 'x_job_card_line_5a94b'
    _description = 'x_job_card_line_5a94b'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_eea7d(models.Model):
    _name = 'x_job_card_line_eea7d'
    _description = 'x_job_card_line_eea7d'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_884f2(models.Model):
    _name = 'x_job_card_line_884f2'
    _description = 'x_job_card_line_884f2'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_8636d(models.Model):
    _name = 'x_job_card_line_8636d'
    _description = 'x_job_card_line_8636d'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_c7b42(models.Model):
    _name = 'x_job_card_line_c7b42'
    _description = 'x_job_card_line_c7b42'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_c5096(models.Model):
    _name = 'x_job_card_line_c5096'
    _description = 'x_job_card_line_c5096'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_c7b07(models.Model):
    _name = 'x_job_card_line_c7b07'
    _description = 'x_job_card_line_c7b07'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_062b9(models.Model):
    _name = 'x_job_card_line_062b9'
    _description = 'x_job_card_line_062b9'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_63a1f(models.Model):
    _name = 'x_job_card_line_63a1f'
    _description = 'x_job_card_line_63a1f'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Supervision Remarks',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')
    x_studio_supervision_serial = fields.Integer('Supervision Serial')
    x_studio_many2one_field_B6j5b = fields.Many2one('hr.job', string='Job Position')

class x_job_card_line_9b77b(models.Model):
    _name = 'x_job_card_line_9b77b'
    _description = 'x_job_card_line_9b77b'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_education_qualificat(models.Model):
    _name = 'x_education_qualificat'
    _description = 'x_education_qualificat'
    _rec_name="x_name"
    x_name = fields.Char('Name',required=True)

    

class x_job_card_line_99be8(models.Model):
    _name = 'x_job_card_line_99be8'
    _description = 'x_job_card_line_99be8'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Edu Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')
    x_studio_edu_serial_no = fields.Integer('Edu Serial No')

    x_studio_importance = fields.Selection([
        ('أساسي', 'أساسي'),
        ('مرغوب به', 'مرغوب به'),
    ], string='Importance')

    x_studio_mandatory_ = fields.Boolean('Mandatory ?')
    x_studio_many2one_field_sQoKm = fields.Many2one('x_education_qualificat', string='Education Qualification')

class x_job_card_line_e5982(models.Model):
    _name = 'x_job_card_line_e5982'
    _description = 'x_job_card_line_e5982'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_3eb3c(models.Model):
    _name = 'x_job_card_line_3eb3c'
    _description = 'x_job_card_line_3eb3c'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_e9940(models.Model):
    _name = 'x_job_card_line_e9940'
    _description = 'x_job_card_line_e9940'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_58956(models.Model):
    _name = 'x_job_card_line_58956'
    _description = 'x_job_card_line_58956'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')


class x_job_card_line_c13a5(models.Model):
    _name = 'x_job_card_line_c13a5'
    _description = 'x_job_card_line_c13a5'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')


class x_job_card_line_52beb(models.Model):
    _name = 'x_job_card_line_52beb'
    _description = 'x_job_card_line_52beb'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')


class x_job_card_line_22666(models.Model):
    _name = 'x_job_card_line_22666'
    _description = 'x_job_card_line_22666'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_65542(models.Model):
    _name = 'x_job_card_line_65542'
    _description = 'x_job_card_line_65542'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_378d1(models.Model):
    _name = 'x_job_card_line_378d1'
    _description = 'x_job_card_line_378d1'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_794ca(models.Model):
    _name = 'x_job_card_line_794ca'
    _description = 'x_job_card_line_794ca'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_1b55d(models.Model):
    _name = 'x_job_card_line_1b55d'
    _description = 'x_job_card_line_1b55d'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_73c2b(models.Model):
    _name = 'x_job_card_line_73c2b'
    _description = 'x_job_card_line_73c2b'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_personal_characteris(models.Model):
    _name = 'x_personal_characteris'
    _description = 'x_personal_characteris'
    _rec_name="x_name"
    x_name = fields.Char('Name')

class x_job_card_line_8bde8(models.Model):
    _name = 'x_job_card_line_8bde8'
    _description = 'x_job_card_line_8bde8'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Personal Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')
    x_studio_personal_serial_no = fields.Integer('Personal Serial No')
    x_studio_selection_field_ZmFbZ = fields.Selection([
        ('أساسي', 'أساسي'),
        ('مرغوب به', 'مرغوب به'),
    ], string='	New Selection')

    x_studio_many2one_field_RfHM2 = fields.Many2one('x_personal_characteris', string='personal characteristics')


class x_job_card_line_df67d(models.Model):
    _name = 'x_job_card_line_df67d'
    _description = 'x_job_card_line_df67d'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_435e7(models.Model):
    _name = 'x_job_card_line_435e7'
    _description = 'x_job_card_line_435e7'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_d8be0(models.Model):
    _name = 'x_job_card_line_d8be0'
    _description = 'x_job_card_line_d8be0'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')


class x_job_card_line_53aa5(models.Model):
    _name = 'x_job_card_line_53aa5'
    _description = 'x_job_card_line_53aa5'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_f0297(models.Model):
    _name = 'x_job_card_line_f0297'
    _description = 'x_job_card_line_f0297'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_77c88(models.Model):
    _name = 'x_job_card_line_77c88'
    _description = 'x_job_card_line_77c88'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_7c79e(models.Model):
    _name = 'x_job_card_line_7c79e'
    _description = 'x_job_card_line_7c79e'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_e7ba1(models.Model):
    _name = 'x_job_card_line_e7ba1'
    _description = 'x_job_card_line_e7ba1'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_c5299(models.Model):
    _name = 'x_job_card_line_c5299'
    _description = 'x_job_card_line_c5299'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_internal_parties(models.Model):
    _name = 'x_internal_parties'
    _description = 'x_internal_parties'
    _rec_name="x_name"
    x_name = fields.Char('Name')

    

class x_job_card_line_b0fc7(models.Model):
    _name = 'x_job_card_line_b0fc7'
    _description = 'x_job_card_line_b0fc7'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Remarks',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')
    x_studio_int_serial_no = fields.Integer('Int Serial No')
    x_studio_many2one_field_GYzQJ = fields.Many2one('x_internal_parties', string='internal parties')
    x_studio_many2one_field_QGeEd = fields.Many2one('hr.job', string='Job Position')
    
class x_job_card_line_6d93b(models.Model):
    _name = 'x_job_card_line_6d93b'
    _description = 'x_job_card_line_6d93b'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_24ae5(models.Model):
    _name = 'x_job_card_line_24ae5'
    _description = 'x_job_card_line_24ae5'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_329f9(models.Model):
    _name = 'x_job_card_line_329f9'
    _description = 'x_job_card_line_329f9'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_12304(models.Model):
    _name = 'x_job_card_line_12304'
    _description = 'x_job_card_line_12304'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')


class x_job_card_line_258d2(models.Model):
    _name = 'x_job_card_line_258d2'
    _description = 'x_job_card_line_258d2'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_bfc4e(models.Model):
    _name = 'x_job_card_line_bfc4e'
    _description = 'x_job_card_line_bfc4e'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_23047(models.Model):
    _name = 'x_job_card_line_23047'
    _description = 'x_job_card_line_23047'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_b62bb(models.Model):
    _name = 'x_job_card_line_b62bb'
    _description = 'x_job_card_line_b62bb'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_7330d(models.Model):
    _name = 'x_job_card_line_7330d'
    _description = 'x_job_card_line_7330d'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_d7015(models.Model):
    _name = 'x_job_card_line_d7015'
    _description = 'x_job_card_line_d7015'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_b9739(models.Model):
    _name = 'x_job_card_line_b9739'
    _description = 'x_job_card_line_b9739'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_6c420(models.Model):
    _name = 'x_job_card_line_6c420'
    _description = 'x_job_card_line_6c420'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_6bd06(models.Model):
    _name = 'x_job_card_line_6bd06'
    _description = 'x_job_card_line_6bd06'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_d4130(models.Model):
    _name = 'x_job_card_line_d4130'
    _description = 'x_job_card_line_d4130'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_f627b(models.Model):
    _name = 'x_job_card_line_f627b'
    _description = 'x_job_card_line_f627b'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_f91c6(models.Model):
    _name = 'x_job_card_line_f91c6'
    _description = 'x_job_card_line_f91c6'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_0904e(models.Model):
    _name = 'x_job_card_line_0904e'
    _description = 'x_job_card_line_0904e'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_9b8a5(models.Model):
    _name = 'x_job_card_line_9b8a5'
    _description = 'x_job_card_line_9b8a5'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_9b8a5(models.Model):
    _name = 'x_job_card_line_9b8a5'
    _description = 'x_job_card_line_9b8a5'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_cc0f4(models.Model):
    _name = 'x_job_card_line_cc0f4'
    _description = 'x_job_card_line_cc0f4'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_df911(models.Model):
    _name = 'x_job_card_line_df911'
    _description = 'x_job_card_line_df911'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_1f8b1(models.Model):
    _name = 'x_job_card_line_1f8b1'
    _description = 'x_job_card_line_1f8b1'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_4ef29(models.Model):
    _name = 'x_job_card_line_4ef29'
    _description = 'x_job_card_line_4ef29'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_02175(models.Model):
    _name = 'x_job_card_line_02175'
    _description = 'x_job_card_line_02175'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_e36fc(models.Model):
    _name = 'x_job_card_line_e36fc'
    _description = 'x_job_card_line_e36fc'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_a3cde(models.Model):
    _name = 'x_job_card_line_a3cde'
    _description = 'x_job_card_line_a3cde'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_6f75d(models.Model):
    _name = 'x_job_card_line_6f75d'
    _description = 'x_job_card_line_6f75d'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_b6fa8(models.Model):
    _name = 'x_job_card_line_b6fa8'
    _description = 'x_job_card_line_b6fa8'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_ac39e(models.Model):
    _name = 'x_job_card_line_ac39e'
    _description = 'x_job_card_line_ac39e'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_2197c(models.Model):
    _name = 'x_job_card_line_2197c'
    _description = 'x_job_card_line_2197c'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_acbb7(models.Model):
    _name = 'x_job_card_line_acbb7'
    _description = 'x_job_card_line_acbb7'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_ff1a1(models.Model):
    _name = 'x_job_card_line_ff1a1'
    _description = 'x_job_card_line_ff1a1'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_3f246(models.Model):
    _name = 'x_job_card_line_3f246'
    _description = 'x_job_card_line_3f246'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_6242a(models.Model):
    _name = 'x_job_card_line_6242a'
    _description = 'x_job_card_line_6242a'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_05856(models.Model):
    _name = 'x_job_card_line_05856'
    _description = 'x_job_card_line_05856'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_eca9c(models.Model):
    _name = 'x_job_card_line_eca9c'
    _description = 'x_job_card_line_eca9c'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_b47a1(models.Model):
    _name = 'x_job_card_line_b47a1'
    _description = 'x_job_card_line_b47a1'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_8cbfb(models.Model):
    _name = 'x_job_card_line_8cbfb'
    _description = 'x_job_card_line_8cbfb'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_84afb(models.Model):
    _name = 'x_job_card_line_84afb'
    _description = 'x_job_card_line_84afb'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_dea7f(models.Model):
    _name = 'x_job_card_line_dea7f'
    _description = 'x_job_card_line_dea7f'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_be641(models.Model):
    _name = 'x_job_card_line_be641'
    _description = 'x_job_card_line_be641'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_97b59(models.Model):
    _name = 'x_job_card_line_97b59'
    _description = 'x_job_card_line_97b59'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_5bc73(models.Model):
    _name = 'x_job_card_line_5bc73'
    _description = 'x_job_card_line_5bc73'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_7d1c6(models.Model):
    _name = 'x_job_card_line_7d1c6'
    _description = 'x_job_card_line_7d1c6'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_f9f54(models.Model):
    _name = 'x_job_card_line_f9f54'
    _description = 'x_job_card_line_f9f54'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_1c08e(models.Model):
    _name = 'x_job_card_line_1c08e'
    _description = 'x_job_card_line_1c08e'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_d2165(models.Model):
    _name = 'x_job_card_line_d2165'
    _description = 'x_job_card_line_d2165'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_dda93(models.Model):
    _name = 'x_job_card_line_dda93'
    _description = 'x_job_card_line_dda93'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_93c60(models.Model):
    _name = 'x_job_card_line_93c60'
    _description = 'x_job_card_line_93c60'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('duty Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')
    x_studio_duty_details = fields.Char('Duty Details')
    x_studio_duty_serial = fields.Integer('duty Serial')



class x_job_card_line_58478(models.Model):
    _name = 'x_job_card_line_58478'
    _description = 'x_job_card_line_58478'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_d2e65(models.Model):
    _name = 'x_job_card_line_d2e65'
    _description = 'x_job_card_line_d2e65'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_18e33(models.Model):
    _name = 'x_job_card_line_18e33'
    _description = 'x_job_card_line_18e33'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_job_card_line_e0e97(models.Model):
    _name = 'x_job_card_line_e0e97'
    _description = 'x_job_card_line_e0e97'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')

class x_external_parties(models.Model):
    _name = 'x_external_parties'
    _description = 'x_external_parties'
    _rec_name="x_name"
    x_name = fields.Char('Name')

    

class x_job_card_line_66f05(models.Model):
    _name = 'x_job_card_line_66f05'
    _description = 'x_job_card_line_66f05'

    _rec_name="x_name"
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Description',required=True)
    x_job_card_id = fields.Many2one('x_job_card', string='X Job Card')
    x_studio_ext_serial_no = fields.Integer('Ext Serial No')
    x_studio_many2one_field_r2EcZ = fields.Many2one('x_external_parties', string='External Parties')

class x_job_standard(models.Model):
    _name = 'x_job_standard'
    _description = 'x_job_standard'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_job_standard_name(models.Model):
    _name = 'x_job_standard_name'
    _description = 'x_job_standard_name'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_job_group(models.Model):
    _name = 'x_job_group'
    _description = 'x_job_group'
    _rec_name="x_name"

    x_name = fields.Char('Name')    

class x_job_item(models.Model):
    _name = 'x_job_item'
    _description = 'x_job_item'
    _rec_name="x_name"

    x_name = fields.Char('Name')    


class x_job_card_tag(models.Model):
    _name = 'x_job_card_tag'
    _description = 'x_job_card_tag'
    _rec_name="x_name"

    x_color = fields.Integer('Color')
    x_name = fields.Char('Name')    






class x_job_card(models.Model):
    _name = 'x_job_card'
    _description = 'x_job_card'

    x_active = fields.Boolean('Active',default=True)
    x_job_card_line_ids_01dcc = fields.One2many('x_job_card_line_dd787', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_0243b = fields.One2many('x_job_card_line_a46c1', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_02606 = fields.One2many('x_job_card_line_308da', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_040a1 = fields.One2many('x_job_card_line_f76d9', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_05230 = fields.One2many('x_job_card_line_d15d8', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_063e1 = fields.One2many('x_job_card_line_adbfb', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_09a1d = fields.One2many('x_job_card_line_38487', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_0a6c1 = fields.One2many('x_job_card_line_d0b43', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_0a7b5 = fields.One2many('x_job_card_line_48653', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_135c9 = fields.One2many('x_job_card_line_5409b', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_15a4c = fields.One2many('x_job_card_line_6cc70', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_1942f = fields.One2many('x_job_card_line_323d1', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_19a3b = fields.One2many('x_job_card_line_cc73b', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_1c145 = fields.One2many('x_job_card_line_927d5', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_23698 = fields.One2many('x_job_card_line_95d8c', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_24a51 = fields.One2many('x_job_card_line_f03ff', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_2606c = fields.One2many('x_job_card_line_a2d81', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_272d8 = fields.One2many('x_job_card_line_69939', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_28676 = fields.One2many('x_job_card_line_e464d', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_29926 = fields.One2many('x_job_card_line_662eb', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_2dff4 = fields.One2many('x_job_card_line_724fa', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_2fb43 = fields.One2many('x_job_card_line_bc98f', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_31948 = fields.One2many('x_job_card_line_14a4d', 'x_job_card_id', string='Administration tasks list')
    x_job_card_line_ids_33d50 = fields.One2many('x_job_card_line_f6cc0', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_33e78 = fields.One2many('x_job_card_line_3ec95', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_36ef4 = fields.One2many('x_job_card_line_e470d', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_3b891 = fields.One2many('x_job_card_line_48288', 'x_job_card_id', string='Competencies List')
    x_job_card_line_ids_3bc1b = fields.One2many('x_job_card_line_e8478', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_3c75e = fields.One2many('x_job_card_line_cfc27', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_40ebf = fields.One2many('x_job_card_line_b050a', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_4381a = fields.One2many('x_job_card_line_12317', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_4430c = fields.One2many('x_job_card_line_09b57', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_44628 = fields.One2many('x_job_card_line_c6d4f', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_44a49 = fields.One2many('x_job_card_line_c9d70', 'x_job_card_id', string='Experience List')
    x_job_card_line_ids_45772 = fields.One2many('x_job_card_line_4103f', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_4a9ff = fields.One2many('x_job_card_line_72dd4', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_4b2db = fields.One2many('x_job_card_line_4f4a9', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_4ccc3 = fields.One2many('x_job_card_line_c7f1f', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_50092 = fields.One2many('x_job_card_line_9b0f8', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_53d9f = fields.One2many('x_job_card_line_107e8', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_555fe = fields.One2many('x_job_card_line_5a94b', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_5ab64 = fields.One2many('x_job_card_line_eea7d', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_603da = fields.One2many('x_job_card_line_884f2', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_61aba = fields.One2many('x_job_card_line_8636d', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_641cf = fields.One2many('x_job_card_line_c7b42', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_68208 = fields.One2many('x_job_card_line_c5096', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_68208 = fields.One2many('x_job_card_line_c5096', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_71c4a = fields.One2many('x_job_card_line_c7b07', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_71e8b = fields.One2many('x_job_card_line_062b9', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_75301 = fields.One2many('x_job_card_line_63a1f', 'x_job_card_id', string='Supervision Scope')
    x_job_card_line_ids_75cd2 = fields.One2many('x_job_card_line_9b77b', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_75e37 = fields.One2many('x_job_card_line_99be8', 'x_job_card_id', string='Qualification List')
    x_job_card_line_ids_75fd5 = fields.One2many('x_job_card_line_e5982', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_778e0 = fields.One2many('x_job_card_line_3eb3c', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_77d83 = fields.One2many('x_job_card_line_e9940', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_77d83 = fields.One2many('x_job_card_line_e9940', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_7f251 = fields.One2many('x_job_card_line_58956', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_8055c = fields.One2many('x_job_card_line_c13a5', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_8537c = fields.One2many('x_job_card_line_52beb', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_86158 = fields.One2many('x_job_card_line_22666', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_86703 = fields.One2many('x_job_card_line_65542', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_86ccd = fields.One2many('x_job_card_line_378d1', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_8743e = fields.One2many('x_job_card_line_794ca', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_88872 = fields.One2many('x_job_card_line_1b55d', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_893b6 = fields.One2many('x_job_card_line_73c2b', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_89b54 = fields.One2many('x_job_card_line_8bde8', 'x_job_card_id', string='Personal Characteristics')
    x_job_card_line_ids_8c3ed = fields.One2many('x_job_card_line_df67d', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_8ca97 = fields.One2many('x_job_card_line_435e7', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_8ec4e = fields.One2many('x_job_card_line_d8be0', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_933db = fields.One2many('x_job_card_line_53aa5', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_93cf8 = fields.One2many('x_job_card_line_f0297', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_95513 = fields.One2many('x_job_card_line_77c88', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_96698 = fields.One2many('x_job_card_line_7c79e', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_99892 = fields.One2many('x_job_card_line_e7ba1', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_9af16 = fields.One2many('x_job_card_line_c5299', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_9b68f = fields.One2many('x_job_card_line_b0fc7', 'x_job_card_id', string='Internal Relations')
    x_job_card_line_ids_a0465 = fields.One2many('x_job_card_line_6d93b', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_a0b7d = fields.One2many('x_job_card_line_24ae5', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_a2ce8 = fields.One2many('x_job_card_line_329f9', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_a474b = fields.One2many('x_job_card_line_12304', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_a4ee7 = fields.One2many('x_job_card_line_258d2', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_a7ec9 = fields.One2many('x_job_card_line_bfc4e', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_a8158 = fields.One2many('x_job_card_line_23047', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_a8654 = fields.One2many('x_job_card_line_b62bb', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_aa4a2 = fields.One2many('x_job_card_line_7330d', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_adbf5 = fields.One2many('x_job_card_line_d7015', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_ae06c = fields.One2many('x_job_card_line_b9739', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_afab2 = fields.One2many('x_job_card_line_6c420', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_afc78 = fields.One2many('x_job_card_line_6bd06', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_b6989 = fields.One2many('x_job_card_line_d4130', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_b93e9 = fields.One2many('x_job_card_line_f627b', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_c36e3 = fields.One2many('x_job_card_line_f91c6', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_c44d0 = fields.One2many('x_job_card_line_0904e', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_c4cd0 = fields.One2many('x_job_card_line_9b8a5', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_c60d7 = fields.One2many('x_job_card_line_cc0f4', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_c9f84 = fields.One2many('x_job_card_line_df911', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_caaa3 = fields.One2many('x_job_card_line_1f8b1', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_cb3c0 = fields.One2many('x_job_card_line_4ef29', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_cc376 = fields.One2many('x_job_card_line_02175', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_cce8b = fields.One2many('x_job_card_line_e36fc', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_cce8b = fields.One2many('x_job_card_line_e36fc', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_cee47 = fields.One2many('x_job_card_line_a3cde', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_cf329 = fields.One2many('x_job_card_line_6f75d', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_d3d96 = fields.One2many('x_job_card_line_b6fa8', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_d7eac = fields.One2many('x_job_card_line_ac39e', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_d8110 = fields.One2many('x_job_card_line_2197c', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_d9896 = fields.One2many('x_job_card_line_acbb7', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_d9afe = fields.One2many('x_job_card_line_ff1a1', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_da7ae = fields.One2many('x_job_card_line_3f246', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_def19 = fields.One2many('x_job_card_line_6242a', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_def19 = fields.One2many('x_job_card_line_6242a', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_df363 = fields.One2many('x_job_card_line_05856', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_e1514 = fields.One2many('x_job_card_line_eca9c', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_e34c8 = fields.One2many('x_job_card_line_b47a1', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_e6b95 = fields.One2many('x_job_card_line_8cbfb', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_e6e78 = fields.One2many('x_job_card_line_84afb', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_e7ee9 = fields.One2many('x_job_card_line_dea7f', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_ed276 = fields.One2many('x_job_card_line_be641', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_ed99c = fields.One2many('x_job_card_line_97b59', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_f0e52 = fields.One2many('x_job_card_line_5bc73', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_f0fb4 = fields.One2many('x_job_card_line_7d1c6', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_f1d67 = fields.One2many('x_job_card_line_f9f54', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_f2503 = fields.One2many('x_job_card_line_1c08e', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_f3ff3 = fields.One2many('x_job_card_line_d2165', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_f5206 = fields.One2many('x_job_card_line_dda93', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_f7b68 = fields.One2many('x_job_card_line_93c60', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_f7c97 = fields.One2many('x_job_card_line_58478', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_f8e0f = fields.One2many('x_job_card_line_d2e65', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_fbd3f = fields.One2many('x_job_card_line_18e33', 'x_job_card_id', string='New Lines')
    x_job_card_line_ids_fdd9f = fields.One2many('x_job_card_line_e0e97', 'x_job_card_id', string='New Lines')
    x_name = fields.Char('Name')
    x_job_card_line_ids_eb8a1 = fields.One2many('x_job_card_line_66f05', 'x_job_card_id', string='External Relations')
    x_studio_direct_manager = fields.Many2one('hr.employee', string='Direct Manager')
    x_studio_general_description = fields.Text('General Description')
    x_studio_job_code = fields.Char('Job Code')

    x_studio_many2one_field_1pLBP = fields.Many2one('hr.work.location', string='Work Location')
    x_studio_many2one_field_3DNrS = fields.Many2one('x_job_standard', string='Job standard ')
    x_studio_many2one_field_8vRQo = fields.Many2one('x_job_standard_name', string='Job standard Name')
    x_studio_many2one_field_CuFqA = fields.Many2one('x_job_group', string='Job Group')
    x_studio_many2one_field_NCUEQ = fields.Many2one('hr.job', string='Job Position')
    x_studio_many2one_field_tqZgy = fields.Many2one('x_job_grade', string='Job Grade')
    x_studio_many2one_field_WenRb = fields.Many2one('x_job_item', string='Job Item')
    x_studio_sequence = fields.Integer('Sequence')
    x_studio_tag_ids = fields.Many2many('x_job_card_tag','x_job_card_tag_rel','x_job_card_id','x_tag_id', string='Tags')
    x_studio_work_location = fields.Many2one('hr.department', string='work location')

