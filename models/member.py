# models/gym_member.py
from odoo import models, fields

class GymMember(models.Model):
    _name = 'gym.member'
    _description = 'Gym Member'

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    membership_id = fields.Many2one('gym.membership', string="Membership")
