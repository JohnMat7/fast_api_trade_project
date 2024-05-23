from fastapi import FastAPI , status , Depends
from sqlalchemy.orm import Session
import schemas , models , db_connection

db_connection.Base.metadata.create_all(bind=db_connection.engine)


app = FastAPI()



# Dependency
def get_db():
    db = db_connection.SessionLocal()
    try:
        yield db
    finally:
        db.close()





# testing api working or not
@app.get("/" , status_code=status.HTTP_200_OK)
def check_status():
    return {"Status" : "Yes API Ready to use"}

#create a trade record in db
@app.post("/create-trade" ,  status_code=status.HTTP_201_CREATED)
def create_trade(trade : schemas.Trade  , db : Session = Depends(get_db)):
    db_trade = models.Trade(
        trade_id  =  trade.trade_id,
        trade_type = trade.trade_type,
        user_id  =  trade.user_id,
        stock_symbol  =  trade.stock_symbol,
        shares =  trade.shares,
        share_price  =  trade.share_price,
        trade_time =  trade.trade_time
    )
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade


@app.get("/all-trades")
def all_trades():
    pass