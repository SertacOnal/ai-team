# AI Team Framework

Karpathy-inspired coding principles ve generic OpenCode agent templates.

## İçerik

```
ai-team/
├── principles.md           # Temel kodlama ilkeleri
├── opencode/
│   ├── opencode.jsonc      # Base configuration
│   └── agents/             # Generic agent templates
│       ├── coordinator.md
│       ├── developer.md
│       ├── qa.md
│       └── designer.md
└── templates/
    ├── handoff.md          # Session devir teslim şablonu
    └── project.json        # Proje config şablonu
```

## Kullanım

### Proje referansı olarak
```jsonc
// your-project/.opencode/opencode.jsonc
{
  "instructions": ["../ai-team/principles.md"]
}
```

### Agent template olarak
```bash
cp -r ai-team/opencode/agents/ your-project/.opencode/agents/
# Proje-specific özelleştirmeler ekle
```

## Dört İlke

1. **Think Before Coding** — Analiz et, sonra kodla
2. **Simplicity First** — Mevcut konvansiyonlarla çöz
3. **Surgical Changes** — Sadece ilgili dosyalara dokun
4. **Goal-Driven** — Observable evidence ile doğrula

Detaylar için `principles.md` dosyasına bak.

## Referans

- [Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills)
- [OpenCode Docs](https://opencode.ai/v2/docs/)
