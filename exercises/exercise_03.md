
# Exercise 03

## Statement -
  Write a test for the following controller routes:
    1. `/workshop/jsonrpc/hello`
       - Test this endpoint to ensure when a user calls it by passing their
         name, the response greeting includes that name.
    2. `/workshop/last-partner/name`
       - This endpoint returns the name of last created partner.
       - Test it to verify if it's logic works correctly.

  Helpers:
    To test controller routes, use:
    ```
      self.url_open('/http-route')
      self.make_jsonrpc_request('/rpc-route', {
          'data': 1
      })
    ```

    To test controller method, use:
    ```
      my_controller = ControllerClass()
      my_controller.method(params)
    ```
