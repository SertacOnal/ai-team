# AI Team — shared framework

Ortak ilkeler ve teslim akışı. **Bu repo agent rolü tanımlamaz.** Karpathy-inspired
kodlama disiplini principles.md içinde; kaynağı ve uyarlama notu aynı dosyadadır.
Yeni bir model, knowledge base veya kendi kendini güncelleyen sistem değildir.

## Kullanım (Python 3.11+)

```sh
git clone git@github.com:SertacOnal/ai-team.git
cd ai-team
python3 scripts/team.py validate
python3 scripts/team.py install --target /absolute/path/to/project
python3 scripts/team.py install --target /absolute/path/to/project --apply
```

Installer `.ai-framework/principles.md` ve GitHub akışını projeye kopyalar;
AGENTS.md girişini ekler. `.ai/project.json` ve `.ai/handoff.md` yalnız yoksa
oluşturulur. Ortam şablonundaki echo komutları yer tutucudur, doğrulama değildir.
`.codex/agents/` içindeki Developer/QA/Designer tanımları **projenin kendi
sorumluluğudur**; installer bunları oluşturmaz veya güncellemez. Küçük yeni PoC
ayrı role ihtiyaç duymadan ana oturumda çalışabilir.

Ana oturum kapsam, planlama, entegrasyon ve kısa araştırmayı üstlenir. Gerektiğinde
proje Developer rolünü, bağımsız QA'yı ve isteğe bağlı Designer'ı görevlendirir.
Ortak ilkeleri rol dosyalarına kopyalamayın; `.ai-framework/principles.md` referansı
kullanın. Proje rolleri yalnız kendi uzmanlık ve kabul gereksinimlerini tanımlar.

## M4 ↔ M1

Kod, proje rolleri, .ai-framework kopyası ve handoff kaydı aynı proje branch'inde
commit/push edilir. Diğer makine temiz checkout'ta fetch ve pull --ff-only yapar
veya ayrı worktree açar; aynı branch'in diğer yazarı önce durur. Secret, ignored
veri, çalışan servis ve sohbet geçmişi Git ile taşınmaz. Ortamı .ai/project.json
göre yeniden kurun; kayıtları güncel kodla doğrulayın.

Codex'e: “AGENTS.md ve .ai/handoff.md dosyalarını oku; branch ve ortamı doğrulayıp
devam et” deyin. Kullanıcı yetkisi olmadan commit/push/deploy yapılmaz.

## Sürüm ve güncelleme

Ortak ilkeler projedeki sürümlenmiş kopyadan okunur; kardeş repo yolu varsayılmaz.
Framework güncellemesi bilinçli olarak git pull ve yeniden install ile yapılır,
sonra proje farkı gözden geçirilip commit edilir. Yerel değişiklikle çatışırsa
installer durur. Önceki sürümün sahip olduğu team_* rolleri yalnız kayıtlı hash ile
aynıysa kaldırılır; proje rolleri korunur. Global Codex ayarları değiştirilmez.

M1'de ai-lab-tasks yalnız connector'dır. Framework ve proje rolleri ayrı kaynaklardan
kurulur. Connector model varsayılanı runtime.toml içindedir (Luna/low); proje rolü
ayarları proje reposundadır. GitHub IO akışı workflows/github-connector.md içindedir.

```sh
python3 -m unittest discover -s tests -v
```
