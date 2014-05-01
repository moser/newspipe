#! /usr/bin/env python
# -*- coding: utf-8 -*-

# pyAggr3g470r - A Web based news aggregator.
# Copyright (C) 2010-2013  Cédric Bonhomme - http://cedricbonhomme.org/
#
# For more information : http://bitbucket.org/cedricbonhomme/pyaggr3g470r/
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

__author__ = "Cedric Bonhomme"
__version__ = "$Revision: 0.2 $"
__date__ = "$Date: 2013/11/05 $"
__revision__ = "$Date: 2013/13/05 $"
__copyright__ = "Copyright (c) Cedric Bonhomme"
__license__ = "GPLv3"

from flask import flash
from flask.ext.wtf import Form
from flask.ext.babel import gettext
from wtforms import TextField, TextAreaField, PasswordField, BooleanField, SubmitField, validators

from pyaggr3g470r.models import User

class SigninForm(Form):
    """
    Sign in form.
    """
    email = TextField("Email", [validators.Required(gettext("Please enter your email address."))])
    password = PasswordField(gettext('Password'), [validators.Required(gettext("Please enter a password."))])
    submit = SubmitField(gettext("Log In"))

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter(User.email == self.email.data).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            flash(gettext('Invalid email or password'), 'danger')
            #self.email.errors.append("Invalid email or password")
            return False

class AddFeedForm(Form):
    title = TextField(gettext("Title"), [validators.Required(gettext("Please enter a title."))])
    link = TextField(gettext("Feed link"), [validators.Required(gettext("Please enter a link for the feed."))])
    site_link = TextField(gettext("Site link"))
    email_notification = BooleanField(gettext("Email notification"), default=False)
    enabled = BooleanField(gettext("Check for updates"), default=True)
    submit = SubmitField(gettext("Save"))

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        return True

class ProfileForm(Form):
    firstname = TextField(gettext("First name"), [validators.Required(gettext("Please enter your first name."))])
    lastname = TextField(gettext("Last name"), [validators.Required(gettext("Please enter your last name."))])
    email = TextField(gettext("Email"), [validators.Required(gettext("Please enter your email."))])
    password = PasswordField(gettext("Password"))
    submit = SubmitField(gettext("Save"))

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        return True
