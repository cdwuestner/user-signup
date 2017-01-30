#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

def build_page():
    header = "<h2>User Signup</h2>"

    username_label = "<label>Username </label>"
    username_input = "<input type='text' name='username'><br>"
    username_form = username_label + username_input

    password_label = "<label>Password </label>"
    password_input = "<input type='password' name='password'><br>"
    password_form = password_label + password_input

    ver_pass_label = "<label>Verify Password </label>"
    ver_pass_input = "<input type='password' name='verify'><br>"
    ver_pass_form = ver_pass_label + ver_pass_input

    email_label = "<label>Email(optional) </label>"
    email_input = "<input type='text' name='email'><br>"
    email_form = email_label + email_input

    form = "<form>" + username_form + password_form + ver_pass_form + email_form + "</form>"

    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page()

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
