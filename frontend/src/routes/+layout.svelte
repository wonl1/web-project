<script>
  import "../app.pcss";
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  import { FontAwesomeIcon } from '@fortawesome/svelte-fontawesome';
  import { faCamera } from '@fortawesome/free-solid-svg-icons';
  import { Footer, FooterCopyright, FooterLinkGroup, FooterLink } from 'flowbite-svelte';
</script>

<div class="flex flex-col min-h-screen">
  <Navbar class="bg-darkblue-600 rounded-t-lg">
    <NavBrand href="/">
      <FontAwesomeIcon icon={faCamera} size="2x" style="margin-right: 8px;" class="text-lightyellow-100" /> 
      <span class="self-center whitespace-nowrap text-xl font-semibold text-lightyellow-100">Travel Sharing</span>
    </NavBrand>
    <NavHamburger class="text-lightyellow-100 hover:bg-darkblue-600"/>
    <NavUl>
      <NavLi href="/" class="text-lightyellow-100 bg-darkblue-600 hover:bg-darkblue-500">Home</NavLi>
      <NavLi href="/category" class="text-lightyellow-100 bg-darkblue-600 hover:bg-darkblue-500">Category</NavLi>
      <NavLi href="/event" class="text-lightyellow-100 bg-darkblue-600 hover:bg-darkblue-500">Event</NavLi>
    </NavUl>
  </Navbar>
  <div class="px-2 sm:px-4 flex-grow">
    <div class="container mx-auto">
      <slot></slot>
    </div>
  </div>

  <Footer footerType="logo" class="bg-darkblue-600 text-gray-400 rounded-t-none">
    <div class="sm:flex sm:items-center sm:justify-between px-20 py-2">
      <div class="flex items-center justify-center"> 
        <FontAwesomeIcon icon={faCamera} size="2x" style="margin-right: 8px;" /> 
        <span class="self-center whitespace-nowrap text-xl font-semibold text-gray-400">Travel Sharing</span>
      </div>
      <FooterLinkGroup ulClass="flex flex-wrap items-center justify-center mb-6 text-sm text-gray-400 sm:mb-0 dark:text-gray-400">
        <FooterLink href="/">About</FooterLink>
        <FooterLink href="/">Privacy Policy</FooterLink>
        <FooterLink href="/">Licensing</FooterLink>
        <FooterLink href="/">Contact</FooterLink>
      </FooterLinkGroup>
    </div>
    <hr class="my-6 border-gray-400 sm:mx-auto dark:border-gray-400 lg:my-8" />
    <div class="text-center"> 
      <FooterCopyright href="/" by="Travel Sharing™" class="text-gray-400"/>
    </div>
  </Footer>
</div>
