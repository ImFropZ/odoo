# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import datetime


class SchoolClassroom(models.Model):
    _name = "school.classroom"
    _description = "School Classrooms"
    _rec_name = "name"

    name = fields.Char(string="Name", required=True)
    teachers = fields.Many2many("school.teacher", string="Teachers")
    students = fields.Many2many("school.student", string="Students")
    schedule = fields.Date(string="Active Class Date",
                           default=lambda self: fields.Date.today())
    duration = fields.Float(string="Duration")
