import os
import re


class Formate_file():
    def process1(self, content, key):
        index = str(content).find(key)
        if index != -1:
            flag1 = self.getIndex1(content, index, '[')
            flag2 = self.getIndex1(content, index, '【')
            flag3 = self.getIndex1(content, index, '（')
            flag4 = self.getIndex1(content, index, '(')
            minn = min(flag1, flag2, flag3, flag4)
            if minn == 0:
                minn = max(flag1, flag2, flag3, flag4)
            if flag1 == minn:
                return self.getkey1(content, index, flag1, ']')
            if flag2 == minn:
                return self.getkey1(content, index, flag2, '】')
            if flag3 == minn:
                return self.getkey1(content, index, flag3, '）')
            if flag4 == minn:
                return self.getkey1(content, index, flag4, ')')
        else:
            return content

    def getkey1(self, content, index, flag, sign):
        return content.replace(content[flag - 1:self.getIndex2(content, index, sign) + 2], '')

    def getkey2(self, content, index, flag, sign):
        return content.replace(content[self.getIndex1(content, index, sign) - 1:flag + 2], '')

    def getIndex1(self, content, index, sign):
        while content[index - 1] != sign and index > 0:
            index -= 1
        return index

    def getIndex2(self, content, index, sign):
        while content[index + 1] != sign and index < len(content):
            index += 1
        return index

    def process2(self, content):
        c = re.compile(r'\(C[0-9][0-9]\)')
        key = c.findall(str(content))
        if len(key) > 0:
            return content.replace(key, '')
        else:
            return content

    def rename(self, path):
        list = ['[雑誌寄せ集め]', '(雑誌寄せ集め)', '[DL版]', '[中国翻訳]', '(マブラヴ オルタードフェイブル)', '(To Heart 2)',
                '(機動戦士ガンダム SEED)', '[真诗君修图]', '[茜新社]', '[Digital]', '[CE家族社]', '[4K掃圖組]', '[火狸翻译]', '(オリジナル)',
                '[風與黑暗掃圖]', '(Fate Grand Order)', '(東方Project)', '[罗洁爱儿个人机翻]', '(新世紀エヴァンゲリオン)', '(ファイナルファンタジーVII)',
                '[Chinese]',
                '[韓漫]', '(Chinese)', '(快盗天使ツインエンジェル)', '[風的工房]', '(オリジナル)', '(Fate／Grand Order)', '(グランブルーファンタジー)',
                '(アイドルマスター シンデレラガールズ)', '[單行本]', '[ 風的工房]', '(中二病でも恋がしたいっ！)', '(やはり俺の青春ラブコメはまちがっている)',
                '(クロスアンジュ 天使と竜の輪舞)',
                '[水晶海]', '(真 三國無双)', '[天鹅之恋]', '(Fatestay night)', '(ラグナロクオンライン)', '(Fatehollow ataraxia)', '(咲-Saki-)',
                '[風與彧製作]', '【CE家族社】', '(魔弾の王と戦姫)',
                '(サンクリ2015 WINTER)', '(交響詩篇エウレカセブン)', '(シュタインズ・ゲート)', '(機動戦士ガンダムSEED DESTINY)', '(FateGrandOrder)',
                '(オリジナル)',
                '[日版弱智嵌字]', '[中国語]', '(Fatestay night)', '[黑暗掃圖]', '[風與萌妳妹與嘘製作]', '(東方Project)', '[栗山同學不高興]',
                '(境界の彼方)',
                '(とある魔術の禁書目録＜インデックス＞)', '(あの日見た花の名前を僕達はまだ知らない)', '(ファイナルファンタジーIV)', '[52H里漫画组]', '(インフィニット・ストラトス)',
                '(コードギアス 反逆のルルーシュ)', '(ドキドキ!プリキュア)', '(IS＜インフィニット・ストラトス＞)', '(恋騎士Purely☆Kiss)', '[中國翻訳]', '(中文)',
                '[魂+工坊]',
                '(TERA The Exiled Realm of Arborea)', '(スーパーダンガンロンパ2)', '(ラブライブ! サンシャイン!!)', '[中国翻译]', '[天鵝之戀]',
                '(STEINS;GATE)', '(モーレツ宇宙海賊)', '(ノーモア☆ヒーローズ)', '(インフィニット_ストラトス)', '(ドラゴンクエスト V 天空の花嫁)', '(アマガミ)',
                '(アマガミ)',
                '(境界線上のホライゾン)', '(ヱヴァンゲリヲン新劇場版)', '(ラブライブ!)',
                '(あの日見た花の名前を僕達はまだ知らない)', '(魔法少女まどか☆マギカ)', '(エヴァンゲリオン)', '[纯爱の隙间娘扫图组]', '[重製]', '[画质修正]', '[神貓在綫]',
                '[維納斯中文]',
                '[風與Y⑨]', '[公主之假日]', '[小4K掃圖組]', '(中二病でも恋がしたい!)', '[風與彧製作]', '(攻殻機動隊)', '(冴えない彼女の育てかた)', '[ROC_1112出品]',
                '[天鵝之戀同人部]', '(ドリームクラブ)', '(ラブプラス)', '(エヴァンゲリオン', '[52H里漫画组]', '(ニセコイ)',
                '[風與彧與嘘製作]', '(新世紀エヴァンゲリオン)', '[風與Y⑨製作]', '(Fate staynight)', '(化物語)', '[漫遊中的蟲譯／final改圖]', '(同人誌)',
                '【靴下搬运组无聊整理】', '[太阳鸽子重嵌]', '[中文]', '[悠月工房]', '[風與uuz製作]', '[gnapiat扫图]', '[風與數字君製作]', '[黑崎貓改圖]',
                '(宇宙戦艦ヤマト2199)', '[sanjiemiejue原创]', '[ROC_1112出品，4K掃圖組]', '[風與sexy哥製作]', '[脸肿X空气系]', '[風與小Q製作]']
        key = ['COMIC', 'BEAST', 'comic', '汉化', '重嵌', '翻译', '漢化', '月号', 'MJK', '掃圖', '月白日语社']
        bath_path = path
        list_name = []
        list_path = []
        for root, dirs, files in os.walk(bath_path):
            for name in files:
                list_name.append(name)
                list_path.append(os.path.join(root, name))
        list_name = list_name[::-1]
        list_path = list_path[::-1]
        for i in range(len(list_name)):
            temp = list_name[i]
            for j in list:
                temp = temp.replace(j, '')
            for k in key:
                temp = self.process1(temp, k)
            temp = str(self.process2(temp))
            new_path = list_path[i].replace(list_name[i], '') + temp
            try:
                jj = 1
                os.rename(list_path[i], new_path)
            except FileExistsError:
                try:
                    os.rename(list_path[i], new_path + '(' + str(jj) + ')')
                except FileExistsError:
                    os.rename(list_path[i], new_path + '(' + str(jj + 1) + ')')
