from poker import *
import pytest

def test_isBrelan_Should_Return_True_When_Hand_Is_Brelan():
    assert isBrelan([('14', 'coeur'), ('14', 'pique'), ('14', 'trefles'), ('3', 'trefles'), ('6', 'trefles')]) == True
    assert isBrelan([('14', 'coeur'), ('13', 'pique'), ('14', 'trefles'), ('3', 'trefles'), ('14', 'carreau')]) == True
    assert isBrelan([('4', 'coeur'), ('4', 'pique'), ('4', 'trefles'), ('4', 'carreau'), ('14', 'trefles')]) == True

def test_isBrelan_Should_Return_False_When_Hand_Is_Not_Brelan():
    assert isBrelan([('14', 'coeur'), ('13', 'pique'), ('12', 'trefles'), ('3', 'trefles'), ('6', 'trefles')]) == False
    assert isBrelan([('14', 'coeur'), ('13', 'pique'), ('12', 'trefles'), ('3', 'trefles'), ('2', 'trefles')]) == False
    assert isBrelan([('4', 'coeur'), ('5', 'pique'), ('6', 'trefles'), ('7', 'carreau'), ('8', 'trefles')]) == False

def test_is_Four_Of_A_Kind_Should_Return_True_When_Hand_Is_Four_Of_A_Kind():
    assert isFourOfAKind([('14', 'coeur'), ('14', 'pique'), ('14', 'trefles'), ('14', 'carreau'), ('6', 'trefles')]) == True
    assert isFourOfAKind([('4', 'coeur'), ('4', 'pique'), ('4', 'trefles'), ('4', 'carreau'), ('14', 'trefles')]) == True

def test_is_Four_Of_A_Kind_Should_Return_False_When_Hand_Is_Not_Four_Of_A_Kind():
    assert isFourOfAKind([('14', 'coeur'), ('13', 'pique'), ('12', 'trefles'), ('3', 'trefles'), ('6', 'trefles')]) == False
    assert isFourOfAKind([('14', 'coeur'), ('13', 'pique'), ('12', 'trefles'), ('3', 'trefles'), ('2', 'trefles')]) == False

def test_is_Full_House_Should_Return_True_When_Hand_Is_Full_House():
    assert isFullHouse([('14', 'coeur'), ('14', 'pique'), ('14', 'trefles'), ('3', 'trefles'), ('3', 'carreau')]) == True
    assert isFullHouse([('4', 'coeur'), ('4', 'pique'), ('4', 'trefles'), ('5', 'carreau'), ('5', 'trefles')]) == True

def test_is_Full_House_Should_Return_False_When_Hand_Is_Not_Full_House():
    assert isFullHouse([('14', 'coeur'), ('13', 'trefles'), ('12', 'trefles'), ('3', 'trefles'), ('6', 'trefles')]) == False
    assert isFullHouse([('14', 'coeur'), ('13', 'pique'), ('12', 'trefles'), ('3', 'trefles'), ('2', 'trefles')]) == False

def test_value_Of_Hand_Should_Return_Correct_Value_When_Hand_Is_Brelan():
    assert value_of_hand([('14', 'coeur'), ('14', 'pique'), ('14', 'trefles'), ('3', 'trefles'), ('6', 'trefles')]) == 30 #Brelan

def test_value_Of_Hand_Should_Return_Correct_Value_When_Hand_Is_Four_Of_A_Kind():
    assert value_of_hand([('14', 'coeur'), ('14', 'pique'), ('14', 'trefles'), ('14', 'carreau'), ('6', 'trefles')]) == 60 #Four of a kind