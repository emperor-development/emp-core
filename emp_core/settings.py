import configparser

class Parser(configparser.ConfigParser):
    def __init__(self, filename = 'settings.ini') -> None:
        super().__init__()
        self.read(filename)

    def get_fastapi_option(self, option: str) -> bool:
        return self.get("fastapi", option) != '0'

    def get_fastapi_docs_url(self) -> bool:
        return self.get_fastapi_option("docs_url") != '0'

    def get_fastapi_openapi_url(self) -> str:
        return self.get_fastapi_option("openapi_url")

    def get_postgres_option(self, option: str) -> str:
        return self.get("postgres", option)

    def get_postgres_user(self) -> str:
        return self.get_postgres_option("user")

    def get_postgres_password(self) -> str:
        return self.get_postgres_option("password")

    def get_postgres_host(self) -> str:
        return self.get_postgres_option("host")

    def get_postgres_port(self) -> str:
        return self.get_postgres_option("port")

    def get_postgres_dbname(self) -> str:
        return self.get_postgres_option("dbname")

    def get_sqlalchemy_conn_str(self) -> str:
        connection_str = "postgresql+psycopg://"
        connection_str += (self.get_postgres_user() + r":" + self.get_postgres_password() + r"@" + 
                           self.get_postgres_host() + r":" + self.get_postgres_port() + r"/" + 
                           self.get_postgres_dbname())
        return connection_str

    def get_sqlalchemy_async_conn_str(self) -> str:
        connection_str = "postgresql+asyncpg://"
        connection_str += (self.get_postgres_user() + r":" + self.get_postgres_password() + r"@" + 
                           self.get_postgres_host() + r":" + self.get_postgres_port() + r"/" + 
                           self.get_postgres_dbname())
        return connection_str