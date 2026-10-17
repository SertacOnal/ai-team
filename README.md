# AI Team — Generic Agent Framework

Karpathy-inspired coding principles ve reusable agent templates. Bu repo **proje-specific agent tanımlamaz**, sadece generic tanımlar ve ilkeler içerir.

## Felsefe

Bu framework Andrej Karpathy'nin kodlama disiplininden esinlenmiştir:
- **Düşün, sonra kodla**: Önce analiz, sonra implementasyon
- **Basitlik**: Mevcut konvansiyonlarla çöz, gereksiz soyutlamalardan kaçın
- **Cerrahi değişiklik**: Sadece ilgili dosyalara dokun
- **Hedefe odaklan**: Gözlemlenebilir başarı kriterleri belirle

Kaynak: [Karpathy Skills](https://github.com/multica-ai/andrej-karpathy-skills)

## Yapı

```
ai-team/
├── principles.md           # Temel kodlama ilkeleri
├── opencode/               # OpenCode generic agent templates
│   ├── opencode.jsonc      # Base configuration
│   └── agents/             # Reusable agent definitions
├── templates/              # Project templates
│   ├── handoff.md          # Session handoff template
│   └── project.json        # Project config template
├── workflows/              # Workflow documentation
└── scripts/                # Utility scripts
```

## Kullanım

### Yeni Projeye Kurulum

1. Projenin root'una `.opencode/` klasörü oluştur
2. `ai-team/opencode/` içeriğini kopyala veya referans al
3. Proje-specific agentları `.opencode/agents/` altına ekle
4. `AGENTS.md` dosyasını projeye uyarla

### OpenCode Hierarchy

```
~/.config/opencode/         # Global user config
ai-team/opencode/           # Generic templates (reference)
your-project/.opencode/     # Project-specific overrides
```

OpenCode, parent'tan child'a doğru merge eder. Generic tanımlar üzerine proje-specific tanımlar eklenir.

## Generic Agents

| Agent | Mode | Açıklama |
|-------|------|----------|
| `coordinator` | primary | Proje koordinasyonu ve delegasyon |
| `developer` | all | Generic yazılım geliştirme |
| `qa` | subagent | Bağımsız test ve review |
| `designer` | subagent | UX/UI tasarım (opsiyonel) |

## Templates

### `templates/handoff.md`
Session devir teslimi için standart format. Branch, commit, yapılan değişiklikler, test sonuçları ve sonraki adımlar.

### `templates/project.json`
Proje komutları ve ortam tanımları. Setup, start, test komutlarını projeye göre özelleştir.

## İlkeler Özeti

1. **Oku önce**: AGENTS.md, handoff.md, proje yapısını anla
2. **Plan yap**: Observable acceptance kriterleri belirle
3. **Delegasyon**: Uygun agentlara görev ver, tek dosya tek yazar
4. **Doğrula**: Test komutlarını çalıştır, evidence kaydet
5. **Devret**: Handoff dokümantasyonunu güncelle

## Kısıtlamalar

- Otomatik commit/push/deploy yok (user authorization gerekli)
- Credentials ve secrets çıktılara dahil edilmez
- Production veritabanı veya API kullanılmaz (synthetic fixtures)
- Coverage/assertion zayıflatılmaz

## Sürümleme

Framework güncellemeleri bilinçli olarak yapılır:
```bash
cd ai-team && git pull
# Değişiklikleri gözden geçir, projelere uygula
```

Proje-specific tanımlar her zaman proje reposunda kalır ve framework güncellemelerinden etkilenmez.
