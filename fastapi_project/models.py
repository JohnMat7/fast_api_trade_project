from sqlalchemy import Column , Integer , String , Float , TIMESTAMP
import db_connection

class Trade(db_connection.Base):
    __tablename__ = "trades"
    trade_id = Column(Integer , primary_key=True)
    trade_type = Column(String)
    user_id = Column(Integer)
    stock_symbol = Column(String)
    shares = Column(Integer)
    share_price = Column(Float)
    trade_time = Column(String)



# type: The trade type, either "buy" or "sell"
# user _id : The unique user id (integer)
# symbol: The stock symbol (string)
# shares: The total number of shares traded. The shares value traded is between 10 and 30 shares, inclusive(integer)
# price
# timestamp   