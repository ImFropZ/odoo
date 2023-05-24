from odoo import http

class DynamicCategorySnippets(http.Controller):
    @http.route(["/snippets/category"], type="json", auth="public", website=True)
    def category(self):
        categories = http.request.env["product.public.category"].search([])
        data = []
        for category in categories:
            field = category.read(['id','name'])
            data.append(field)

        return http.request.env['ir.ui.view']._render_template('custom_snippets.s_dynamic_category_card', {
            "categories": data
        })