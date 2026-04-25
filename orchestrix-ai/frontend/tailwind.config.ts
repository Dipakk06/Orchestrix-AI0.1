import type { Config } from 'tailwindcss';

export default {
  content: ['./app/**/*.{ts,tsx}', './components/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        bg: '#060816',
        panel: 'rgba(20, 24, 44, 0.72)'
      },
      boxShadow: {
        glow: '0 0 0 1px rgba(99,102,241,.3), 0 10px 40px rgba(80,70,229,.25)'
      }
    }
  },
  plugins: []
} satisfies Config;
