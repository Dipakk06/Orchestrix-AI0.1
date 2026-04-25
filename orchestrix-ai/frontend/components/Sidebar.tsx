'use client';

import Link from 'next/link';
import { Bot, MemoryStick, Settings, TerminalSquare } from 'lucide-react';

const links = [
  { href: '/', label: 'Dashboard', icon: Bot },
  { href: '/chat', label: 'Chat', icon: TerminalSquare },
  { href: '/', label: 'Memory', icon: MemoryStick },
  { href: '/settings', label: 'Settings', icon: Settings }
];

export default function Sidebar() {
  return (
    <aside className="glass w-full p-4 lg:w-64">
      <h1 className="mb-6 text-xl font-semibold tracking-wide text-indigo-300">Orchestrix AI</h1>
      <nav className="space-y-2">
        {links.map(({ href, label, icon: Icon }) => (
          <Link
            key={label}
            href={href}
            className="flex items-center gap-2 rounded-xl px-3 py-2 text-sm text-slate-200 transition hover:bg-indigo-500/20"
          >
            <Icon size={16} />
            {label}
          </Link>
        ))}
      </nav>
    </aside>
  );
}
