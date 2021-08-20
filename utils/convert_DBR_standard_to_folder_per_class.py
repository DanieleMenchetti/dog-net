import os
import pandas as pd
import shutil
from tqdm import tqdm

# Convert DBR standard dataset (used in Sistemi Digitali M)
# to a dataset with a folder for each class (train and val)


# Variables
dataset_old_path = './_DBR_dataset'
dataset_new_path = './_dataset_FPC' #FPC = folder per class



test_new_path = os.path.join(dataset_new_path, 'val')
train_new_path = os.path.join(dataset_new_path, 'train')

test_old_path = os.path.join(dataset_old_path, 'test')
train_old_path = os.path.join(dataset_old_path, 'train')

if os.path.isdir(dataset_new_path):
    shutil.rmtree(dataset_new_path)
os.mkdir(dataset_new_path)

os.mkdir(test_new_path)
os.mkdir(train_new_path)

dataframe = pd.read_csv(os.path.join(dataset_old_path, '_breeds/unique_breed_translation.csv'))
for b in dataframe['UNIQUE_BREED']:
    os.mkdir(os.path.join(test_new_path, b))
    os.mkdir(os.path.join(train_new_path, b))

# Test
f = open(os.path.join(test_old_path, 'test_labels.txt'))

for i, l in tqdm(enumerate(f.readlines())):
    if '\n' in l:
        l = l[:-1]
    img = str(i).zfill(5)+'.jpg'
    shutil.copy2(
        os.path.join(test_old_path, 'images', img),
        os.path.join(test_new_path, l, img) )

f.close()

# Train
f = open(os.path.join(train_old_path, 'train_labels.txt'))

for l in tqdm(f.readlines()):
    img = l.split(' ')[0]
    breed = l.split(' ')[1]
    if '\n' in breed:
        breed = breed[:-1]

    shutil.copy2(
        os.path.join(train_old_path, 'images', img),
        os.path.join(train_new_path, breed, img) )

f.close()

# unique_breed_translation.csv
shutil.copy2(
    os.path.join(dataset_old_path, '_breeds/unique_breed_translation.csv'),
    os.path.join(dataset_new_path, 'unique_breed_translation.csv') )
