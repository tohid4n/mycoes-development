/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js}",
    "./src/**/forms.py",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {
      screens: {
        exsm: '360px',
        xsm: '470px',
        smMd: '570px'
      },
      width: {
        'r26': '26rem',
        'c43': '43%',
        'c45': '45%',
        'c28': '28%'
      },
      minHeight: {
        'h60': '60px'
      },
      fontFamily: {
        Karla: ['Karla', 'sans-serif'],
        WorkSans: [ 'Work Sans', 'sans-serif'],
        Montserrat: ['Montserrat', 'sans-serif'],
        LibreFranklin: ['Libre Franklin', 'sans-serif'],
        Nunito: ['Nunito', 'sans-serif'],
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ]
}

