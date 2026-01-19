<script>
	import './layout.css';
	import favicon from '$lib/assets/favicon.svg';
	import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from "flowbite-svelte";
	import { scale } from "svelte/transition";
	import { onMount } from 'svelte';

	let { children } = $props();
	let turunbar = $state(true);


	//Kita masukin instruksi cari elemen (document.querySelector) ke onMount biar instruksinya 
	//dipegang dulu sampai elemen yang kita cari muncul semua dihalaman
	//Setelah elemennya muncul, baru kita bisa ngejalanin
	//Alternatifnya bisa buat file js baru yang dihubungin kesini dengan keterangan defer biar rendernya terakhir
	onMount(() => {
		const target = document.querySelector(".child");

		if (!target) return; //Buat mastiin aja si target ada. Biar nggak salah tembak

		const observer = new IntersectionObserver((entries) => {
			entries.forEach(entry => {
				turunbar = !entry.isIntersecting;
				/*if (!entry.isIntersecting) {
					console.log("86, Konten terlihat");
				} else {
					console.log("komandan, konten hilang!");
				}*/
			});
		}, {
			
			rootMargin: "-950px 0px 0px 0px", 
			threshold: 0
		})	
		observer.observe(target);
		return () => {
			observer.disconnect(); //fungsi pengawasannya dihentikan disini...kayaknya ya
		}
	});
</script>

<svelte:head><link rel="icon" href={favicon} /></svelte:head>

<div class="dalam">
	<div class="nav" class:scrolled={turunbar}>
		<h1 class="logo">AQFI</h1>
		<ul class="menu"  class:scrolled={turunbar}>
			<li class="home">Home</li>
			<li>Dev</li>
			<li>Daily</li>
			<li>About</li>
		</ul>
	</div>

	<Navbar>
	<NavBrand href="/">
		<span class="self-center text-xl font-semibold whitespace-nowrap dark:text-white">Flowbite</span>
	</NavBrand>
	<NavHamburger />
		<NavUl transition={scale} transitionParams={{ start: 0.8, duration: 200 }}>
			<NavLi href="/">Home</NavLi>
			<NavLi href="/about">About</NavLi>
			<NavLi href="/docs/components/navbar">Navbar</NavLi>
			<NavLi href="/pricing">Pricing</NavLi>
			<NavLi href="/contact">Contact</NavLi>
		</NavUl>
	</Navbar>
	<div class="child">
		{@render children()}
	</div>
</div>
