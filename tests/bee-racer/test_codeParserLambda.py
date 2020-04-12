import pytest
from beeracer import codeParserLambda as cpl


def test_set():
    code = '''
    set 4 4
    '''
    parser = cpl.CodeParser(code)
    parser.parse()
    assert parser.bee.check_ram(4) == 4

    code = '''
    set 5 4
    '''
    parser = cpl.CodeParser(code)
    parser.parse()
    assert parser.bee.check_ram(5) == 4

    code = '''
    set SPEED 4
    '''
    parser = cpl.CodeParser(code)
    parser.parse()
    assert parser.bee.check_ram(1) == 4

    code = '''
    set ANGLE 4
    '''
    parser = cpl.CodeParser(code)
    parser.parse()
    assert parser.bee.check_ram(2) == 4

    '''
    code = """set 4 a"""
    parser = cpl.CodeParser(code)
    parser.parse()
    assert parser.bee.check_ram(4) == 4

    code = """SET 4 a"""
    parser = cpl.CodeParser(code)
    parser.parse()
    assert parser.bee.check_ram(4) == 4
    '''


def test_add():
    basecode = """
    set 4 4
    """
    code = basecode + "add 4 4"
    parser = cpl.CodeParser(code)
    parser.parse()
    assert parser.bee.check_ram(4) == 8

    code = "add 4 4"
    parser = cpl.CodeParser(code)
    parser.parse()
    assert parser.bee.check_ram(4) == 4

    code = '''
    add SPEED 4
    '''
    parser = cpl.CodeParser(code)
    parser.parse()
    assert parser.bee.check_ram(1) == 4

    code = '''
    add ANGLE 4
    '''
    parser = cpl.CodeParser(code)
    parser.parse()
    assert parser.bee.check_ram(2) == 4
