<script lang="ts">

    import {
    Table, TableBody, 
    TableBodyCell, TableBodyRow, 
    TableHead, TableHeadCell, Badge, Button
    } from "flowbite-svelte";

    import { CirclePlusSolid, PenSolid, TrashBinSolid, CheckCircleSolid, ArchiveSolid, ThumbsUpSolid, GridSolid } from "flowbite-svelte-icons";

    import type { PageData } from './$types';
	import { page } from "$app/state";
    let { data }: { data: PageData } = $props();

</script>

<div class="p-10">

    <div class="tabel">
        <Table hoverable={true} striped={true}>
            <caption class="bg-white p-5 text-left text-xl font-semibold text-gray-900">
                <GridSolid class="shrink-0 h-10 w-10" />  
                Kategori
                <p class="mt-1 mb-5 text-sm font-normal text-gray-500 dark:text-gray-400">
                Yang ini buat kategori
                </p>
            
                <Button color="dark" size="lg" pill href="{page.url.pathname}/add">
                    <CirclePlusSolid class="shrink-0 h-6 w-6 mr-1" />    
                    Tambah
                </Button>
            </caption>
            <TableHead>
                <TableHeadCell>No</TableHeadCell>
                <TableHeadCell>Nama</TableHeadCell>
                <TableHeadCell>Aksi</TableHeadCell>
            </TableHead>
            <TableBody>
                {#if data.category == null}
                    <TableBodyRow class="text-center p-10 col-span-3">
                        <h1 class="text-5xl">Yah Kosong</h1>
                    </TableBodyRow>
                {:else}
                    {#each data.category as c, i}
                    <TableBodyRow>
                        <TableBodyCell>{i+1}</TableBodyCell>
                        <TableBodyCell>{c.name}</TableBodyCell>
                        <TableBodyCell class="flex gap-2">
                            <Button color="blue" size="lg" pill href="/dashback/post_control/edit/{c.id_cat}">
                                <PenSolid class="shrink-0 h-6 w-6" />    
                                Edit
                            </Button>
                            <form method="POST" action="?/hapus">
                                <input type="hidden" name="id" value={c.id_cat} />
                                <Button type=submit color="red" size="lg" pill  value={c.id_cat}>
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