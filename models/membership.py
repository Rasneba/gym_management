from odoo import models, fields

class GymMembership(models.Model):
    _name = 'gym.membership'
    _description = 'Gym Membership'

    name = fields.Char(string='Membership Name', required=True)
    duration_months = fields.Integer(string='Duration (Months)')
    price = fields.Float(string='Price')
    active = fields.Boolean(default=True)