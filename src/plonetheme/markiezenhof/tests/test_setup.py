# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plonetheme.markiezenhof.testing import PLONETHEME_MARKIEZENHOF_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.markiezenhof is properly installed."""

    layer = PLONETHEME_MARKIEZENHOF_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.markiezenhof is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.markiezenhof'))

    def test_browserlayer(self):
        """Test that IPlonethemeMarkiezenhofLayer is registered."""
        from plonetheme.markiezenhof.interfaces import (
            IPlonethemeMarkiezenhofLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeMarkiezenhofLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_MARKIEZENHOF_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.markiezenhof'])

    def test_product_uninstalled(self):
        """Test if plonetheme.markiezenhof is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.markiezenhof'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeMarkiezenhofLayer is removed."""
        from plonetheme.markiezenhof.interfaces import IPlonethemeMarkiezenhofLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeMarkiezenhofLayer, utils.registered_layers())
