# class HumanClass:
#   def __init__(self):
#     print("HumanClassのinit")
#     self.hp = 100

class WizardClass():
  def __init__(self):
    # super().__init__()
    self.mp = 100
    print("WizardClassのinit")

  def cast_spell(self):
    print("呪文を唱える")
  # def output_info(self):
  #   print(f"現在のHPは{self.hp}で、"
  #         f"MPは{self.mp}です。")

# wizard = WizardClass()
# wizard.output_info()

class SwordFighterClass:
  # def __init__(self):
  #   print("SwordFighterClassのinit")

  def attack_with_sword(self):
    print("剣で攻撃する")


class MagicSwordFighterClass(WizardClass, 
                            SwordFighterClass):
  pass

msf = MagicSwordFighterClass()
msf.cast_spell()
msf.attack_with_sword()