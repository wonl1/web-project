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
          100: '#FFFFE0',  // very light yellow
        },
      }
    }
  }
};

module.exports = config;
