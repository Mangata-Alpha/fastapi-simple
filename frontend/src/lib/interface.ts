export interface Postingan {
    id: number,
    title: string,
    content: string,
    featured: boolean,
    status: boolean,
    created_date: string
    list_category: Category[]
}
export interface Category {
    id_cat: number,
    name: string,
    list_post: Postingan[]
}