#!/usr/bin/env/python3

import unittest
import tv_service
# https://docs.python.org/3/library/unittest.mock.html
from unittest.mock import patch


class TestTvService(unittest.TestCase):

    def test_tvcommand(self):
        expect_dash_separated = 'volume-decrease-increase'
        self.assertEqual(tv_service.TVCommand.volume_decrease_increase.value, expect_dash_separated)

    def test_command_url_volume_decrease_increase(self):
        expected = 'http://10.0.0.4:5000/api/v1/tv/volume-decrease-increase/'
        actual = tv_service.command_url(tv_service.TVCommand.volume_decrease_increase)
        self.assertEqual(actual, expected)

    # TODO: check if this is correct way to mock
    @patch('tv_service.request_command')
    def test_volume_decrease_increase_calls_request_command(self, mock):
        """
        https://stackoverflow.com/questions/18762293/how-to-test-that-a-function-is-called-within-a-function-with-nosetests
        """
        duration_seconds = 15.7
        tv_service.volume_decrease_increase(duration_seconds=duration_seconds)
        self.assertTrue(mock.called)

    @patch('tv_service.request_command')
    def test_volume_decrease_calls_request_command(self, mock):
        tv_service.volume_decrease()
        self.assertTrue(mock.called)

