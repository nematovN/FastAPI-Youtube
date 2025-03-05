from fastapi import FastAPI, HTTPException
import youtube_dl
import os

app = FastAPI()


@app.get("/download/")
async def download_video(url: str):
    try:
        # youtube-dl sozlamalari
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',  # Saqlash joyi
        }

        # youtube-dl ni ishga tushirish
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', None)
            return {"message": f"Video '{title}' muvaffaqiyatli yuklandi!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Video yuklashda xato yuz berdi.")

