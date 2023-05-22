import json
from odoo import http
from odoo.http import request

class Timeoff(http.Controller):
    @http.route("/api/timeoff/request", auth="public")
    def index(self, **kw):
        records = request.env["timeoff.request"].search([])
        return records
