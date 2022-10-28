from odoo import fields, models


class PatientProfile(models.Model):
    _name = 'hr_hospital.patient_profile'
    _description = 'Patient profile'

    name = fields.Char()

    patient_id = fields.Many2one(comodel_name='hr_hospital.patient')

    diagnosis_ids = fields.Many2many(
        comodel_name='hr_hospital.diagnosis', )

    doctor_ids = fields.Many2many(
        comodel_name='hr_hospital.doctor', )