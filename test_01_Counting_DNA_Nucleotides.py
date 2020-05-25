import pytest
import counting_DNA_Nucleotides_001 as sut

@pytest.mark.parametrize('string, expected',
    [(None, False), ('  ', False), ('', False), ('ACTGAA', True), ('aCGGTG', False), ('WCTAG', False)])
def test_for_valid_string(string, expected):
    assert sut.is_string_valid(string) == expected


@pytest.mark.parametrize('string, expected',
    [(None, False), ('', False), ('QWERTYUIOPASDFG', False), ('ACTGAAA', True), ('aCGGTG', True), ('G', True)])
def test_is_string_right_len(string, expected):
    assert sut.is_string_right_len(string, 10) == expected


@pytest.mark.parametrize('string, expected',
[('AACCTTGG', '2 2 2 2'),
('ACTG', '1 1 1 1'),
('WACTG', None)])
def test_get_nucleotide_count(string, expected):
    assert sut.get_nucleotide_count(string) == expected