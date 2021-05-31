from datetime import date, datetime, timedelta
import django
import django.db.utils
import django.core.exceptions
from django.test import TestCase
from .models import Widget
from zoneinfo import ZoneInfo
import time_machine

future_test_date = datetime(2222, 3, 4, tzinfo=ZoneInfo('America/Denver'))


class WidgetTests(TestCase):
    """
    WidgetTests(TestCase):
        tests against Widget model
    """

    # data for creating and comparing widgets
    # for testing
    _widget_create = [
        {'name': 'screwdriver', 'number_of_parts': 10},
        {'name': 'pliers', 'number_of_parts': 6},
    ]

    def setUp(self):
        """
        setUp():  create widgets for tests
        """
        self.tomorrow_date = date.today() + timedelta(days=1)

        for widget_create_info in self._widget_create:
            Widget.objects.create(**widget_create_info)

    def test_widget_parts(self):
        """
        test_widget_parts():  test various parts of
            Widget model
        """
        for widget_create_info in self._widget_create:
            widget = Widget.objects.get(name=widget_create_info['name'])
            # widget should exist
            self.assertNotEqual(None, widget)
            # widget parts should equal what we created
            self.assertEqual(
                widget_create_info['number_of_parts'],
                widget.number_of_parts
            )
            # at this point widget should have created date
            self.assertEqual(
                True,
                widget.created_date >= date.today()
            )
            # and updated date should equal created date
            self.assertEqual(
                widget.created_date,
                widget.updated_date
            )

    def test_widget_null_name(self):
        """
        test_widget_null_name():
            name cannot be null
        """
        # shouldn't allow null names
        self.assertRaises(
            django.core.exceptions.ValidationError,
            Widget.objects.create,
            **{'name': None, 'number_of_parts': 5}
        )

    def test_widget_name_too_long(self):
        """
        test_widget_name_too_long():
            name cannot be more than 64 chars
        """
        # shouldn't allow names > 64 chars
        # sqlite3 will NOT enforce max_len, but if we
        # call clean_fields() django will validate it
        self.assertRaises(
            django.core.exceptions.ValidationError,
            Widget.objects.create,
            **{'name': '1'*75, 'number_of_parts': 7}
        )

    def test_widget_null_number_of_parts(self):
        """
        test_widget_null_number_of_parts():
            number_of_parts cannot be null
        """
        # shouldn't allow null number_of_parts
        self.assertRaises(
            django.core.exceptions.ValidationError,
            Widget.objects.create,
            **{'name': 'sample', 'number_of_parts': None}
        )

    @time_machine.travel(future_test_date)
    def test_widget_updated_date(self):
        """
        test_widget_updated_date():
            updated date should change to current date any
            time that widget is updated
            simulate date in future with time_machine
        """
        widget_create_vals = self._widget_create[0]
        widget = Widget.objects.get(**widget_create_vals)
        widget.number_of_parts += 1
        widget.save()
        self.assertEqual(date(2222, 3, 4), widget.updated_date)
