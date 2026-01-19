import type { Postingan } from '$lib/interface'
import { request } from 'node:http';
import type { PageServerLoad, Actions } from "./$types";
import { fail } from '@sveltejs/kit';


export const load: PageServerLoad = async ({fetch}) => { //Kita tentuin async ini mau buat apaan. Kalau sini sih buat ambil
    const ambil = await fetch("http://localhost:8000/blog");

    const post: Postingan[] = await ambil.json();

    return { post };
};

export const actions = {
    hapus: async ({request}) => {
        const data = await request.formData();
        const ambilId = data.get('id');

        if (!ambilId) {
            return fail(400, {message:"Id missing"})
        }

        try {
            const panggil = await fetch(`http://localhost:8000/blog/${ambilId}`, {
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
} satisfies Actions;
