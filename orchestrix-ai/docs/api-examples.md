# Orchestrix AI API Examples

## Chat
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"user_id":"demo","message":"Plan my week","stream":false,"history":[]}'
```

## Agent Run
```bash
curl -X POST http://localhost:8000/api/agent/run \
  -H "Content-Type: application/json" \
  -d '{"user_id":"demo","objective":"Research local AI meetups"}'
```

## Save Memory
```bash
curl -X POST http://localhost:8000/api/memory/save \
  -H "Content-Type: application/json" \
  -d '{"user_id":"demo","text":"User likes concise answers","metadata":{"type":"preference"}}'
```

## Search Memory
```bash
curl "http://localhost:8000/api/memory/search?query=concise&limit=5"
```
