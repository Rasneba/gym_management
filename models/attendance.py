from odoo import models, fields

class GymAttendance(models.Model):
    _name = 'gym.attendance'
    _description = 'Gym Attendance'

    member_id = fields.Many2one('gym.member', string="Member", required=True)
    check_in = fields.Datetime(string="Check-In", default=fields.Datetime.now)
    check_out = fields.Datetime(string="Check-Out")