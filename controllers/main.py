from odoo import http


class WorkshopController(http.Controller):

    def _some_method(self):
        return 'hello'

    @http.route('/workshop/last-partner/name', type='http', auth='user', readonly=True, csrf=False)
    def last_partner(self):
        partner = self.env['res.partner'].search([], order='create_date desc', limit=1)
        return partner.name

    @http.route('/workshop/jsonrpc/hello', type='jsonrpc', auth='public')
    def hello(self, name='World'):
        return {'greeting': f'Hello {name}'}
