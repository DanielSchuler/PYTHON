class Usuario:

    def __init__(self, nId=None, nUser=None, nPassword=None):
        self.__id = nId
        self.__user = nUser
        self.__password = nPassword

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, nId):
        self.__id = nId

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, nUser):
        self.__user = nUser

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, nPassword):
        self.__password = nPassword

    def __str__(self):
        return f'''
                Se presenta la informacion del Usuario con la siguiente información
                Persona:
                Id:{self.id},
                Usuario:{self.user},
                Password:{self.password}
                '''
