<h1 align="center">
  <a href="https://github.com/fieldneoneo/flashcard">
    <img alt="Flashcard" src="fastlane/metadata/android/en-US/images/icon.png" width="180" />
  </a>
  <br>
  Flashcard
</h1>

<h3 align="center">Passive learning with your phone! 📱</h3>

> **This repository is a personal fork of [CardPop](https://github.com/Craeckie/CardPop) by [Craeckie](https://github.com/Craeckie), which is itself a fork of [FloFla Cards](https://github.com/flofladev/floflacards) by [flofladev](https://github.com/flofladev).**  
> The original idea and base implementation are flofladev's. FSRS scheduling, Anki and Pleco import and the other features listed under "Added in CardPop" are Craeckie's work. This fork adds the items under "Added in this fork". The app was renamed from CardPop to Flashcard in v2.11.1 and has its own icon.

**中文简介**：Flashcard 是 CardPop 的个人分支，主要用来学德语。它会在你用手机时把卡片悬浮显示在其他应用上方，利用碎片时间背词。这个分支在它的基础上增加了“接收分享的 CSV 文件并直接进入导入预览”，方便把别处整理好的生词一步送进来。原始创意和基础实现来自 flofladev，FSRS 排程、Anki 导入等功能来自 Craeckie。

## What is Flashcard?

Flashcard helps you learn **passively** while using your phone. Flashcards will appear on top of other apps at intervals you choose – so you can memorize words, formulas, or definitions while scrolling, chatting, or browsing.No extra effort. Just daily learning in the background.

### With Flashcard, you can: 
- Learn new words daily while scrolling social media 
- Revise definitions before a test 
- Practice foreign languages without opening a book 
- Build your own library of flashcards for any subject

### Perfect for: 
- Students and high schoolers preparing for exams 
- Language learners who want to expand vocabulary 
- Anyone who wants tolearn on the go

### Why Flashcard? 
- Unlike other flashcard apps, Flashcard **doesn’t** require you to open it every time. It gently reminds you of what you want to learn while you’re already using your phone. Simple,effective, and distraction-free.📌 
- Privacy first: Flashcard works fully offline. We do notcollect, store, or share any personal data. No ads, no analytics, no hidden costs – just learning. Start learning passively today and turn your screen time into studytime! 🚀

## Features
- 📂 Create your own categories and flashcards
- ⏰ Set the interval for how often cards appear
- 📐 Adjust the size and opacity so they don’t disturb you
- 🔒 100% offline – no internet, no accounts, no data collection
- 💡 Learn languages, prepare for exams, or memorize anything
- 🎉 Completely free, no ads, no tracking

### Added in this fork
- 📥 **Share to import** — other apps can hand a CSV or TSV file to Flashcard through the Android share sheet or "Open with". The file opens directly in the import preview, where you pick the category and confirm. A header row of `Front,Back,Category` (or the other column names the importer already recognises) maps the columns automatically. Available from v2.11.0.

### Added in CardPop (by Craeckie)
- 🧠 **FSRS v6 spaced repetition** — cards are scheduled using [FSRS](https://github.com/open-spaced-repetition/fsrs4anki), the algorithm that powers the newest Anki scheduler. Intervals adapt to your performance, with configurable target retention (80–95 %, default 90 %).
- 🌅 **Daily new-card limit & morning front-loading** — cap how many brand-new cards are introduced per day (Settings → Scheduling) to prevent review pile-up, and optionally front-load new cards earlier in the day while reserving the evening for reviews of existing cards.
- 📦 **Anki import** — import `.apkg` decks from Anki Web
- 📇 **Pleco import** — import flashcards exported as XML from the [Pleco](https://www.pleco.com/) dictionary app; simplified headword → front, pinyin (converted to tone marks) + every sense of the definition → back
- 📊 **More statistics** — review history chart (last 30 days) and rating distribution chart
- 💾 **Backup includes settings** — every card change is immediately backed up as a JSON file (including app settings) via Android’s Storage Access Framework
- 😴 **Snooze** — pause the overlay for a configurable number of minutes
- 🚫 **App blocklist** — suppress the overlay while specific apps are in the foreground
- 👆 **Swipe to rate** — opt-in mode (Settings → Appearance) that replaces the rating buttons with directional swipes: ← Again, → Easy, ↑ Good, ↓ Hard. The overlay fades to the rating colour as you pull; release past the threshold to submit.
- 🔍 **Pleco lookup** — tap a button on the overlay to look up the front side in the Pleco dictionary app
- 🖋️ **Custom question font** — load any TTF or OTF font file from your device (Settings → Flashcard Font → Load font file). Applied to the flashcard question only; the answer always uses the system font. Suggestions for Chinese study:
  - **LXGW WenKai** — open-source 楷书 font, available at [github.com/lxgw/LxgwWenKai](https://github.com/lxgw/LxgwWenKai/releases) (SIL OFL 1.1 license)
  - **Gukai** — the handwriting font bundled with the [Hanping Chinese Dictionary](https://hanping.app/) app; extract it from the APK and load it here
- 🌍 **Translations** — English, Polish, German


---
## Building
Every push runs the unit tests and Android lint in GitHub Actions (`.github/workflows/ci.yml`). The release workflow (`.github/workflows/release.yml`) builds and signs an APK when a version tag is pushed or when it is started by hand; it needs the repository secrets `KEYSTORE_BASE64`, `KEYSTORE_PASSWORD`, `KEY_ALIAS` and `KEY_PASSWORD`. Signed builds of this fork are on its [Releases](https://github.com/fieldneoneo/flashcard/releases) page. The fork uses its own application id (`com.fieldneoneo.flashcard`), so it installs next to the upstream CardPop app rather than replacing it; move your cards over with a backup in one app and a restore in the other. For released builds of the upstream apps, see [CardPop](https://github.com/Craeckie/CardPop/releases) and [FloFla Cards](https://github.com/flofladev/floflacards/releases).

## License
This project is licensed under the GNU General Public License v3.0, the same as CardPop and FloFla Cards. See [LICENSE](LICENSE).
