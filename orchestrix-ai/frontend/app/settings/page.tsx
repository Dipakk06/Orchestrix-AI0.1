import ParticlesBackground from '@/components/ParticlesBackground';
import Sidebar from '@/components/Sidebar';

export default function SettingsPage() {
  return (
    <main className="relative mx-auto grid min-h-screen max-w-7xl gap-4 p-4 lg:grid-cols-[260px,1fr]">
      <ParticlesBackground />
      <Sidebar />
      <section className="glass p-6">
        <h2 className="mb-3 text-xl font-semibold text-indigo-300">Settings</h2>
        <div className="grid gap-4 md:grid-cols-2">
          <div className="rounded-xl bg-slate-900/70 p-4">
            <p className="mb-1 text-sm text-slate-300">Default model</p>
            <p className="text-sm">gemma3 (Ollama)</p>
          </div>
          <div className="rounded-xl bg-slate-900/70 p-4">
            <p className="mb-1 text-sm text-slate-300">Voice engine</p>
            <p className="text-sm">Whisper + pyttsx3</p>
          </div>
        </div>
      </section>
    </main>
  );
}
