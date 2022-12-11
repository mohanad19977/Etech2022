from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re

class x_hr_employee_line_8990a(models.Model):
    _name = 'x_hr_employee_line_8990a'
    _description = 'x_hr_employee_line_8990a'
    _rec_name="x_name"
    
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Name',required=True)
    x_hr_employee_id = fields.Many2one('hr.employee', string='X Hr Employee')


class x_hr_employee_line_3bc13(models.Model):
    _name = 'x_hr_employee_line_3bc13'
    _description = 'x_hr_employee_line_3bc13'
    _rec_name="x_name"
    
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Name',required=True)
    x_hr_employee_id = fields.Many2one('hr.employee', string='X Hr Employee')

class x_hr_employee_line_c2aed(models.Model):
    _name = 'x_hr_employee_line_c2aed'
    _description = 'x_hr_employee_line_c2aed'
    _rec_name="x_name"
    
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Name',required=True)
    x_hr_employee_id = fields.Many2one('hr.employee', string='X Hr Employee')

class x_hr_employee_line_f0daa(models.Model):
    _name = 'x_hr_employee_line_f0daa'
    _description = 'x_hr_employee_line_f0daa'
    _rec_name="x_name"
    
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Name',required=True)
    x_hr_employee_id = fields.Many2one('hr.employee', string='X Hr Employee')

class x_hr_employee_line_40ceb(models.Model):
    _name = 'x_hr_employee_line_40ceb'
    _description = 'x_hr_employee_line_40ceb'
    _rec_name="x_name"
    
    x_studio_sequence = fields.Integer('Sequence')
    x_name = fields.Char('Name',required=True)
    x_hr_employee_id = fields.Many2one('hr.employee', string='X Hr Employee')

class x_birth_country(models.Model):
    _name = 'x_birth_country'
    _description = 'x_birth_country'
    _rec_name="x_name"
    
    x_name = fields.Char('Name',required=True)

class x_job_grade(models.Model):
    _name = 'x_job_grade'
    _description = 'x_job_grade'
    _rec_name="x_name"
    
    x_name = fields.Char('Grade')
    x_active = fields.Boolean('Active',default=True)
    x_studio_description = fields.Char('Description')
    x_studio_grade = fields.Char('Grade')
    x_studio_level = fields.Char('Level')
    x_studio_sequence = fields.Integer('Sequence')

class x_competitiveness_line_27484(models.Model):
    _name = 'x_competitiveness_line_27484'
    _description = 'x_competitiveness_line_27484'
    _rec_name="x_name"
    
    x_name = fields.Char('Name',required=True)
    x_competitiveness_id = fields.Many2one('x_competitiveness', string='Competitiveness')
    x_studio_sequence = fields.Integer('Sequence')

class x_competitiveness_line_828bd(models.Model):
    _name = 'x_competitiveness_line_828bd'
    _description = 'x_competitiveness_line_828bd'
    _rec_name="x_name"
    
    x_name = fields.Char('Description',required=True)
    x_competitiveness_id = fields.Many2one('x_competitiveness', string='Competitiveness')
    x_studio_id = fields.Char('ID')
    x_studio_many2one_field_emvoa = fields.Many2one('hr.employee', string='Employee')

    x_studio_priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High'),
    ], string='Skillset Level')



    x_studio_sequence = fields.Integer('Sequence')


