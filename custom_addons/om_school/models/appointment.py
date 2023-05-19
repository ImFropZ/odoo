from odoo import api, models, fields
from datetime import timedelta


class SchoolAppointment(models.Model):
    _name = "school.appointment"
    _description = "School Appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "code"

    code = fields.Char(string="Code", required=True)
    date = fields.Datetime(
        string="Date", default=lambda self: fields.Datetime.now(), required=True)

    student_id = fields.Many2one("school.student", string="Student")
    duration = fields.Float(string="Duration (Hours)")
    # reason = fields.Text(string="Reason", default="")
    state = fields.Selection([("upcoming", "Upcoming"), ("today", "Today"), ("running", "Running"), ("done", "Done")], string="Status", compute="_compute_state", tracking=True)

    @api.depends("date", "duration")
    def _compute_state(self):
        datetime = self.date.strftime("%m/%d/%Y, %H:%M:%S")
        datetime_with_duration = (
            self.date + timedelta(hours=self.duration)).strftime("%m/%d/%Y, %H:%M:%S")
        date = self.date.strftime("%m/%d/%Y")

        datetime_now = fields.Datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        date_now = fields.Datetime.now().strftime("%m/%d/%Y")

        if (datetime > datetime_now):
            self.state = "upcoming"
            return

        if (datetime <= datetime_now and datetime_now <= datetime_with_duration):
            self.state = "running"
            return

        if (date == date_now):
            self.state = "today"
            return

        if (datetime < datetime_now):
            self.state = "done"
            return

        return
