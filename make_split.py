import os
import shutil
from sklearn.model_selection import train_test_split

dataset_dir, train_dir, test_dir = 'dataset', 'train', 'test'

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

def split_data(category):
    category_path = os.path.join(dataset_dir, category)
    images = os.listdir(category_path)
    train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)

    os.makedirs(os.path.join(train_dir, category), exist_ok=True)
    os.makedirs(os.path.join(test_dir, category), exist_ok=True)

    for img in train_images:
        shutil.move(os.path.join(category_path, img), os.path.join(train_dir, category, img))
    for img in test_images:
        shutil.move(os.path.join(category_path, img), os.path.join(test_dir, category, img))

split_data('cats')
split_data('dogs')