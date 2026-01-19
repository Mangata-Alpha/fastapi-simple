<script lang="ts">
	import './lay_bel.css';
	import {
		Sidebar, SidebarGroup, SidebarItem, 
		SidebarButton, uiHelpers, NavBrand, Navbar,
		Breadcrumb, BreadcrumbItem
	} from "flowbite-svelte";
	import { HomeSolid, NewspaperSolid, GridSolid, UserSolid, ChevronDoubleRightOutline } from "flowbite-svelte-icons";
	import { page } from "$app/state";

	let link = $derived(
		page.url.pathname
		.split("/") //Hasilnya jadi ["", "path1", "path 2", ""]
		.filter((pecahan) => pecahan !== "") //ambil semua array kecuali yang kosong
	);

	let activeUrl = $derived(page.url.pathname);
	const spanClass = "flex-1 ms-3 whitespace-nowrap";
	const sideBar = uiHelpers();
	let isDemoOpen = $state(false);
	const closeDemoSidebar = sideBar.close;

	const menuSide = [
		{ 
			label: 'Dashboard',
			href: '/dashback',
			icon: HomeSolid
		},
		{
			label: 'Postingan',
			href: '/dashback/post_control',
			icon: NewspaperSolid
		},
		{
			label: 'Kategori',
			href: '/dashback/category',
			icon: GridSolid
		},
	]

  $effect(() => {
    isDemoOpen = sideBar.isOpen;
    activeUrl = page.url.pathname;
  });

  let { children } = $props();

</script>

<Navbar class="bg-stone-700">
  <NavBrand href="/">
				<span class="mb-4 text-5xl font-semibold text-white">AQFI</span>
  </NavBrand>
  

	<SidebarButton onclick={sideBar.toggle} class="mb-2" />
</Navbar>
<div class="relative">
	<Sidebar
		{activeUrl}
		backdrop={false}
		isOpen={isDemoOpen}
		closeSidebar={closeDemoSidebar}
		params={{ x: -50, duration: 50 }}
		class="z-50 h-screen bg-stone-600! text-white!"
		position="absolute"
		classes={{ nonactive: "p-2", active: "p-2", div: "bg-stone-600! h-full border-none"}}
	>
		<SidebarGroup>

			{#each menuSide as menu}
				<SidebarItem
				activeClass="flex items-center p-2 text-base font-normal text-white bg-stone-500! rounded-lg"
				nonActiveClass="flex items-center p-2 text-base font-normal text-stone-200 hover:bg-stone-500! rounded-lg" 
				label={menu.label} href={menu.href}>
				{#snippet icon()}
					<menu.icon class="h-5 w-5 text-white transition duration-75 group-hover:text-gray-900" />
				{/snippet}
				</SidebarItem>
			{/each}
			<SidebarItem activeClass="flex items-center p-2 text-base font-normal text-white bg-stone-500! rounded-lg"
			nonActiveClass="flex items-center p-2 text-base font-normal text-stone-200 hover:bg-stone-500! rounded-lg" label="Sidebar" href="/components/sidebar">
			{#snippet icon()}
				<UserSolid class="h-5 w-5 text-white transition duration-75 group-hover:text-gray-900" />
			{/snippet}
			</SidebarItem>
		</SidebarGroup>
	</Sidebar>
	<section class="overflow-y-auto px-4 md:ml-64 max-h-[100dvh]">
		<Breadcrumb aria-label="Solid background breadcrumb example" class="bg-gray-50 px-5 py-3 dark:bg-gray-900">
			<BreadcrumbItem href="/" home>
				{#snippet icon()}
				<HomeSolid class="me-2 h-4 w-4" />
				{/snippet}Home
			</BreadcrumbItem>
			{#each link as b, i}
			{@const href = '/' + link.slice(0, i + 1).join('/')}
			<BreadcrumbItem {href}>
				{#snippet icon()}
				<ChevronDoubleRightOutline class="mx-2 h-5 w-5 dark:text-white" />
				{/snippet}
				{b}
			</BreadcrumbItem>
			{/each}
		</Breadcrumb>
		<div class="bg-white">
			{@render children()}
		</div>
	</section>
</div>