class x_competitiveness_line_1a44d(models.Model):
    _name = 'x_competitiveness_line_1a44d'
    _description = 'x_competitiveness_line_1a44d'
    _rec_name="x_name"
    
    x_competitiveness_id = fields.Many2one('x_competitiveness', string='Competitiveness')
    x_name = fields.Char('Description',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_studio_many2one_field_k6RS6 = fields.Many2one('hr.employee', string='Employee')


class x_competitiveness(models.Model):
    _name = 'x_competitiveness'
    _description = 'x_competitiveness'
    _rec_name="x_name"
    
    x_name = fields.Char('Specialty',required=True)
    x_active = fields.Boolean('Active',default=True)
    x_competitiveness_line_ids_1f29c = fields.One2many('x_competitiveness_line_27484', 'x_competitiveness_id', string='New Lines')
    x_competitiveness_line_ids_2e4e2 = fields.One2many('x_competitiveness_line_828bd', 'x_competitiveness_id', string='New Lines')
    x_competitiveness_line_ids_4db5a = fields.One2many('x_competitiveness_line_1a44d', 'x_competitiveness_id', string='New Lines')
    x_studio_class_code = fields.Char('CLASS_CODE')
    x_studio_code = fields.Integer('code')
    x_studio_description = fields.Char('Description')
    x_studio_employee = fields.One2many('hr.employee', 'x_studio_many2one_field_7p7Qz', string='Employee')
    x_studio_id = fields.Char('ID')
    x_studio_is_active_1 = fields.Selection([
        ('مفعل', 'مفعل'),
        ('غير مفعل', 'غير مفعل'),
    ], string='is active')

    x_studio_many2many_field_1JZGO = fields.Many2many('hr.employee','x_hr_employee_x_competitiveness_rel','x_competitiveness_id','hr_employee_id', string='Employee')
    x_studio_many2one_field_B0KEP = fields.Many2one('hr.employee', string='Employee')
    x_studio_many2one_field_C6DTI = fields.Many2one('hr.employee', string='Employee')
    x_studio_many2one_field_iryvz = fields.Many2one('hr.employee', string='Employee')
    x_studio_parent = fields.Many2one('x_competitiveness', string='Parent')
    x_studio_sequence = fields.Integer('Sequance')

class x_x_hr_employee_depend_line_6466e(models.Model):
    _name = 'x_x_hr_employee_depend_line_6466e'
    _description = 'x_x_hr_employee_depend_line_6466e'
    _rec_name="x_name"
    
    x_name = fields.Char('Description',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_x_hr_employee_depend_id = fields.Many2one('x_x_hr_employee_depend', string='X X Hr Employee Depend')

class x_x_hr_employee_depend(models.Model): #from mahmoud code
    _name = 'x_x_hr_employee_depend'
    _description = 'x_x_hr_employee_depend'
    _rec_name="x_name"

    x_active = fields.Boolean('Active',default=True)
    x_name = fields.Char('benefecairy Name')
    x_studio_address = fields.Char('Address')
    x_studio_attachment = fields.Binary('Attachment')
    x_studio_attachment_filename = fields.Char('Filename for x_studio_binary_field_dr6ml')
    x_studio_birth_place = fields.Char('BIRTH Place')
    x_studio_contdt = fields.Date('CONTDT')
    x_studio_contno = fields.Char('CONTNO')
    x_studio_date = fields.Date('Date')
    x_studio_edit_attachment = fields.Boolean('Edit Attachment')
    x_studio_email = fields.Char('Email') #CheckSelection
    x_studio_gender = fields.Selection([
        ('ذكر', 'Male'),
        ('أنثى', 'Female'),
    ], string='Gender')

    x_studio_many2one_field_BHtKm = fields.Many2one('res.lang', string='Languages')
    x_studio_many2one_field_F9toM = fields.Many2one('res.partner', string='Contact')
    x_studio_many2one_field_pIoXl = fields.Many2one('hr.employee', string=' Dep Employee')
    x_studio_many2one_field_PvJxd = fields.Many2one('hr.employee', string='Employee')
    x_studio_mobile = fields.Char('Mobile')
    x_studio_name_1 = fields.Char('Name')
    x_studio_nationalid = fields.Char('NationalID')
    x_studio_nationality_1 = fields.Many2one('res.country', string='Nationality')
    x_studio_phone = fields.Char('Phone')

    x_studio_relation = fields.Selection([
        ('Spouse', 'Spouse'),
        ('Child', 'Child'),
    ], string='Relation')

    x_studio_selection_field_reAR9 = fields.Selection([
        ('NS','not submitted'),
        ( 'S','Submitted'),
        ('APV','Approved'),
        ('Rejected','Rejected'),
    ], string='Pipeline status bar')

    x_studio_sequence = fields.Integer('Sequence')

    x_studio_status = fields.Selection([
        ('1', '1'),
        ('2', '2'),
    ], string='STATUS')

    x_studio_stop_date = fields.Date('STOP_DATE')

    x_studio_tags = fields.Many2many('res.partner.category','x_res_partner_category_x_x_hr_employee_depend_rel','x_x_hr_employee_depend_id','res_partner_category_id', string='Tags')

    x_studio_wifwork = fields.Selection([
        ('1', '1'),
        ('2', '2'),
    ], string='WIFWORK')

    x_x_hr_employee_depend_line_ids_46e6a = fields.One2many('x_x_hr_employee_depend_line_6466e', 'x_x_hr_employee_depend_id', string='New Lines')



    #oooooo

    @api.onchange('x_studio_date')
    @api.constrains('x_studio_date')
    def _constrains_x_studio_date(self):
         for record in self:
           if record.x_studio_date:
               fmt = '%Y-%m-%d'
               start_date = record.x_studio_date 
               end_date = date.today()
               if start_date > end_date:
                 raise ValidationError("Enter Vaild Date")  

    @api.onchange('x_studio_phone','x_studio_email','x_studio_mobile')
    @api.constrains('x_studio_phone','x_studio_email','x_studio_mobile')
    def _check_name(self):
        for record in self:
           if record.x_studio_mobile:     
                if re.match('^\d{10}$', record.x_studio_mobile) == None:     
                    raise ValidationError("Enter valid 10 digits Mobile number")
           if record.x_studio_phone:     
                if re.match('^\d{9}$', record.x_studio_phone) == None:     
                    raise ValidationError("Enter valid phone number")         
           if record.x_studio_email:     
                if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', record.x_studio_email) == None:     
                    raise ValidationError("Enter valid email")  


class x_religion(models.Model):
    _name = 'x_religion'
    _description = 'x_religion'
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_employment_type(models.Model):
    _name = 'x_employment_type'
    _description = 'x_employment_type'
    
    _rec_name="x_name"

    x_name = fields.Char('Name')

class x_work_center(models.Model):
    _name = 'x_work_center'
    _description = 'x_work_center'

    _rec_name="x_name"

    x_name = fields.Char('Name')
    x_active = fields.Boolean('Active',default=True)
    x_studio_sequence = fields.Integer('Sequence')
    
  
class x_Customresumline(models.Model):
    _inherit="hr.resume.line"  
    
    x_studio_edit_attachment = fields.Boolean('Edit Attachment')
    x_studio_attachment = fields.Binary('Attachment', readonly="['&',('id','>','0'),('x_studio_edit_attachment','=','false']")
    x_studio_job_title = fields.Char('Job Title')
    x_studio_job_type = fields.Selection([
        ('1', 'عام'),
         ('2', 'خاص')
    ], string='Job Type')
    x_studio_exp_type = fields.Selection([
        ('1', '1'),
         ('2', '2'),
          ('3', '3'),
           ('4', '4')
    ], string='Exp Type')
    x_studio_employer = fields.Text('Employer')
    x_studio_duration = fields.Float('Duration',readonly=True)
    x_studio_resignation_reason = fields.Char('Resignation Reason')
    x_studio_many2one_field_7U76H = fields.Many2one('x_experience_country', string='Experience country')
    x_studio_many2one_field_DsV8W = fields.Many2one('x_course_location', string='Course Location')
    x_studio_many2one_field_HJbxW = fields.Many2one('hr.skill.type', string='Skill Type')
    x_studio_many2one_field_NrNns = fields.Many2one('hr.skill.level', string='Skill Level')
    x_studio_many2one_field_ZCcgZ = fields.Many2one('x_course_subject', string='Course subject')
    x_studio_qualification = fields.Char('Qualification')
    x_studio_qualification_track = fields.Selection([
        ('أطروحة', 'أطروحة'),
        ('امتحان', 'امتحان')
    ], string='Qualification track')
    x_studio_many2one_field_1oArJ = fields.Many2one('x_qualifications_provi', string='Qualifications Provider')

    x_studio_grade = fields.Selection([
        ('1', 'Low'),
        ('2', 'مقبول'),
        ('3', 'جيد'),
        ('4', 'جيد جدا'),
        ('5', 'متوسط'),
        ('8', 'مستحسن'),
        ('7', 'حسن')
       
    ], string='Grade')
    x_studio_accreditation = fields.Boolean('Accreditation')
    x_studio_qualified_from = fields.Date('Qualified from')
    x_studio_thesis = fields.Char('Thesis')
    x_studio_type_desc = fields.Char('TYPE_DESC')
    x_studio_course_name = fields.Char('Course Name')
    x_studio_description = fields.Text('Description')

    x_studio_skill = fields.Char('Skill')
    x_studio_syb = fields.Selection([
        ('داخل الأردن', 'داخل الأردن'),
         ('خارج الأردن', 'خارج الأردن')
    ], string='SYB')

    x_studio_thesis = fields.Char('Thesis')
    x_studio_type_desc = fields.Char('TYPE_DESC')
    x_studio_average = fields.Float('Average')

    x_studio_country = fields.Many2one('x_birth_country', string='Country')
    x_studio_description = fields.Text('Description')
    x_studio_description_1 = fields.Html('Description')
    x_studio_major = fields.Char('Major')
    x_studio_course_length = fields.Integer('COURSE_LENGTH')
    x_studio_hours = fields.Integer('HOURS')
    x_studio_no = fields.Integer('No')
    x_studio_place = fields.Char('Place')
    x_studio_attendance_status = fields.Char('ATTENDANCE_STATUS')
    x_studio_absent_type = fields.Char('ABSENT_TYPE')
    x_studio_absent_reason = fields.Char('ABSENT_Reason')



class birth_countrytechnical(models.Model):
    _name = 'x_birth_country'
    _description = 'x_birth_country'
    _rec_name='x_name'
     
    x_name = fields.Char('name')
class experiencetechnical(models.Model):
    _name = 'x_experience_country'
    _description = 'x_experience_country'
    _rec_name='x_name'
     
    x_name = fields.Char('name')
    
class subjecttechnical(models.Model):
    _name = 'x_course_subject'
    _description = 'x_course_subject'
    _rec_name='x_name'
     
    x_name = fields.Char('name')    

class coursetechnical(models.Model):
    _name = 'x_course_location'
    _description = 'x_course_location'
    _rec_name='x_name'
     
    x_name = fields.Char('name')

class qualificationstechnical(models.Model):
    _name = 'x_qualifications_provi'
    _description = 'x_qualifications_provi'
    _rec_name='x_name'
     
    x_name = fields.Char('name')
    
class x_CustomEmployee(models.Model):
    _inherit="hr.employee"

    x_accummulated_missions = fields.Integer('Accummulated Missions')
    x_accummulated_secondment = fields.Integer('Accummulated Secondment')
    x_hr_employee_line_ids_52a30  = fields.One2many('x_hr_employee_line_8990a', 'x_hr_employee_id', string='New Lines')
    x_hr_employee_line_ids_57fcd = fields.One2many('x_hr_employee_line_3bc13', 'x_hr_employee_id', string='New Lines')
    x_hr_employee_line_ids_77c74 = fields.One2many('x_hr_employee_line_c2aed', 'x_hr_employee_id', string='New Lines')
    x_hr_employee_line_ids_91f52 = fields.One2many('x_hr_employee_line_f0daa', 'x_hr_employee_id', string='New Lines')
    x_hr_employee_line_ids_f5700 = fields.One2many('x_hr_employee_line_40ceb', 'x_hr_employee_id', string='New Lines')
    x_studio_ = fields.Selection([
        ('العربية', 'العربية'),
        ('English', 'English')
    ], string='لغة الام')

    x_studio_birth_country_custom = fields.Many2one('x_birth_country', string='birth country')
    x_studio_boolean_field_qQ6bT = fields.Boolean('New Checkbox')
    x_studio_category = fields.Selection([
        ('مصنف', 'مصنف'),
        ('غير مصنف', 'غير مصنف'),
    ], string='Employment Category')

    x_studio_char_field_Sowp2 = fields.Char('New النص')
    x_studio_char_field_T6xkO = fields.Char('New النص')
    x_studio_date = fields.Date('Date')
    x_studio_decision_file = fields.Binary('Decision attachment')
    x_studio_decision_file_filename = fields.Char('Filename for x_studio_binary_field_M9csF')
    x_studio_decision_number = fields.Char('Decision Number')
    x_studio_department_location = fields.Char('Department Location',readonly=True)
    x_studio_effective_date = fields.Date('Effective Date')
    x_studio_employee_id = fields.Char('Employee')
    x_studio_employee_status = fields.Selection([
        ('على رأس عمله', 'على رأس عمله'),
        ('معار', 'معار'),
        ('متقاعد', 'متقاعد'),
        ('فاقد', 'فاقد'),
        ('متوفى', 'متوفى'),
        ('انهاء خدمة', 'انهاء خدمة'),
        ('مستقيل', 'مستقيل'),
        ('مبعوث', 'مبعوث'),
        ('محال على الاستيداع', 'محال على الاستيداع'),
        ('منقول من الوزارة', 'منقول من الوزارة'),
        ('عزل من الخدمة', 'عزل من الخدمة'),
        ('استنكاف', 'استنكاف'),
        ('استغناء عن الخدمة', 'استغناء عن الخدمة'),
    ], string='Employee Status')

    x_studio_employment_type = fields.Selection([
        ('دوام كامل', 'دوام كامل'),
        ('دوام جزئي', 'دوام جزئي'),
        ('استشاري', 'استشاري'),
    ], string='Employment Type')

    x_studio_first_name = fields.Char('First Name')
    x_studio_first_name_en = fields.Char('first name EN')
    x_studio_first_name_en_1 = fields.Char('first Name En')

    # #page2 

    x_studio_float_field_g1V8r	 = fields.Float('New Decimal')
    x_studio_fourth_name_en = fields.Char('Fourth Name En')
    x_studio_full_name = fields.Char(compute="_compute_x_studio_full_name",string='English Full Name',readonly=True)
    x_studio_full_name_ar = fields.Char(compute="_compute_x_studio_full_name_ar",string='Full Name Ar',readonly=True)
    x_studio_Garde = fields.Char('Grade')
    x_studio_iban = fields.Char('IBAN')
    x_studio_job_position_1 = fields.Char('Job Position',readonly=True)
    x_studio_joining_date = fields.Date('Joining Date')
    x_studio_judge_code = fields.Char('Judge Code')
    x_studio_last_name = fields.Char('Last Name')


    x_studio_many2many_field_Ak76e = fields.Many2many('x_competitiveness','x_hr_employee_x_competitiveness_rel_1','hr_employee_id','x_competitiveness_id', string='Competitiveness')
    x_studio_many2many_field_s6W7s = fields.Many2many('x_competitiveness','x_hr_employee_x_competitiveness_rel','hr_employee_id','x_competitiveness_id', string='field_name')
    x_studio_many2many_field_YyM4J = fields.Many2many('x_x_hr_employee_depend','x_hr_employee_x_x_hr_employee_depend_rel','hr_employee_id','x_x_hr_employee_depend_id', string='x.hr.employee_dependent')



    x_studio_many2one_field_1thIi = fields.Many2one('hr.payroll.structure', string='Salary Structure')
    x_studio_many2one_field_4aoaB = fields.Many2one('x_job_grade', string='Job Grade')
    x_studio_many2one_field_4lxEZ = fields.Many2one('account.analytic.account', string='Analytic Account')
    x_studio_many2one_field_7p7Qz = fields.Many2one('x_competitiveness', string='Competitiveness')
    x_studio_many2one_field_EGTtU = fields.Many2one('hr.contract', string='Employee Contract')
    x_studio_many2one_field_hI2xy = fields.Many2one('x_x_hr_employee_depend', string='x.hr.employee_dependent') #continue work here
    x_studio_many2one_field_iWbvK = fields.Many2one('x_x_hr_employee_depend', string='x.hr.employee_dependent')
    x_studio_many2one_field_IxOfq = fields.Many2one('hr.job', string='Job Position')
    x_studio_many2one_field_Jdzux = fields.Many2one('x_religion', string='Religion')
    x_studio_many2one_field_LPO0Y = fields.Many2one('x_x_hr_employee_depend_line_6466e', string='X Hr Employee Depend  Lines')
    x_studio_many2one_field_OHxlc = fields.Many2one('x_job_grade', string='X Studio Many2One Field Ohxlc')    
    x_studio_many2one_field_qU4Lc = fields.Many2one('account.account', string='Account')
    x_studio_many2one_field_X2xk3 = fields.Many2one('x_grade', string='grade') #x_grade model in termination file
    x_studio_many2one_field_Z0Im7 = fields.Many2one('x_employment_type', string='employment type')
    x_studio_many2one_field_ZpjQr = fields.Many2one('res.bank', string='Bank')
    x_studio_mother_en_name = fields.Char('اسم الام - لغة النجليزية')
    x_studio_mother_name = fields.Char('Mother Name')
    x_studio_mother_name_ar = fields.Char('Mother Name Ar')
    x_studio_one2many_field_aEyHc = fields.One2many('x_x_hr_employee_depend', 'x_studio_many2one_field_pIoXl', string='New One2many')
    x_studio_po_box = fields.Char('Po Box')
    x_studio_second_name = fields.Char('Second Name')
    x_studio_second_name_en = fields.Char('second name EN')
    x_studio_second_name_en_1 = fields.Char('Second Name En')
    x_studio_second_nationality = fields.Many2one('res.country', string='Second Nationality')

    x_studio_selection_field_9qzTm = fields.Selection([
        ('Option 1', 'Option 1'),
        ('Option 2', 'Option 2'),
    ], string='New Selection')

    x_studio_selection_field_lPruz = fields.Selection([
        ('متوفى', 'متوفى'),
        ('على قيد الحياة', 'على قيد الحياة'),
    ], string='Life Status')

    x_studio_selection_field_qnDeX = fields.Selection([
        ('العربية', 'العربية'),
        ('English', 'English'),
    ], string='اللغة الأم')

    x_studio_solidarity_fund = fields.Boolean('Solidarity Fund')
    x_studio_specialities = fields.One2many('x_competitiveness', 'x_studio_many2one_field_B0KEP', string='Specialities')
    x_studio_status_date = fields.Date('Status Date')
    x_studio_system_id = fields.Char('System')
    x_studio_third_name = fields.Char('Third Name')
    x_studio_third_name_en = fields.Char('Third Name En')
    x_studio_title = fields.Many2one('res.partner.title', string='Title')
    x_studio_work_center = fields.Many2one('x_work_center', string='Work center')
    x_studio_work_mobile_2 = fields.Char('Work Mobile 2')



    @api.depends('x_studio_first_name_en','x_studio_second_name_en','x_studio_third_name_en','x_studio_fourth_name_en')
    def _compute_x_studio_full_name(self):
        for record in self:
            record['x_studio_full_name'] = str(record.x_studio_first_name_en) + ' ' + str(record.x_studio_second_name_en) + ' ' + str(record.x_studio_third_name_en) + ' ' + str(record.x_studio_fourth_name_en)

    @api.depends('x_studio_first_name','x_studio_second_name','x_studio_third_name','x_studio_last_name')
    def _compute_x_studio_full_name_ar(self):
        for record in self:
            record['x_studio_full_name_ar'] = str(record.x_studio_first_name) + ' ' + str(record.x_studio_second_name) + ' ' + str(record.x_studio_third_name) + ' ' + str(record.x_studio_last_name)












