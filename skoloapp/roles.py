from rolepermissions.roles import AbstractUserRole

class Kam(AbstractUserRole):
    available_permissions = {
        'is_kam': True,
    }

class Cso(AbstractUserRole):
    available_permissions = {
        'is_cso': True,
    }

class Management(AbstractUserRole):
    available_permissions = {
        'is_management': True,
    }