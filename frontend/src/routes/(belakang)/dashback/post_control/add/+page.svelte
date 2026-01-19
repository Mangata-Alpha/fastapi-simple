<script lang="ts">

    import { Modal, Label, Input, Button, ButtonGroup, Checkbox, Radio, Listgroup } from "flowbite-svelte";
    
    import { FormatButtonGroup, TextEditor, HeadingButtonGroup, ListButtonGroup, AlignmentButtonGroup, Divider, ToolbarRowWrapper } from "@flowbite-svelte-plugins/texteditor";
    import type { Editor } from "@tiptap/core";
    import { goto } from "$app/navigation";
    import { FileCirclePlusOutline, ExclamationCircleOutline } from "flowbite-svelte-icons";
    import { EditorState } from '@tiptap/pm/state'

    let showModal = $state(false);
    let modalMsg = $state("");

    let title = $state("")
    let editorInstance = $state<any>(null);
    let featured = $state(false)
    let status = $state(false)
    let list_category = ([])

    async function simpanPost() {
        if (!editorInstance || title == "") {
            alert("Kok kosong?")
            return
        }
        try {
            const kontenHtml = editorInstance.getHTML();
            
            const panggil = await fetch("http://localhost:8000/blog", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    title: title,
                    content: kontenHtml,
                    status: status,
                    featured: featured,
                    list_category: list_category
                })
            });

            if (panggil.ok) {
                const hubung = await panggil.json()
                modalMsg = "Hore! Postingan kamu sudah meluncur.";
                showModal = true;
            } else {
                const errorpost = await panggil.json()
                console.error(errorpost);
                alert("Gagal karena" + JSON.stringify(errorpost.detail))
            }
        } catch (err) {
            alert("Ada masalah sama server")
        }
    }

</script>

<Modal bind:open={showModal} size="xs" autoclose>
  <div class="text-center">
    <ExclamationCircleOutline class="mx-auto mb-4 text-gray-400 w-12 h-12" />
    <h3 class="mb-5 text-lg font-normal text-gray-500">{modalMsg}</h3>
    <Button color="blue" onclick={() => goto('/dashback/post_control')}>Sip!</Button>
  </div>
</Modal>

<h1 class="text-4xl font-semibold mx-4 mt-8">Tambah Postingan</h1>

<div class="m-4 p-8">
  <Label class="mb-2" for="input-addon-md">Judul</Label>
  <ButtonGroup class="w-full">
    <Input id="input-addon-md" type="text" placeholder="Judul" bind:value={title} />
  </ButtonGroup>
  <Label class="my-2">Konten</Label>
  <TextEditor bind:editor={editorInstance} contentprops={{ id: "formats-ex" }}>
    <ToolbarRowWrapper>
        <FormatButtonGroup editor={editorInstance} />
        <Divider />
        <HeadingButtonGroup editor={editorInstance} />
        <Divider />
        <ListButtonGroup editor={editorInstance} />
        <Divider />
        <AlignmentButtonGroup editor={editorInstance} />
        <Divider />
    </ToolbarRowWrapper>
</TextEditor>
</div>


<div class="m-4 p-8">
    <Label class="mb-2">Misc</Label>
    <Checkbox bind:checked={featured} >Featured?</Checkbox>
    
    <Label class="mb-2">Status</Label>
    <Radio name="status" bind:group={status} value={false}>Draft</Radio>
    <Radio name="status" bind:group={status} value={true}>Publish</Radio>

    <div class="overflow-y-auto h-[100px]">
        <p class="mb-4 font-semibold text-gray-900 dark:text-white">Category</p>
        <Listgroup class="w-48">
            {#each data.post}
            <li><Checkbox classes={{ div: "p-3" }}>svelte</Checkbox></li>
            {/each}
        </Listgroup>
    </div>

    <Button color="blue" class="w-full my-4" onclick={simpanPost}>
        <FileCirclePlusOutline class="shrink-0 h-6 w-6 pr-2" />
        Kirim
    </Button>
</div>
