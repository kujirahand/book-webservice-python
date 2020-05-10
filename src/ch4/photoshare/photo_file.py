import os
from PIL import Image

# パスの指定 --- (*1)
BASE_DIR = os.path.dirname(__file__)
DATA_FILE = BASE_DIR + '/data/photos.sqlite3'
FILES_DIR = BASE_DIR + '/files'

# 画像ファイルの保存パスを返す --- (*2)
def get_path(file_id, ptype = ''):
	return FILES_DIR + '/' + str(file_id) + ptype + '.jpg' 

# サムネイルを作成する --- (*3)
def make_thumbnail(file_id, size):
    src = get_path(file_id)
    des = get_path(file_id, '-thumb')
    # 既にサムネイルが作成されているなら作らない --- (*4)
    if os.path.exists(des): return des
    # 正方形に切り取る --- (*5)
    img = Image.open(src)
    msize = img.width if img.width < img.height else img.height
    img_crop = image_crop_center(img, msize)
    # 指定サイズにリサイズ --- (*6)
    img_resize = img_crop.resize((size, size))
    img_resize.save(des, quality=95)
    return des

# 画像の中心を正方形に切り取る --- (*7)
def image_crop_center(img, size):
    cx = int(img.width / 2)
    cy = int(img.height / 2)
    img_crop = img.crop((
        cx - size / 2, cy - size / 2, 
        cx + size / 2, cy + size / 2))
    return img_crop

