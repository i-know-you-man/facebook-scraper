import os
import csv
from facebook_scraper import get_posts

post_url = os.environ.get('POST_URL')
print(f"📌 กำลังดึงข้อมูลจาก: {post_url}")

try:
    for post in get_posts(post_urls=[post_url], options={"comments": True}):
        comments = post.get('comments_full', [])
        
        if not comments:
            print("ไม่พบคอมเมนต์ หรือโพสต์นี้ติดข้อจำกัดของ Facebook")
        else:
            # สร้างไฟล์ CSV พร้อมรองรับภาษาไทย (utf-8-sig)
            with open('comments.csv', 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(['ชื่อผู้คอมเมนต์', 'ข้อความ'])
                
                for comment in comments:
                    writer.writerow([comment['commenter_name'], comment['comment_text']])
            
            print(f"✅ บันทึก {len(comments)} คอมเมนต์ลงไฟล์ comments.csv สำเร็จ!")
except Exception as e:
    print(f"❌ เกิดข้อผิดพลาด: {e}")
