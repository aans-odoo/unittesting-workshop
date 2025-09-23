
# Exercise 01

## Statement -
  Write two tests on a product:
    1. Verify that when you create a product with listing price, the listing
       price field is stored correctly.
    2. Verify that when you add some tag on a product, the tag is correctly
       linked to that product.

## Helpers -
  To create a product and tag you can use:
    ```
    product_tag = self.env['product.tag'].create({'name': 'Test Tag'})
    product = self.env['product.product'].create({
        'name': 'Test Product',
        'lst_price': 99.0,
        'all_product_tag_ids': [(4, product_tag.id)],
    })
    ```
