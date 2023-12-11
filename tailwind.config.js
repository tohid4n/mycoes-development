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
        smMd: '570px',
        biMd: '880px',
      },
      width: {
        'r26': '26rem',
        'c43': '43%',
        'c45': '45%',
        'c28': '28%',
        'w-500': '500px',
      },
      minHeight: {
        'h60': '60px'
      },
      borderWidth: {
        DEFAULT: '1px',
        '0': '0',
        '0.9': '0.9px',
      },
      lineHeight: {
        '90': '3', // You can adjust the value as needed
      },
      fontFamily: {
        Montserrat: ['Montserrat', 'sans-serif'],
        Poppins: ['Poppins', 'sans-serif'],

        Carme: ['Carme', 'sans-serif'],
        Content: [ 'Content', 'sans-serif'],
        Inter: ['Inter', 'sans-serif'],
        Lato: ['Lato', 'sans-serif'],
        Lexend: ['Lexend', 'sans-serif'],
        OpenSans: ['OpenSans', 'sans-serif'],
        Roboto: [ 'Roboto', 'sans-serif'],
        Sintony: [ 'Sintony', 'sans-serif'],
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ]
}


