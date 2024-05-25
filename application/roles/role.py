from flask_principal import Principal, RoleNeed, UserNeed

from application.ticket_system.scripts.auth import User

# Означення ролей
admin_role = RoleNeed('admin')
manager_role = RoleNeed('manager')
analyst_role = RoleNeed('analyst')

# Означення потреб користувачів
user_need = UserNeed('user')

# Створення екземпляру Principal
principals = Principal()


# Додавання ролей до користувачів
@principals.identity_loader
def load_identity(user_id):
    user = User.query.get(user_id)
    if user:
        if user.role == 'admin':
            return [admin_role, user_need]
        elif user.role == 'manager':
            return [manager_role, user_need]
        elif user.role == 'analyst':
            return [analyst_role, user_need]
    return None
