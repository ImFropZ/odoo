# -*- coding: utf-8 -*-

from odoo import api, fields, models


class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _description = "School Teachers"

    picture = fields.Image(string="Profile Picture", required=True)
    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age", required=True)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string="Gender", required=True)


@api.onchange('age')
def check_positive_age(self):
    if (self.age < 1):
        self.age = 0
