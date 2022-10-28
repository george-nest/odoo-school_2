from odoo import fields, models


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Patient'

    name = fields.Char()
    isbn = fields.Char()
    patient_profile_ids = fields.Many2one('hr_hospital.patient_profile', 'Profile')
