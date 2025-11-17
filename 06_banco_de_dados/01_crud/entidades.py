from sqlalchemy import Column, String, Integer, Date

# função que cria o banco de dados e as entidades
def criar_tb_pessoa(engine, Base):
    # tratamento de exceção
    try:
        class Pessoa(Base):
            __tablename__ = "pessoa"

            # atributos
            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
            nome = Column(String, nullable=False)
            nascimento = Column(Date, nullable=False)
            email = Column(String, nullable= False, unique=True)
            genero = Column(String, nullable=True)
            
        Base.metadata.create_all(engine)

        return Pessoa
    except Exception as e:
        print(f"Não foi possivel conectar com o banco de dados.{e}.")