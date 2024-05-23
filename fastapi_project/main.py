from fastapi import FastAPI , status , Depends , HTTPException
from sqlalchemy.orm import Session
from typing import List
import schemas , models , db_connection
import uvicorn


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
    return {f"trade registration succesfull for userid :  {db_trade.user_id} "}


@app.get("/all-trades" , status_code=status.HTTP_200_OK , response_model= List[schemas.Trade])
def all_trades(db : Session = Depends(get_db)):
    trade = db.query(models.Trade).all()
    return trade


@app.get("/trade/{trade_id}" , status_code=status.HTTP_202_ACCEPTED)
def user_id_trades(trade_id : int , db : Session = Depends(get_db)):
    trade = db.query(models.Trade).filter(models.Trade.trade_id == trade_id).first()
    if not trade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"{trade_id} mentioned does not exist")
    return trade


@app.put("/trade/{trade_id}" , status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
def update_trade(trade_id : int):
    raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED , detail= "update operations are not allowed")


@app.delete("/trade/{trade_id}" , status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
def update_trade(trade_id : int):
    raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED , detail= "delete operations are not allowed")







if __name__ == "__main__":
    uvicorn.run("main:app" , host = "0.0.0.0" , port=8000 , reload=True)