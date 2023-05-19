# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "School Students"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    picture = fields.Image(string="Profile Picture", required=True)
    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string="Gender", required=True)
    state = fields.Selection(
        [("reject", "Reject"), ("active", "Active"), ("move", "Move")], default="active", string="Status")


@api.onchange('age')
def check_positive_age(self):
    if (self.age < 1):
        self.age = 0
