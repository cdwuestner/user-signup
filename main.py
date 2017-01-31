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

page_header = """
<!DOCTYPE html>
<html>
<head>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
"""

page_footer = """
</body>
</html>
"""

invalid_username = "Please enter a valid username."

pass_too_short = "Your password is too short."

unmatching_pass = "The passwords must match."

def build_page(entered_username, error_name):
    header = "<h2>User Signup</h2>"

    username_label = "<label>Username </label>"
    if "invalid_user" in error_name:
        username_input = ("<input type='text' name='username' value='" + entered_username
                        + "'><span class='error'>" + invalid_username + "</span><br>")
    else:
        username_input = ("<input type='text' name='username' value='" + entered_username
                        + "'><br>")
    username_form = username_label + username_input

    password_label = "<label>Password </label>"
    if "short_pass" in error_name:
        password_input = ("<input type='password' name='password'><span class='error'>"
                        + pass_too_short + "</span><br>")
    else:
        password_input = "<input type='password' name='password'><br>"
    password_form = password_label + password_input

    ver_pass_label = "<label>Verify Password </label>"
    if "unmatching" in error_name:
        ver_pass_input = ("<input type='password' name='password'><span class='error'>"
                        + unmatching_pass + "</span><br>")
    else:
        ver_pass_input = "<input type='password' name='verify'><br>"
    ver_pass_form = ver_pass_label + ver_pass_input

    email_label = "<label>Email(optional) </label>"
    email_input = "<input type='email' name='email'><br>"
    email_form = email_label + email_input

    submit_input = "<input type='submit'>"

    form = ("<form method='post'>" + username_form + password_form +
            ver_pass_form + email_form + submit_input + "</form>")

    return page_header + header + form + page_footer

class MainHandler(webapp2.RequestHandler):
    def get(self):
        error = self.request.get("error")

        if error:
            content = build_page("", cgi.escape(error, quote=True))
        else:
            content = build_page("", "")

        self.response.write(content)

    def post(self):
        error = ""

        username = cgi.escape(self.request.get("username"))

        if len(username) < 1 or (' ' in username) == True:
            error += " invalid_user "
            error_escaped = cgi.escape(error, quote=True)

            self.redirect("/?error=" + error_escaped)

        password = cgi.escape(self.request.get("password"))
        verify = cgi.escape(self.request.get("verify"))

        if len(password) < 5:
            error += " short_pass "
            error_escaped = cgi.escape(error, quote=True)

            self.redirect("/?error=" + error_escaped)

        if password != verify:
            error += " unmatching "
            error_escaped = cgi.escape(error, quote=True)

            self.redirect("/?error=" + error_escaped)

        content = page_header + "<h2>Welcome, " + username + "!</h2>" + page_footer
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
