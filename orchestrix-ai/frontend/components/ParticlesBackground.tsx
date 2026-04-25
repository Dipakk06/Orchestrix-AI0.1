'use client';

import { motion } from 'framer-motion';

interface Particle {
  id: number;
  x: string;
  y: string;
  size: number;
  duration: number;
}

const seededFloat = (seed: number, min = 0, max = 1) => {
  const x = Math.sin(seed * 9999) * 10000;
  const fraction = x - Math.floor(x);
  return min + fraction * (max - min);
};

const particles: Particle[] = Array.from({ length: 24 }, (_, i) => ({
  id: i,
  x: `${seededFloat(i + 1, 0, 100).toFixed(2)}%`,
  y: `${seededFloat(i + 101, 0, 100).toFixed(2)}%`,
  size: Number(seededFloat(i + 201, 2, 6).toFixed(2)),
  duration: Number(seededFloat(i + 301, 6, 12).toFixed(2))
}));

export default function ParticlesBackground() {
  return (
    <div className="pointer-events-none fixed inset-0 -z-10 overflow-hidden">
      {particles.map((p) => (
        <motion.span
          key={p.id}
          className="absolute rounded-full bg-indigo-300/40"
          style={{ left: p.x, top: p.y, width: p.size, height: p.size }}
          animate={{ y: [0, -16, 0], opacity: [0.2, 0.8, 0.2] }}
          transition={{ duration: p.duration, repeat: Infinity, ease: 'easeInOut' }}
        />
      ))}
    </div>
  );
}
