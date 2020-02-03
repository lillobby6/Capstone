import os, shutil
from keras import layers
from keras import models

def main():
    # original_dataset_dir = '/Users/lillo/Desktop/Capstone/UNCOMPRESSED_FILE_NAME' #TODO
    # base_dir = '/Users/lillo/Desktop/Capstone/small_code' #TODO
    # os.mkdir(base_dir)

    # train_dir = os.path.join(base_dir, 'train')
    # os.mkdir(train_dir)
    # validation_dir = os.path.join(base_dir, 'validation')
    # os.mkdir(validation_dir)
    # test_dir = os.path.join(base_dir, 'test')
    # os.mkdir(test_dir)

    # train_code_dir = os.path.join(train_dir, 'code')
    # os.mkdir(train_code_dir)

    # validation_code_dir = os.path.join(validation_dir, 'code')
    # os.mkdir(validation_code_dir)

    # test_code_dir = os.path.join(test_dir, 'code')
    # os.mkdir(test_code_dir)

    # fnames = ['code.{}.py'.format(i) for i in range(1000)]
    # for fname in fnames:
    #     src = os.path.join(original_dataset_dir, fname)
    #     dst = os.path.join(train_code_dir, fname)
    #     shutil.copyfile(src, dst)
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation = 'relu'), input_shape=(150,105,3))
    model.add(layers.MaxPooling2D(2, 2))
    model.add()


if __name__ == "__main__":
    main()