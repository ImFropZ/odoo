# -*- coding: utf-8 -*-

from odoo import api, fields, models


class RemoveClassroomWizard(models.TransientModel):
    _name = "remove.classroom.wizard"
    _description = "Remove Classroom Wizard"

    classroom_id = fields.Many2one(
        "school.classroom", string="Name", required=True)
    reason = fields.Text(string="Reason")

    def confirm(self):
        classroom = self.classroom_id
        classroom.unlink()
        return {'type': 'ir.actions.act_window_close'}
