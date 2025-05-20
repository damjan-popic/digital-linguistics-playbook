---
title:   Auto  subtitle  burn  in  with  FFmpeg
---

**When to use** Create bilingual hard‑sub video.

**Input** video.mp4

**Tools** [Whisper](https://github.com/openai/whisper), [FFmpeg](https://ffmpeg.org)

**Steps** Whisper ▸ Translate ▸ `ffmpeg ... subtitles=`

**Output** out.mp4

!!! tip "Pro tip"
    Use `-crf 23` to compress.

---
