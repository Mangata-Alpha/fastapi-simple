import type { Category } from '$lib/interface'
import type { PageServerLoad, Actions } from "./$types";
import { fail } from '@sveltejs/kit';


export const load: PageServerLoad = async ({fetch}) => { //Kita tentuin async ini mau buat apaan. Kalau sini sih buat ambil
    const ambil = await fetch("http://localhost:8000/category");

    const category: Category[] = await ambil.json();

    return { category };
};

/*export const actions = {
    hapus: async ({request}) => {
        const data = await request.formData();
        const ambilId = data.get('id');

        if (!ambilId) {
            return fail(400, {message:"Id missing"})
        }

        try {
            const panggil = await fetch(`http://localhost:8000/category/${ambilId}`, {
                method: 'DELETE',
            });
            if (panggil.ok) {
                return {success: true}
            } else {
                return fail(500, {message: "Gagal hapus"})
            }
        } catch (err) {
            return fail(500, { message: 'Koneksi ke server putus' });
        }
    }
} satisfies Actions; */
