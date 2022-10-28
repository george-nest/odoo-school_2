

import logging

from odoo import fields, models

_loger = logging.getLogger(__name__)


class diagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _description = 'diagnosis'

    name = fields.Char()
    isbn = fields.Char()
    patient_id = fields.Many2one(comodel_name='hr_hospital.patient')
    patient_profile_id = fields.Many2one(comodel_name='hr_hospital.patient_profile')
    doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor')