import os
import shutil
from fuzzywuzzy import fuzz
from function import DB_function as db

# 归档+创建文件夹
class Sort():
    def sort(self, author, work):
        root = author  # 目的地文件夹       1层（作者层）
        move = work  # 被移动的文件夹    1层（作品层）
        # 构造目的地 路径
        # 第一层
        auth_name = os.listdir(root)
        auth_path = []
        for i in auth_name:
            auth_path.append(root + '\\' + i)
        # 构造 被移动路径
        # 第一层
        move_name = os.listdir(move)
        move_path = []

        for i in move_name:
            move_path.append(move + '\\' + i)
        for i in range(len(move_name)):
            sign1 = move_name[i].find('[')
            sign2 = move_name[i].find(']')
            sign3 = 0
            a = 0
            while a in range(len(auth_name)):
                # if (fuzz.token_set_ratio(move_name[i][sign1 + 1:sign2].strip(), auth_name[a])) > 56:
                #     print(fuzz.token_set_ratio(move_name[i][sign1 + 1:sign2].strip(), auth_name[a]))
                #     print(move_name[i] + '||| ' + auth_path[a])
                if (fuzz.token_set_ratio(move_name[i][sign1 + 1:sign2].strip(), auth_name[a])) > 62:
                    sign3 += 1
                    try:
                        shutil.move(move_path[i], auth_path[a])
                        print(move_path[i] + '移动到' + auth_path[a])
                    except shutil.Error:
                        if os.path.getsize(move_path[i]) > os.path.getsize(auth_path[a] + '/' + move_name[i]):
                            shutil.rmtree(auth_path[a] + '/' + move_name[i])
                            shutil.move(move_path[i], auth_path[a])
                        else:
                            shutil.rmtree(move_path[i])
                    break
                else:
                    a += 1
            if sign3 == 0:
                try:
                    new_path = root + '\\' + move_name[i][sign1:sign2 + 1]
                    os.makedirs(new_path)
                    shutil.move(move_path[i], new_path)
                except FileExistsError:
                    print(move_name[i])
