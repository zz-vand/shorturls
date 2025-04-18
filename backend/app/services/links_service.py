from app.bd_logic.bd_logic import Linkrepository
from app.services import service_words


class NewLinkService:
    
    def __init__(self) -> None:
        self.linkrepository = Linkrepository()

    async def put_link_user(self, user_link_: str, userword: str) -> str:

        new_link_ = userword + service_words.random_num()

        qr_code = await self.linkrepository.put_link(user_link=user_link_, new_link=new_link_)

        return {"qr": qr_code, "new_link": new_link_}
    
    async def put_link_rand(self, user_link_: str) -> str:

        new_link_ = service_words.random_english_word()

        qr_code = await self.linkrepository.put_link(user_link=user_link_, new_link=new_link_)

        await self.linkrepository.put_link(user_link=user_link_, new_link=new_link_)

        return {"qr": qr_code, "new_link": new_link_}

    async def get_user_link(self, new_link: str):
        return await self.linkrepository.get_user_link(new_link_= new_link)