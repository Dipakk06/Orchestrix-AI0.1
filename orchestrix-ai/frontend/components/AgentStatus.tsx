'use client';

const steps = ['Planner', 'Researcher', 'Executor', 'Memory Agent', 'Responder'];

export default function AgentStatus() {
  return (
    <div className="glass p-4">
      <h3 className="mb-2 text-sm font-semibold text-indigo-300">Agent Status</h3>
      <ul className="space-y-2 text-sm text-slate-200">
        {steps.map((step, idx) => (
          <li key={step} className="flex items-center justify-between rounded-lg bg-slate-800/60 px-3 py-2">
            <span>{step}</span>
            <span className="text-xs text-emerald-300">Ready #{idx + 1}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
