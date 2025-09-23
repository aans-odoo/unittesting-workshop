from odoo.tests.common import TransactionCase
from odoo.tests import tagged

@tagged('arib')
class TestSampleClass(TransactionCase):
    
    def test_sample_case_01(self):
        self.assertEqual(1, 1)

    def test_sample_case_02(self):
        self.assertEqual(1, 1)
    
    def test_sample_case_03(self):
        self.assertEqual(1, 1)
    

@tagged('arib')
class TestSampleClass02(TransactionCase):
    
    def test_sample_case_03(self):
        self.assertEqual(1, 1)

    def test_sample_case_04(self):
        self.assertEqual(1, 1)
    
    def test_sample_case_05(self):
        self.assertEqual(1, 1)
    