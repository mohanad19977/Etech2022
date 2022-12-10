
from urllib import request
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta
import re





class attachmentList(models.Model):
    _name = 'salary.attachmentlist'	
    
    Employee_id = fields.Many2one('hr.employee', string='Employee',required=True)
    StartDate = fields.Date('Start Date',required=True)
    EndDate = fields.Date('End Date',required=True)
    
  
    salary_attach_ids = fields.One2many('hr.salary.attachment', 'attachmenyList_id', string='salary attachment',tracking=True)


class x_salary_attachmentlis(models.Model):
    _name = 'x_salary_attachmentlis'
    _description = 'x_salary_attachmentlis'
    _rec_name="x_name"

    x_active = fields.Boolean('Active',default=True)
    x_name = fields.Char('Name')
    x_studio_sequence = fields.Integer('Sequance')


             

class contactcustom(models.Model):
    _inherit = 'res.partner'


    @api.constrains('phone','email','mobile')
    def _check_name(self):
        for record in self:
           if record.mobile:     
                if re.match('^\d{10}$', record.mobile) == None:     
                    raise ValidationError("Enter valid 10 digits Mobile number")
           if record.phone:     
                if re.match('^\d{9}$', record.phone) == None:     
                    raise ValidationError("Enter valid phone number")         
           if record.email:     
                if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', record.email) == None:     
                    raise ValidationError("Enter valid email")     

class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    
    ssnid = fields.Char(size=10) 
    
    # def _check_length(self, cr, uid, ids, context=None):
    #     for record in self.browse(cr, uid, ids, context=context):   
    #         if len(record.ssnid)==10:
    #             return True
    #             # if  re.match("^[0-9]\d{10}$", record.ssnid) == None:    
    #         elif len(record.ssnid)<1 :
    #               return True   
    #     return False
    # _constraints = [(_check_length, 'Values should be 10 digit.', ['ssnid'])] 
 

  
    @api.constrains('ssnid','birthday')
    def _check_name(self):
        for record in self:
           if record.ssnid:     
                if not(record.ssnid.isnumeric()) or (len(record.ssnid)>=1 and len(record.ssnid)!=10):     
                    raise ValidationError("SSN ID should be 10 digit")
           if record.birthday:     
            if record.birthday: 
                fmt = '%Y-%m-%d'
                start_date = record.birthday 
                end_date = date.today()
                date_difference = end_date.year - start_date.year 
                if date_difference < 18:     
                    raise ValidationError("The Age Shoud be More Than 18 Yares")

                    

    # def create(self, vals):
    #     res = super(HrContract, self).create(vals)
    #     if res.emp_transfer:
    #         res.emp_transfer.write(
    #             {'state': 'done'})
    #     return res
