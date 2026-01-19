from sqlmodel import Field, SQLModel, Relationship
from datetime import timezone, datetime


class BlogCatLink(SQLModel, table=True):
    id_cat: int | None = Field(default=None, foreign_key="category.id_cat", primary_key=True)
    id_blog: int | None = Field(default=None, foreign_key="blog.id", primary_key=True)

class Category(SQLModel, table=True):
    id_cat: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    desc: str
    list_post: list["Blog"] = Relationship(back_populates="list_category", link_model=BlogCatLink) #Ngasi kunci password ke bagian post kalau pengen liat list

class BlogBase(SQLModel): #Yah..ini dasarnya. Hantuin tabel Blog dimana-mana
    
    title: str = Field(index=True)
    #image image
    content: str
    status: bool 
    featured: bool

class Blog(BlogBase, table=True): #Buat ngubunginnya. Sini ditaruh data yang nggak perlu diisi user. Soalnya dah otomatis
    id: int | None = Field(default=None, primary_key=True)
    slug: str = Field(default=None, index=True)
    created_date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    #Beda default_factory dan default biasa adalah kondisinya.
    #Default factory mulai untuk item tersebut diproses
    list_category: list["Category"] = Relationship(back_populates="list_post", link_model=BlogCatLink) #Ambil list dari tabel category dengan password list_post

class BlogPublic(BlogBase): #agar bisa diliat publik. Kalau kasus ini diliat svelte
    id: int
    slug: str
    created_date: datetime
    list_category: list["CategoryPublic"] = [] 

# Kamu juga butuh ini agar tidak error
class CategoryPublic(SQLModel):
    id_cat: int
    name: str
    desc: str

class BlogCreate(BlogBase): #disini nampilin base. User cuma bisa isi data baru dengan format field yang ada di base
    category_id: list[int] = []
    pass

class BlogUpdate(SQLModel):
    title: str | None = None
    slug: str | None = None
    content: str | None = None
    status: bool | None = None
    featured: bool | None = None