'use client';

import { FormEvent, useState } from 'react';
import ReactMarkdown from 'react-markdown';

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000';

export default function ChatPanel() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    if (!input.trim() || loading) return;

    const userMessage: Message = { role: 'user', content: input.trim() };
    const nextHistory = [...messages, userMessage];

    setMessages(nextHistory);
    setInput('');
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(`${API_BASE}/api/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          user_id: 'demo-user',
          message: userMessage.content,
          stream: false,
          history: messages
        })
      });

      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }

      const data = await response.json();
      const assistantReply = data.response || 'No response.';
      setMessages((prev) => [...prev, { role: 'assistant', content: assistantReply }]);
    } catch (err) {
      const message =
        err instanceof Error
          ? `Could not reach Orchestrix API (${API_BASE}). ${err.message}`
          : `Could not reach Orchestrix API (${API_BASE}).`;

      setError(message);
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content:
            '⚠️ I could not connect to the backend API. Please make sure FastAPI is running and NEXT_PUBLIC_API_BASE is correct.'
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="glass flex h-[70vh] flex-col p-4">
      <div className="mb-3 flex-1 space-y-3 overflow-auto pr-1">
        {messages.map((m, idx) => (
          <div key={idx} className={`rounded-xl p-3 ${m.role === 'user' ? 'bg-indigo-500/20' : 'bg-slate-800/70'}`}>
            <p className="mb-1 text-xs uppercase text-indigo-300">{m.role}</p>
            <div className="prose prose-invert max-w-none text-sm">
              <ReactMarkdown>{m.content}</ReactMarkdown>
            </div>
          </div>
        ))}
      </div>

      {error ? (
        <p className="mb-2 rounded-lg border border-amber-400/40 bg-amber-500/10 px-3 py-2 text-xs text-amber-200">{error}</p>
      ) : null}

      <form onSubmit={handleSubmit} className="mt-auto flex gap-2">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 rounded-xl border border-indigo-400/30 bg-slate-900/70 px-4 py-2 text-sm outline-none focus:border-indigo-300"
          placeholder="Ask Orchestrix AI..."
        />
        <button
          disabled={loading}
          className="rounded-xl bg-gradient-to-r from-indigo-500 to-purple-500 px-4 py-2 text-sm font-medium disabled:opacity-60"
        >
          {loading ? 'Thinking...' : 'Send'}
        </button>
      </form>
    </section>
  );
}
