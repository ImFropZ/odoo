from odoo import api, models, fields
from datetime import timedelta

class TimeOffRequest(models.Model):
    _name = "timeoff.request"
    _description = "Time Off Request"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "id"

    ttype = fields.Selection([("sick_time_off","Sick Time Off"), ("compensatory_days", "Compensatory Days")], string="Time Off Type", default="sick_time_off", required=True)
    start_date = fields.Date(string="From", default=lambda self:fields.Date.today(), tracking=True)
    end_date = fields.Date(string="To", compute="_calculate_duration")
    duration = fields.Integer(string="Duration", default=0, tracking=True)
    delay_date = fields.Integer(compute="_calculate_duration_to_hour", store=True)
    description = fields.Text(string="Description")
    state = fields.Selection([("rejected", "REJECTED"),("to_approve", "TO APPROVE"), ("approved", "APPROVED")], string="Status", default="to_approve")

    def button_approve(self):
        self.state = "approved"

    def button_reject(self):
        self.state = "rejected"

    @api.depends("start_date", "duration")
    def _calculate_duration(self):
        for record in self:
            record.end_date = record.start_date + timedelta(days=record.duration)

    @api.depends("duration")
    def _calculate_duration_to_hour(self):
        for record in self:
            record.delay_date = record.duration * 24

            