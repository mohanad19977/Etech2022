from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re


class x_misison_extension_re (models.Model):
    _name = 'x_misison_extension_re'
    _description = 'x_misison_extension_re'
    _rec_name="x_name"

    x_name = fields.Char('Name')
    

class x_x_hr_external_messio_line_13deb(models.Model):
    _name = 'x_x_hr_external_messio_line_13deb'
    _description = 'x_x_hr_external_messio_line_13deb'
    _rec_name="x_name"

    x_name = fields.Char('Name',required=True)
    x_studio_sequence = fields.Integer('Sequence')
    x_x_hr_external_messio_id = fields.Many2one('x_x_hr_external_messio', string='Hr External Messio')    

class x_x_hr_external_messio(models.Model):
    _name = 'x_x_hr_external_messio'
    _description = 'x_x_hr_external_messio'
    _rec_name="x_name"

    x_name = fields.Char('Name')
    x_studio_organization = fields.Char('Organization')
    x_studio_sequence = fields.Integer('Sequence')
    x_studio_many2one_field_oWRm1 = fields.Many2one('res.country', string='Country')
    x_x_hr_external_messio_line_ids_cb35d = fields.One2many('x_x_hr_external_messio_line_13deb', 'x_x_hr_external_messio_id', string='New Lines')

class x_mission_extension (models.Model):
    _name = 'x_mission_extension'
    _rec_name="x_name"

    x_studio_extension_date = fields.Date('Extension Date')
    x_studio_new_end_date = fields.Date('New End Date')
    x_studio_many2one_field_RzC3N = fields.Many2one('x_misison_extension_re', string='x_studio_many2one_field_RzC3N')
    x_studio_extension_letter_no = fields.Char(' Extension Letter No',required=True)
    x_studio_extension_letter_date = fields.Date(' Extension Letter Date',required=True)
    x_studio_many2one_field_OeHVB = fields.Many2one('x_x_hr_external_messio', string='x.hr.external_messions')
    x_studio_sequence = fields.Integer('Sequance')
    x_active = fields.Boolean('Active',default=True)
    x_name = fields.Char('Name')

class x_externalmissionextension(models.Model):
    _name = 'x_externalmissionextension'
    _description = 'x_externalmissionextension'

    x_ExtensionDate = fields.Date('Extension Date',required=True)
    x_ExtensionEndDate = fields.Date('Extension End Date',required=True)
    x_ExtensionLetterDate = fields.Date('Extension Letter Date',required=True)
    x_ExtensionLetterNo = fields.Text('Extension Letter No',required=True)
    x_ExtensionNotes = fields.Text('Extension Notes')
    



