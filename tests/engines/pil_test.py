# coding: utf-8
# author: v.bazhin@gmail.com

from base_case import BaseCase
from sorl_watermarker.engines.pil_engine import Engine as PILEngine
from PIL import Image as PILImage
import unittest
import os


class PILTestCase(BaseCase):

    def __init__(self, *args, **kwargs):
        super(PILTestCase, self).__init__(*args, **kwargs)
        self.engine = PILEngine()

    def get_comparable_image(self, options):
        """
        Creates a watermarked image
        """
        bg = PILImage.open(self.bg_path)
        mark = self.engine.watermark(bg, options)
        return mark


def pil_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PILTestCase, 'test'))
    return suite