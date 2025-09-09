from odoo.tests.common import TransactionCase

# Exercise 01
# 
# Statement -
#   Write two tests on a product:
#     1. Verify that when you set the product’s list price, the field is stored
#        correctly.
#     2. Verify that when you assign the tag to a product to a category, the tag
#        is correctly linked.
# 
# Helpers -
#   To create a product and tag:
#     ```
#     product_tag = self.env['product.tag'].create({'name': 'Test Tag'})
#     product = self.env['product.product'].create({
#         'name': 'Test Product',
#         'lst_price': 99.0,
#         'all_product_tag_ids': [product_tag.id],
#     })
#     ```

class TestClass(TransactionCase):

    def test_case(self):
        self.assertEqual(1, 1)
