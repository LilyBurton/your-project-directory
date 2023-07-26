from lib.gratitudes import *

def testing_gratitudes_with_names():
    gratitudes = Gratitudes()
    gratitudes.add("Lily")
    gratitudes.add("Momo")
    assert gratitudes.format() == "Be grateful for: Lily, Momo"

def testing_gratitudes_with_one_name():
    gratitudes = Gratitudes()
    gratitudes.add("Lily")
    assert gratitudes.format() == "Be grateful for: Lily"

def testing_gratitudes_with_no_name():
    gratitudes = Gratitudes()
    gratitudes.add(" ")
    assert gratitudes.format() == "Be grateful for:  "