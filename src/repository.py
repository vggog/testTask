from sqlalchemy import create_engine, select, insert, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from settings import Settings
from src.model import user_table


class Repo:
    engine = create_engine(Settings.db_url)

    def _get_sessionmaker(self) -> sessionmaker:
        return sessionmaker(self.engine)

    def _get_session(self) -> Session:
        session = self._get_sessionmaker()
        return session()

    def get_user(self, user_id: str):
        """
        Получить нужного юзера.
        Возвращает Кортеж(id, sity), в случае, если юзер есть в базе данных.
        None в противном случае.
        """
        statement = select(user_table).filter(user_table.c.id==user_id)

        with self._get_session() as session:
            return session.execute(statement).first()

    def add_user(self, user_id: int, sity: str):
        """
        Добавить юзера в базу данных.
        :param user_id:
        :param sity:
        :return:
        """
        statement = insert(user_table).values(
            id=user_id,
            sity=sity
        )
        with self._get_session() as session:
            session.execute(statement)
            session.commit()

    def update_user(self, user_id: int, city: str):
        """
        Обновить город юзера в базе данных.
        :param user_id:
        :param city:
        """
        statement = (
            update(user_table).
            where(user_table.c.id==user_id).
            values(sity=city)
        )

        with self._get_session() as session:
            session.execute(statement)
            session.commit()

    def create_or_update(self, user_id, city: str):
        """
        Метод для добавление города пользователя,
            или обновление города у пользователя.
        :param user_id:
        :param city:
        """
        if self.get_user(user_id):
            self.update_user(user_id, city)
        else:
            self.add_user(user_id, city)
