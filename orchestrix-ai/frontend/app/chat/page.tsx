import ChatPanel from '@/components/ChatPanel';
import ParticlesBackground from '@/components/ParticlesBackground';
import Sidebar from '@/components/Sidebar';

export default function ChatPage() {
  return (
    <main className="relative mx-auto grid min-h-screen max-w-7xl gap-4 p-4 lg:grid-cols-[260px,1fr]">
      <ParticlesBackground />
      <Sidebar />
      <ChatPanel />
    </main>
  );
}
