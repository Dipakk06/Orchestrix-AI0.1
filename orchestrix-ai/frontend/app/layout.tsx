import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Orchestrix AI',
  description: 'Advanced AI assistant platform with tools, memory, and voice.'
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
