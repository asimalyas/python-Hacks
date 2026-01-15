from icrawler.builtin import GoogleImageCrawler, BingImageCrawler
import os

# ====== SETTINGS ======
keywords = ["cats", "dogs"]  # Replace with your dataset classes
num_images = 5              # Images per class
base_dir = "ML_Dataset"      # Root folder to save datasets
 
# Create base directory
os.makedirs(base_dir, exist_ok=True)
 
# ====== FUNCTION TO CRAWL IMAGES ======
def crawl_images(keyword, num_images, engine="google"):
    save_dir = os.path.join(base_dir, keyword)
    os.makedirs(save_dir, exist_ok=True)

    print(f"🚀 Downloading '{keyword}' using {engine}...")
    
    try:
        if engine == "google":
            crawler = GoogleImageCrawler(storage={'root_dir': save_dir})
        elif engine == "bing":
            crawler = BingImageCrawler(storage={'root_dir': save_dir})
        else:
            print("❌ Unknown engine. Using Google by default.")
            crawler = GoogleImageCrawler(storage={'root_dir': save_dir})

        crawler.crawl(
            keyword=keyword,
            max_num=num_images,
            min_size=(200,200),   # filters tiny images
            overwrite=True        # overwrite if rerunning
        )
        print(f"✅ Completed '{keyword}' download!\n")

    except Exception as e:
        print(f"❌ Error downloading '{keyword}': {e}\n")


# ====== START DOWNLOADING ======
for kw in keywords:
    crawl_images(kw, num_images, engine="google")   # Try Google first
    # Optionally, fallback to Bing if Google fails
    crawl_images(kw, num_images, engine="bing")
