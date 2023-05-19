from odoo import api, models, fields


class SchoolAppointment(models.Model):
    _name = "school.appointment"
    _description = "School Appointment"
    _rec_name = "code"

    code = fields.Char(string="Code", required=True)
    date = fields.Datetime(
        string="Date", default=lambda self: fields.Datetime.now())

    student_id = fields.Many2one("school.student", string="Student")
    duration = fields.Float(string="Duration (Hours)")
