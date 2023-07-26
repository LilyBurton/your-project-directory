from lib.string_builder import *

def testing_string_bulding_with_empty_string():
    string_builder = StringBuilder()
    assert string_builder.output() == ""

def testing_string_building_with_added_string():
    string_builder = StringBuilder()
    string_builder.add("Woah!")
    result = string_builder.output()
    assert result == "Woah!"

def testing_string_building_with_size():
    string_builder = StringBuilder()
    string_builder.add("Woah!")
    assert string_builder.size() == 5

def testing_string_building_with_multiple_added_strings():
    string_builder = StringBuilder()
    string_builder.add("Crash")
    string_builder.add(" ")
    string_builder.add("Bandicoot!")
    result = string_builder.output()
    assert result == "Crash Bandicoot!"

def testing_string_building_with_multiple_added_strings_and_size():
    string_builder = StringBuilder()
    string_builder.add("Crash")
    string_builder.add(" ")
    string_builder.add("Bandicoot!")
    result = string_builder.size()
    assert result == 16