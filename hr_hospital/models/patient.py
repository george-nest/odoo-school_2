import logging
from odoo import models, fields, api, exceptions
_logger = logging.Logger(_name__)
class Patient(models.Model)
    _name = "hr.hospital.patient"
    _description = "Patient"

    name = fields.Char()

    active = fields.Boolean(defolt = True)
    isbn = fields.Char()
