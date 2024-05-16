const config = {
  content: ['./src/**/*.{html,js,svelte,ts}', './node_modules/flowbite-svelte/**/*.{html,js,svelte,ts}'],

  plugins: [require('flowbite/plugin')],

  darkMode: 'selector',

  theme: {
    extend: {
      colors: {
        darkblue: {
          50: '#e4e6ec',
          100: '#bcc2d4',
          200: '#9299b8',
          300: '#67709c',
          400: '#4a547c',
          500: '#1A2039',  // base color
          600: '#121832',
          700: '#0d122a',
          800: '#090c22',
          900: '#050617',
        },
        lightyellow: {
          50: '#FFFFF3',  // lighter yellow
          100: '#FFFFE0',  // very light yellow
          200: '#FFFFCC',  // light yellow
          300: '#FFFFB8',  // medium light yellow
          400: '#FFFFA3',  // yellow
          500: '#FFFF8F',  // medium yellow
          600: '#FFFF7A',  // dark yellow
          700: '#FFFF66',  // darker yellow
          800: '#FFFF52',  // very dark yellow
          900: '#FFFF3D',  // darkest yellow
        },
      }
    }
  }
};

module.exports = config;
