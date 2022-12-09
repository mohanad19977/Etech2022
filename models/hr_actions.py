
from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re



class DisciplinaryActionscustom(models.Model):
    _name = 'x_disciplinaryeffect'
    _rec_name='x_name'	

    IsGrade  = fields.Boolean('Is Grade') 
     

class DisciplinaryActionscustom(models.Model):
    _name = 'x_disciplinaryactionty'
    _rec_name='x_name'	

    PreviesAction = fields.Many2one('x_disciplinaryactionty', string='Previous Action') 




    
    

    

class x_scholarshipcustom(models.Model):
    _name = 'x_scholarship'
    
	
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


class x_committees_line_1678dtcustom(models.Model):
    _name = 'x_committees_line_1678d'
    
    x_studio_judge =fields.Many2one('hr.employee', string='Judge' ,domain="[('x_studio_employee_status','=','على رأس عمله')]")

