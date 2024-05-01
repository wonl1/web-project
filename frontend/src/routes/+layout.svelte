<script>
    import "../app.pcss";
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
   </script>
   <Navbar let:NavContainer color="primary">
    <NavContainer class="border px-5 py-2 rounded-lg bg-white dark:bg-gray-600">
      <NavBrand href="/">
        <img src="/images/flowbite-svelte-icon-logo.svg" class="me-3 h-6 sm:h-9" alt="Flowbite Logo" />
        <span class="self-center whitespace-nowrap text-xl font-semibold">Flowbite</span>
      </NavBrand>
      <NavHamburger />
      <NavUl>
        <NavLi href="/">Home</NavLi>
        <NavLi href="/about">지역</NavLi>
        <NavLi href="/docs/components/navbar">계절</NavLi>
        <NavLi href="/pricing">테마</NavLi>
        <NavLi href="/contact">이벤트</NavLi>
      </NavUl>
    </NavContainer>
  </Navbar>
   <div class="px-2 sm:px-4"><div class="container mx-auto">
   <slot></slot>
   </div></div>