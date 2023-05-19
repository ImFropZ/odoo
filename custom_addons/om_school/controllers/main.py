import json
from odoo import http
from odoo.http import request


class School(http.Controller):

    @http.route("/school/student", website=True, auth="public")
    def school(self, **kw):
        students_record = request.env['school.student'].sudo().search([])
        print(students_record)
        return request.render("om_school.students", {
            'students': students_record
        })
    
    @http.route("/foo", auth="public")
    def student(self, **kw):
        students_record = request.env['school.student'].sudo().search([])
        
        return "json.dump(students_record)"
