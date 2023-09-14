def load_img(num):
    from PIL import Image
    import pandas as pd
    import matplotlib.pyplot as plt
    
    train_labels = pd.read_csv('train.csv')
    train_labels = dict(zip(train_labels['image_name'], train_labels['label']))
    
    name = f'{num:04}.png'
    
    if name in train_labels.keys():
        file = f'train/{name}'
        title = name + f' (train label={train_labels[name]})'
    else:
        file = f'test/{name}'
        title = name + ' (test)'
    
    img = Image.open(file)
    return img