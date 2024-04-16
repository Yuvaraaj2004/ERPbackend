from fastapi import Depends, FastAPI
import Models as MDL
import Schemas as SCH
import DataBase as DB
import uvicorn

app = FastAPI()
DB.Base.metadata.create_all(DB.engine)


@app.get("/")
def root():
    return {"value": 100}


@app.post("/AddMark")
def AddMark(data: SCH.AddMark, db=Depends(DB.get_db)):
    print(data.model_dump())
    try:
        f = MDL.Mark(**data.model_dump())
        db.add(f)
        db.commit()
        return {"Status": "Success"}
    except Exception as e:
        print(e)


@app.post("/CreateUser")
def CreateUser(data: SCH.UserCreateIN, db=Depends(DB.get_db)):
    print(data.model_dump())
    try:
        f = MDL.User(**data.model_dump())
        db.add(f)
        db.commit()
        f = db.query(MDL.User).filter(MDL.User.email == data.email).first()
        print(f.id, f.email)
        if data.user_type == 0:
            db.add(MDL.Student(register_number=data.register_number, user_id=f.id))
        elif data.user_type == 1:
            db.add(MDL.Faculty(user_id=f.id))
        db.commit()
    except Exception as e:
        print(e)
    return {'Status': 'Success'}


@app.post("/AddSubject")
def AddSubject(data: SCH.AddSubject, db=Depends(DB.get_db)):
    print(data.model_dump())
    try:
        f = MDL.Subjects(**data.model_dump())
        db.add(f)
        db.commit()
    except Exception as e:
        print(e)
    return {'Status': 'Success'}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
