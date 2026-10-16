# AI Team

Projeden ve makineden bağımsız Codex yazılım takımı. M4'te geliştirme yapıp Git'e
push ettikten sonra M1'de aynı branch ve devir kaydıyla devam edebilmek için.
Bir çalışan servis, model sunucusu veya otomatik dağıtım sistemi değildir.

## M4'te başlangıç

Python **3.11+**, Git ve kendi hesabınla giriş yapılmış Codex gerekir.

```sh
git clone git@github.com:SertacOnal/ai-team.git
cd ai-team
python3 scripts/team.py validate
python3 scripts/team.py install --target /absolute/path/to/your-project
python3 scripts/team.py install --target /absolute/path/to/your-project --apply
```

İlk install dry-run'dır. Hedef ayrı bir Git reposu olmalıdır. Projeyi Codex'te aç
ve yeni oturum başlat. Üretilen `.ai/project.json` şablonundaki kurulum/başlatma/test
komutlarını projeye göre doldur; echo yer tutucuları doğrulama sayılmaz. Kurulum
hiçbir proje komutunu çalıştırmaz, paket/servis başlatmaz ve global Codex config'ini
değiştirmez. Var olan config korunur; roller GPT-6 Luna / low kullanır.

## Takım

Ana Codex oturumu PO + Lead koordinasyonu, kapsam, entegrasyon ve kısa araştırmayı
üstlenir. Ayrı koordinatör agent başlatılmaz. Üç rol vardır:

- `team_developer`: frontend, backend, mobil ve geliştirme altyapısı.
- `team_qa`: bağımsız kabul, test ve Playwright doğrulaması.
- `team_designer`: yalnız anlamlı UI/UX veya görsel tasarım ihtiyacında.

Varsayılan: ana oturum → Developer → QA. Görsel yeniden tasarımda araya Designer
girer. Küçük işler ana oturumda yapılabilir; her görevde bütün roller çalıştırılmaz.
Bağımsız alanlarda aynı Developer rolünün birden fazla örneği çalışabilir;
dosya sahipliği ve API sözleşmesi önceden belirlenir. Tüm roller Luna/low kullanır.

## M4 → M1 → M4

1. Çalışmayı durdur; `.ai/handoff.md` içine tamamlananları, testleri ve sonraki
   adımı yaz. Kullanıcı yetkisiyle kodu ve devir kaydını **geliştirme branch'ine**
   commit/push et. Push edilmemiş değişiklikler diğer makineye ulaşmaz.
2. Diğer makinede repoyu clone/fetch et. Aynı branch'in başka aktif yazarı
   olmadığını doğrula. Temiz checkout'ta `git pull --ff-only` kullan veya ayrı
   worktree aç; yerel değişiklikleri reset ile silme.
3. `.ai/project.json` uyarınca bağımlılık ve sentetik veriyi hazırla. Secret'ları
   o makinede yerel olarak ayarla. `.env`, veritabanı ve sohbet geçmişi taşınmaz.
4. Codex'e: **“AGENTS.md ve .ai/handoff.md dosyalarını okuyup kaldığımız yerden
   devam et. Önce branch ve ortamı doğrula.”** de.
5. Dönüşte aynı devir akışını ters yönde uygula. Paralel işler ayrı branch kullanır.

Handoff dosyasındaki sahip alanı bilgilendirmedir; dağıtık kilit değildir.
Agent kodu yorumlayarak devam eder; aynı sohbet oturumunun taşınması gerekmez.

## Proje sınırları

Kurulum `.codex/agents/team_*.toml`, `.ai-team/AGENTS.md` ve AGENTS.md içinde
ayrı bir blok ekler. Mevcut proje kuralları, roller ve kullanıcı değişiklikleri
korunur; dosya çatışmasında durur. Önceden kurulan emekli team_* rolleri yalnız
kurulum kaydındaki hash ile eşleşiyorsa kaldırılır; yerel düzenleme varsa durulur. `.ai/project.json` ve `.ai/handoff.md` yalnız
ilk seferde oluşturulur. Bu dosyaları gözden geçirip proje reposuna commit edin;
sonraki makine repo üzerinden alır. Güncelleme için ai-team'i pull edip install'ı
tekrar çalıştırın. Global ayar kurulmaz, otomatik fetch/push yapılmaz.

Pnlcal, AI Lab runner, dashboard ve makineye özel servisler ayrı kalır. Bu repo
yeni task tracker/webhook/scheduler kurmaz. M1 üzerindeki ai-lab-tasks connector bu repodaki rolleri kurar; GitHub teslim
ve QA devir davranışı workflows/github-connector.md içinde tek kaynaktır.

## Kontrol

```sh
python3 scripts/team.py validate
python3 -m unittest discover -s tests -v
```