class x_employeecustom(models.Model):
    _name = 'x_employee_actions'

    #x_studio_many2one_field_z9f19 = fields.Many2one('hr.employee', string='Judge' ,domain="[('x_studio_employee_status','=','على رأس عمله')]")


    x_studio_judge_name = fields.Many2one('hr.employee', string='Judge' ,domain="[('x_studio_employee_status','=','على رأس عمله')]",readonly="[('id','>','0')]",required=True)
    x_studio_start_date = fields.Date('تاريخ بدء الاعارة')
    duration = fields.Integer(compute='_compute_dateend', string='المدة (أيام )',readonly=True) #check
    Fullduration = fields.Char(compute='_compute_duration', string='المدة ( سنوات )',readonly=True)
    Fulldurationfloat = fields.Float(string='المدة)')  #check
    x_studio_letter_ref_no = fields.Char('Ref No',required=True)
    x_studio_many2one_field_XrM3J = fields.Many2one('x_birth_country', string='الدولة')
    x_studio_job_title  = fields.Many2one('hr.job', string='مسمى وظيفي',required=True)
    x_studio_related_field_F5BJc = fields.Char('موقع العمل قبل الاعارة',readonly=True) # check (Dependencies = x_studio_judge_name)
    x_studio_work_center_before = fields.Char('Work Center Before',related='x_studio_judge_name.department_id.name',readonly=True)
    x_studio_last_work_location = fields.Char(string='Last Work location',readonly=True)
    x_studio_reference_institution = fields.Char('المرجع المختص بالإعارة',required=True)
    x_studio_end_date_1 = fields.Date('تاريخ انتهاء الاعارة')
    x_studio_accumulative_periods = fields.Char('مدة الاعارة التراكمية')
    x_studio_letter_date = fields.Date('تاريخ صدور كتاب الإعارة')
    
    x_studio_organization = fields.Many2one('x_x_hr_external_messio', string='الجهة الطالبة للإعارة')
    x_studio_related_field_XRjMY = fields.Char('الوظيفة السابقة',readonly=True)

    x_studio_many2one_field_rGN1T = fields.Many2one('hr.work.location', string='مركز العمل بعد انتهاء الاعارة')

    x_studio_many2many_field_cKx7X = fields.Many2many('x_mission_extension', string='Mission extension')


    #for seconed part in the end
    x_studio_termination_letter_no = fields.Char('X Studio Termination Letter No')
    x_studio_termination_date = fields.Date('X Studio Termination Date')
    x_studio_many2one_field_J5hWI = fields.Many2one('x_termination_reason', string='X Studio Many2One Field J5Hwi')
    x_studio_termination_by_jc_ = fields.Boolean('Termination By JC?')
    
    x_studio_country = fields.Many2one('res.country', string='Country')
    x_studio_work_location_before_mission = fields.Many2one('hr.work.location', string='Work location before mission')
    x_studio_many2one_field_7dK3W = fields.Many2one('x_externalmissionextension', string='externalmissionextension')
    x_studio_many2one_field_7e3Pe = fields.Many2one('x_mission_extension', string='Mission extension')
    x_studio_text_field_uFAFS = fields.Text('New Multiline Text')
    x_studio_many2one_field_Ouftk = fields.Many2one('x_mission_extension', string='Mission extension')
    x_studio_many2one_field_JAfBr = fields.Many2one('x_mission_extension', string='Mission extension')
    x_studio_many2one_field_JAfBr = fields.Many2one('x_mission_extension', string='Mission extension')
    x_studio_many2one_field_WZ8yA = fields.Many2one('x_externalmissionextension', string='externalmissionextension')
    x_studio_termination_reason = fields.Char('Termination Reason')
    x_studio_char_field_kzUUk = fields.Char(compute='_compute_field_kzUUk',string='Mission Duration',readonly=True)

    x_active = fields.Boolean('Active',default=True)
    x_name = fields.Char('Name')
    x_studio_sequence = fields.Integer('Sequance')

    x_change = fields.Text('x_change')
    

    x_studio_selection_field_5CEax = fields.Selection([
        ('initiated','تم تقديم الطلب'),
        ('inprocess','بانتظار الموافقة'),
        ('approved','تمت الموافقة'),
        ('rejected','مرفوض'),
    ], string='Pipeline status bar')

    

    @api.depends('x_studio_judge_name')
    def _compute_x_studio_last_work_location(self):
        for record in self:  
            if record.x_studio_judge_name:
                if not record.x_change:
                    record["x_studio_last_work_location"]=record.x_studio_judge_name.work_location_id.display_name
                    record["x_change"]="done"

   
               
    # PreviesPso = fields.Many2one('hr.employee', string='Judge' ,domain="['active','=',true]")
    @api.depends('x_studio_end_date_1','x_studio_start_date')
    def _compute_dateend(self):
        try:
           for record in self:   
            if record.x_studio_end_date_1 and record.x_studio_start_date:
               record.duration = (record.x_studio_end_date_1 - record.x_studio_start_date).days
            else: 
             record.duration= 0
        except ValueError:
             record.duration= 0
    
    @api.constrains('x_studio_end_date_1','x_studio_start_date')
    def _constrainsdate(self):
        for record in self: 
          if record.x_studio_end_date_1 and record.x_studio_start_date:    
            if record.x_studio_end_date_1 < record.x_studio_start_date:
                  raise ValidationError("End Date Must Grater Than Start Date")
            enddatebewteen=self.env["x_employee_actions"].search_count(["&",("x_studio_judge_name.id", "=", self.x_studio_judge_name.id) , ("x_studio_end_date_1" ,">" , record.x_studio_start_date) ])     
            # ("x_studio_end_date_1" ,">" , record.x_studio_end_date_1) startdatebewteen=self.env["x_employee_actions"].search_count(["&",("x_studio_judge_name.id", "=", self.x_studio_judge_name.id) ,("x_studio_start_date" ,"<" , record.x_studio_end_date_1), ("x_studio_start_date" ,">" , record.x_studio_start_date) ])     
            if enddatebewteen != 1:     
                    raise ValidationError("Judge have another Extenal Mission in same Date")      

   
    # @api.onchange('Fullduration')
    # def _constrains_Fullduration(self):
    #       for record in self:
    #         if record.Fullduration:
    #            dates=int(sum(self.env["x_employee_actions"].search([("x_studio_judge_name.id", "=", self.x_studio_judge_name.id)]).mapped('duration')))/365
    #            year=int(dates)
              
    
    
    @api.depends('duration','x_studio_judge_name')
    def _compute_duration(self):
        try:
            for record in self:
               dates=int(sum(self.env["x_employee_actions"].search([("x_studio_judge_name.id", "=", self.x_studio_judge_name.id)]).mapped('duration')))/365
               year=int(dates)
               days=dates-int(dates)
               record.Fullduration=" " + str(year) + " Year and "+ str(int(days*365)) +" Days" 
            #    if int(year+(record.duration/365)) >= 5 :
            #       raise ValidationError("مدة الاعارة يجب الا تتجاوز ال 5 السنوات")
        except ValueError:
             record.Fullduration= "0"

    @api.depends('x_studio_end_date_1')
    def _compute_field_kzUUk(self):
        for record in self:
            record['x_studio_char_field_kzUUk'] = record.x_studio_end_date_1 - record.x_studio_start_date
   

  
    @api.onchange('x_studio_end_date_1','x_studio_start_date')
    def _compute_Fulldurationfloat(self):
        for record in self:
             if record.duration:
                 dates=int(sum(self.env["x_employee_actions"].search([("x_studio_judge_name.id", "=", self.x_studio_judge_name.id)]).mapped('duration')))/365
                 record.Fulldurationfloat=dates


    @api.constrains('Fulldurationfloat')
    def _constrains_Fulldurationfloat(self):
        for record in self:
            if record.Fulldurationfloat and record.Fulldurationfloat+(record.duration/365) >= 5:
               raise ValidationError("مدة الاعارة يجب الا تتجاوز ال 5 السنوات")
    # @api.depends('duration','x_studio_judge_name')
    # def _compute_duration(self):
    #     try:
    #         for record in self:   
    #            record.Fullduration=str(sum(self.env["x_employee_actions"].search([("x_studio_judge_name.id", "=", self.x_studio_judge_name.id)]).mapped('duration')))              
    #     except ValueError:
    #          record.Fullduration= "0"
    