# Copyright 2014 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for services relating to typed objects."""

from constants import constants
from core.domain import interaction_registry
from core.domain import obj_services
from core.tests import test_utils
from extensions.objects.models import objects

class ObjectRegistryUnitTests(test_utils.GenericTestBase):
    """Test the Registry class in obj_services."""

    def test_get_object_class_by_type_method(self):
        """Tests the normal behavior of get_object_class_by_type()."""
        self.assertEqual(
            obj_services.Registry.get_object_class_by_type('Int').__name__,
            'Int')

    def test_fake_class_is_not_gettable(self):
        """Tests that trying to retrieve a fake class raises an error."""
        with self.assertRaisesRegexp(TypeError, 'not a valid object class'):
            obj_services.Registry.get_object_class_by_type('FakeClass')

    def test_base_object_is_not_gettable(self):
        """Tests that BaseObject exists and cannot be set as an obj_type."""
        assert getattr(objects, 'BaseObject')
        with self.assertRaisesRegexp(TypeError, 'not a valid object class'):
            obj_services.Registry.get_object_class_by_type('BaseObject')


class ObjectDefaultValuesUnitTests(test_utils.GenericTestBase):
    """Test that the default value of objects recorded in
    assets/constants.js correspond to the defined default
    values in objects.py for all objects that
    are used in rules.
    """

    def test_get_object_default_values_is_valid(self):
        """Checks that the default values provided by get_default_values()
        correspond to the ones defined in objects.py.
        """
        object_default_vals = constants.DEFAULT_OBJECT_VALUES
        all_object_classes = obj_services.Registry.get_all_object_classes()
        for (obj_type, default_value) in object_default_vals.iteritems():
            self.assertIn(obj_type, all_object_classes)
            self.assertEqual(
                default_value, all_object_classes[obj_type].default_value)
