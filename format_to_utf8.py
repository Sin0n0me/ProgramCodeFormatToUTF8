import os
import glob
import chardet
import shutil

TARGET_FILE_NAME_LIST = 'check_list.txt'
TARGET_FILE_EXTENDS_SAVE_UTF_8_SIG = []
TARGET_FILE_EXTENDS_SAVE_UTF_8 = ['c', 'cpp', 'h', 'hpp', 'hlsl', 'glsl']
RECURSIVE = False

ENCODING_TYPE_UTF_8 = 'UTF-8'
ENCODING_TYPE_UTF_8_SIG = 'UTF-8-SIG'
BACKUP_DIRECTORY = './backup/'

def save_file(file_path: str, encoding: str):
    backup_dir = BACKUP_DIRECTORY + encoding.replace('-','_')
    # 一時保存用のディレクトリが存在しなければ新規作成
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    file_path = file_path.replace('\\', '/')    # バックスラッシュをスラッシュに変更

    # 一度ファイルを開き文字コードの判定
    with open(file_path, mode='rb') as base_binary_file:
        br = base_binary_file.read()            # 文字コードの判定

    file_info = chardet.detect(br)
    print(f'{file_path}:{file_info}')

    file_encode_type = file_info['encoding']

    # Windows-1254に判定されると高確率で0x8eのエラーが起こるので回避のためSJISで開く
    if file_encode_type == 'Windows-1254':
        file_encode_type = 'Shift_JIS'

    if file_encode_type != encoding:
        # 変更がかかる場合バックアップ
        shutil.copy2(
            file_path,
            f'{backup_dir}/{os.path.basename(file_path)}'
        )

        # 読み込み
        with open(file_path, mode='r', encoding=file_encode_type) as file:
            lines = file.readlines()

        # 上書き
        with open(file_path, mode='w', encoding=encoding) as file:
            for line in lines:
                raw_string = line.encode()
                temp_string = raw_string.decode(encoding=encoding)
                file.write(temp_string)


def main():
    with open(TARGET_FILE_NAME_LIST, 'r') as f:
        target_list = f.read().splitlines()
        
    target_extends_dict = {
        ENCODING_TYPE_UTF_8_SIG : TARGET_FILE_EXTENDS_SAVE_UTF_8_SIG,
        ENCODING_TYPE_UTF_8 : TARGET_FILE_EXTENDS_SAVE_UTF_8,
    }
    
    for target in target_list:
        for key in target_extends_dict.keys():
            for extends in target_extends_dict[key]:
                files = glob.glob(pathname=f'{target}/*.{extends}', recursive=RECURSIVE)
                for file_path in files:
                    save_file(file_path, key)



if __name__ == '__main__':
    main()
