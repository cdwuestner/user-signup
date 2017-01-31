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
import cgi

def build_page(error_name):
    header = "<h2>User Signup</h2>"

    username_label = "<label>Username </label>"
    if error_name == "Please provide a valid username.":
        username_input = "<input type='text' name='username'>" + error_name + "<br>"
    else:
        username_input = "<input type='text' name='username'><br>"
    username_form = username_label + username_input

    password_label = "<label>Password </label>"
    if error_name == "Your password must contain at least 5 characters.":
        password_input = "<input type='password' name='password'>" + error_name + "<br>"
    else:
        password_input = "<input type='password' name='password'><br>"
    password_form = password_label + password_input

    ver_pass_label = "<label>Verify Password </label>"
    if error_name == "The two passwords do not match.":
        ver_pass_input = "<input type='password' name='password'>" + error_name + "<br>"
    else:
        ver_pass_input = "<input type='password' name='verify'><br>"
    ver_pass_form = ver_pass_label + ver_pass_input

    email_label = "<label>Email(optional) </label>"
    email_input = "<input type='text' name='email'><br>"
    email_form = email_label + email_input

    submit_input = "<input type='submit'>"

    form = ("<form method='post'>" + username_form + password_form +
            ver_pass_form + email_form + submit_input + "</form>")

    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):

        error = self.request.get("error")
        if error:
            content = build_page(cgi.escape(error, quote=True))
        else:
            content = build_page("")

        self.response.write(content)

    def post(self):
        username = self.request.get("username")

        if len(username) < 1 or (' ' in username) == True:
            error = "Please provide a valid username."
            error_escaped = cgi.escape(error, quote=True)

            self.redirect("/?error=" + error_escaped)

        password = self.request.get("password")
        verify = self.request.get("verify")

        if len(password) < 5:
            error = "Your password must contain at least 5 characters."
            error_escaped = cgi.escape(error, quote=True)

            self.redirect("/?error=" + error_escaped)

        if password != verify:
            error = "The two passwords do not match."
            error_escaped = cgi.escape(error, quote=True)

            self.redirect("/?error=" + error_escaped)

        content = build_page("")
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
