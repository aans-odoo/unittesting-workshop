
# Exercise 02

## Statement -
  Write two tests for invoice validation:
    1. Write a test to ensure posting an invoice (`account.move`) with an
       invoice line (`invoice_line_ids`) changes it's state to "posted".
    2. Write another test to ensure that we can't post an invoice
       (`account.move`) without any invoice line (`invoice.line.ids`).

## Helpers -
  To create invoice, products, partner, you can use:
    ```
    # To create a partner
    partner = self.env['res.partner'].create({'name': 'John Doe'})

    # To create a product
    product = self.env['product.product'].create({'name': 'Workshop Product'})
    
    # To create an invoice with invoice lines
    invoice = self.env['account.move'].create({
         'move_type': 'out_invoice',
         'partner_id': partner.id,
         'invoice_line_ids': [(0, 0, {
              'product_id': product.id,
              'quantity': 1,
              'price_unit': 50,
          })]
     })

     # To create an invoice without invoice lines
    invoice_without_invoice_line = self.env['account.move'].create({
         'move_type': 'out_invoice',
         'partner_id': partner.id,
     })
    
    # To post an invoice
    invoice.action_post()
    ```
