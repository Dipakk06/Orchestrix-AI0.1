'use client';

import { useEffect, useState } from 'react';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000';

export default function MemoryViewer() {
  const [items, setItems] = useState<Array<{ text: string }>>([]);

  useEffect(() => {
    fetch(`${API_BASE}/api/memory/search?query=demo&limit=5`)
      .then((r) => r.json())
      .then((d) => setItems(d.results || []))
      .catch(() => setItems([]));
  }, []);

  return (
    <div className="glass p-4">
      <h3 className="mb-2 text-sm font-semibold text-indigo-300">Memory Viewer</h3>
      <ul className="space-y-2 text-sm text-slate-200">
        {items.length ? (
          items.map((item, idx) => (
            <li key={idx} className="rounded-lg bg-slate-800/60 p-2">
              {item.text}
            </li>
          ))
        ) : (
          <li className="rounded-lg bg-slate-800/60 p-2 text-slate-400">No memory items loaded.</li>
        )}
      </ul>
    </div>
  );
}
