export const load = async ({ params }) => {
    const panggil = await fetch(`http://localhost:8000/blog/${params.id}`);

    const dataLama = await panggil.json();

    return { dataLama }
}