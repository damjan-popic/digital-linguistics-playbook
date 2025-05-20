---
title: _Auto_subtitle_burn_in_with_FFmpeg
---

**When to use** Create bilingual hard‑sub video.
**Input** video.mp4
**Tools** [Whisper](https://github.com/openai/whisper), [FFmpeg](https://ffmpeg.org)
**Steps** Whisper ▸ Translate ▸ `ffmpeg ... subtitles=`
**Output** out.mp4
**Pro tips** Use `-crf 23` to compress.

---
