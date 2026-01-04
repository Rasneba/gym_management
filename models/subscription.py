from odoo import models, fields

class GymSubscription(models.Model):
    _name = 'gym.subscription'
    _description = 'Gym Subscription'

    name = fields.Char(string="Reference", required=True, copy=False, readonly=True, default='New')
    member_id = fields.Many2one('gym.member', string="Member", required=True)
    membership_id = fields.Many2one('gym.membership', string="Membership Plan", required=True)
    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    end_date = fields.Date(string="End Date")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('expired', 'Expired')
    ], string="Status", default='draft')