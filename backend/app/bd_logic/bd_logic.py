from app.insrastructure_bd.connection import async_connection, create_all
from app.persistent_db.db import Link
from sqlalchemy import insert, select 
from app.services.qr_code_generation import generate_qr_code

class Linkrepository:
    def __init__(self) -> None:
        self.sessionmaker = async_connection()
        create_all()
    
    async def put_link(self, user_link: str, new_link: str):
        qr_code = generate_qr_code(user_link)


        stmp = insert(Link).values({"user_link": user_link, "new_link": new_link, "qr_code": qr_code})

        async with self.sessionmaker() as session:
            await session.execute(stmp)
            await session.commit()
        return qr_code
    

    async def get_user_link(self, new_link_: str):

        stmp = select(Link.user_link).where(Link.new_link == new_link_).order_by(Link.created_at.desc()).limit(1)

        async with self.sessionmaker() as session:
            resp = await session.execute(stmp)
        
        row = resp.fetchone()

        if row is None:
            return None 
        
        return row[0]
   
