# Copyright 2014 OpenStack Foundation
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
#  under the License.

import mock

from quark.tests import test_base
import quark.utils


class TestCommand(test_base.TestBase):
    def setUp(self):
        self.f = mock.MagicMock()
        self.cmd = quark.utils.Command(self.f)

    def test_init(self):
        self.assertFalse(self.cmd.called)

    def test_call(self):
        args = mock.MagicMock()
        fake_kwarg = mock.MagicMock()
        ret = self.cmd(args, fake=fake_kwarg)
        self.assertTrue(self.cmd.called)
        self.assertEqual(ret, self.f.return_value)
        self.f.assert_called_once_with(args, fake=fake_kwarg)


class TestCommandManager(test_base.TestBase):
    def setUp(self):
        self.cmd_mgr = quark.utils.CommandManager()

    def test_wrap_do(self):
        pass

    def test_wrap_undo(self):
        pass

    def test_execute_success(self):
        pass

    def test_rollback_success(self):
        pass

    def test_rollback_exception(self):
        pass
