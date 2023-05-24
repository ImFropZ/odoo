import json

from odoo import http

class WebsiteController(http.Controller):
    # @http.route('/api/category', auth='public', website=True)
    # def list_products(self, **kwargs):
    #     website = http.request.env['website'].search([])

    #     print(website)
    #     # categories = http.request.env['product.public.category'].search([('website_id', '=', website.id)])
    #     categories = http.request.env['product.public.category'].search([])
    #     data = {
    #         'categories': [{
    #             'id': category.id,
    #             'name': category.name,
    #         } for category in categories],
    #     }
    #     return json.dumps(data)
    
    @http.route('/api/category', auth='public', website=True, type="json")
    def list_products(self, **kwargs):
        categories = http.request.env['product.public.category'].search([])
        data = [{
                'id': category.id,
                'name': category.name,
            } for category in categories],
        
        return http.request.env['ir.ui.view']._render_template("timeoff.hello_world_template")
