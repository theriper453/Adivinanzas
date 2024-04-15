from flask_login import UserMixin, LoginManager
from users import users


class User(UserMixin):
    pass


def def_loader(login_manager: LoginManager):
    global user_loader
    global request_loader

    @login_manager.user_loader
    def user_loader(username):
        if username not in users:
            return

        username = User()
        username.id = username
        return username


    @login_manager.request_loader
    def request_loader(request):
        username = request.form.get('username')
        if username not in users:
            return

        user = User()
        user.id = username
        return user