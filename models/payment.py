from odoo import models, fields

class GymPayment(models.Model):
    _name = 'gym.payment'
    _description = 'Gym Payment'

    member_id = fields.Many2one('gym.member', string="Member", required=True)
    subscription_id = fields.Many2one('gym.subscription', string="Subscription")
    amount = fields.Float(string="Amount", required=True)
    payment_date = fields.Date(string="Payment Date", default=fields.Date.today)