from odoo import api, models, fields
from datetime import timedelta

class TimeOffRequest(models.Model):
    _name = "timeoff.request"
    _description = "Time Off Request"

    ttype = fields.Selection([("sick_time_off","Sick Time Off"), ("compensatory_days", "Compensatory Days")], string="Time Off Type")
    start_date = fields.Date(string="From", default=lambda self:fields.Date.today())
    end_date = fields.Date(string="To", compute="_calculateDuration")
    duration = fields.Integer(string="Duration", default=0)
    description = fields.Text(string="Description")
    state = fields.Selection([("to_approve", "TO APPROVE"), ("approved", "APPROVED")], string="Status", default="to_approve")

    @api.depends("start_date", "duration")
    def _calculateDuration(self):
        self.end_date = self.start_date + timedelta(days=self.duration)