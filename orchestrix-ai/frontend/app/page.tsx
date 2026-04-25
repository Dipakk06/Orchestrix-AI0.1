import AgentStatus from '@/components/AgentStatus';
import MemoryViewer from '@/components/MemoryViewer';
import ParticlesBackground from '@/components/ParticlesBackground';
import Sidebar from '@/components/Sidebar';
import ToolLogs from '@/components/ToolLogs';
import VoiceControls from '@/components/VoiceControls';

export default function DashboardPage() {
  return (
    <main className="relative mx-auto grid min-h-screen max-w-7xl gap-4 p-4 lg:grid-cols-[260px,1fr]">
      <ParticlesBackground />
      <Sidebar />
      <section className="grid gap-4 lg:grid-cols-2">
        <AgentStatus />
        <ToolLogs />
        <MemoryViewer />
        <VoiceControls />
      </section>
    </main>
  );
}
