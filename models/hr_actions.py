
from ast import Try
from odoo import models, fields, api 
from odoo.exceptions  import ValidationError
from datetime import date,datetime
from dateutil.relativedelta import relativedelta
import re


class payrollstructure(models.Model):
    _inherit = 'hr.payroll.structure'
   
    @api.model
    def _get_default_rule_ids2(self):
        return [
            (0, 0, {
                'name': _('Tax'),
                'sequence': 2,
                'code': 'Tax',
                'category_id': self.env.ref('hr_payroll.DED').id,
                'condition_select': 'range',
                'condition_range':'contract.wage',
                'condition_range_min':750.00,
                'condition_range_max':10000000000000.00,
                'amount_select': 'code',
                'amount_python_compute': """if contract.employee_id.marital == 'single':
   if contract.wage >= (9000/ 12):
       if (contract.wage - (9000/ 12)) / (5000/12)<= 1:
           result = -((contract.wage - (9000/ 12))* 0.05)
       else:
           cont=1
           res=0
           number=0
           for n in range(5000, int(contract.wage*12) - 9000,5000):
               if cont >=5:
                       res= res - ((5000/12)* (0.25) )
               else:
                        res=res- ((5000/12)* (cont* 0.05))    
               number=(n/12)+(5000/12)
               cont=cont+1

           if number >= (contract.wage - (9000/ 12)):
                   if cont >=5:
                       res= res - ((5000/12)- (number  - (contract.wage - (9000/ 12)))) * (0.25) 
                   else:
                        res=res- ((5000/12)- (number  - (contract.wage - (9000/ 12)))) * (cont* 0.05) 
           result=res   
   else:
      result=0
elif contract.employee_id.marital == 'married':
  if contract.wage >= (18000/ 12):
       if (contract.wage - (18000/ 12)) / (5000/12)<= 1:
           result = -((contract.wage - (18000/ 12))* 0.05)
       else:
           cont=1
           res=0
           number=0
           for n in range(5000, int(contract.wage*12) - 18000,5000):
               if cont >=5:
                       res= res - ((5000/12)* (0.25) )
               else:
                        res=res- ((5000/12)* (cont* 0.05))    
               number=(n/12)+(5000/12)
               cont=cont+1

           if number >= (contract.wage - (18000/ 12)):
                   if cont >=5:
                       res= res - ((5000/12)- (number  - (contract.wage - (18000/ 12)))) * (0.25) 
                   else:
                        res=res- ((5000/12)- (number  - (contract.wage - (18000/ 12)))) * (cont* 0.05) 
           result=res   
  else:
      result=0
else:
  result=0""",
            }),
            (0, 0, {
                'name': _('Basic Salary'),
                'sequence': 1,
                'code': 'BASIC',
                'category_id': self.env.ref('hr_payroll.BASIC').id,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': 'result = payslip.paid_amount',
            }),
            (0, 0, {
                'name': _('Gross'),
                'sequence': 100,
                'code': 'GROSS',
                'category_id': self.env.ref('hr_payroll.GROSS').id,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': 'result = categories.BASIC + categories.ALW',
            }),
            (0, 0, {
                'name': _('Deduction'),
                'sequence': 198,
                'code': 'DEDUCTION',
                'category_id': self.env.ref('hr_payroll.DED').id,
                'condition_select': 'python',
                'condition_python': 'result = inputs.DEDUCTION',
                'amount_select': 'code',
                'amount_python_compute': """result = -inputs.DEDUCTION.amount
result_name = inputs.DEDUCTION.name""",
            }),
            (0, 0, {
                'name': _('Attachment of Salary'),
                'sequence': 174,
                'code': 'ATTACH_SALARY',
                'category_id': self.env.ref('hr_payroll.DED').id,
                'condition_select': 'python',
                'condition_python': 'result = inputs.ATTACH_SALARY',
                'amount_select': 'code',
                'amount_python_compute': """result = -inputs.ATTACH_SALARY.amount
result_name = inputs.ATTACH_SALARY.name""",
            }),
            (0, 0, {
                'name': _('Assignment of Salary'),
                'sequence': 174,
                'code': 'ASSIG_SALARY',
                'category_id': self.env.ref('hr_payroll.DED').id,
                'condition_select': 'python',
                'condition_python': 'result = inputs.ASSIG_SALARY',
                'amount_select': 'code',
                'amount_python_compute': """result = -inputs.ASSIG_SALARY.amount
result_name = inputs.ASSIG_SALARY.name""",
            }),
            (0, 0, {
                'name': _('Child Support'),
                'sequence': 174,
                'code': 'CHILD_SUPPORT',
                'category_id': self.env.ref('hr_payroll.DED').id,
                'condition_select': 'python',
                'condition_python': 'result = inputs.CHILD_SUPPORT',
                'amount_select': 'code',
                'amount_python_compute': """result = -inputs.CHILD_SUPPORT.amount
result_name = inputs.CHILD_SUPPORT.name""",
            }),
            (0, 0, {
                'name': _('Reimbursement'),
                'sequence': 199,
                'code': 'REIMBURSEMENT',
                'category_id': self.env.ref('hr_payroll.ALW').id,
                'condition_select': 'python',
                'condition_python': 'result = inputs.REIMBURSEMENT',
                'amount_select': 'code',
                'amount_python_compute': """result = inputs.REIMBURSEMENT.amount
result_name = inputs.REIMBURSEMENT.name""",
            }),
            (0, 0, {
                'name': _('Net Salary'),
                'sequence': 200,
                'code': 'NET',
                'category_id': self.env.ref('hr_payroll.NET').id,
                'condition_select': 'none',
                'amount_select': 'code',
                'amount_python_compute': 'result = categories.BASIC + categories.ALW + categories.DED',
            })
            
        ]


    rule_ids = fields.One2many(
        'hr.salary.rule', 'struct_id',
        string='Salary Rules', default=_get_default_rule_ids2)


    