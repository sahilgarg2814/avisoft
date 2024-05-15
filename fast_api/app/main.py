from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
import psycopg2
import schema
from random import randrange
from psycopg2.extras import RealDictCursor
import time
# pudantic is used to validate data that is sent into the database
import models
from database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app=FastAPI()



while True:
    try:
        conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='24412441',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connection was succesfull")
        break
    except Exception as error:
        print("Conection to database failed")
        print("Error: ",error)
        time.sleep(2)


my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},
          {"title":"favourite foods","content":"I like pizza","id":2}]

def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p
        
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i

#path operations
@app.get("/")
def root():
    return{"message":"Hello World"}  # python convert this dictionary into json

# --reload will automatically restart your server in case you change your code, no need to do it maually

# @app.get("/sqlalchemy")
# def test_posts(db:Session=Depends(get_db)):
#     posts=db.query(models.Post).all()
#     return {"data" : posts}


# @app.get("/posts")
# def get_posts():
#     cursor.execute(""" SELECT * FROM posts """)
#     posts=cursor.fetchall()
#     return {"data":posts}

@app.get("/posts")
def get_posts(db:Session=Depends(get_db)):
    posts=db.query(models.Post).all()
    return {"data" : posts}


# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     return {"message":"Succesfully created posts"}

# @app.post("/createposts")
# def create_posts(new_post : POST):
#     print(new_post.published)
#     print(new_post.rating)
#     return {"data":"new post"}

# @app.post("/posts",status_code=status.HTTP_201_CREATED)
# def create_posts(new_post : POST):
#     new_post_dict=new_post.dict()
#     new_post_dict['id']=randrange(0,1000000)
#     my_posts.append(new_post_dict)
#     return {"data":new_post_dict}

# @app.post("/posts",status_code=status.HTTP_201_CREATED)
# def create_posts(new_post : POST):
#     cursor.execute(""" INSERT INTO posts (title,content,published) values (%s, %s,%s) RETURNING * """,(new_post.title,new_post.content,new_post.published))
#     new_post=cursor.fetchone()
#     conn.commit()  # to save the changes in the database
#     return {"data":new_post}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(new_post : schema.PostCreate,db:Session=Depends(get_db),response_model=schema.Post):
    new_post=models.Post(title=new_post.title,content=new_post.content,published=new_post.published)
    # another method of doing the above thing in there are many columns in the table
    #new_post=models.Post(**new_post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data":new_post}


# @app.get("/posts/latest")
# def get_latest_post():
#     post=my_posts[len(my_posts)-1]
#     return {"detail":post}


# @app.get("/posts/{id}")
# def get_post(id:int,response:Response):
#     post=find_post(id)

#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with {id} not found")
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         # return {"message":f"Post with {id} not found"}
#     return {"post_detail":post}

# @app.get("/posts/{id}")
# def get_post(id:int):
#     cursor.execute(""" SELECT * from posts where id = %s """,(str(id)))
#     post=cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with {id} not found")
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         # return {"message":f"Post with {id} not found"}
#     return {"post_detail":post}

@app.get("/posts/{id}")
def get_post(id:int,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with {id} not found")
    return {"post_detail":post}



# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id :int):
#     index=find_index_post(id)

#     if index==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} does not exist")
#     my_posts.pop(index)
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id :int):
#     cursor.execute("""DELETE from posts WHERE id = %s returning * """,(str(id)))
#     deleted_post=cursor.fetchone()
#     conn.commit()

#     if deleted_post==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} does not exist")
    
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id :int,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id)


    if post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.put("/posts/{id}")
# def update_post(id: int,post: POST):
#     index=find_index_post(id)

#     if index==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} does not exist")
#     post_dict=post.dict()
#     post_dict['id']=id
#     my_posts[index]=post_dict
#     return {"message":"updated Post"}

# @app.put("/posts/{id}")
# def update_post(id: int,post: POST):
#     cursor.execute("""UPDATE posts set title = %s ,content = %s ,published=%s where id = %s returning *""",(post.title,post.content,post.published,str(id)))

#     updated_post=cursor.fetchone()
#     conn.commit()

#     if updated_post==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} does not exist")
    
#     return {"message":"updated Post"}

@app.put("/posts/{id}")
def update_post(id: int,post: schema.PostCreate,db:Session=Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id)


    if post.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    
    post.update({'title':'Hey this my updated title','content':'this is my updated title'},synchronize_session=False)
    db.commit()
    return {"message":"updated Post"}

