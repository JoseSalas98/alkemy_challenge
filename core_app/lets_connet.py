#   Importamos las librerías
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

#   Definimos la clase "db_connetion"
class db_connetion:
    def __init__(self, db_name, db_user, db_pass, db_host, db_port):
        self.__db_name = db_name
        self.__db_user = db_user
        self.__db_pass = db_pass
        self.__db_host = db_host
        self.__db_port = db_port
        self.__db_string = "postgresql://{}:{}@{}:{}/{}".format(self.__db_user, self.__db_pass, 
                                                                self.__db_host, self.__db_port, self.__db_name)
        self.__engine = None

    def name_inpt(self, name = None):
        if (name is None):
            nm = input("Indique el nombre de la base de datos:")
            self.name_inpt(name = nm)
            pass
        
        else:
            if (type(name) != str):
                raise TypeError("name debe ser una cadena de caracteres")
            else:
                self.__db_name = name
                self.__db_string = "postgresql://{}:{}@{}:{}/{}".format(self.__db_user, self.__db_pass, 
                                                                        self.__db_host, self.__db_port, self.__db_name)
                print(self.__db_name)
                print(self.__db_string)

    def user_inpt(self, user = None):
        if (user is None):
            usr = input("Indique el usuario:")
            self.user_inpt(user = usr)
            pass

        else:
            if (type(user) != str):
                raise TypeError("user debe ser una cadena de caracteres")
            else:
                self.__db_user = user
                self.__db_string = "postgresql://{}:{}@{}:{}/{}".format(self.__db_user, self.__db_pass, 
                                                                        self.__db_host, self.__db_port, self.__db_name)
                print(self.__db_user)
                print(self.__db_string)
    
    def password_inpt(self, password = None):
        if (password is None):
            passwrd = input("Indique la contraseña:")
            self.password_inpt(password = passwrd)
            pass

        else:
            if (type(password) != str):
                raise TypeError("password debe ser una cadena de caracteres")
            else:
                self.__db_pass = password
                self.__db_string = "postgresql://{}:{}@{}:{}/{}".format(self.__db_user, self.__db_pass, 
                                                                        self.__db_host, self.__db_port, self.__db_name)
                print(self.__db_pass)
                print(self.__db_string)

    def host_inpt(self, host = None):
        if (host is None):
            hst = input("Indique la red:")
            self.host_inpt(host = hst)
            pass

        else:
            if (type(host) != str):
                raise TypeError("host debe ser una cadena de caracteres")
            else:
                self.__db_host = host
                self.__db_string = "postgresql://{}:{}@{}:{}/{}".format(self.__db_user, self.__db_pass, 
                                                                        self.__db_host, self.__db_port, self.__db_name)
                print(self.__db_host)
                print(self.__db_string)

    def port_inpt(self, port = None):
        if (port is None):
            prt = input("Indique la red:")
            self.port_inpt(port = prt)
            pass

        else:
            if (type(port) != str):
                raise TypeError("host debe ser una cadena de caracteres")
            else:
                self.__db_port = port
                self.__db_string = "postgresql://{}:{}@{}:{}/{}".format(self.__db_user, self.__db_pass, 
                                                                        self.__db_host, self.__db_port, self.__db_name)
                print(self.__db_port)
                print(self.__db_string)

    def default(self):
        self.__db_name = "database"
        self.__db_user = "postgres"
        self.__db_pass = "changeme"
        self.__db_host = "localhost"
        self.__db_port = "5432"
        self.__db_string = "postgresql://{}:{}@{}:{}/{}".format(self.__db_user, self.__db_pass, self.__db_host, self.__db_port, self.__db_name)
        self.shw_evn_var()
        self.shw_string()

    def shw_string(self):
        return self.__db_string
    
    def shw_evn_var(self):
        print(f"db_name: {self.__db_name} \n user: {self.__db_user} \n pass: {self.__db_pass} \n host: {self.__db_host} \n port:{self.__db_port}")
    
    def db_exist(self):
        return database_exists(self.__db_string)

    def create(self):
        if self.db_exist():
            print("La base de datos existe")
            pass

        else:
            print("La base de datos no existe: crea la base datos")
            return create_database(self.__db_string)                                                           
            
    def start_connt(self):
        if self.__engine is None:
                if self.db_exist():
                    print("La base de datos existe")
                    db_created = None
                    pass

                else:
                    print("La base de datos no existe: crea la base datos")
                    db_created = create_database(self.__db_string)

                print("La conexión no existe: crea la conexión")
                self.__engine = create_engine(self.__db_string)
        else:
            print("Ya ha sido establecida una conexión previa con el motor de base de datos")

        return db_created, self.__engine

    def end_connt(self):

        if self.__engine is not None:
            self.__engine = self.__engine.dispose()
            print("Finalizó la conexión")
            return self.__engine
        else:
            print("No se han establecido conexiones con el motor de base de datos")
            pass
