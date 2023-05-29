import json
from odoo import http
from odoo.http import request
from odoo.exceptions import ValidationError

class CustomSnippetsDynamicCategory(http.Controller):
    @http.route(['/total_product_sold'], type="json", auth="public")
    def sold_total(self):
        sale_obj = request.env['sale.order'].sudo().search([
            ('state', 'in', ['done', 'sale']),
        ])
        total_sold = sum(sale_obj.mapped('order_line.product_uom_qty'))
        return total_sold                    
   
    @http.route(['/get_product_category'], type="json", auth="public")
    def product_category(self, domain=None, **kwargs):
        try:
            if domain:
                category_obj = request.env['product.public.category'].search(domain)
            else:
                category_obj = request.env['product.public.category'].search([])

            categories = category_obj.read(['id', 'name', 'image_1920'])

            for category in categories:
                if category.get('image_1920'):
                    category['image'] = category.get('image_1920')
                    category.pop('image_1920', None)
                else:
                    category['image'] = False

                category['website_url'] = f"/shop/category/{category.get('id')}"

            return categories

        except ValidationError as e:
            error_message = {'error': str(e)}
            return request.make_response(json.dumps(error_message), headers=[('Content-Type', 'application/json')])

       