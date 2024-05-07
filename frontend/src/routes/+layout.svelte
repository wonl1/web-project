<script>
  import "../app.pcss";
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';
  import { faCamera } from '@fortawesome/free-solid-svg-icons';
</script>

<Navbar let:NavContainer color="blue">
  <NavContainer class="border px-5 py-2 rounded-lg bg-white dark:bg-gray-600">
    <NavBrand href="/">
      <FontAwesomeIcon icon={faCamera} size="2x" style="margin-right: 8px;" /> 
      <span class="self-center whitespace-nowrap text-xl font-semibold">Travel Sharing</span>
    </NavBrand>
    <NavHamburger />
    <NavUl>
      <NavLi href="/">Home</NavLi>
      <NavLi href="/지역">지역</NavLi>
      <NavLi href="/계절">계절</NavLi>
      <NavLi href="/테마">테마</NavLi>
      <NavLi href="/이벤트">이벤트</NavLi>
    </NavUl>
  </NavContainer>
</Navbar>
<div class="px-2 sm:px-4"><div class="container mx-auto">
<slot></slot>
   </div></div>