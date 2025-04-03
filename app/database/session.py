from sqlmodel import create_engine, Session, select, SQLModel


sql_file_name = "dados.db"
sql_url = f"sqlite:///{sql_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sql_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


