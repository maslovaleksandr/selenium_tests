from .DefaultPage import DefaultPage
from ..locators.Common import Common


class UserPage(DefaultPage):

    def login_user(self, user, password):
        self._input(Common.user_login.email_input, user)
        self._input(Common.user_login.password_input, password)
        self._click(Common.user_login.submit)
        return self
