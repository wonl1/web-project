<script>
  import "../app.pcss";
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';
  import { faCamera } from '@fortawesome/free-solid-svg-icons';
  import { Footer, FooterCopyright, FooterLinkGroup, FooterBrand, FooterLink } from 'flowbite-svelte';
</script>

<div class="flex flex-col min-h-screen">
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
  <div class="px-2 sm:px-4 flex-grow">
    <div class="container mx-auto">
      <slot></slot>
    </div>
  </div>

  <Footer footerType="logo" class="bg-blue-50 text-gray-500">
    <div class="sm:flex sm:items-center sm:justify-between px-20 py-2">
      <div class="flex items-center justify-center"> <!-- 수정된 부분: justify-center -->
        <FontAwesomeIcon icon={faCamera} size="2x" style="margin-right: 8px;" /> 
        <span class="self-center whitespace-nowrap text-xl font-semibold">Travel Sharing</span>
      </div>
      <FooterLinkGroup ulClass="flex flex-wrap items-center justify-center mb-6 text-sm text-gray-500 sm:mb-0 dark:text-gray-400"> <!-- 수정된 부분: justify-center -->
        <FooterLink href="/">About</FooterLink>
        <FooterLink href="/">Privacy Policy</FooterLink>
        <FooterLink href="/">Licensing</FooterLink>
        <FooterLink href="/">Contact</FooterLink>
      </FooterLinkGroup>
    </div>
    <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
    <div class="text-center"> 
      <FooterCopyright href="/" by="Travel Sharing™" />
    </div>
  </Footer>
</div>