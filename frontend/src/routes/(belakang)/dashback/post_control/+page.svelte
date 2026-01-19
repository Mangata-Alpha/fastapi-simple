<script lang="ts">

    import {
    Table, TableBody, 
    TableBodyCell, TableBodyRow, 
    TableHead, TableHeadCell, Badge, Button
    } from "flowbite-svelte";

    import { CirclePlusSolid, PenSolid, TrashBinSolid, CheckCircleSolid, ArchiveSolid, ThumbsUpSolid } from "flowbite-svelte-icons";

    import type { PageData } from './$types';
	import { page } from "$app/state";
    let { data }: { data: PageData } = $props();

</script>

<div class="p-10">

    <div class="tabel">
        <Table hoverable={true} striped={true}>
            <caption class="bg-white p-5 text-left text-xl font-semibold text-gray-900">
                <PenSolid class="shrink-0 h-10 w-10" />  
                Postingan
                <p class="mt-1 mb-5 text-sm font-normal text-gray-500 dark:text-gray-400">
                Ini tempat buat ngatur postingannya
                </p>
            
                <Button color="dark" size="lg" pill href="{page.url.pathname}/add">
                    <CirclePlusSolid class="shrink-0 h-6 w-6 mr-1" />    
                    Tambah
                </Button>
            </caption>
            <TableHead>
                <TableHeadCell>Judul</TableHeadCell>
                <TableHeadCell>Tanggal Buat</TableHeadCell>
                <TableHeadCell>Status</TableHeadCell>
                <TableHeadCell>Featured?</TableHeadCell>
                <TableHeadCell>Kategori</TableHeadCell>
                <TableHeadCell>Aksi</TableHeadCell>
            </TableHead>
            <TableBody>
                {#if data.post == null}
                    <TableBodyRow>
                        <h1 class="text-5xl">Yah Kosong</h1>
                    </TableBodyRow>
                {:else}
                    {#each data.post as p}
                    <TableBodyRow>
                        <TableBodyCell>{p.title}</TableBodyCell>
                        <TableBodyCell>{new Date(p.created_date).toLocaleDateString('id-ID')}</TableBodyCell>
                        <TableBodyCell>
                            {#if p.status}
                                <Badge rounded large color="green"> <CheckCircleSolid class="shrink-0 h-6 w-6 mr-1" /> Publish!</Badge>
                            {:else}
                                <Badge rounded large color="yellow"><ArchiveSolid class="shrink-0 h-6 w-6 mr-1" /> Draf</Badge>
                            {/if}
                        </TableBodyCell>
                        <TableBodyCell>
                            {#if p.featured}
                                <Badge rounded large color="purple"><ThumbsUpSolid class="shrink-0 h-6 w-6 mr-1" /> Yap</Badge>
                            {:else}
                                <Badge rounded large color="gray">Nggak si</Badge>
                            {/if}
                        </TableBodyCell>
                        <TableBodyCell>
                            <div class="flex gap-2">
                                {#each p.list_category as cat}
                                    <Badge rounded large color="purple">{cat.name}</Badge>
                                {:else}
                                    <span class="text-gray-400 text-xs italic">Tanpa Kategori</span>
                                {/each}
                            </div>
                        </TableBodyCell>
                        <TableBodyCell class="flex gap-2">
                            <Button color="blue" size="lg" pill href="/dashback/post_control/edit/{p.id}">
                                <PenSolid class="shrink-0 h-6 w-6" />    
                                Edit
                            </Button>
                            <form method="POST" action="?/hapus">
                                <input type="hidden" name="id" value={p.id} />
                                <Button type=submit color="red" size="lg" pill  value={p.id}>
                                    <TrashBinSolid class="shrink-0 h-6 w-6" />   
                                        Hapus
                                </Button>
                            </form>
                        </TableBodyCell>
                    </TableBodyRow>
                    {/each}
                {/if}
            </TableBody>
        </Table>
    </div>
</div>