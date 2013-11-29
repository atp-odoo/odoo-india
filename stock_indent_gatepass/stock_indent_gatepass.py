# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv

class stock_gatepass(osv.Model):
    _inherit = 'stock.gatepass'
    
    def onchange_indent(self, cr, uid, ids, indent=False, *args, **kw):
        result = {'line_ids': []}
        lines = []
 
        if not indent:
            return {'value': result}
        products = self.pool.get('indent.indent').browse(cr, uid, indent).product_lines
        location_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'stock', 'stock_location_stock')
        location = location_id and location_id[1] or False
        for product in products:
            vals = dict(product_id=product.original_product_id.id or product.product_id.id or False, product_qty=product.product_uom_qty, uom_id=product.product_uom.id, name=product.product_id.name, location_id=location, location_dest_id=location, price_unit=product.price_unit)
            lines.append(vals)
        result['line_ids'] = lines
        return {'value': result}
    
    _columns = {
        'indent_id': fields.many2one('indent.indent', 'Indent', readonly=True, states={'draft': [('readonly', False)]})
    }

stock_gatepass()