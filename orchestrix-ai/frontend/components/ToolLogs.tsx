'use client';

const sampleLogs = [
  'calculator(expression="2+2") -> 4',
  'web_search(query="langgraph roadmap") -> placeholder',
  'memory.save(user_fact) -> success'
];

export default function ToolLogs() {
  return (
    <div className="glass p-4">
      <h3 className="mb-2 text-sm font-semibold text-indigo-300">Tool Execution Logs</h3>
      <div className="space-y-2 text-xs text-slate-300">
        {sampleLogs.map((log) => (
          <p key={log} className="rounded-lg bg-slate-900/70 p-2 font-mono">
            {log}
          </p>
        ))}
      </div>
    </div>
  );
}
