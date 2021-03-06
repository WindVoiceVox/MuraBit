# -*- coding: utf-8 -*-
import random
import time

########################################################
# Global Settings
########################################################
MESSAGE_WAIT = 0.2
MIN_POPULATION =  5
MAX_POPULATION = 30

########################################################
# Classes
########################################################
class Mura(list):
    osa = None
    decision = None

    def __init__(self):
        self.osa = MuraAuth()

    def bitborn(self, murabit):
        self.append(murabit)

    def butsugi(mura, option):
        output(u"[MuraAuth] 物議じゃ！")
        mura.osa.think(option)
        for bit in mura:
            bit.think(option)

class MuraBit:
    opinion = None
    number = 0

    def __init__(self, num):
        self.number = num
        output(u"[%2d] おぎゃー" % num)

    # 村人は発言する
    def say(self):
        output(u"[%2d] %s！" % ( self.number, self.opinion ))
        return self.opinion

    # 村人は考えて、意見を持つ
    def think(self, option):
        self.opinion = option[random.randint(0, len(option)-1)]

class MuraAuth(MuraBit):
    option = []

    def __init__(self):
        MuraBit(MAX_POPULATION)

    # 村長は意見を聞く（ように見えて実は聞いていない）
    def listen(self, opinion):
        pass

    # 村長は村の物議を確定する（村人の意見を聞いたようで実は自分の意見で決めている）
    def decide(self):
        return self.opinion

########################################################
# Main Routine
########################################################
def output(message):
    time.sleep(MESSAGE_WAIT)
    print message

def main():
    # むかしむかし村があったそうな
    mura = Mura()

    # 村にはたくさんの村人がおった
    for n in range(0, random.randint(MIN_POPULATION, MAX_POPULATION)):
        mura.bitborn(MuraBit(n))

    # 村長は村人に来年の作物を決めようと呼びかけたのじゃ
    # 【村長が村人に選択肢を提示するのが村の取り決め】
    mura.osa.option = [u"コメ", u"ムギ", u"イモ", u"ソバ"]

    # 村人はそれぞれ自分の考えを言った。村長は意見を聞いた。
    mura.butsugi(mura.osa.option)
    for murabit in mura:
        mura.osa.listen(murabit.say())

    # そして村長は決めたのじゃ
    mura.decision = mura.osa.decide()
    output(u"[100] よし！ %sに決まりじゃ！" % mura.decision)

    # ToDo:決議に沿って実行され

    # ToDo:結果が出る……

if __name__ == '__main__':
    main()