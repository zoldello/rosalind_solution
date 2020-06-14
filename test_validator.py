import pytest
import validator as sut

@pytest.mark.parametrize('dna_string, expected',
    [(None, False),
    ('  ', False),
    ('', False),
    ('ACTGAA', True),
    ('aCGGTG', False),
    ('WCTAG', False)])
def is_string_valid_dna_string(dna_string, expected):
    assert sut.is_string_valid_dna(dna_string) == expected


@pytest.mark.parametrize('rna_string, expected',
    [(None, False),
    ('  ', False),
    ('', False),
    ('WCTAG', False),
    ('aCGGTG', False),
    ('ACUGAA', True),
    ('ACTGAA', True),
    ('UUU', True)])
def is_string_valid_rna_string(rna_string, expected):
    assert sut.is_string_valid_rna(rna_string) == expected


@pytest.mark.parametrize('string, expected',
    [(None, False),
    ('', False),
    ('QWERTYUIOPASDFG', False),
    ('ACTGAAA', True),
    ('aCGGTG', True),
    ('G', True)])
def test_is_string_right_len(string, expected):
    assert sut.is_string_right_len(string, 10) == expected
