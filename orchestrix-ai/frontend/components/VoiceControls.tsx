'use client';

import { useState } from 'react';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || 'http://localhost:8000';

export default function VoiceControls() {
  const [text, setText] = useState('');

  const playTTS = async () => {
    const response = await fetch(`${API_BASE}/api/voice/tts/file`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: text || 'Hello from Orchestrix AI' })
    });

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const audio = new Audio(url);
    audio.play();
  };

  return (
    <div className="glass p-4">
      <h3 className="mb-2 text-sm font-semibold text-indigo-300">Voice Assistant</h3>
      <input
        className="mb-2 w-full rounded-lg border border-indigo-400/30 bg-slate-900/70 px-3 py-2 text-sm"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type text to synthesize voice"
      />
      <button className="rounded-lg bg-indigo-500/70 px-3 py-2 text-sm" onClick={playTTS}>
        ▶ Play Voice
      </button>
    </div>
  );
}
