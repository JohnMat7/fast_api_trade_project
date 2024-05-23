from pydantic import BaseModel

class Trade(BaseModel):
    trade_id : int
    trade_type : str
    user_id : int
    stock_symbol : str 
    shares : int
    share_price : float
    trade_time : str

    

