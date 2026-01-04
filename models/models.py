from odoo import models, fields, api
from datetime import date, timedelta

class GymMembership(models.Model):
    _name = 'gym.membership'
    _description = 'Gym Membership'

    name = fields.Char(string="Membership Name", required=True)
    duration_months = fields.Integer(string="Duration (Months)", required=True)
    price = fields.Float(string="Price")
    active = fields.Boolean(default=True)


class GymMember(models.Model):
    _name = 'gym.member'
    _description = 'Gym Member'

    name = fields.Char(string="Full Name", required=True)
    phone = fields.Char()
    email = fields.Char()
    membership_id = fields.Many2one('gym.membership', string='Membership')
    start_date = fields.Date(default=date.today)
    end_date = fields.Date()
    active = fields.Boolean(default=True)
    frozen = fields.Boolean(string="Frozen", default=False)

    @api.onchange('membership_id')
    def _compute_end_date(self):
        """Set end_date automatically based on membership duration"""
        for rec in self:
            if rec.membership_id:
                rec.end_date = rec.start_date + timedelta(days=30 * rec.membership_id.duration_months)

    def action_freeze_subscription(self):
        """Freeze a subscription"""
        for rec in self:
            if rec.frozen:
                raise ValueError("Subscription already frozen!")
            rec.frozen = True
            rec.active = False

    def action_unfreeze_subscription(self):
        """Unfreeze a subscription"""
        for rec in self:
            rec.frozen = False
            rec.active = True


class GymAttendance(models.Model):
    _name = 'gym.attendance'
    _description = 'Gym Attendance'

    member_id = fields.Many2one('gym.member', string="Member")
    check_in = fields.Datetime(default=fields.Datetime.now)
    check_out = fields.Datetime()
