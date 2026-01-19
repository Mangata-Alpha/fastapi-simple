from typing import Annotated
from fastapi import Depends, FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, create_engine, select, col, desc
from sqlalchemy.orm import selectinload
from contextlib import asynccontextmanager
import re

#Import file model
from models import Blog, BlogCreate, BlogPublic, BlogUpdate, Category, BlogCatLink

sqlite_file_name = "database_blog.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread" : False}
engine = create_engine(sqlite_url, connect_args=connect_args)

#Kita mulai buat db disini...
def buat_db_dan_tabel():
    from models import SQLModel
    SQLModel.metadata.create_all(engine)

#Disini buat sesi. Buat rekam perubahan aja
def ambil_sesi():
    with Session(engine) as sesi:
        yield sesi

SessionDep = Annotated[Session, Depends(ambil_sesi)]
#dia bakal nyatet perubahan database yang ada

@asynccontextmanager
async def lifespan(app:FastAPI):
    buat_db_dan_tabel()
    yield

app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost:5173",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/blog", response_model=BlogPublic) #response model buat sistem cuma ngambil field model yang perlu
def tambah_post(masuk: BlogCreate, session: SessionDep):
    #blog: Blog, ini parameter blog disuruh ngikut bentukannya class Blog
    db_post = Blog.model_validate(masuk)
    if not db_post.slug:
        new_slug = db_post.title.lower()
        db_post.slug = re.sub(r"[^a-z0-9\s]", "", new_slug).replace(" ", "-")
        #pakai re.sub untuk ganti karakter selain(tandanya ^) alpabet dan angka jadi hilang
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    if masuk.category_id:
        for cat in masuk.category_id:
            link = BlogCatLink(id_blog=db_post.id, id_cat=cat)
            session.add(link)
        session.commit()
    return db_post

@app.get("/blog", response_model=list[BlogPublic])
def baca_post(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
    ) -> list[Blog]: #ubah database blog menjadi list?
    blog = session.exec(
        select(Blog).options(selectinload(Blog.list_category))
        .offset(offset).limit(limit).order_by(desc(Blog.id))
        ).all() #langsung masuk segala
    #blog = session.exec(select(Blog).offset(offset).limit(limit).all())
    #Hati-hati, di line yang dikomen, ini bisa error karena akan menimbulkan proses yang nggak sabaran
    #Istilahnya kayak masih proses ambil beras udah suruh sajiin ke konsumen
    return blog

#Disini offset dan limit berfungsi sebagai paginasi
#Offset menandakan kita lompat berapa banyak data
#Kalau limit membatasi berapa banyak data yang muncul

@app.get("/blog/search")
def cari_post(cari:str, session:SessionDep):
    #pernyataan = select(Blog).where(Blog.title).contains(cari)
    pernyataan = select(Blog).where(col(Blog.title).ilike(f"%{cari}%"))

    hasil = session.exec(pernyataan).all() #eksekusi query sqlnya
    if not hasil:
        return{"message":"Yah nggak ada"}
    return hasil

@app.get("/blog/{id}", response_model=BlogPublic)
def baca_post_tunggal(id: int, session: SessionDep) -> Blog:
    #ini nyuruh sistem cari data dengan id(int) sekian, habis tu nyuruh SessionDep rekam
    blog = session.get(Blog, id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog Not Found")
    return blog

@app.delete("/blog/{id}", response_model=BlogPublic)
def hapus_post(id:int, session: SessionDep):
    blog = session.get(Blog, id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog Not Found")
    session.delete(blog)  #kalau ini kayaknya cuma ngomong kalau bakal dihapus?  
    session.commit() #ini baru pelaksanaannya
    return {"ok":True}

@app.patch("/blog/{id}", response_model=BlogPublic)
def edit_post(id:int, blog_update: BlogUpdate, session: SessionDep):
    blog = session.get(Blog, id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog Not Found")
    data_post = blog_update.model_dump(exclude_unset=True)
    #exclude_unset ngasi tau kalau misalkan nggak diubah, dia bakal dicuekin
    blog.sqlmodel_update(data_post)
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog

@app.get("/category") #response model buat sistem cuma ngambil field model yang perlu
def baca_cat(session: SessionDep) -> list[Category]:
    cat = session.exec(select(Category).order_by(desc(Category.id_cat))).all()
    return cat

@app.post("/category") #response model buat sistem cuma ngambil field model yang perlu
def tambah_cat(cat: Category, session: SessionDep):
    #blog: Blog, ini parameter blog disuruh ngikut bentukannya class Blog
    db_cat = Category.model_validate(cat)
    session.add(db_cat)
    session.commit()
    session.refresh(db_cat)
    return db_cat

@app.get("/")
async def Home():
    return{"pesan":"Hello World!"}