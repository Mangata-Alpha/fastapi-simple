<script lang="ts">
  import { 
        Table, 
        TableBody, 
        TableBodyCell, 
        TableBodyRow, 
        TableHead, 
        TableHeadCell,
    } from "flowbite-svelte";

    interface View {
        id: number,
        nama: string,
        kalimat: string,
        tanggal: string,
    }

    let tampilHasil = $state<View[]>([]);

    async function ViewJson() {
        try {
            const res = await fetch("http://localhost:8000/data");

            const data = await res.json(); //ubah data yang didapet jadi json

            tampilHasil = data;

            return data;
        } catch {
            console.log("Gagal", Error)
        }
    }

    $effect( () => {
        ViewJson().then( data => {
            console.log(data);
        });
    });
</script>

<div class="p-8">
    <Table>
        <TableHead>
            <TableHeadCell>ID</TableHeadCell>
            <TableHeadCell>Nama</TableHeadCell>
            <TableHeadCell>Kalimat</TableHeadCell>
            <TableHeadCell>Tanggal</TableHeadCell>
        </TableHead>
        <TableBody>
            {#each tampilHasil as tampil}
            <TableBodyRow>
                <TableBodyCell>{tampil.id}</TableBodyCell>
                <TableBodyCell>{tampil.nama}</TableBodyCell>
                <TableBodyCell>{tampil.kalimat}</TableBodyCell>
                <TableBodyCell>{tampil.tanggal}</TableBodyCell>
            </TableBodyRow>
            {/each}
            <TableBodyRow>
                <TableBodyCell>Microsoft Surface Pro</TableBodyCell>
                <TableBodyCell>White</TableBodyCell>
                <TableBodyCell>Laptop PC</TableBodyCell>
                <TableBodyCell>$1999</TableBodyCell>
            </TableBodyRow>
            <TableBodyRow>
                <TableBodyCell>Magic Mouse 2</TableBodyCell>
                <TableBodyCell>Black</TableBodyCell>
                <TableBodyCell>Accessories</TableBodyCell>
                <TableBodyCell>$99</TableBodyCell>
            </TableBodyRow>
            <TableBodyRow class="try">
                <TableBodyCell>Apple MacBook Pro 17"</TableBodyCell>
                <TableBodyCell>Silver</TableBodyCell>
                <TableBodyCell>Laptop</TableBodyCell>
                <TableBodyCell>$2999</TableBodyCell>
            </TableBodyRow>
            <TableBodyRow>
                <TableBodyCell>Microsoft Surface Pro</TableBodyCell>
                <TableBodyCell>White</TableBodyCell>
                <TableBodyCell>Laptop PC</TableBodyCell>
                <TableBodyCell>$1999</TableBodyCell>
            </TableBodyRow>
            <TableBodyRow>
                <TableBodyCell>Magic Mouse 2</TableBodyCell>
                <TableBodyCell>Black</TableBodyCell>
                <TableBodyCell>Accessories</TableBodyCell>
                <TableBodyCell>$99</TableBodyCell>
            </TableBodyRow>
        </TableBody>
    </Table>
    
    

</div>